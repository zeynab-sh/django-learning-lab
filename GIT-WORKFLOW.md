# Git Workflow Guide

**Target Audience**: Django Learning Lab Students
**Purpose**: Learn professional Git workflow with small, focused commits and PRs

---

## 🎯 Overview

This project uses a **task-based branch workflow** where:
- Each small piece of work gets its own branch
- Branch names follow `task/T<phase>-<topic>` convention
- Each branch creates a separate Pull Request
- After PR merge, always branch from `main` for next task
- Commit messages are descriptive and follow conventional format

**Key Principle**: Small, focused changes that are easy to review and rollback.

---

## 🌿 Branch Naming Convention

### Format
```
task/T<phase-number>-<descriptive-topic>
```

### Examples by Phase

**Phase 1 (Make Tests Pass):**
- `task/T1-url-configuration`
- `task/T1-forms-module`
- `task/T1-signup-view`
- `task/T1-signin-view`
- `task/T1-profile-view`

**Phase 2 (Add User Interface):**
- `task/T2-template-structure`
- `task/T2-base-template`
- `task/T2-signup-template`
- `task/T2-signin-template`
- `task/T2-profile-template`
- `task/T2-messages-integration`

**Phase 3 (Security & Polish):**
- `task/T3-env-configuration`
- `task/T3-decouple-setup`
- `task/T3-requirements-txt`
- `task/T3-code-cleanup`

**Phase 4 (Final Verification):**
- `task/T4-readme-update`
- `task/T4-evidence-collection`

### Rules
- ✅ Use lowercase
- ✅ Use hyphens for spaces
- ✅ Be specific (not `task/T1-views` but `task/T1-signup-view`)
- ✅ One topic per branch
- ❌ Don't use generic names (`task/T1-stuff`, `task/T1-fixes`)

---

## 🔄 Workflow Steps

### 1. Start New Task (Always from main!)

```bash
# Make sure you're on main and it's up to date
git checkout main
git pull origin main

# Create new branch for specific topic
git checkout -b task/T1-url-configuration
```

**Important**: Always start from `main`, never from another task branch!

---

### 2. Make Changes

Work on ONE specific topic only. Examples:
- Create URL configuration files
- Add a single view
- Create one template

```bash
# Check what changed
git status
git diff
```

---

### 3. Commit Changes

**When to Commit:**
- ✅ After completing a logical unit of work
- ✅ When tests pass
- ✅ When code runs without errors
- ✅ Before switching tasks

**When NOT to Commit:**
- ❌ Broken/incomplete code
- ❌ Code that doesn't run
- ❌ Work in progress (WIP)
- ❌ Commented-out debug code

**Commit Command:**
```bash
git add <specific-files>  # Better than git add .
git commit -m "Add URL configuration for accounts app"
```

---

### 4. Push to Remote

```bash
git push -u origin task/T1-url-configuration
```

**First push**: Use `-u` flag to set upstream
**Subsequent pushes**: Just `git push`

---

### 5. Create Pull Request

**Via GitHub UI:**
1. Go to repository on GitHub
2. Click "Compare & pull request"
3. **Base branch**: `main`
4. **Compare branch**: `task/T1-url-configuration`
5. Fill PR template:
   ```markdown
   ## Task
   Phase 1: URL Configuration

   ## What Changed
   - Created `accounts/urls.py` with 4 URL patterns
   - Updated `config/urls.py` to include accounts URLs
   - All URL patterns have names for reverse resolution

   ## How to Test
   ```bash
   python manage.py shell
   from django.urls import reverse
   print(reverse('signup'))  # Should print /accounts/signup/
   ```

   ## Checklist
   - [x] Code runs without errors
   - [x] URLs can be reversed
   - [x] Follows project conventions
   ```

6. Click "Create pull request"

**Via gh CLI (optional):**
```bash
gh pr create --base main --head task/T1-url-configuration \
  --title "Add URL configuration for accounts app" \
  --body "Created URL patterns for signup, signin, signout, profile"
```

---

### 6. After PR Merged

```bash
# Switch back to main
git checkout main

# Pull the merged changes
git pull origin main

# Delete local branch (cleanup)
git branch -d task/T1-url-configuration

# Start next task from fresh main
git checkout -b task/T1-forms-module
```

**Important**: Always pull `main` before creating next branch!

---

## 💬 Commit Message Format

### Structure
```
<type>: <short description>

<optional detailed description>
```

