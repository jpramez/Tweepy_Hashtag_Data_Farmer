from __future__ import absolute_import, print_function

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json as json
import urllib.request

# Go to http://apps.twitter.com and create an app.
# The consumer key and secret will be generated for you after
consumer_key="ZErwpxZ83whbL39OGNgXZ29xE"
consumer_secret="TY1ATX7BccVYbbdEFw9O7AGTLyLcOzP7FTRF2AGOTNDyy34lx3"

# After the step above, you will be redirected to your app's page.
# Create an access token under the the "Your access token" section
access_token="3344870459-mFA9YOe5aXL1IiCAoqDfnCcQG6IQIduJcDadQat"
access_token_secret="9OzcCnquWYChI3TnPWW9tZVEKwSI2ciST2X92inzNSPBm"

#Array Hashtags
HT_ARRAY=['']


class StdOutListener(StreamListener):
    """ A listener handles tweets that are received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """
    def on_data(self, data):
        decoded = json.loads(data)
        if 'media' not in decoded['entities']:
            return True
        else:
            # Also, we convert UTF-8 to ASCII ignoring all bad characters sent by users
            string = decoded['entities']['media'][0]['media_url']
            path = 'imgs/'+decoded['user']['screen_name']+'_'+decoded['id_str']+'.jpg'
            if decoded['user']['screen_name'] == 'rocket_adeleia':
                path = 'imgs/pekku/'+decoded['user']['screen_name']+'_'+decoded['id_str']+'.jpg'
            # Save the file
            img = urllib.request.urlopen(string)
            localFile = open(path, 'wb')
            localFile.write(img.read())
            localFile.close()
            print('@'+decoded['user']['screen_name']+' -> '+string)
        return True

    def on_error(self, status):
        f.close()
        print(status)

if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, l)
stream.filter(track=HT_ARRAY)