from items.models import Item
from django.db.models import Q


def q_search(query):
    if query.isdigit() and len(query) <= 5:
        return Item.objects.filter(id=int(query))

    keywords = [word for word in query.split() if len(word) > 2]

    q_objects = Q()
    for token in keywords:
        q_objects |= Q(name__icontains=token)
        q_objects |= Q(description__icontains=token)

    return Item.objects.filter(q_objects)
