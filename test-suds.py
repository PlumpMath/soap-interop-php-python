import suds

if True:
    #
    # Test case for my WSDL - works
    #
    url = "http://sdr.cs.colorado.edu:4444/?wsdl"
    client = suds.client.Client(url)
    print client.service.getQuestionMetadata("one", "two", "tree")
else:
    #
    # testcase for spyne WSDL - works too
    #
    url = "http://localhost:8000/?wsdl"
    client = suds.client.Client(url)
    print client.service.say_hello("one", 3)
