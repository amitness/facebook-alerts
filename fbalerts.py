'''
    Check your Facebook notifications on command line.
    Author: Amit Chaudhary ( studenton.com@gmail.com )
'''
import json

# Configuration
notifications = 5  # Number of Notifications
profile_id = '1XXXXXXXXXXXXXX'
token = 'write token here'
url = 'https://www.facebook.com/feeds/notifications.php?id=' + \
    profile_id + '&viewer=' + profile_id + '&key=' + token + '&format=rss20'


def get_page(url):
    try:
        import urllib
        return urllib.urlopen(url).read()
    except:
        return ''


def main():
    try:
        data = json.loads(get_page(url))
        for i in range(notifications):
            print data['entries'][i]['title'] + "\n"

    except:
        print """
        Couldnot fetch the notifications. The possible causes are:
        1. You are not connected to the internet.
        2. You haven't entered the correct api token.
        """

if __name__ == "__main__":
    main()
