from django.shortcuts import render, redirect
from personal.forms import ContactForm
from personal.forms import RegistrationForm
from personal.forms import SignupForm

# add to your views

def signup(request):
    form_class = SignupForm
    if request.method == 'POST':
        form = form_class(data=request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            contact_name = request.POST.get('contact_name', '')
            contact_email = request.POST.get('contact_email', '')

            return render(request, 'personal/success.html', {'text': contact_name})
        else:
            return render(request, 'personal/error_message.html')

    return render(request, 'personal/signup.html', {'form': form_class, })


def contact(request):
    form_class = ContactForm
    if request.method == 'POST':
        form = form_class(data=request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            #post.user = request.user
            post.save()
            contact_name = request.POST.get('contact_name', '')
            contact_email = request.POST.get('contact_email', '')
            form_content = request.POST.get('content', '')
            return render(request, 'contact/contact_redirect.html', {'text': contact_name})

        else:
            return render(request, 'personal/error_message.html')

    return render(request, 'contact/contact.html', {'form': form_class, })



def index(request):
    return render(request, 'personal/home.html')

def about(request):
    return render(request, 'personal/about.html')

def products(request):
    return render(request, 'personal/products.html')


def signupREMOVE(request):

    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'personal/success.html')
            #return redirect('/blog')
        else:
            return render(request, 'personal/error_message.html')


    else:
        form = RegistrationForm()
        args = {'form': form}
        return render(request, 'personal/signup.html', args)





