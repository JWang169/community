# community
create account funcionality for website

accounts/models.py: 
    create the user model by importing "auth.models.User" and "auth.models.PermissionsMixin"

accounts/views.py:
    create a signup view, connect it to a UserCreateForm
    
accounts/forms.py:
    create a usercreateform by importing "UserCreationForm", set customized label for username and email