### Types
- `feat:` - New feature (new view, new template)
- `fix:` - Bug fix
- `refactor:` - Code restructuring without behavior change
- `test:` - Adding or updating tests
- `docs:` - Documentation changes
- `style:` - Code formatting (no logic change)
- `chore:` - Maintenance tasks (dependencies, config)

### Examples

**Good Commit Messages:**
```bash
git commit -m "feat: add URL configuration for accounts app"

git commit -m "feat: create SignUpForm with username validation"

git commit -m "feat: implement signup view with form handling"

git commit -m "fix: strip whitespace from username in SignUpForm"

git commit -m "refactor: extract message strings to constants"

git commit -m "test: add test for username whitespace handling"

git commit -m "docs: update README with installation steps"

git commit -m "chore: add python-decouple to requirements"
```

**Bad Commit Messages:**
```bash
git commit -m "update"  # What was updated?
git commit -m "fix stuff"  # What stuff?
git commit -m "wip"  # Work in progress - don't commit!
git commit -m "asdfasdf"  # Not descriptive
git commit -m "Final version"  # Not specific
```

### Multi-line Commits (for complex changes)

```bash
git commit -m "feat: implement signin view with authentication

- Use AuthenticationForm for validation
- Call login() to create session
- Redirect to profile after successful login
- Show error message for invalid credentials"
```

---

## 📋 Task Breakdown Strategy

### Phase 1 Example Breakdown

Instead of one big `task/T1-phase1` branch, create:

1. `task/T1-url-configuration`
   - Create `accounts/urls.py`
   - Update `config/urls.py`
   - **Commit**: "feat: add URL configuration for accounts app"

2. `task/T1-forms-module`
   - Create `accounts/forms.py`
   - Add SignUpForm with validation
   - **Commit**: "feat: create SignUpForm with username validation"

3. `task/T1-signup-view`
   - Implement `signup_view` in `accounts/views.py`
   - **Commit**: "feat: implement signup view with form handling"

4. `task/T1-signin-view`
   - Implement `signin_view`
   - **Commit**: "feat: implement signin view with authentication"

5. `task/T1-signout-view`
   - Implement `signout_view`
   - **Commit**: "feat: implement signout view"

6. `task/T1-profile-view`
   - Implement `profile_view` with `@login_required`
   - **Commit**: "feat: implement profile view with login requirement"

**Each step**: Branch → Code → Commit → Push → PR → Merge → Delete branch → Next!

---

## 🔍 Before Each Commit Checklist

- [ ] Code runs without errors (`python manage.py runserver`)
- [ ] Tests pass (if applicable: `pytest`)
- [ ] No debug print statements left
- [ ] No commented-out code
- [ ] Files are saved
- [ ] Only relevant files staged (`git status` to check)
- [ ] Commit message is descriptive

---

## 🚫 What NOT to Commit

### Never Commit:
- ❌ `.env` file (contains secrets)
- ❌ `db.sqlite3` (database file)
- ❌ `__pycache__/` directories
- ❌ `.pyc` files
- ❌ IDE config (`.idea/`, `.vscode/`)
- ❌ `*.log` files
- ❌ Personal notes

### Check `.gitignore`:
```bash
cat .gitignore  # Make sure these are listed
```

---

## 🛠️ Common Git Commands Quick Reference

### Branch Management
```bash
# List all branches
git branch -a

# Create and switch to new branch
git checkout -b task/T1-topic

# Switch to existing branch
git checkout main

# Delete local branch (after merged)
git branch -d task/T1-topic

# Delete remote branch (if needed)
git push origin --delete task/T1-topic
```

### Checking Status
```bash
# See what changed
git status

# See detailed changes
git diff

# See commit history
git log --oneline -10
```

### Staging and Committing
```bash
# Stage specific file
git add path/to/file.py

# Stage multiple files
git add file1.py file2.py

# Unstage file (if added by mistake)
git restore --staged file.py

# See what's staged
git diff --staged
```

### Syncing with Remote
```bash
# Get latest from main
git checkout main
git pull origin main

# Push current branch
git push

# Push new branch first time
git push -u origin task/T1-topic
```

### Undoing Changes
```bash
# Discard local changes (before commit)
git restore file.py

# Undo last commit (keep changes)
git reset --soft HEAD~1

# Undo last commit (discard changes) - DANGEROUS!
git reset --hard HEAD~1
```

---

## 🎯 Best Practices

