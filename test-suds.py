import suds

import suds
url = "http://sdr.cs.colorado.edu:4444/?wsdl"
client = suds.client.Client(url)
print client.service.getQuestionMetadata("one", "two", "tree")
