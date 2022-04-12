import argparse
import io
from urllib import response
from google.cloud import vision
from google.cloud.vision import types

def main(image_file):
    client = vision.ImageAnnotatorClient()
    #carregando a imagem na memoria
    with to.open(image_file, 'rb') as image_file:
        content = image_file.read()
    image = types.Image(content=content)
    
    response = client.face_detection(image=image)
    labels = response.face_annotations
    for label in labels:
        print('Joy Likehood: {}'.format(label.joy_likehood))
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('image_file', help='The image you\'d like to label.')
    args = parser.parse_args()
    main(args.image_file)