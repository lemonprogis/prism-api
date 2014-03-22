prism-api
=========

Built off Jive API for Leidos Prism Social Networking
Requires requests library 

Usage
=====

Authentication
--------------

You can use this to make requests to our Jive API 
Only requires HTTPBasicAuth  
Just use your user name and password to start searching and using the API

Every thing is returned as json objects or lists of json objects for easy navigation. 
Most of the generic keys are included in the API.

<pre>
from PrismAPI.Main import PrismAPI

prism = PrismAPI.PrismAPI()
prism.set_basic_auth("username","pword")
</pre>

Searching
---------
In order to search for key words in people, pass in a list of strings to search.
Count and start index have defaults but can be used for paging through results

<pre>
search = ['programmer']
results = prism.search_people(search,25,0) # returns a json object
</pre>

Use the next and previous functions to go through pages
<pre>
search = ['programmer']
results = prism.search_people(search,25,0) # returns a json object
more_results = prism.next(results)
prev_results = prism.previous(more_results)
</pre>

Can use get a single person by prism id

<pre>
 me = prism.get_person("user_id")
</pre>

If you just want to get a simple view of jive information, use the simple_view function

<pre>
results = prism.search_people(search,25,0)
simple_view = prism.simple_view(results)
</pre>

Output
------

JSON objects

Disclaimer
==========

This code here has no warranties. It can be freely distributed and modified to suit your needs. 

