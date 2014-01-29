from PrismAPI.Main import PrismAPI

################################
##  test.py file used for demonstration
##  of jive in python
################################

if __name__ == '__main__':
    # log on to prism.leidos.com and edit your profile to see your id...it's in the url (targetUser=12345)
    p_id = '<user_id>'
    prism = PrismAPI.PrismAPI()
    # jive uses basic http auth
    prism.set_basic_auth("<username>","<password>")
##    stuff = prism.page_prism(25,25,'summary') # page results of users and print emails
##    for s in stuff['list']:
##        print s['emails'][0]['value']
##    # get me
##    me = prism.me(p_id)
##    print me['emails'][0]['value'] # print my email
    prism.post_announcement(p_id,"python subject","hello from python!")
