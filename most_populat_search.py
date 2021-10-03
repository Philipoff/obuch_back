def most_popular_search(collection_themes, subject, count=5):
    documents = collection_themes.aggregate(
        [{"$match": {"subject": {"$eq": subject}}}, {"$sort": {"count": -1}}, {"$limit": count}])
    result = []
    for theme in documents:
        result.append(theme["theme"])

    return result
