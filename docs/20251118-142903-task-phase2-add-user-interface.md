# Phase 2: Add User Interface

**Target Audience**: Beginner Django Students
**Estimated Time**: 2-3 hours
**Difficulty**: Medium-Hard

---

## 🎯 Objective

Your views from Phase 1 work but there's no user interface. In this phase:
- Create HTML pages using Django Template system
- Use template inheritance (base.html) to avoid code repetition
- Provide user feedback with Django Messages Framework
- Learn how to render forms in templates

**Success Criteria**: Navigate to `/accounts/signup/` in browser and see a working form.

---

## 📋 Prerequisites

You must have completed Phase 1:
- ✅ Tests passing (`pytest` → 2/2 passed)
- ✅ URLs defined
- ✅ Views implemented
- ✅ Forms created

**Currently**:
- Views use `render()` but template files don't exist
- Navigating to pages in browser gives `TemplateDoesNotExist` error

---

## 📝 Step-by-Step Instructions

### Step 1: Create Template Directory Structure

**What you'll do:**
Create the correct folder structure so Django can find templates.

**Required structure**:
```
accounts/
└── templates/
    └── accounts/
        ├── base.html
        ├── signup.html
        ├── signin.html
        └── profile.html
```

**Why `accounts/templates/accounts/`**: Django convention. First `templates/` tells Django, second `accounts/` provides namespace.

**Terminal command** (example):
```bash
mkdir -p accounts/templates/accounts
```

---

### Step 2: Create Base Template (Template Inheritance)

**What you'll do:**
Create a common layout for all pages (header, footer, messages).

**base.html minimal structure** (you complete it):
```django
<!DOCTYPE html>
<html lang="en">
<head>
    <title>{% block title %}Auth System{% endblock %}</title>
</head>
<body>
    <header>
        <h1>Django Learning Lab</h1>
    </header>

    <!-- Messages Framework goes here -->
    {% if messages %}
        {% for message in messages %}
            <div class="alert">{{ message }}</div>
        {% endfor %}
    {% endif %}

    <!-- Each page puts its content here -->
    {% block content %}
    {% endblock %}
</body>
</html>
```

**Key points**:
- `{% block title %}` → Each page can provide its own title
- `{% block content %}` → Main content goes here
- `{% if messages %}` → For Django Messages

---

### Step 3: Create Signup Template

**What you'll do:**
Create a page showing the user registration form.

**signup.html minimal structure** (you complete it):
```django
{% extends 'accounts/base.html' %}

{% block title %}Sign Up{% endblock %}

{% block content %}
    <h2>Create Account</h2>

    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Sign Up</button>
    </form>

    <p>Already have an account? <a href="{% url 'signin' %}">Sign In</a></p>
{% endblock %}
```

**Pay attention to**:
- `{% extends %}` → Extends base.html
- `{% csrf_token %}` → Required for security
- `{{ form.as_p }}` → Renders form as paragraphs
- `{% url 'signin' %}` → Reverse URL resolution

---

### Step 4: Create Signin Template

**What you'll do:**
Create the login form page.

**signin.html minimal structure** (you write it):
```django
{% extends 'accounts/base.html' %}

{% block title %}Sign In{% endblock %}

{% block content %}
    <h2>Login</h2>

    {% if form.non_field_errors %}
        <!-- Show non-field errors (invalid credentials) here -->
    {% endif %}

    <form method="post">
        <!-- Add CSRF token -->
        <!-- Render form -->
        <!-- Add submit button -->
    </form>

    <p>Don't have an account? <!-- Add signup link --></p>
{% endblock %}
```

**Tip**: `form.non_field_errors` shows login errors (wrong password, etc).

---

### Step 5: Create Profile Template

**What you'll do:**
Create a page showing welcome message to logged-in user.

**profile.html minimal structure** (you write it):
```django
{% extends 'accounts/base.html' %}

{% block title %}Profile{% endblock %}

{% block content %}
    <h2>Welcome, {{ user.username }}!</h2>

    <p>You are successfully logged in.</p>

    <a href="{% url 'signout' %}">Logout</a>
{% endblock %}
```

**Note**: `{{ user.username }}` → Django automatically adds to context.

---

### Step 6: Render Templates in Views

