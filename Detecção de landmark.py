import argparse
from ast import parse
from email import parser
import io
from google.cloud import vision
from google.cloud.vision import types

def main(image_file):
    #Instanciando o cliente
    client = vision.ImageAnnotatorClient()
    #carregando a foto na memoria
    with to.open(image_file, 'rb') as image_file:
        content = image_file.read()
    image = types.image(content=content)
    
    response = client.landmark_detection(image=image)
    labels = response.landmark_annotations
    for label in labels:
        print('found landmark: {}'.format(label.description))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('image_file', help = 'The imageyou\'d like the label.')
    args = parser.parse_args()
    main(args.images_file)
