from django.db.models import Q
from django.contrib.postgres.search import SearchVector,SearchQuery,SearchRank
from goods.models import Products


def q_search(query):
    vector=SearchVector('name',)
    query=SearchQuery(query)
    

    return Products.objects.annotate(rank=SearchRank(vector,query)).filter(rank__gt=0.005).order_by("-rank")
    
    
