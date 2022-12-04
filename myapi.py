import paralleldots


class API:

    def __init__(self):
        paralleldots.set_api_key('Enter- Komprehend.io site-API-Key')

    def sentiment_analysis(self, text):
        response = paralleldots.sentiment(text)
        return response

    def emotions_analysis(self, text):
        emotion_response = paralleldots.emotion(text)
        return emotion_response

    def intent_analysis(self, text):
        intent_response = paralleldots.intent(text)
        return intent_response
