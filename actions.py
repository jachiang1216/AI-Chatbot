from __future__ import absolute_import      # __future enables new language features
from __future__ import division
from __future__ import unicode_literals
from __future__ import print_function

from rasa_core_sdk import Action
from rasa_core_sdk.events import AllSlotsReset
import pafy
import vlc


class ActionMusic(Action):  # Plays Selected Song
    def name(self):
        return 'actions.ActionMusic'

    def run(self, dispatcher, tracker, domain):   # Use VLC to play
        import requests
        from bs4 import BeautifulSoup
        import re
        artist = str(tracker.get_slot('artist'))
        song = str(tracker.get_slot('song'))
        if artist == 'None':
            artist = ''
        search = "https://www.youtube.com/results?search_query=song+"+artist.replace(' ', '+').replace('\'', '')\
                 + "+"+song.replace(' ', '+').replace('\'', '')
        source_code = requests.get(search)
        plain_txt = source_code.text
        soup = BeautifulSoup(plain_txt, 'html.parser')
        regex = re.compile(r'/watch\?v=.*')
        # print(search)
        url = ''
        for vid in soup.findAll('a', {'class': 'yt-uix-sessionlink spf-link'},
                                href=True):
            if regex.search(vid['href']):
                url = 'https://www.youtube.com' + str(vid['href'])
                dispatcher.utter_message("Playing: "+url)
                break
        video = pafy.new(url)
        best = video.getbestaudio()
        playurl = best.url
        Instance = vlc.Instance()
        media = Instance.media_new(playurl)
        media.get_mrl()
        player.set_media(media)
        player.play()
        return [AllSlotsReset()]


class ActionStop(Action):  # Stop Playing
    def name(self):
        return 'actions.ActionStop'

    def run(self, dispatcher, tracker, domain):
        player.stop()
        dispatcher.utter_message("Music stopped")
        return [AllSlotsReset()]


class ActionComedy(Action):
    def name(self):
        return "actions.ActionComedy"

    def run(self, dispatcher, tracker, domain):
        import requests
        url = 'https://icanhazdadjoke.com/'
        headers = {'Accept': 'application/json'}
        joke_msg = requests.get(url, headers=headers).json().get('joke')
        dispatcher.utter_message(joke_msg)
        return [AllSlotsReset()]


class ActionPicture(Action):
    def name(self):
        return "actions.ActionPicture"

    def run(self, dispatcher, tracker, domain):
        import requests
        animal = tracker.get_slot('animal')

        r = requests.get('http://shibe.online/api/{}?count=1&urls=true&httpsUrls=true'.format(animal))
        response = r.content.decode()
        response = response.replace('["', "")
        response = response.replace('"]', "")

        # display(Image(response[0], height=550, width=520))
        dispatcher.utter_message("Here you go: {}".format(response))


Instance = vlc.Instance()
player = Instance.media_player_new()



