import urllib.request
import json
from django.shortcuts import render


def index(request):

    if request.method == 'POST':
        city = request.POST['city']
        city = city.lower()
        lst = []
        lst = city.split(' ')
        city = '+'.join(lst)
        source = urllib.request.urlopen('https://openlibrary.org/search.json?q=' +
                                        city ).read()
        list_of_data = json.loads(source)

        data = {
            "authorname": str(list_of_data['docs'][0]['author_name'][0]),
            "genre": str(list_of_data['docs'][0]['subject'][1]),
            
        }
        print(data)
    else:
        data = {}

    return render(request, "weatherApp/index.html", data)



    