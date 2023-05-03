import concurrent.futures
import json
import logging
from datetime import date
import os
import boto3
from botocore.exceptions import ClientError
from numpy import ndarray
import pandas as pd
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from config import API_KEY


def upload_file(file_name:str, bucket: str) -> bool:
    """Função de carregar arquivos para um bucket
    Args:
        file_name (str): Arquivo a ser enviado para o bucket S3
        bucket (str): Nome do bucket

    Returns:
        bool: Retorna False se a operação der erro, caso contrário True
    """

    session = boto3.Session(profile_name="default")
    s3_client = session.client("s3")
    
    #Tenta dar Upload no arquivo, os parâmetros passados são:
    #Extensão do arquivo, retirada com os.splittext()
    #Data com o datetime (YYYY/MM/DD)
    #Nome do arquivo. É usado uma substring pelo fato de arquivos como CSV e JSON, em execução no AWS Lambda,
    #serem lidos dentro do diretório /tmp/. Essa substring elimina isso.
    try:
        s3_client.upload_file(
            file_name,
            bucket,
            f"Raw/TMDB/{os.path.splitext(file_name)[1][1:].upper()}/{str(date.today())[0:4]}/{str(date.today())[5:7]}/{str(date.today())[8:10]}/{file_name[5:]}",
        )
    except ClientError as error:
        logging.error(error)
        return False
    return True


def drama() -> ndarray:
    """Abre o csv de series

    Returns:
        ndarray: Array do numpy com todos os valores únicos com "romance" 
    """
    session = boto3.Session(profile_name="default")
    s3_client = session.client("s3")
    obj = s3_client.get_object(Bucket = 'data-lake-desafio-1', Key = 'Raw/Local/CSV/SERIES/2023/04/21/series.csv')

    df = pd.read_csv(obj['Body'],
                     delimiter='|',
                     )
    df = df.replace(r'\N','', ) 

    #Regex selecionando qualquer midia na categoria "Romance" e o ano de lançamento depois dos anos 2000,
    #retornando os ids unique
    return df[(df['genero'].str.contains(r'\bRomance\b') == True) & (pd.to_numeric(df['anoLancamento'])>= 2000)]['id'].unique()

def search(id:str) -> json:
    """ Retorna o id procurado

    Args:
        id (str): id a ser procurado

    Returns:
        json: Json do id procurado
    """
    
    url = f"https://api.themoviedb.org/3/find/{id}?api_key={API_KEY}&external_source=imdb_id"

    #Pelo fato do número de requests ser muito grande e multithreading estar sendo utilizado,
    #uma sessão com múltiplos retries é necessário
    session = requests.Session()
    retry = Retry(connect=3, backoff_factor=0.5)
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)

    data = session.get(url).json()
    return data
            

if __name__ == '__main__':
    
    with concurrent.futures.ThreadPoolExecutor() as executor:
        ids = drama()
        counter = 0
        before = 0
        futures = (executor.submit(search, id) for id in ids)
        result = [future.result() for future in concurrent.futures.as_completed(futures)]
        #Arquivos 20 partes de 239 dados cada
        for i in enumerate(result):
            if i[0]%239 == 0 and i[0] != 0:
                counter += 1
                with open(f'json_{counter}.json', 'w') as f:
                    json.dump(result[before: before + 239], f, indent=2)
                    upload_file(f.name, "data-lake-desafio-1")
                before = i[0]
        



