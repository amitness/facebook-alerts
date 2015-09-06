''' Lists your Facebook notifications on command line
    Author: Amit Chaudhary ( studenton.com@gmail.com )
'''

notifications = 5  # Number of Notifications
profile_id = '1XXXXXXXXXXXXXX'
token = 'write token here'
url = 'https://www.facebook.com/feeds/notifications.php?id='+ profile_id +'&viewer=' + profile_id +'&key=' + token + '&format=rss20'


def get_page(url):
    try:
        import urllib
        return urllib.urlopen(url).read()
    except:
        return ''


def titles(xml, pos):
    pos1 = xml.find('<title>',pos)
    pos1 = xml.find('A[', pos1)
    pos2 = xml.find(']]', pos1)
    return pos1+2, pos2

pos = 0
xml = get_page(url)

for i in range(notifications):
    pos1, pos2 = titles(xml, pos)
    pos = pos2
    print '', u"\u2022", xml[pos1:pos2].replace('.', '')
