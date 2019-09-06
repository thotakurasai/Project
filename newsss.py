from newsapi import NewsApiClient

newsapi = NewsApiClient(api_key='5579350968fb43f6861a0db1b887235c')

sources = newsapi.get_sources()

print (sources)
