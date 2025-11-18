import pytest
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()

@pytest.mark.django_db
def test_signup(client):
    response = client.post(reverse('signup'),{
        'username':' newuser ',
        'password1':' strongpassword123 ',
        'password2':' strongpassword123 ',

    })

    assert response.status_code == 302 #this checks if your app redirected the user after sign-up
    assert User.objects.filter(username ='newuser').exists()

@pytest.mark.django_db
def test_signin(client, django_user_model): #pytest gives access to Django's user model through this model
    django_user_model.objects.create_user( #different from the signup signin should create user first
        username='existinguser',
        password='mypassword'
    )

    response = client.post(reverse('signin'), {
        'username':'existinguser',
        'password':'mypassword',
    })

    assert response.status_code == 302
    assert '_auth_user_id'in client.session

    #inside the session, if login was successful django adds 'auth_user_id'