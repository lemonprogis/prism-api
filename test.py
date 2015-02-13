from PrismAPI.Main import PrismAPI
import os

################################
##  test.py file used for demonstration
##  of jive in python
################################

# log on to prism.leidos.com and edit your profile to see your id...it's in the url (targetUser=12345)
#p_id = '<user_id>'
prism = PrismAPI.PrismAPI()
# set your Leidos username/password as environment variables
PRISM_USERNAME = os.environ.get('PRISM_USERNAME')
PRISM_PASSWORD = os.environ.get('PRISM_PASSWORD')
# Jive uses basic http auth
prism.set_basic_auth(PRISM_USERNAME,PRISM_PASSWORD)
# searching 
query = ['President']
results = prism.search_people(query,100,0)

s_results = prism.simple_view(results) # simple view of jive information

for result in s_results:
    print "%s, %s" % (result["Display Name"], result['Title'])
