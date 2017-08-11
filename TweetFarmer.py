from __future__ import absolute_import, print_function

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json as json
import urllib.request

# Go to http://apps.twitter.com and create an app.
# The consumer key and secret will be generated for you after
consumer_key="YOUR_COSTUMER_KEY_HERE"
consumer_secret="YOUR_COSTUMER_SECRET_KEY_HERE"

# After the step above, you will be redirected to your app's page.
# Create an access token under the the "Your access token" section
access_token="YOUR_ACCESS_TOKEN_HERE"
access_token_secret="YOUR_SECRET_ACCESS_TOKEN_HERE"

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
