import urllib2
import json

URL = 'https://randomuser.me/api/'


class RandomDataGenerator(object):
    data = {}

    def __init__(self):
        self.url = URL
        self.data = json.loads(urllib2.urlopen(URL).read())

    def get_address(self):
        street = self.data['results'][0]['location'][
            'street'].encode('ascii', 'ignore')
        city = self.data['results'][0]['location'][
            'city'].encode('ascii', 'ignore')
        state = self.data['results'][0]['location'][
            'state'].encode('ascii', 'ignore')
        return '{0} ,{1}, {2}'.format(street, city, state)

    def get_name(self):
        return '{0} {1}'.format(self.data['results'][0]['name']['first'].encode('ascii', 'ignore'),
                                self.data['results'][0]['name']['last'].encode('ascii', 'ignore'))

    def get_postcode(self):
        return self.data['results'][0]['location']['postcode']

    def get_phone(self):
        return self.data['results'][0]['phone']

    def get_mail(self):
        return self.data['results'][0]['email'].encode('ascii', 'ignore')

    def get_username(self):
        return self.data['results'][0]['login']['username']

    def get_gender(self):
        return self.data['results'][0]['gender']
