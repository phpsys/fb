import facebook

api_version = "2.9"
api_token = ""

graph = facebook.GraphAPI(access_token=api_token, version=api_version)
page = graph.get_object('6127898346')

print(page)