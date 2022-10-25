import json

class JSONReader():

    def readContent(self, msg, content_message):
        with open("content.json", "r") as contentjson:
            json_file = contentjson.read()   

        return json.loads(json_file)[msg][0][content_message] 

class Validation():

    def song_name(self, answer):
        artist = answer.split(' - ')[0]
        song_name = answer.split(' - ')[1]

        output_message = 'Is it correct?\n\n*🎶 Artist: ' + artist + '\n🎶 Song: ' + song_name + '*'

        return output_message