from django.shortcuts import render
from application.models import names

def index(request):
    context = {}
    if request.method == "POST":
        context = {}
        fname = request.POST['fname']
        lname = request.POST['lname']
        namesum = fname + lname
#Now I want to check true love in this string called namesum

        t = namesum.count('t')
        r = namesum.count('r')
        u = namesum.count('u')
        e = namesum.count('e')

        first_person = t + r + u + e



        l = namesum.count('l')
        o = namesum.count('o')
        v = namesum.count('v')
        e_2 = namesum.count('e')

        last_person = l + o + v + e_2

        
        final_name = str(first_person) + str(last_person)

        context = {"final_name":final_name}
        
    return render(request,"index.html",context)