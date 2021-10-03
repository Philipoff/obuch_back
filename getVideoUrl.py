def getVideoUrl(query):
    query= query.split()
    query='+'.join(query)
    url="https://www.youtube.com/results?search_query="+query
    return url