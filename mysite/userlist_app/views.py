from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages 
from userlist_app.models import User

def test(request):
    return HttpResponse("This is a test")

def index(request):
    all_users = User.objects.all()
    return render(request, 'index.html', {
        'all_users': all_users,
    })

def add_user(request):
    if request.method == "POST":

        details = {}

        details['first-name'] = request.POST.get('first-name','')
        details['second-name'] = request.POST.get('second-name','')
        details['country'] = request.POST.get('country','')        

        # _error_summary = get_errors(_form)

        # if _error_summary:            
        #     return render_template("add_user.html", error_summary=_error_summary)

        invalid_input = list()

        for i, k in details.items():
            if k == "":
                invalid_input.append(i)
        
        if invalid_input:
            messages.add_message(
                request, messages.WARNING, f"Following information is required: {', '.join(invalid_input)}")
            return render(request, "add_user.html")

        new_user = User(firstname=details['first-name'],
                         secondname=details['second-name'],
                         country=details['country'])

        print(new_user)
        
        new_user.save()

        return redirect("/")

    return render(request, "add_user.html")


# def get_errors(form_to_validate):
#         invalid_input = list()

#         field_name_provider = FieldNameProvider()

#         for i, k in form_to_validate.items():
#             if k == "":
#                 invalid_input.append(field_name_provider.get_name(i))
        
#         if invalid_input:
#             error_summary = f"Following information is required: {', '.join(invalid_input)}"
#             return error_summary
