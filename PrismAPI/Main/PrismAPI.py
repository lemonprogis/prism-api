import requests, json, urllib2,base64
from requests.auth import HTTPBasicAuth

class PrismAPI():
    '''
        Prism (Jive) API for Python
    '''

    MAIN_URL = "https://prism.leidos.com/api/core/v3/"
    PEOPLE = "people/"
    PEOPLE_SEARCH = "search/people?filter=search(%s)&count=%s&startIndex=%s"
    PLACE_SEARCH = "search/place?filter=search(%s)&count=%s&startIndex=%s"
    CONTENT_SEARCH = "search/content?filter=search(%s)&count=%s&startIndex=%s"
    MEMBERS = "members/"
    ANNOUNCEMENTS = "announcements/"
    PLACES = "places/"
    CONTENTS = "contents/"

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

    def make_request(self,url):
        return self.escaper(requests.get(url,auth=self.auth,verify=False))

    def post_request(self,url,data):
        headers = {'Content-Type': 'application/json'}
        return requests.post(url,auth=self.auth, data=data, headers=headers)
        
    def status_update(self,status):
        url = PrismAPI.MAIN_URL + PrismAPI.CONTENTS
        headers = {'Content-Type': 'application/json'}
        data = json.dumps(  
         { "content": 
              {  
               "type": "text/html",  
               "text": status 
               },  
           "type": "update"
         })  
        return requests.post(url,auth=self.auth, data=data, headers=headers)    

    def page_prism(self, action, count=25, start_index=0):
        url = PrismAPI.MAIN_URL+PrismAPI.PEOPLE+"?sort=firstNameAsc&fields=%s&count=%s&startIndex=%s" % (PrismAPI.actions[action],
                                                                                                         str(count),
                                                                                                         str(start_index))
        json_data = self.make_request(url)
        return [self.get_person(p['id']) for p in json_data['list']]

    def get_person(self, id):
        url = PrismAPI.MAIN_URL+PrismAPI.PEOPLE+"%s" % id
        print url
        return self.make_request(url)

    def search_people(self,query,count=25,start_index=0):
        url = PrismAPI.MAIN_URL+PrismAPI.PEOPLE_SEARCH % (",".join(query),str(count),str(start_index))
        #print url
        return self.make_request(url)

    def search_content(self,query,count=25,start_index=0):
        url = PrismAPI.MAIN_URL+PrismAPI.PEOPLE_CONTENT % (",".join(query),str(count),str(start_index))
        #print url
        return self.make_request(url)
    def next(self,results):
        url = results['links']['next']
        return self.make_request(url)

    def previous(self, results):
        url = results['links']['previous']
        return self.make_request(url)

    def simple_view(self,results):
        return [{str(r['jive_label']) : str(r['value']) for r in result['jive']['profile']} for result in results['list']]



