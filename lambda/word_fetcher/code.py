import json
import boto3
import uuid
import datetime
from wordnik import swagger, WordsApi

def get_wotd():
    with open('.context', 'r') as f:
        gordon_context = json.loads(f.read())
    apiUrl = 'http://api.wordnik.com/v4'
    client = swagger.ApiClient(gordon_context['wordnik_api_key'], apiUrl)
    wordsApi = WordsApi.WordsApi(client)
    wotd = wordsApi.getWordOfTheDay()
    return wotd

def wotd2json(wotd):
    result = {}
    result['uid'] = str(uuid.uuid4())
    result['updateDate'] = datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.0Z')
    result['titleText'] = '{}: {}'.format(wotd.word, wotd.definitions[0].text)
    result['redirectionUrl'] = 'https://www.wordnik.com/word-of-the-day'
    text = wotd.word + '. ' + '. '.join(wotd.word) + '. ' + wotd.word + '. '
    for definition in wotd.definitions:
        text += ' ' + definition.partOfSpeech + '. ' + definition.text
        if definition.note:
            text += ' ' + definition.note
        text += ' Source, ' + definition.source + '.'
    if wotd.examples:
        examples = wotd.examples[:3]
        text += ' Here are {} examples of {}, '.format(len(examples), wotd.word)
        for num, example in enumerate(examples):
            text += "Example number {}: ".format(num+1) + example.text
            if example.title:
                text += " from {}.".format(example.title)
    if wotd.note:
        text += ' Note, ' + wotd.note
    result['mainText'] = text
    return json.dumps(result)

def save_wotd_json_to_s3(wotd_json):
    s3 = boto3.client('s3')
    s3.put_object(Bucket='alexa-word-of-the-day-763881559496', 
                  Key='flashbriefing.json', Body=wotd_json,
                  ACL='public-read', ContentType='application/json')

def handler(event, context):
    wotd = get_wotd()
    wotd_json = wotd2json(wotd)
    save_wotd_json_to_s3(wotd_json)
    print('Received Event: ' + json.dumps(event, indent=2))
    print('Saved {} as the word of the day to S3'.format(wotd.word))
    return wotd.word
