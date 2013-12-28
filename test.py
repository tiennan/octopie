import octopie

client = octopie.GitHubAPI()

try:
   result = client.search.users.get(q='language:python')
   print result.headers
   print result.json()
except APIError as e:
    print e