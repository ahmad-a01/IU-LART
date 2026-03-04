## IU-LART Website

Static website for the IU-LART lab, built with plain HTML, CSS, and JavaScript.

### Project Structure

- **HTML pages**: `index.html`, `about.html`, `research.html`, `media.html`, `competitions.html`, `sponsorship.html`, `contact.html`
- **Styles**: `css/styles.css`
- **Scripts**: `js/script.js`

### Prerequisites

- Any modern web browser (Chrome, Firefox, Edge, Safari, etc.)
- **Optional for local server**: Python 3 (for a simple HTTP server)

You can check that Python 3 is installed by running:

```bash
python3 --version
```

### Running the Site Locally

#### Option 1: Open files directly

1. Open the project folder: `/home/hjardali/repos/IU-LART`.
2. Double-click `index.html` (or open it from your browser with `File → Open`).

> Note: Some browser features (like `fetch` or certain JS APIs) may not work when opening files directly via the `file://` protocol. If anything looks off, use Option 2 with a local server.

#### Option 2: Run with a local HTTP server (recommended)

From the project root (`/home/hjardali/repos/IU-LART`), run:

```bash
python3 -m http.server 8000
```

Then open this URL in your browser:

```text
http://localhost:8000
```

The main page is:

```text
http://localhost:8000/index.html
```

To stop the server, go back to the terminal window and press `Ctrl + C`.

### Deployment

Because this is a static site (HTML/CSS/JS only), it can be hosted on any static hosting service (e.g., GitHub Pages, Netlify, Vercel, or a simple web server). Just upload the contents of the repository, preserving the folder structure (`css/`, `js/`, and the HTML files).

### Contributing

1. Create a new branch.
2. Make your changes in the HTML, CSS, or JS files.
3. Test locally using the local server instructions above.
4. Open a pull request describing your changes.