**What you'll do:**
Add template paths to your views from Phase 1.

**signup_view update** (example):
```python
def signup_view(request):
    if request.method == 'POST':
        # ... form processing ...
        pass
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})
    #                      ^^^^^^^^^^^^^^^^^^^^^ Template path
```

**For other views similarly**:
- `signin_view` → `'accounts/signin.html'`
- `profile_view` → `'accounts/profile.html'`

---

### Step 7: Integrate Django Messages Framework

**What you'll do:**
Give user feedback about successful/failed operations.

**Add message in signup_view** (example):
```python
from django.contrib import messages

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully!')
            return redirect('profile')
    # ...
```

**Add message in signin_view** (example):
```python
def signin_view(request):
    # ...
    if form.is_valid():
        user = form.get_user()
        login(request, user)
        messages.success(request, f'Welcome back, {user.username}!')
        return redirect('profile')
    # ...
```

**Add message in signout_view** (example):
```python
def signout_view(request):
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('signin')
```

**Message levels**:
- `messages.success()` → Successful operations (green)
- `messages.error()` → Errors (red)
- `messages.warning()` → Warnings (yellow)
- `messages.info()` → Information (blue)

---

## ✅ Verification Steps

### 1. Start Server
```bash
python manage.py runserver
```
**Purpose**: Test templates in browser.

---

### 2. Visit Signup Page
**URL**: http://127.0.0.1:8000/accounts/signup/

**Check**:
- [ ] Form appeared?
- [ ] Username, Password1, Password2 fields present?
- [ ] "Sign In" link works?
- [ ] Submit button present?

---

### 3. Test Signup Process
**Do**:
1. Fill form (username: `testuser`, password: `strongpass123`)
2. Click Submit

**Expected**:
- [ ] Redirected to `/accounts/profile/`?
- [ ] "Account created successfully!" message shown?
- [ ] "Welcome, testuser!" text present?

---

### 4. Test Signin Page
**URL**: http://127.0.0.1:8000/accounts/signin/

**Check**:
- [ ] Form appeared?
- [ ] "Sign Up" link works?

**Try with wrong credentials**:
1. Enter wrong password
2. Click Submit
3. "Invalid username or password" error shown?

**Try with correct credentials**:
1. Enter correct username/password
2. Redirected to profile?
3. Welcome message shown?

---

### 5. Test Logout
While on profile page, click "Logout" link.

**Expected**:
- [ ] Redirected to `/accounts/signin/`?
- [ ] "You have been logged out" message shown?

---

### 6. Protected Page Check
**After logging out**:
1. Manually navigate to http://127.0.0.1:8000/accounts/profile/

**Expected**:
- [ ] Redirected to login page?
- [ ] `@login_required` decorator working?

---

## 🧪 Test Commands

### Are tests still passing?
```bash
pytest
```
**Purpose**: Ensure tests didn't break after adding templates. Should still show 2/2 passed.

---

### Django Check Command
```bash
python manage.py check
```
**Purpose**: Check for syntax errors in template paths.

---

### Template Debugging
```bash
python manage.py runserver
```
**Purpose**: Real-time testing in browser. Error messages appear in browser.

---

### Test Template Rendering in Shell
```bash
python manage.py shell
```
```python
from django.template.loader import render_to_string
html = render_to_string('accounts/signup.html', {'form': None})
print(html[:100])  # First 100 characters
```
**Purpose**: Check if template syntax is correct.

---

## ⚠️ Common Pitfalls

### Don't Forget CSRF Token
❌ **Wrong**:
```django
<form method="post">
    {{ form.as_p }}
    <button type="submit">Submit</button>
</form>
```
✅ **Correct**:
```django
<form method="post">
    {% csrf_token %}  <!-- Must include this -->
    {{ form.as_p }}
    <button type="submit">Submit</button>
</form>
```
**Why**: Without CSRF token you'll get 403 Forbidden error.

---

### Template Path Must Be Correct
❌ **Wrong**:
```python
return render(request, 'signup.html', {'form': form})
# TemplateDoesNotExist error!
```
✅ **Correct**:
```python
return render(request, 'accounts/signup.html', {'form': form})
#                      ^^^^^^^^^^^^ Include namespace
```

---

