# Phase 3: Security & Professional Polish

**Target Audience**: Beginner Django Students
**Estimated Time**: 1-2 hours
**Difficulty**: Easy-Medium

---

## 🎯 Objective

You built a working authentication system in Phase 2. Now:
- Fix security vulnerabilities (hardcoded SECRET_KEY)
- Learn to use environment variables
- Manage dependencies properly
- Clean up code to professional standards

**Success Criteria**: SECRET_KEY shouldn't be committed to git, project should be installable in fresh environment.

---

## 📋 Prerequisites

You must have completed Phase 1-2:
- ✅ Tests passing
- ✅ UI working
- ✅ Signup/signin/profile flow works end-to-end

**Currently**:
- ⚠️ SECRET_KEY hardcoded in `settings.py` (security risk)
- ⚠️ Unused import exists (`settings.py:15`)
- ⚠️ No `requirements.txt` (others can't install project)

---

## 📝 Step-by-Step Instructions

### Step 1: Create .env File

**What you'll do:**
Store secrets (SECRET_KEY, DEBUG) outside of code in a file.

**Create `.env` file in project root**:
```env
SECRET_KEY=django-insecure-#8#b1(0l*wb3$)c##n3uymmh2+l$&c-$#g_(!kn$t*8tg@zr3+
DEBUG=True
```

**Note**: You'll add this file to `.gitignore` (next step).

---

### Step 2: Install python-decouple

**What you'll do:**
Install a library to read variables from `.env` file.

**Terminal command**:
```bash
pip install python-decouple
```

**Why python-decouple**: Widely used in Django for simple environment variable management.

---

### Step 3: Update settings.py

**What you'll do:**
Replace hardcoded SECRET_KEY with reading from `.env` file.

**Change in settings.py** (you do it):

**Old code** (lines 15-28):
```python
from django.conf.global_settings import AUTH_USER_MODEL  # Unused

SECRET_KEY = 'django-insecure-#8#b1(0l*wb3$)c##n3uymmh2+l$&c-$#g_(!kn$t*8tg@zr3+'
DEBUG = True
```

**New code structure** (example):
```python
from decouple import config

SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', default=False, cast=bool)
```

**Also**:
- Delete unused import on line 15: `from django.conf.global_settings import AUTH_USER_MODEL`

---

### Step 4: Update .gitignore

**What you'll do:**
Ensure `.env` file isn't committed to git.

**Add to `.gitignore`**:
```
# Environment variables
.env
```

**Check**:
```bash
git status
```
`.env` file shouldn't appear (should be ignored).

---

### Step 5: Create .env.example

**What you'll do:**
Show other developers the format of `.env` file.

**Create `.env.example` in project root**:
```env
SECRET_KEY=your-secret-key-here
DEBUG=True
```

**Why**: New developers can copy `.env.example` and fill in their own values.

**Note**: This file WILL be committed to git (no real secrets inside).

---

### Step 6: Create requirements.txt

**What you'll do:**
Document project dependencies.

**Terminal command**:
```bash
pip freeze > requirements.txt
```

**Generated file looks like**:
```
Django==5.2.5
pytest==8.x.x
pytest-django==4.x.x
python-decouple==3.x.x
```

**Why**: Others can `pip install -r requirements.txt` to set up same environment.

---

### Step 7: Code Cleanup

**What you'll do:**
Remove unnecessary code.

**Clean settings.py Line 15**:
```python
# DELETE THIS:
from django.conf.global_settings import AUTH_USER_MODEL
```

This import is unused because:
- Line 45 directly assigns `AUTH_USER_MODEL = 'accounts.CustomUser'`
- Import is unnecessary

---

## ✅ Verification Steps

### 1. Is .env File Working?
**Add print to settings.py** (temporarily):
```python
from decouple import config
SECRET_KEY = config('SECRET_KEY')
print(f"SECRET_KEY loaded: {SECRET_KEY[:10]}...")  # First 10 chars
```

**Start server**:
```bash
python manage.py runserver
```

**In terminal output**:
```
SECRET_KEY loaded: django-ins...
```
If you see this, it's working! Delete the print statement.

---

### 2. Is .gitignore Working?
```bash
git status
```

**Check**:
- [ ] `.env` file NOT in list
- [ ] `.env.example` file IS in list
- [ ] `requirements.txt` file IS in list

---

### 3. Is requirements.txt Correct?
**Test in new virtual environment** (optional):
```bash
# In a new terminal window
python3 -m venv test_env
source test_env/bin/activate  # Mac/Linux
# or
test_env\Scripts\activate  # Windows

pip install -r requirements.txt
```

**Expected**: All packages install, no errors.

---

### 4. Are Tests Still Passing?
```bash
pytest
```
**Expected**: 2/2 passed (nothing broke).

---

### 5. Is Application Working?
```bash
python manage.py runserver
```

**Test in browser**:
- [ ] `/accounts/signup/` opens?
- [ ] Signup works?
- [ ] Signin works?

---

### 6. What Happens if SECRET_KEY Changes?
**Test**:
1. Change SECRET_KEY in `.env` file
2. Restart server
3. Old sessions should be invalid (you'll be logged out)

**Why**: SECRET_KEY is used for session encryption.

---

## 🧪 Test Commands

### Django Check
```bash
python manage.py check
```
**Purpose**: Verify SECRET_KEY loads successfully and no config errors.

---

### Import Check
```bash
python manage.py shell
```
```python
from decouple import config
print(config('SECRET_KEY'))
print(config('DEBUG'))
```
**Purpose**: Check if environment variables are read correctly.

---

### Pip List
```bash
pip list
```
**Purpose**: Verify python-decouple is installed.

---

### Git Diff
```bash
git diff config/settings.py
```
**Purpose**: See what changed in settings.py.

---

## ⚠️ Common Pitfalls

### Don't Commit .env File!
❌ **Wrong**:
```bash
git add .env  # NEVER DO THIS!
git commit -m "Add environment variables"
```
✅ **Correct**:
```bash
# Check if .env is in .gitignore
cat .gitignore | grep .env
```

**Why**: If SECRET_KEY goes public, anyone can decrypt your sessions.

---

### .env Format
❌ **Wrong**:
```env
SECRET_KEY = "django-insecure-..."  # Quotes unnecessary
DEBUG = "True"                      # As string
```
✅ **Correct**:
```env
SECRET_KEY=django-insecure-...  # No quotes, no spaces
DEBUG=True                       # As bool (decouple will cast)
```

---

### decouple config() Usage
❌ **Wrong**:
```python
DEBUG = config('DEBUG')  # Returns string: "True"
if DEBUG:  # Always True!
```
✅ **Correct**:
```python
DEBUG = config('DEBUG', default=False, cast=bool)  # Returns boolean
```

---

### Keep requirements.txt Updated
❌ **Wrong**:
```bash
# Install new package and do nothing
pip install some-package
```
✅ **Correct**:
```bash
pip install some-package
pip freeze > requirements.txt  # Update
git add requirements.txt
git commit -m "Add some-package dependency"
```

---

## 💡 Tips and References

### Django Docs - Must Read

1. **Django Settings**: https://docs.djangoproject.com/en/5.2/topics/settings/
   - Why SECRET_KEY is important
   - Why DEBUG=True is dangerous in production
   - Environment-specific settings

2. **Deployment Checklist**: https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/
   - Security checks for production
   - `python manage.py check --deploy` command

---

### python-decouple Docs
https://pypi.org/project/python-decouple/

**Basic usage**:
```python
from decouple import config

# String value
DATABASE_NAME = config('DATABASE_NAME')

# Integer value
PORT = config('PORT', default=8000, cast=int)

# Boolean value
DEBUG = config('DEBUG', default=False, cast=bool)

# Required value (error if missing)
SECRET_KEY = config('SECRET_KEY')

# Optional value
OPTIONAL = config('OPTIONAL', default='default_value')
```

---

### .gitignore Best Practices

**Should be ignored in Django projects**:
```gitignore
# Environment
.env
.venv/
venv/
env/

# Database
*.sqlite3
db.sqlite3

# Python
__pycache__/
*.py[cod]
*.so

# IDE
.idea/
.vscode/
*.swp

# OS
.DS_Store
Thumbs.db
```

---

### Debugging Tips

**Problem**: `decouple.UndefinedValueError: SECRET_KEY not found`
- ✅ Solution: Is `.env` file in project root?
- ✅ Solution: Does `.env` have `SECRET_KEY=...` line?
- ✅ Solution: Did you restart server?

**Problem**: DEBUG always True
- ✅ Solution: Are you using `cast=bool`?
- ✅ Solution: In `.env` file write `DEBUG=False` (as string)

**Problem**: Git sees .env file
- ✅ Solution: Did you add `.env` to `.gitignore`?
- ✅ Solution: If already committed: `git rm --cached .env`

**Problem**: pip freeze shows too many packages
- ✅ Solution: Are you using virtual environment?
- ✅ Solution: If in global Python, all packages show

---

### 12-Factor App Methodology

Why are you doing this practice? → **12-Factor App** principles:

**III. Config**: Store config in the environment
- No hardcoded values in code
- Each environment (dev, staging, production) can use different config
- Secrets kept outside version control

**More info**: https://12factor.net/config

---

### When Moving to Production

What you learned in this Phase is the foundation for production. Additionally:

1. **Change SECRET_KEY**:
   ```bash
   python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
   ```

2. **Set DEBUG=False** (in production)

3. **Set ALLOWED_HOSTS**:
   ```python
   ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='localhost,127.0.0.1').split(',')
   ```

4. **Use HTTPS**

5. **Move database password to .env**

---

### Git Commit Messages

Example commits for this Phase:
```bash
git add .gitignore
git commit -m "Add .env to .gitignore"

git add .env.example
git commit -m "Add .env.example template"

git add requirements.txt
git commit -m "Add requirements.txt with project dependencies"

git add config/settings.py
git commit -m "Move SECRET_KEY and DEBUG to environment variables"

git add config/settings.py
git commit -m "Remove unused AUTH_USER_MODEL import"
```

**Separate commit for each change** → Easier review and rollback.

---

## 🔀 Git Workflow for This Phase

This phase has **4 separate topics**, each should be its own branch and PR.

### Recommended Branch Structure

#### Topic 1: Environment Configuration
```bash
git checkout main && git pull origin main
git checkout -b task/T3-env-configuration

# Work: Create .env file, update .gitignore, create .env.example
git add .gitignore .env.example
git commit -m "chore: add environment variable configuration

- Added .env to .gitignore to prevent secret exposure
- Created .env.example template for developers
- Prepared for SECRET_KEY migration to environment variables"

git push -u origin task/T3-env-configuration
# PR → Merge → Delete
```
**PR Title**: `Phase 3: Add environment variable configuration`

**Note**: `.env` file is NOT committed (in .gitignore), only `.env.example` is committed.

---

#### Topic 2: Decouple Setup
```bash
git checkout main && git pull origin main
git checkout -b task/T3-decouple-setup

# Work: Install python-decouple, update settings.py
git add config/settings.py
git commit -m "feat: migrate SECRET_KEY and DEBUG to environment variables

- Installed python-decouple for env variable management
- Updated settings.py to read SECRET_KEY from .env
- Updated DEBUG setting with safe default (False)
- Removed hardcoded SECRET_KEY from version control"

git push -u origin task/T3-decouple-setup
# PR → Merge → Delete
```
**PR Title**: `Phase 3: Migrate secrets to environment variables`

---

#### Topic 3: Requirements and Code Cleanup
```bash
git checkout main && git pull origin main
git checkout -b task/T3-requirements-cleanup

# Work: Create requirements.txt, remove unused imports
pip freeze > requirements.txt
git add requirements.txt config/settings.py
git commit -m "chore: add requirements.txt and remove unused imports

- Created requirements.txt with pip freeze
- Removed unused AUTH_USER_MODEL import from settings.py
- Project dependencies now documented for reproducible builds"

git push -u origin task/T3-requirements-cleanup
# PR → Merge → Delete
```
**PR Title**: `Phase 3: Add requirements.txt and code cleanup`

---

### Phase 3 Commit Examples
```bash
"chore: add environment variable configuration"
"feat: migrate SECRET_KEY and DEBUG to environment variables"
"chore: add requirements.txt and remove unused imports"
"fix: correct decouple config type casting for DEBUG"
"docs: update .env.example with all required variables"
```

---

### Verification Before Each PR
- [ ] `.env` file NOT in git status (gitignored)
- [ ] `.env.example` IS in git status
- [ ] `python manage.py runserver` → Starts successfully
- [ ] `python manage.py check` → No errors
- [ ] `pytest` → Still 2/2 passed
- [ ] SECRET_KEY loads from .env (test with print, then remove)

---

**📖 For detailed Git workflow, see**: [GIT-WORKFLOW.md](../GIT-WORKFLOW.md)

---

## 🎓 What You Learned

✅ Environment variables usage (12-factor app)
✅ Secret management (SECRET_KEY, passwords)
✅ python-decouple library
✅ .gitignore usage
✅ Dependency documentation (requirements.txt)
✅ Code cleanup and refactoring
✅ Production-ready configuration patterns

**Next Step**: In Phase 4, you'll do final verification and update README!
