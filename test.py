from PrismAPI.Main import PrismAPI

################################
##  test.py file used for demonstration
##  of jive in python
################################

# log on to prism.leidos.com and edit your profile to see your id...it's in the url (targetUser=12345)
#p_id = '<user_id>'
prism = PrismAPI.PrismAPI()
# jive uses basic http auth
prism.set_basic_auth("brigglere","13S!ri-3")
# searching 
query = ['programmer']
results = prism.search_people(query,25,0)

s_results = prism.simple_view(results) # simple view of jive information

for result in s_results:
    print "%s, %s" % (result["Display Name"], result['Title'])

