# Copyright 2015, Google, Inc.
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use
# this file except in compliance with the License. You may obtain a copy of the
# License at http://www.apache.org/licenses/LICENSE-2.0 Unless required by applicable
# law or agreed to in writing, software distributed under the License is distributed
# on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
# or implied. See the License for the specific language governing permissions and
# limitations under the License.


from urllib.request import urlopen
import json

from flask import Flask
app = Flask(__name__)

from api_key import key

# [START app]
@app.route('/', methods=['GET'])
def get_author():
    # host = 'https://www.googleapis.com/books/v1/volumes?q={}&key={}&country=US'.format(title, key)
    # request = urllib2.Request(host)
    # try:
    #     response = urlopen(request)
    # except urllib2.HTTPError, error:
    #     contents = error.read()
    #     print ('Received error from Books API {}'.format(contents))
    #     return str(contents)
    # html = response.read()
    # author = json.loads(html)['items'][0]['volumeInfo']['authors'][0]
    # return author
    return "Hey! The service is up, how about doing something useful"
# [END app]

if __name__ == '__main__':
    app.run(debug=True)
