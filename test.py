from PrismAPI.Main import PrismAPI

################################
##  test.py file used for demonstration
##  of jive in python
################################

# log on to prism.leidos.com and edit your profile to see your id...it's in the url (targetUser=12345)
p_id = '<user_id>'
prism = PrismAPI.PrismAPI()
# jive uses basic http auth
prism.set_basic_auth("<username>","<password>")
me = prism.me(p_id)
print me['emails'][0]['value'] # print my email

# searching 
query = ['programmer']
results = prism.search_people(query,25,0)

print prism.simple_view(results) # simple view of jive information

