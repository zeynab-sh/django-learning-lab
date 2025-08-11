# WEEK-01 — Lab: Basic User System (Web-first)

> Goal: Build a **sign‑up → sign‑in → profile** flow using **Django + SQLite** with minimal complexity. Focus on concepts, clean structure, and small, reviewable steps. No command lines or code snippets here—follow the official docs for exact actions.

---

## Outcomes (Definition of Done)
- [ ] Project runs locally with **SQLite** as the database.
- [ ] **Sign-up**, **sign-in/sign-out**, and **profile** pages work end to end.
- [ ] You can see users in the **Admin** panel (provide a redacted screenshot as proof).
- [ ] **README** clearly explains setup and how to verify the main flow (in plain steps).
- [ ] At least **two basic tests** exist (one for sign-up, one for sign-in), passing.
- [ ] All changes are on a focused branch (e.g., `feat/lab-auth-01`) and reviewed via a small PR.

> Reminder: Keep PRs small and single-purpose. One flow = one PR.

---

## Weekly Tech Stack
- **Language & Framework:** Python, **Django** (stable release)
- **Database:** **SQLite** (local, zero setup)
- **IDE & VCS:** PyCharm Community, Git + GitHub
- **Templates & UX:** Django Templates + Messages Framework
- **Authentication:** Django built-in session-based auth
- **Testing (light intro):** pytest + pytest-django (2 “happy path” tests)
- **Configuration:** Starter `.env` awareness (only `SECRET_KEY` / `DEBUG` for now)

---

## Concepts to Understand (this week)
- Repository hygiene: README, simple structure, small commits.
- Branch naming with intent (e.g., `feat/…`, `fix/…`, `docs/…`).
- Django project vs. Django app; where things live (settings, urls, templates).
- Why we start with **SQLite** (speed and simplicity for learning).
- **CustomUser** early (extensible design with `AbstractUser`-based model).
- URL routing, forms, and template inheritance.
- Session-based authentication (high level).
- “Happy path” testing mindset (minimal but real).

---

## Session Plan (6 short sessions, ~45–60 min each)

### Session 1 — Project Skeleton & Git Hygiene
**Purpose:** A clean repository that anyone can understand.
- Create a new GitHub repository and open it in PyCharm.
- Add essential files: README, requirements/notes, and a simple folder structure.
- Initialize a Django project.
- Make a **single, focused commit**: “project skeleton”.

**Evidence to Provide**
- Repo link + screenshot of README and project tree.

**Common Pitfalls**
- Large, unfocused commits.
- Empty or outdated README.

---

### Session 2 — Solid Auth Foundation (CustomUser)
**Purpose:** Start correctly so you can evolve later.
- Create an `accounts` app.
- Configure a **custom user model** that extends the built-in user (behavior unchanged, extensible later).
- Point Django settings to use this custom user model.
- Prepare the database; ensure the Admin panel is accessible.

**Evidence to Provide**
- Screenshot of the Admin user list (redact personal data).
- Small PR titled “CustomUser and admin working”.

**Common Pitfalls**
- Generating migrations before switching to a custom user model.
- Forgetting to create an admin/superuser for the admin panel.

---

### Session 3 — Sign-up, Sign-in/Out, and Profile
**Purpose:** Deliver the core user journey end to end.
- Add **Sign-up** (user name + password) using a simple form.
- Add **Sign-in/Sign-out** pages with clear navigation.
- Add a **Profile** page that requires authentication (welcome message is enough).
- Show **success/warning messages** where appropriate.

**Evidence to Provide**
- Short screen recording: **sign-up → sign-in → profile → sign-out**.

**Common Pitfalls**
- Inconsistent redirects after sign-in/sign-out.
- Accidentally exposing sensitive data in templates.

---

### Session 4 — Mini UX & Security Awareness
**Purpose:** Keep it simple, consistent, and user-friendly.
- Use a base template (layout) and extend it in each page.
- Display form errors and success messages clearly.
- Ensure unauthorized users are redirected gracefully when accessing protected pages.

**Evidence to Provide**
- Two screenshots showing clear error messages on invalid sign-up and sign-in attempts.

**Common Pitfalls**
- Hidden or unclear error messages; users don’t know what went wrong.

---

### Session 5 — Gentle Testing Intro (Happy Path Only)
**Purpose:** Make testing feel normal, not scary.
- Add **one test** for successful sign-up (valid data creates a user).
- Add **one test** for successful sign-in (valid credentials authenticate).
- Keep tests small and single-purpose.

**Evidence to Provide**
- Screenshot showing tests passing.
- Small PR titled “Add first two auth tests”.

**Common Pitfalls**
- Overloading a single test with multiple behaviors.

---

### Session 6 — README & Self-Sufficiency
**Purpose:** The project should be understandable and runnable by others.
- Update **README** so a newcomer can install, set up, and run the project by reading.
- Include a short “How to verify” section for the **sign-up → sign-in → profile** flow.
- Add a tiny “Troubleshooting” section: admin access, redirects, common mistakes.

**Evidence to Provide**
- Updated README in the repo; mentor confirms clarity after a quick read.

---

## Mentor PR Review Checklist
- [ ] PR scope is **single-topic** and small.
- [ ] Templates are tidy; repeated parts are in a base template.
- [ ] Sign-up / sign-in / profile flow works both manually and via two basic tests.
- [ ] No sensitive data leaks in templates.
- [ ] README makes the project runnable and verifiable **by reading only**.

---

## What We Intentionally Skip This Week
- JWT or Django REST Framework (coming next week).
- Postgres or Docker (planned around Week 5, earlier if needed).
- CI, pre-commit hooks, advanced logging/monitoring (later weeks).

---

## Heads-Up for Next Week
- Add a **small API surface** for the same user journey (session-based), then get ready for JWT.
- Add 1–2 tiny negative tests to complement your happy paths.
