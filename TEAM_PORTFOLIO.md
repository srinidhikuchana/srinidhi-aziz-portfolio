# Team Portfolio Notes

This document explains the shared team portfolio changes made for the MLH Fellowship portfolio project.

## Overview

This project now includes a shared team homepage and separate portfolio and hobbies pages for both team members.

The shared homepage allows visitors to choose between:

- Sri Nidhi Kuchana
- Aziz Ercoban

Each team member has their own portfolio page and hobbies page.

## Team Members

### Sri Nidhi Kuchana

Sri Nidhi's existing portfolio content is preserved and moved under dedicated routes.

Main pages:

- `/sri-nidhi`
- `/sri-nidhi/hobbies`

The old `/hobbies` route is also kept as an alias for Sri Nidhi's hobbies page.

### Aziz Ercoban

Aziz's portfolio and hobbies pages were added as new pages.

Main pages:

- `/aziz`
- `/aziz/hobbies`

Aziz's portfolio page includes:

- About section
- Experience section
- Education section
- Interactive travel map

Aziz's hobbies page includes:

- Traveling
- Building Projects
- Animals

## Main Routes

| Route | Description |
|---|---|
| `/` | Shared team homepage |
| `/sri-nidhi` | Sri Nidhi's portfolio page |
| `/sri-nidhi/hobbies` | Sri Nidhi's hobbies page |
| `/hobbies` | Alias for Sri Nidhi's hobbies page |
| `/aziz` | Aziz's portfolio page |
| `/aziz/hobbies` | Aziz's hobbies page |

## Files Updated

Main files changed during the team portfolio update:

- `app/__init__.py`
- `app/data.py`
- `app/templates/homepage.html`
- `app/templates/aziz.html`
- `app/templates/aziz_hobbies.html`
- `app/templates/hobbies.html`
- `app/templates/_nav.html`
- `app/static/styles/main.css`

New image assets added:

- `app/static/img/aziz-profile.jpeg`
- `app/static/img/travel.jpeg`
- `app/static/img/project.jpeg`
- `app/static/img/animal.jpeg`

Unused Cocoon images were removed because the hobbies page now uses `project.jpeg`.

## Tech Stack

This portfolio uses:

- Python
- Flask
- Jinja templates
- HTML
- CSS
- JavaScript
- Leaflet.js
- OpenStreetMap

## Local Testing

To run the project locally:

```bash
flask run