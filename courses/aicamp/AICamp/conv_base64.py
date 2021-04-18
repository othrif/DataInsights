import click
import requests
import base64
import json



def get_prediction(image_data, url):
    print(url)
    r = requests.post(url, data=image_data)
    raw_response = getattr(r,'_content').decode("utf-8")
    print(raw_response)
    return raw_response


@click.command()
@click.option('-i', '--input', default='./Cat_1.jpg')
@click.option('-u', '--url', default='https://8fpen8bch3.execute-api.us-east-1.amazonaws.com/AICamp-ImageClassification/aicamp-imageclassification')


def test(input, url):
	print(input, url)
	with open(input, "rb") as image:
		payload = base64.b64encode(image.read())
		payload = "{\"body\":\""+ str(payload, 'UTF-8') + "\"}"
		response = get_prediction(payload, url)



test()


