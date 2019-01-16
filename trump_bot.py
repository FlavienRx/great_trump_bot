import random
import tweepy

# from conf import *
# from PIL import Image
# from PIL import ImageFont
# from PIL import ImageDraw

# WORD
# Open the file and lines
fo_nouns = open("nouns.txt", "r+")
fo_verbs = open("verbings.txt", "r+")
fo_an_nouns = open("an_noun.txt", "r+")

nouns = fo_nouns.read().splitlines()
verbs = fo_verbs.read().splitlines()
an_nouns = fo_an_nouns.read().splitlines()

noun =random.choice(nouns)
verb =random.choice(verbs)

article = 'a'

try:
    an_nouns.index(noun)
    article = 'an'

except ValueError:
    pass

print(verb.title() + ' ' + article + ' ' + noun + " is now illegal !")

# Close the file
fo_nouns.close()
fo_verbs.close()

# TWEET
# Tweet authentification
# auth = tweepy.OAuthHandler(API_key, API_secret_key)
# auth.set_access_token(Access_token, Access_token_secret)
# api = tweepy.API(auth)
# # Create the status
# status = "Holy shit, {} is on fire !".format(sentence)
# # Tweet the fun
# api.update_with_media("image_out.png", status=status)