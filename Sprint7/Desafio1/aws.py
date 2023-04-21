import os
import logging
from datetime import date
import boto3
from botocore.exceptions import ClientError

session = boto3.Session(profile_name="default")


def upload_file(file_name: list, bucket: str) -> bool:
    """_summary_
    Args:
        file_name (list): Lista de arquivos a serem enviados para o bucket S3
        bucket (str): Nome do bucket

    Returns:
        bool: Retorna False se a operação der erro, caso contrário True
    """
    # Upload the file
    s3_client = session.client("s3")
    #
    for i in file_name:
        try:
            s3_client.upload_file(
                i,
                bucket,
                f"Raw/Local/{os.path.splitext(i)[1][1:].upper()}/{os.path.splitext(i)[0].upper()}\
                                  /{str(date.today())[0:4]}/{str(date.today())[5:7]}/{str(date.today())[8:10]}/{i}",
            )
        except ClientError as error:
            logging.error(error)
            return False
    return True


if __name__ == "__main__":
    if upload_file(["movies.csv", "series.csv"], "data-lake-desafio-1"):
        print("Arquivos Enviado")

    else:
        print("Erro no Upload")
