# days Documentation Site

This directory contains the single-page documentation website for the `days` project.

## Local Preview

To preview the site locally, simply open `index.html` in your browser:

```bash
# Using Python's built-in server
python3 -m http.server 8000 --directory docs

# Or just open the file directly
open docs/index.html  # macOS
xdg-open docs/index.html  # Linux
start docs/index.html  # Windows
```

Then visit: http://localhost:8000

## GitHub Pages

This site is designed to be hosted on GitHub Pages. To enable:

1. Go to your repository Settings
2. Navigate to Pages (in the sidebar)
3. Under "Source", select "Deploy from a branch"
4. Choose the `modernize-with-uv` branch (or `main` after merge)
5. Select the `/docs` folder
6. Click Save

Your site will be available at: `https://bradmontgomery.github.io/days/`

## Features

- 🌞 Brand identity with sun emoji
- 📱 Fully responsive design
- ✨ Smooth scroll animations
- 🎨 Modern gradient design
- 📊 Interactive features
- 💻 Syntax-highlighted code examples
- 🏆 Professional tech startup aesthetic

## Design

The landing page features:
- **Hero Section**: Large typography, brand icon, call-to-action buttons
- **Stats**: 0 dependencies, 35+ tests, 3 Python versions
- **Features Grid**: 6 key benefits with icons
- **Quick Start**: 3 installation methods with code blocks
- **Examples**: All README examples with color-coded output
- **Command Reference**: Complete help text with syntax highlighting
- **Footer**: Badges, links, and attribution

Built with vanilla HTML, CSS, and JavaScript – no frameworks required!
