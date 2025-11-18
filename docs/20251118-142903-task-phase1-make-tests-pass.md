# Phase 1: Make Tests Pass

**Target Audience**: Beginner Django Students
**Estimated Time**: 2-3 hours
**Difficulty**: Medium

---

## 🎯 Objective

Make the two existing tests in `accounts/tests/test_auth.py` pass by learning Django's core building blocks:
- URL routing and reverse resolution
- Django Forms system
- View functions and request/response cycle
- Authentication flow

**Success Criteria**: Running `pytest` should show all tests passing (2/2 passed).

---

## 📋 Prerequisites

Current project state:
- ✅ `accounts/models.py` → CustomUser model exists
- ✅ `accounts/tests/test_auth.py` → Two tests written (but not working)
- ✅ Database migrations applied
- ❌ `accounts/urls.py` → Missing (you'll create this)
- ❌ `accounts/forms.py` → Missing (you'll create this)
- ❌ `accounts/views.py` → Empty (you'll add views)

**If you run tests now**:
```bash
pytest
# ERROR: NoReverseMatch: Reverse for 'signup' not found.
```
This is expected! URLs aren't defined yet.

---

## 📝 Step-by-Step Instructions

### Step 1: Create URL Configuration

**What you'll do:**
- Create `accounts/urls.py` file
- Define 4 URL patterns (signup, signin, signout, profile)
- Name each URL (like `name='signup'`)

**Minimal example** (you complete it):
```python
from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    # Add the other 3 URLs yourself...
]
```

**Then** update `config/urls.py` to include accounts URLs.

**Small hint**:
```python
from django.urls import path, include  # Don't forget include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),  # Add this line
]
```

---

### Step 2: Create Forms Module

**What you'll do:**
- Create `accounts/forms.py` file
- Create a signup form (extend Django's `UserCreationForm`)
- Add validation to strip whitespace from username

**Why**: Your test sends `' newuser '` and expects it to be saved as `'newuser'`.

**Minimal example** (you complete it):
```python
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class SignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'password1', 'password2')

    def clean_username(self):
        # Get username and use .strip() to clean it
        pass  # You write this
```

**Note**: For signin, import and use `AuthenticationForm`, no need to create a new form.

---

### Step 3: Implement Views

**What you'll do:**
Write 4 view functions:

#### 3.1 `signup_view`
- GET request → Display form
- POST request → Validate form, create user, redirect

**Minimal structure example**:
```python
from django.shortcuts import render, redirect
from .forms import SignUpForm

def signup_view(request):
    if request.method == 'POST':
        # Create form with POST data
        # Validate (is_valid check)
        # Save
        # Redirect
        pass
    else:
        # Create empty form
        pass
    # Render to template
```

**Note**: Think about where to redirect after saving the form.

---

#### 3.2 `signin_view`
- GET request → Display form
- POST request → Authenticate, login, redirect

**Minimal structure example**:
```python
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm

def signin_view(request):
    if request.method == 'POST':
        # Use AuthenticationForm (needs request and data)
        # Check is_valid
        # Get user with form.get_user()
        # Call login(request, user) to create session
        pass
    # ...
```

**Note**: `AuthenticationForm` works differently - constructor needs `request` and `data`.

---

#### 3.3 `signout_view`
- Logout user, redirect to signin page

**Minimal example**:
```python
from django.contrib.auth import logout

def signout_view(request):
    # Call logout(request)
    # Redirect
    pass
```

---

#### 3.4 `profile_view`
- **Only** logged-in users should access
- Render simple context

**Minimal example**:
```python
from django.contrib.auth.decorators import login_required

@login_required  # This decorator is crucial!
def profile_view(request):
    # Render to template
    pass
```

**Note**: Don't forget `@login_required` decorator, otherwise anyone can access.

---

## ✅ Verification Steps

Check after each step:

### Are URLs working correctly?
```bash
python manage.py shell
```
```python
from django.urls import reverse
print(reverse('signup'))    # Returns /accounts/signup/
print(reverse('signin'))    # Returns /accounts/signin/
print(reverse('profile'))   # Returns /accounts/profile/
```
**Why**: Your test file uses `reverse('signup')`, if this fails, tests will fail.

---

### Are Forms working correctly?
```bash
python manage.py shell
```
```python
from accounts.forms import SignUpForm
form = SignUpForm(data={'username': ' test ', 'password1': 'strong123', 'password2': 'strong123'})
form.is_valid()  # Should return True
form.cleaned_data['username']  # Should return 'test' (without spaces)
```
**Why**: Your form validation must work correctly.

---

### Can Views be imported?
```bash
python manage.py check
```
**Why**: If there are syntax errors, you'll see them here.

---

### Are Tests passing?
```bash
pytest
```
**Expected output**:
```
accounts/tests/test_auth.py::test_signup PASSED
accounts/tests/test_auth.py::test_signin PASSED
====== 2 passed in 0.5s ======
```
**Why**: This is your whole goal! Tests must pass.

---

## 🧪 Test Commands

### Run all tests
```bash
pytest
```
**Purpose**: Both signup and signin tests should pass.

---

### Verbose mode with detailed output
```bash
pytest -v
```
**Purpose**: See which tests pass/fail and when.

---

### Run only signup test
```bash
pytest accounts/tests/test_auth.py::test_signup
```
**Purpose**: Test signup view without worrying about other tests.

---

### Run only signin test
```bash
pytest accounts/tests/test_auth.py::test_signin
```
**Purpose**: Test signin view without looking at signup.

---

### Show print statements
```bash
pytest -s
```
**Purpose**: If you added debug `print()` to views, you can see them.

---

## ⚠️ Common Pitfalls

### URL Pattern Names
❌ **Wrong**:
```python
path('signup/', views.signup_view),  # No name!
```
✅ **Correct**:
```python
path('signup/', views.signup_view, name='signup'),  # Test expects this
```

---

### AuthenticationForm Constructor
❌ **Wrong**:
```python
form = AuthenticationForm(request.POST)  # Will error!
```
✅ **Correct**:
```python
form = AuthenticationForm(request, data=request.POST)  # First param is request
```

---

### Login Function
❌ **Wrong**:
```python
user.login()  # User has no such method
```
✅ **Correct**:
```python
from django.contrib.auth import login
login(request, user)  # Django's login function
```

---

### Redirect After POST
❌ **Wrong**:
```python
if form.is_valid():
    form.save()
    return render(request, 'success.html')  # Violates POST-redirect-GET pattern
```
✅ **Correct**:
```python
if form.is_valid():
    form.save()
    return redirect('profile')  # Use redirect
```
**Why**: Browser refresh shouldn't re-submit form.

---

### login_required Decorator
❌ **Wrong**:
```python
def profile_view(request):  # Anyone can access!
    return render(request, 'profile.html')
```
✅ **Correct**:
```python
@login_required
def profile_view(request):  # Only logged-in users
    return render(request, 'profile.html')
```

---

## 💡 Tips and References

### Django Docs - Must Read
1. **URL dispatcher**: https://docs.djangoproject.com/en/5.2/topics/http/urls/
   - How `path()` function works
   - How to make app URLs modular with `include()`
   - Why `reverse()` is important

2. **Forms**: https://docs.djangoproject.com/en/5.2/topics/forms/
   - When to call `is_valid()`
   - What is `cleaned_data`
   - How `clean_<fieldname>()` method works

3. **Authentication**: https://docs.djangoproject.com/en/5.2/topics/auth/default/
   - `login()` and `logout()` functions
   - `@login_required` decorator
   - `AuthenticationForm` vs `UserCreationForm`

---

### Debugging Tips

**Problem**: `NoReverseMatch: 'signup'`
- ✅ Solution: Did you add `name='signup'` in `accounts/urls.py`?
- ✅ Solution: Did you `include('accounts.urls')` in `config/urls.py`?

**Problem**: `AttributeError: module 'accounts.views' has no attribute 'signup_view'`
- ✅ Solution: You might have misspelled the function name in `views.py`
- ✅ Solution: You might not have written the function at all

**Problem**: Test passes but user isn't created
- ✅ Solution: You might have forgotten to call `form.save()`
- ✅ Solution: You're trying to save without checking `is_valid()`

**Problem**: Signin test fails, "Invalid credentials"
- ✅ Solution: Are you using `create_user()` in test? Not `create()`!
- ✅ Solution: If password isn't hashed, login won't work

---

### Understanding the Test File

Open `accounts/tests/test_auth.py` and examine:

**test_signup expects:**
1. POST request to `/accounts/signup/`
2. Send username, password1, password2
3. Response should be 302 (redirect)
4. User should exist in database

**test_signin expects:**
1. First create a user (manually)
2. POST request to `/accounts/signin/`
3. Send username and password
4. Response should be 302 (redirect)
5. Session should have `_auth_user_id` (shows login worked)

---

### Recommended Order

1. ✅ First create URLs (accounts/urls.py + config/urls.py)
2. ✅ Then write Forms (accounts/forms.py)
3. ✅ Finally implement Views
4. ✅ Test each step in shell
5. ✅ Run `pytest` when everything is done

**Why this order**: Can't test views without URLs, views won't work without forms.

---

## 🔀 Git Workflow for This Phase

This phase has **6 separate topics**, each should be its own branch and PR.

### Recommended Branch Structure

**Important**: After each PR is merged to `main`, create the next branch from fresh `main`.

#### Topic 1: URL Configuration
```bash
git checkout main
git pull origin main
git checkout -b task/T1-url-configuration

# Work: Create accounts/urls.py, update config/urls.py
# Test: python manage.py shell → test reverse()

git add accounts/urls.py config/urls.py
git commit -m "feat: add URL configuration for accounts app

- Created accounts/urls.py with signup, signin, signout, profile patterns
- Updated config/urls.py to include accounts URLs
- All URL patterns have names for reverse resolution"

git push -u origin task/T1-url-configuration
# Create PR → Merge → Delete branch
```

**PR Title**: `Phase 1: Add URL configuration for accounts app`

---

#### Topic 2: Forms Module
```bash
git checkout main
git pull origin main
git checkout -b task/T1-forms-module

# Work: Create accounts/forms.py with SignUpForm
# Test: python manage.py shell → test form validation

git add accounts/forms.py
git commit -m "feat: create SignUpForm with username validation

- Extended UserCreationForm for CustomUser model
- Added clean_username() to strip whitespace
- Form validates username, password1, password2 fields"

git push -u origin task/T1-forms-module
# Create PR → Merge → Delete branch
```

**PR Title**: `Phase 1: Create forms module with signup form`

---

#### Topic 3: Signup View
```bash
git checkout main
git pull origin main
git checkout -b task/T1-signup-view

# Work: Implement signup_view in accounts/views.py
# Test: Run server, try accessing /accounts/signup/ (will show TemplateDoesNotExist - that's OK for now)

git add accounts/views.py
git commit -m "feat: implement signup view with form handling

- Handle GET request to display empty form
- Handle POST request to validate and save user
- Redirect to profile after successful signup
- Render signup.html template (placeholder for Phase 2)"

git push -u origin task/T1-signup-view
# Create PR → Merge → Delete branch
```

**PR Title**: `Phase 1: Implement signup view`

---

#### Topic 4: Signin View
```bash
git checkout main
git pull origin main
git checkout -b task/T1-signin-view

# Work: Implement signin_view
# Test: Check authentication logic works

git add accounts/views.py
git commit -m "feat: implement signin view with authentication

- Use AuthenticationForm for credential validation
- Call login() to create user session
- Redirect to profile after successful login
- Render signin.html template (placeholder for Phase 2)"

git push -u origin task/T1-signin-view
# Create PR → Merge → Delete branch
```

**PR Title**: `Phase 1: Implement signin view`

---

#### Topic 5: Signout and Profile Views
```bash
git checkout main
git pull origin main
git checkout -b task/T1-signout-profile-views

# Work: Implement both signout_view and profile_view
# Test: Check @login_required decorator works

git add accounts/views.py
git commit -m "feat: implement signout and profile views

- Added signout_view to logout user and redirect to signin
- Added profile_view with @login_required decorator
- Profile view renders profile.html (placeholder for Phase 2)"

git push -u origin task/T1-signout-profile-views
# Create PR → Merge → Delete branch
```

**PR Title**: `Phase 1: Implement signout and profile views`

---

#### Topic 6: Verify Tests Pass
```bash
git checkout main
git pull origin main

# At this point, all code from previous PRs is merged
# Run tests to verify everything works

pytest -v

# If tests pass (2/2 passed), Phase 1 complete!
# If tests fail, create fix branches: task/T1-fix-<issue>
```

---

### Phase 1 Commit Message Examples

**Good examples for this phase:**
```bash
"feat: add URL configuration for accounts app"
"feat: create SignUpForm with username validation"
"feat: implement signup view with form handling"
"feat: implement signin view with authentication"
"feat: implement signout and profile views"
"fix: correct redirect URL after signup"
"fix: handle empty form data in signin view"
"refactor: extract form creation to separate method"
"test: verify URL reverse resolution works"
```

---

### Verification Before Each PR

Before creating PR, check:
- [ ] `python manage.py check` → No errors
- [ ] `python manage.py runserver` → Starts without errors
- [ ] For URL topic: `reverse()` works in shell
- [ ] For forms topic: Form validation works in shell
- [ ] For views topic: View can be imported without errors
- [ ] No debug print statements left
- [ ] No commented code

---

### After Phase 1 Complete

```bash
# All 6 PRs merged to main
# Tests passing (pytest → 2/2 passed)

git checkout main
git pull origin main

# Ready to start Phase 2!
```

**📖 For detailed Git workflow, see**: [GIT-WORKFLOW.md](../GIT-WORKFLOW.md)

---

## 🎓 What You Learned

✅ Django URL routing and reverse resolution
✅ Django Forms framework (validation, cleaning)
✅ Function-based views (GET vs POST)
✅ Authentication system (login, logout)
✅ Decorator usage (@login_required)
✅ Test-driven development approach
✅ POST-redirect-GET pattern

**Next Step**: In Phase 2, you'll add templates to these views to create the user interface!
