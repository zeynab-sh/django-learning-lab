# django-learning-lab

This project is the starting point for building a basic user system with Django + SQLite
It includes simple authentication : **sign-up**, **sign-in**, and a profile page.

## Project Setup
- Python 3.11+
- Django
- Virtual environment: `.venv/`

## 📚 For Students

**New to this project?**
- 📖 **Git Workflow Guide**: See [GIT-WORKFLOW.md](GIT-WORKFLOW.md) for branch naming, commit messages, and PR workflow
- 📋 **Task Documents**: Check `docs/` folder for phase-by-phase instructions
- 🎯 **Project Guide**: See [CLAUDE.md](CLAUDE.md) for architecture and development commands

## Installation 
- Terminal:
```
git clone https://github.com/zeynab-sh/django-learning-lab.git
cd django-learning-lab
```
- Or use Pycharm's "Clone Repository"

## How to Verify
``` 
python manage.py runserver
```
`/accounts/signup/` - Create a new user
`/accounts/signin/` - Log in
After login - redirected to `/accounts/profile/`

**Running tests**
```
pytest
```

## Troubleshooting
_Log in not working?_

Make sure you first created user vi `/signup/`

_Access to Admin_

1. Go to [`/admin/`](http://127.0.0.1:8000/admin) 
2. Create a superuser with:
```
python manage.py createsuperuser
```







