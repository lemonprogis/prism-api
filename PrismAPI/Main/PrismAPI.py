import requests, json, urllib2,base64
from requests.auth import HTTPBasicAuth

class PrismAPI():
    '''
        Leidos Prism API in Python
    '''

    MAIN_URL = "https://prism.leidos.com/api/core/v3/"
    PEOPLE = "people/"
    MEMBERS = "members/"
    ANNOUNCEMENTS = "announcements/"
    PLACES = "places/"
    
    actions = {'following':'@following',
               'reports':'@reports',
               'followers':'@followers',
               'manager':'@manager',
               'summary':'@summary',
               'images':'images',
               'followingIn':'followingIn',
               'colleagues':'@colleagues',
               'avatar':'avatar',
               'activities':'activities'
               }
    
    def __init__(self):
        pass

    def set_basic_auth(self, username, password):
        self.username = username
        self.auth = HTTPBasicAuth(username,password)
        
    def escaper(self,data):
        return json.loads(data.content.replace("throw 'allowIllegalResourceCall is false.';",""))


    def page_prism(self, count, start_index, action):
        url = PrismAPI.MAIN_URL+PrismAPI.PEOPLE+"?sort=firstNameAsc&fields=%s&count=%s&startIndex=%s" % (PrismAPI.actions[action],
                                                                                                         str(count),
                                                                                                         str(start_index))
        data = requests.get(url,auth=self.auth,verify=False)
        return self.escaper(data)

    def me(self,id):
        url = PrismAPI.MAIN_URL+PrismAPI.PEOPLE+"%s" % id
        data = requests.get(url,auth=self.auth,verify=False)
        return self.escaper(data)

    def post_announcement(self,id, subject, text):
        payload = {
                "subject":subject,
                "content":{
                    "type":"text/html",
                    "text":text
                    }
            }
        headers = { "Content-Type": "application/json", "Authorization": self.auth }
        requests.post(PrismAPI.MAIN_URL+PrismAPI.PEOPLE+id+"/"+PrismAPI.ANNOUNCEMENTS, data=json.dumps(payload),headers=headers, verify=False)


    def status_update(self, id, subject, text):
        payload = {
                "content":{
                    "type":"text/html",
                    "text":text
                    },
                "subject":subject,
                "type":"document",
            }
        headers = { "Content-Type": "application/json", "Authorization": self.auth }
        data = requests.post(PrismAPI.MAIN_URL+PrismAPI.PEOPLE+id+PrismAPI.ANNOUNCEMENTS, data=json.dumps(payload),headers=headers, verify=False)
        print data
