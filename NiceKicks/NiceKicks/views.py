from django.shortcuts import render
import pyrebase
from django.contrib import auth
config = {

    'apiKey': "AIzaSyDbqvRmUmE5vctdRuws-tXNMQ2u9oC3G9I",
    'authDomain': "nicekicks-dab54.firebaseapp.com",
    'databaseURL': "https://nicekicks-dab54.firebaseio.com",
    'projectId': "nicekicks-dab54",
    'storageBucket': "nicekicks-dab54.appspot.com",
    'messagingSenderId': "446750447754",
    'appId': "1:446750447754:web:862eea5c93797b7e563573",
    'measurementId': "G-15P0S42P1B"
}

firebase = pyrebase.initialize_app(config)
authe = firebase.auth()


def signIn(request):

    return render(request, "signIn.html")


def postsign(request):
    email = request.POST.get('email')
    password = request.POST.get('password')

    try:
        user = authe.sign_in_with_email_and_password(email, password)
    except:
        message = "invalid credentials"
        return render(request, "signIn.html", {"message": message})
    print(user['idToken'])
    session_id = user['idToken']
    request.session['uid'] = str(session_id)

    return render(request, "welcome.html", {"e": email})


def logout(request):
    auth.logout(request)
    return render(request, 'signIn.html')
