from PrismAPI.Main import PrismAPI



if __name__ == '__main__':
    p_id = '<id>'
    prism = PrismAPI.PrismAPI()
    prism.set_basic_auth("<username>","<password>")
##    stuff = prism.page_prism(25,25,'summary')
##    for s in stuff['list']:
##        print s['emails'][0]['value']
##
##    me = prism.me(p_id)
##    print me['emails'][0]['value']
    print prism.post_announcement(p_id,"python subject","hello from python!")