### Extends Path
❌ **Wrong**:
```django
{% extends 'base.html' %}  <!-- Won't find it! -->
```
✅ **Correct**:
```django
{% extends 'accounts/base.html' %}  <!-- With namespace -->
```

---

### Messages Loop
❌ **Wrong**:
```django
{% for message in messages %}
    {{ message }}  <!-- No tag information -->
{% endfor %}
```
✅ **Correct**:
```django
{% for message in messages %}
    <div class="alert-{{ message.tags }}">{{ message }}</div>
    <!-- message.tags → success, error, warning, info -->
{% endfor %}
```

---

### Form Errors Display
❌ **Wrong**:
```django
{{ form.as_p }}  <!-- Errors auto-display but ugly -->
```
✅ **Better**:
```django
{% if form.errors %}
    <div class="errors">
        {{ form.errors }}
    </div>
{% endif %}
{{ form.as_p }}
```

---

## 💡 Tips and References

### Django Docs - Must Read

1. **Templates**: https://docs.djangoproject.com/en/5.2/topics/templates/
   - Template inheritance (`{% extends %}`, `{% block %}`)
   - Template tags (`{% url %}`, `{% csrf_token %}`)
   - Template variables (`{{ user.username }}`)

2. **Messages Framework**: https://docs.djangoproject.com/en/5.2/ref/contrib/messages/
   - Message levels (success, error, warning, info)
   - Displaying messages in templates
   - Adding messages in views

3. **Forms in Templates**: https://docs.djangoproject.com/en/5.2/topics/forms/#rendering-forms
   - `{{ form.as_p }}` vs `{{ form.as_table }}` vs `{{ form.as_ul }}`
   - Manual form rendering
   - `{{ form.non_field_errors }}`

---

### Debugging Tips

**Problem**: `TemplateDoesNotExist: accounts/signup.html`
- ✅ Solution: Is folder structure correct? Should be `accounts/templates/accounts/signup.html`
- ✅ Solution: Is `'accounts'` in `INSTALLED_APPS` in `settings.py`?

**Problem**: 403 Forbidden (CSRF verification failed)
- ✅ Solution: Do you have `{% csrf_token %}` in your form?
- ✅ Solution: Did you write `method="post"` (POST uppercase)?

**Problem**: Messages not showing
- ✅ Solution: Do you have `{% if messages %}` block in `base.html`?
- ✅ Solution: Is `django.contrib.messages` in `INSTALLED_APPS` in `settings.py`?
- ✅ Solution: Is `MessageMiddleware` in middleware?

**Problem**: Form errors not showing
- ✅ Solution: If using `{{ form.as_p }}` it shows automatically
- ✅ Solution: Add `{% if form.errors %}` block

**Problem**: User not in context
- ✅ Solution: In `settings.py` → `TEMPLATES` → `context_processors`, is `auth` present?

---

### Template Development Tips

**Adding CSS**:
- For now use inline CSS (with `<style>` tag)
- Later when you learn static files, you'll add external CSS

**Form Styling**:
```django
{{ form.as_p }}  <!-- Simplest -->
```

**Manual field rendering** (advanced):
```django
{% for field in form %}
    <div class="field">
        {{ field.label_tag }}
        {{ field }}
        {% if field.errors %}
            <span class="error">{{ field.errors }}</span>
        {% endif %}
    </div>
{% endfor %}
```

**Navigation Menu** (in base.html):
```django
{% if user.is_authenticated %}
    <a href="{% url 'profile' %}">Profile</a>
    <a href="{% url 'signout' %}">Logout</a>
{% else %}
    <a href="{% url 'signin' %}">Sign In</a>
    <a href="{% url 'signup' %}">Sign Up</a>
{% endif %}
```

---

### Recommended Order

1. ✅ First create folder structure
2. ✅ Write `base.html` (all pages depend on this)
3. ✅ Write `signup.html` and test
4. ✅ Write `signin.html` and test
5. ✅ Write `profile.html` and test
6. ✅ Add Messages and test
7. ✅ Test everything end-to-end once more

---

## 🔀 Git Workflow for This Phase

This phase has **6 separate topics**, each should be its own branch and PR.

### Recommended Branch Structure

**Remember**: Always branch from `main` after each PR merge!

