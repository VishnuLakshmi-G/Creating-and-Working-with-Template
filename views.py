# checker/views.py
from django.shortcuts import render

def odd_even_and_name_filter(request):
    result = None
    number = None
    query = ''
    filtered_words = []
    words = ["Hello", "Helen", "Henry", "world", "Russia", "Luna", "India", "Vietnam"]

    if request.method == 'POST':
        if 'number' in request.POST:
            # Odd or Even Checker form submission
            number = int(request.POST['number'])
            if number % 2 == 0:
                result = 'even'
            else:
                result = 'odd'
        
        elif 'query' in request.POST:
            # Name Filter form submission
            query = request.POST['query']
            filtered_words = [word for word in words if word.lower().startswith(query.lower())]

    return render(request, 'combined.html', {
        'result': result, 
        'number': number, 
        'filtered_words': filtered_words, 
        'query': query
    })
