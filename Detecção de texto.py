from __future__ import annotations
import argparse
from ast import parse
from email import parser
import io
from urllib import response
from google.cloud import vision
from google.cloud.vision import types

def main(image_file):
    #Instanciando o cliente
    client = vision.ImageAnnotatorClient()
    #carregando a foto na memoria
    with to.open(image_file, 'rb') as image_file:
        content = image_file.read()
    image = types.Image(content=content)
    
    response = client.text_detection(image=image)
    labels = response.text_annotations
    for label in labels:
        print(label.description)
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('image_file', help='The image you\'d like to label.')
    args = parser.parse_args()
    main(args.image_file)
    