#### Topic 1: Template Directory Structure
```bash
git checkout main && git pull origin main
git checkout -b task/T2-template-structure

# Work: Create accounts/templates/accounts/ directory structure
mkdir -p accounts/templates/accounts

git add accounts/templates/
git commit -m "feat: create template directory structure for accounts app"
git push -u origin task/T2-template-structure
# PR → Merge → Delete
```
**PR Title**: `Phase 2: Create template directory structure`

---

#### Topic 2: Base Template
```bash
git checkout main && git pull origin main
git checkout -b task/T2-base-template

# Work: Create base.html with blocks and message display
git add accounts/templates/accounts/base.html
git commit -m "feat: create base template with message framework support

- Added template inheritance structure with title and content blocks
- Integrated Django Messages Framework display loop
- Created reusable layout for all account pages"

git push -u origin task/T2-base-template
# PR → Merge → Delete
```
**PR Title**: `Phase 2: Create base template with message framework`

---

#### Topic 3: Signup Template
```bash
git checkout main && git pull origin main
git checkout -b task/T2-signup-template

# Work: Create signup.html, update signup_view to render it
git add accounts/templates/accounts/signup.html accounts/views.py
git commit -m "feat: create signup template and connect to view

- Created signup.html extending base template
- Added CSRF token and form rendering
- Updated signup_view to use template path
- Added link to signin page"

git push -u origin task/T2-signup-template
# PR → Merge → Delete
```
**PR Title**: `Phase 2: Create signup template`

---

#### Topic 4: Signin Template
```bash
git checkout main && git pull origin main
git checkout -b task/T2-signin-template

# Work: Create signin.html, update signin_view
git add accounts/templates/accounts/signin.html accounts/views.py
git commit -m "feat: create signin template and connect to view

- Created signin.html with form and error display
- Updated signin_view to use template path
- Added link to signup page for new users"

git push -u origin task/T2-signin-template
# PR → Merge → Delete
```
**PR Title**: `Phase 2: Create signin template`

---

#### Topic 5: Profile Template
```bash
git checkout main && git pull origin main
git checkout -b task/T2-profile-template

# Work: Create profile.html, update profile_view
git add accounts/templates/accounts/profile.html accounts/views.py
git commit -m "feat: create profile template and connect to view

- Created profile.html with welcome message
- Display username from authenticated user context
- Added logout link
- Updated profile_view to use template path"

git push -u origin task/T2-profile-template
# PR → Merge → Delete
```
**PR Title**: `Phase 2: Create profile template`

---

#### Topic 6: Messages Integration
```bash
git checkout main && git pull origin main
git checkout -b task/T2-messages-integration

# Work: Add messages.success/info to all views
git add accounts/views.py
git commit -m "feat: integrate Django Messages in all views

- Added success message after signup
- Added welcome back message after signin
- Added logout confirmation message
- All messages display via base template"

git push -u origin task/T2-messages-integration
# PR → Merge → Delete
```
**PR Title**: `Phase 2: Integrate Django Messages Framework`

---

### Phase 2 Commit Examples
```bash
"feat: create template directory structure for accounts app"
"feat: create base template with message framework support"
"feat: create signup template and connect to view"
"feat: create signin template and connect to view"
"feat: create profile template and connect to view"
"feat: integrate Django Messages in all views"
"fix: correct template path in signup view"
"style: improve form display in signup template"
```

---

### Verification Before Each PR
- [ ] `python manage.py runserver` → No template errors
- [ ] Navigate to page in browser → Template renders
- [ ] CSRF token present in form source
- [ ] Messages display correctly
- [ ] Links work between pages
- [ ] `pytest` → Still 2/2 passed

---

**📖 For detailed Git workflow, see**: [GIT-WORKFLOW.md](../GIT-WORKFLOW.md)

---

## 🎓 What You Learned

✅ Django Template Language (DTL) syntax
✅ Template inheritance to avoid code repetition
✅ Form rendering in templates
✅ CSRF protection
✅ Django Messages Framework
✅ Context variables (user, form, messages)
✅ URL reversal in templates (`{% url %}`)
✅ Conditional rendering (`{% if %}`)

**Next Step**: In Phase 3, you'll improve security and make the project production-ready!
