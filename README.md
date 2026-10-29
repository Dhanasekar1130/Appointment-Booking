# Appointment Booking

A front-end appointment booking app: services, 6-step booking wizard, My Appointments, admin dashboard, XP/badges, light/dark mode, installable PWA.

## Run
- Quickest: open `index.html` in a browser.
- For PWA/install support, serve it: `python -m http.server 8000` then open http://localhost:8000

## Structure
- `index.html` – markup
- `css/style.css` – theme and animations
- `js/app.js` – all app logic (data stored in browser localStorage)
- `manifest.json`, `sw.js`, `icon.svg` – PWA files

## Demo
Admin tab password: `admin123` (demo only, checked in the browser).

## Limits
No real backend: no login, payments, email reminders or database. The admin check is not real security. A production version needs a server (e.g. Node/Express + PostgreSQL) enforcing roles and slot conflicts.
