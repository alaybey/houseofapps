from django.shortcuts import render
from .voyager import get_apod, search_images,search_next_page
from django.contrib.auth.decorators import login_required


@login_required()
def index(request):
    context = get_apod()    # apod and info getting from Voyager def :wq
    return render(request, 'observatory/index.html', {'context': context})

@login_required()
def search(request):
        if request.method=="POST":
            keyword = request.POST.get('keyword')
            data = search_images(keyword)       # Get images from Voyager tool with using images.api of nasa
            total_hits= data['collection']['metadata']['total_hits']    # total image
            results = []            # list for return
            page=0      # collections page at json.
            while True:
                for i in data['collection']['items']:   # foreach for data of items
                    results.append(i)                   # insert to list
                if "rel': 'next'" in str(data['collection']):       # checking next page
                    data = search_next_page(data['collection']['links'][page]['href'])      # next page url include 'href'
                    page=1                  # On multiple pages always has a 'next' value of 1 except the first page (0)
                else:
                    break

            return render(request, 'observatory/results.html', {'keyword':keyword, 'total': total_hits, 'results': results})

        else:
            return index(request)
