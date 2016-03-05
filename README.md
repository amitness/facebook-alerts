# facebook-alerts
Check your facebook notifications from the command line.

## Configuration:
Open this [page](http://www.facebook.com/notifications) and click the RSS link. You must be logged in to Facebook.

![Screenshot](http://i.imgur.com/zQTW2jc.png?1)

A new page opens in RSS format. Look at the address bar and copy the values of *id=1XXXXXXXXXXXXXX* and *key=xXXXXxXXXXxXX*.

Replace the **profile_id** and **token** in the script with the values you got from the address bar from that page.

## Usage
`python fbalerts.py` 

