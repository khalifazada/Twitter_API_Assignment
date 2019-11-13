from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from kafka import SimpleProducer, KafkaClient

ACCESS_TOKEN = ""
TOKEN_SECRET = ""
CONSUMER_KEY = ""
CONSUMER_SECRET = ""
TOPIC = "trump"

class StdOutListener(StreamListener):
    def on_data(self, data):
        producer.send_messages(TOPIC, data.encode('utf-8'))
        print (data)
        return True
    def on_error(self, status):
        print (status)

kafka = KafkaClient("localhost:9092")
producer = SimpleProducer(kafka)
l = StdOutListener()
auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_ACCESS_TOKEN(ACCESS_TOKEN, TOKEN_SECRET)
stream = Stream(auth, l)
stream.filter(track=TOPIC)
