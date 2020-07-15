from django.shortcuts import render


def calculator_view(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    elif request.method == 'POST':
        # print(request.POST)
        context = {
            'first_number': request.POST.get('first_number'),
            'second_number': request.POST.get('second_number'),
            'acton': request.POST.get('action')
        }
        if context['first_number'] and context['second_number'] and context['acton']:
            if context['acton'] == '-':
                context['result'] = '= ' + str(int(context['first_number']) - int(context['second_number']))
            elif context['acton'] == '+':
                context['result'] = '= ' + str(int(context['first_number']) + int(context['second_number']))
            elif context['acton'] == '*':
                context['result'] = '= ' + str(int(context['first_number']) * int(context['second_number']))
            elif context['acton'] == '/':
                try:
                    context['result'] = '= ' + str(int(context['first_number']) / int(context['second_number']))
                except ZeroDivisionError:
                    context['result'] = 'ZeroDivisonError'
            context['first_number'] = 'Result: ' + context['first_number']
            return render(request, 'index.html', context)
        else:
            return render(request, 'index.html')
