from StringIO import StringIO
import json
import pycurl


def fetch_json(url):
    buffer = StringIO()
    c = pycurl.Curl()
    c.setopt(c.URL, url)
    c.setopt(c.WRITEDATA, buffer)
    c.perform()
    c.close()

    data = buffer.getvalue()
    return json.loads(data)