### Do ✅
- **Small, focused branches** - One topic per branch
- **Descriptive names** - Clear what the branch does
- **Frequent commits** - After each logical change
- **Meaningful messages** - Future you will thank you
- **Pull before branch** - Always start from latest main
- **Delete merged branches** - Keep repo clean
- **Test before commit** - Make sure code works

### Don't ❌
- **Big branches** - Hard to review, hard to rollback
- **Generic names** - `task/T1-updates`, `task/T1-stuff`
- **Rare commits** - Lose granular history
- **WIP commits** - Commit only working code
- **Branch from branch** - Always use main as base
- **Keep merged branches** - Clutters branch list
- **Commit broken code** - Always test first

---

## 🔀 Working with Pull Requests

### PR Title Format
```
Phase <number>: <Short description>
```

**Examples:**
- `Phase 1: Add URL configuration for accounts app`
- `Phase 1: Implement signup view with form handling`
- `Phase 2: Create base template with message display`
- `Phase 3: Move SECRET_KEY to environment variables`

### PR Description Template
```markdown
## Task
Phase <number>: <Topic>

## What Changed
- Bullet point of changes
- Another change
- etc.

## How to Test
```bash
# Commands to verify changes
```

## Checklist
- [ ] Code runs without errors
- [ ] Tests pass (if applicable)
- [ ] No debug code left
- [ ] Follows project conventions
```

### PR Size Guidelines
- ✅ **Small**: 1-3 files changed, < 100 lines
- ⚠️ **Medium**: 4-6 files, 100-300 lines (acceptable)
- ❌ **Large**: 7+ files, 300+ lines (split into smaller PRs)

**If PR too large**: Break into multiple topics/branches

---

## 📖 Example Complete Workflow

### Scenario: Student Working on Phase 1

```bash
# Step 1: Start from main
git checkout main
git pull origin main

# Step 2: Create branch for URL configuration
git checkout -b task/T1-url-configuration

# Step 3: Make changes
# (Create accounts/urls.py, update config/urls.py)

# Step 4: Test changes
python manage.py shell
# Test reverse() works

# Step 5: Commit
git add accounts/urls.py config/urls.py
git commit -m "feat: add URL configuration for accounts app

- Created accounts/urls.py with signup, signin, signout, profile patterns
- Updated config/urls.py to include accounts URLs
- All patterns have names for reverse resolution"

# Step 6: Push
git push -u origin task/T1-url-configuration

# Step 7: Create PR on GitHub
# (Via UI: base=main, compare=task/T1-url-configuration)

# Step 8: After PR merged
git checkout main
git pull origin main
git branch -d task/T1-url-configuration

# Step 9: Start next topic
git checkout -b task/T1-forms-module
# ... repeat process
```

---

## 🆘 Troubleshooting

### "Branch is behind main"
```bash
# Your branch is outdated, update it:
git checkout task/T1-topic
git rebase main
# Or merge (simpler but creates merge commit):
git merge main
```

### "Merge conflict"
```bash
# Open conflicted files, look for:
<<<<<<< HEAD
your changes
=======
main's changes
>>>>>>> main

# Manually fix, then:
git add fixed-file.py
git rebase --continue
# Or if merged:
git commit
```

### "Accidentally committed to main"
```bash
# Move commit to new branch:
git branch task/T1-topic
git reset --hard HEAD~1
git checkout task/T1-topic
```

### "Want to undo last commit"
```bash
# Keep changes, undo commit:
git reset --soft HEAD~1

# Discard changes, undo commit (CAREFUL!):
git reset --hard HEAD~1
```

---

## 📚 Learning Resources

**Git Basics:**
- https://git-scm.com/book/en/v2
- https://www.atlassian.com/git/tutorials

**GitHub Flow:**
- https://docs.github.com/en/get-started/quickstart/github-flow

**Conventional Commits:**
- https://www.conventionalcommits.org/

**Interactive Git Tutorial:**
- https://learngitbranching.js.org/

---

## 🎓 Summary

**Remember:**
1. **One topic** = One branch = One PR
2. **Always branch from main** after PR merge
3. **Descriptive names** for branches and commits
4. **Test before commit** - broken code stays local
5. **Small PRs** - easier to review, easier to rollback
6. **Clean up** - delete merged branches

**This workflow teaches you:**
- Professional Git practices
- Code review culture
- Incremental development
- Clean commit history
- Team collaboration skills

Good luck! 🚀
