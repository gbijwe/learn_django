## Problems & Solutions ##

### major changes -1 ###
- added functioning of admin and company seperately.
- added resource type drop down menu.

### Mar 2 ###
 
- users added through custom form in website cannot be used to login in through the login page. [different roles/types for users](https://forum.djangoproject.com/t/how-to-create-custom-users-with-different-roles-types/20772/2)
    - **SOLVED: in settings.py:** `AUTH_USER_MODEL = "base_app.CustomUsers"`
- Custom login view not working.  Need to check conditionals for `usr_type` at login to redirect accordingly.
    - **--> SOLVED: used GEMINI for rewriting StackExch code for my needs. also, `from django.urls import reverse` by defining function.**
- CSRF_verification_failed. Request aborted. NGROK.
When CSRF token is added, it does not work at all, locally or no NGROK.
- `@login_required` decorator not working.

### Mar 3 ###

- logout page not functioning, need POST method to logout. not implemented. *(Mar 2)*
    - **SOLVED: using POST form (StackExchange) in place of a button** Added `btn btn-danger` class in bootstrap

### Mar 8 ###
- ```
    Environment:


    Request Method: GET
    Request URL: http://127.0.0.1:8090/land-admin/

    Django Version: 5.0.2
    Python Version: 3.10.11
    Installed Applications:
    ['django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'base_app',
    'crispy_forms',
    'crispy_bootstrap4']
    Installed Middleware:
    ['django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware']



    Traceback (most recent call last):
    File "/Users/gauravbijwe/Developer/CORECO/prototype/venv/lib/python3.10/site-packages/django/core/handlers/exception.py", line 55, in inner
        response = get_response(request)
    File "/Users/gauravbijwe/Developer/CORECO/prototype/venv/lib/python3.10/site-packages/django/core/handlers/base.py", line 197, in _get_response
        response = wrapped_callback(request, *callback_args, **callback_kwargs)
    File "/Users/gauravbijwe/Developer/CORECO/prototype/bench_app/bench_app/base_app/views.py", line 39, in myAdmin
        "usr_type": request.user.usr_type
    File "/Users/gauravbijwe/Developer/CORECO/prototype/venv/lib/python3.10/site-packages/django/utils/functional.py", line 253, in inner
        return func(_wrapped, *args)

    Exception Type: AttributeError at /land-admin/
    Exception Value: 'AnonymousUser' object has no attribute 'usr_type'

- How to give context in class-based-views? 
    - Need to find a way so that I can use conditional formatting for the templates such as usr_type etc in ListView, CreateView, UpdateView 
    
### Mar 9 ###
- Profile page --> Log book of all resources hired and how long hired for. (using date)
- List view page --> Cards of Resource types and their numbers. On click, go to list view of resource type with detail


- NoReverseMatch found: 
    - with no arguments
    - with (') argument
    - with (6') argument