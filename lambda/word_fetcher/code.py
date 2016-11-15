import json
import boto3
from wordnik import swagger, WordsApi

def get_wotd():
    with open('.context', 'r') as f:
        gordon_context = json.loads(f.read())
    apiUrl = 'http://api.wordnik.com/v4'
    client = swagger.ApiClient(gordon_context['wordnik_api_key'], apiUrl)
    wordsApi = WordsApi.WordsApi(client)
    wotd = wordsApi.getWordOfTheDay()
    return wotd

def handler(event, context):
    wotd = get_wotd()
    print(wotd)
    print("Received Event: " + json.dumps(event, indent=2))
    return wotd.word
