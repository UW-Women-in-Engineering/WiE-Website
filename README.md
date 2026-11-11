### WiE Website: WIP :)

## Preview and edit

Run `npm run dev` (Python 3 required), then open http://localhost:5173.

- `/` — Home
- `/about-us/` — About Us
- `/events/` — Events
- `/our-sponsors/` — Our Sponsors

No package installation is needed. Edit content in `pages/`, shared HTML in `templates/`, styles in `styles.css`, and interactions in `app.js`. Run `npm run build` after editing templates/content to regenerate the tracked HTML pages. The build uses Python's standard library only.

## Layout

Each `.hero` fills at least the viewport height minus `--header-height`, keeping the following section below the opening screen. The header is 93px on desktop and 80px on mobile. Inner artwork keeps its Figma proportions. All design images and fonts are stored locally; duplicate downloads were matched by SHA-256 and consolidated.

Desktop sections follow the Figma layout; mobile stacks the notebook and sponsor sections, uses two columns for team photos and sponsor logos, and presents each event as a labeled row group. The activities tabs support mouse and arrow/Home/End keyboard navigation.

## Content and integration gaps from the design

- Placeholder headings, copy, dates, prices, empty image slots and missing team photos are retained from Figma.
- Event signup URLs are `https://bit.ly/something` placeholders. Clicking one displays “Work in Progress :)”.
- Calendar, feedback and the sponsorship PDF have no supplied destinations/files. Their controls display “Work in Progress :)” instead of opening a broken URL. Instagram and Linktree use the user-supplied URLs; the shared footer links to Instagram. Other footer social labels remain text.
- Four supplied sponsor logos link to the respective official company sites. Empty sponsor cards remain empty.
- The sponsorship form validates required fields and email syntax, then opens a populated email draft to `wie@uwaterloo.ca`. It does not send or store enquiries and does not claim delivery. A real form service can replace this draft flow when provided.
- The non-default activities tabs use relevant copy already supplied elsewhere in the design, because only the Events panel has designed content.

## Verification

All four routes returned HTTP 200. Local file references and JavaScript syntax were checked. Browser checks covered the desktop notebook, timeline, activities, team board, sponsor grid, packages, form and events table; mobile asset loading, no horizontal overflow, full-height heroes, tab switching and keyboard controls, menu navigation, placeholder notices and form validation.
