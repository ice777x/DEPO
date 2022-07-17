import requests
import json

acc_token = None


class Telegraph:
    def __init__(self, text):
        self.text = text
        self.content = None

    def make_content(self):
        dedi = {"tag": "p", "children": [self.text]}
        al = json.dumps(dedi)
        self.content = "[{}]".format(al)

    def get_page(self):
        self.make_content()
        if self.content:
            url = f"https://api.telegra.ph/createPage?access_token={acc_token}&title=Sample+Page&author_name=ice777x&content={self.content}&return_content=true"
            r = requests.get(url)
            data = r.json()
            return data["result"]["url"]
        else:
            return None
