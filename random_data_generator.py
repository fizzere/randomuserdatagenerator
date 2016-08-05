import urllib2
import json
from random import randint

URL = 'https://randomuser.me/api/'


class RandomDataGenerator(object):
    data = {}

    def __init__(self):
        self.data = json.loads(urllib2.urlopen(URL).read())

    def get_street(self):
        street_data = self.data['results'][0]['location'][
            'street'].encode('ascii', 'ignore')
        street_name = street_data.split()[1:]
        street = ' '.join(street_name)
        return street

    def get_home(self):
        street_data = self.data['results'][0]['location'][
            'street'].encode('ascii', 'ignore')
        home_number = street_data.split()[0]
        return home_number

    def get_inn(self):
        return randint(10000000000, 99999999999)

    def get_passport_serial(self):
        serial1 = randint(1, 99)
        serial2 = randint(1, 99)
        serial = '{0} {1}'.format(serial1, serial2)
        return serial

    def get_passport_number(self):
        return randint(100000, 999999)

    def get_passport_day(self):
        return '{0}.{1}.'.format(randint(1, 31), randint(1, 12))

    def get_passport_year(self):
        return randint(1960, 2016)

    def get_appartment(self):
        return randint(1, 1000)

    def get_city(self):
        return self.data['results'][0]['location']['city'].encode('ascii', 'ignore')

    def get_state(self):
        return self.data['results'][0]['location']['state'].encode('ascii', 'ignore')

    def get_name(self):
        return '{0} {1}'.format(self.data['results'][0]['name']['first'].encode('ascii', 'ignore'),
                                self.data['results'][0]['name']['last'].encode('ascii', 'ignore'))

    def get_postcode(self):
        postcode_raw = self.data['results'][0]['location']['postcode']
        if isinstance(postcode_raw, int):
            postcode = ''.join([x for x in str(postcode_raw).split()])
        else:
            postcode = ''.join([x for x in postcode_raw.split()])
        if len(postcode) > 6:
            postcode = postcode[:6]
        elif len(postcode) < 6:
            postcode = postcode + '1'
        return postcode

    def get_phone(self):
        lst = ['(', ')', '-', ' ']
        phone_raw = self.data['results'][0]['phone']
        phone = ''.join([x for x in phone_raw if x not in lst])
        if len(phone) > 10:
            phone = phone[:10]
        return phone

    def get_mail(self):
        return self.data['results'][0]['email'].encode('ascii', 'ignore')

    def get_username(self):
        return self.data['results'][0]['login']['username']

    def get_gender(self):
        return self.data['results'][0]['gender']
