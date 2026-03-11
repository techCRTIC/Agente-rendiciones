# CRTIC Brand Guidelines

## Overview

CRTIC's brand identity reflects its core purpose: an ecosystem and support network for the technological revolution in creative industries in Chile. The visual language is clean, modern, and accessible, utilizing plenty of whitespace, bold readable typography, and vibrant energetic accent colors that represent creativity and technology.

**Brand Essence**: Creativo. Innovador. Profesional. Tecnológico.

**Keywords**: branding, CRTIC, Chile, light theme, orange accent, teal accent, ecosistema tecnocreativo, Manrope

---

## Color System

### Primary Colors

**Backgrounds & Foundation:**
- `#ffffff` (`rgb(255, 255, 255)`) - Primary Background (White)
- `#f7f7f7` (`rgb(247, 247, 247)`) - Secondary Background (Light Gray)
- `#f5f5f5` (`rgb(245, 245, 245)`) - Tertiary Background

**Typography & Dark Elements:**
- `#3e424b` (`rgb(62, 66, 75)`) - Primary Text Color (Dark Slate Gray)
- `#1d1f23` (`rgb(29, 31, 35)`) - Headings / Darkest Elements (Very Dark Gray)
- `#000000` (`rgb(0, 0, 0)`) - True Black (used sparingly)

### Accent Colors

**Energía Creativa (Brand Accents):**
- `#ff4613` (`rgb(255, 70, 19)`) - Primary Energetic Orange (Buttons, Highlights)
- `#c53811` (`rgb(197, 56, 17)`) - Darker Burnt Orange (Links, Hover States)
- `#3bd4ae` (`rgb(59, 212, 174)`) - Mint/Teal Green (Secondary Accent, Technological counterpoint)

---

## Typography

### Font Stack

**Primary Font Family:**
```css
font-family: 'Manrope', sans-serif;
```
*(Manrope is the core typeface across the entire CRTIC site, used for both headings and body text to provide a modern, geometric yet readable feel.)*

### Type Scale (Reference)

**Headings:**
- H1: ~65px - Semibold (600), Color: `#3e424b` or `#1d1f23`
- H2: ~45px - Semibold (600), Color: `#3e424b`
- H3: ~30px - Medium (500)
- H4: ~20px - Medium (500)

**Body:**
- Base: 16px - Light/Regular (300/400), Color: `#3e424b`
- Links: 16px - Light/Regular, Color: `#c53811` (Burnt Orange)

### Font Weights
- Light: 300 (Used extensively for body text)
- Regular: 400
- Medium: 500
- Semibold: 600 (Used for strong, impactful headings)

---

## Design Patterns

### Minimalist Light Theme

**Card / Panel Effects:**
```css
background-color: #ffffff;
border: 1px solid #eaeaea; /* Light border for separation */
box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05); /* Very subtle shadow */
border-radius: 0px; /* CRTIC heavily uses sharp, square corners (0px radius) */
```

### Button Styles

**Primary (Orange):**
```css
background-color: #ff4613;
color: #ffffff;
font-family: 'Manrope', sans-serif;
font-weight: 600;
padding: 12px 24px;
border: none;
border-radius: 0px; /* Sharp corners */
text-transform: uppercase; /* Often used for primary CTAs */
transition: background-color 0.3s ease;
```
*(Hover State: `background-color: #c53811;`)*

**Secondary (Outline/Ghost):**
```css
background-color: transparent;
color: #ff4613;
border: 2px solid #ff4613;
padding: 10px 22px;
border-radius: 0px;
```

---

## Best Practices

### Do's ✅
- Use **Manrope** for all text to maintain the brand's geometric, modern voice.
- Embrace ample whitespace (White and Light Grays) to make content breathe.
- Use sharp corners (0px border-radius) for buttons and prominent UI elements to match the current site style.
- Keep body text light (font-weight: 300) and headings bold (font-weight: 600).
- Use the vibrant Orange (`#ff4613`) for primary calls to action.

### Don'ts ❌
- Do not use rounded corners heavily; CRTIC uses a sharper, more structured aesthetic.
- Do not use dark mode as the primary theme. The brand is fundamentally light-themed.
- Avoid generic fonts like Arial or Times New Roman. Always default to Manrope or a geometric sans-serif fallback if necessary.

---

## Technical Implementation

### Tailwind Configuration

Key custom values mapped to Tailwind for CRTIC web applications:

```javascript
// tailwind.config.js
module.exports = {
  theme: {
    extend: {
      colors: {
        crtic: {
          text: '#3e424b',
          heading: '#1d1f23',
          bg: '#ffffff',
          'bg-alt': '#f7f7f7',
          orange: '#ff4613',
          'orange-dark': '#c53811',
          teal: '#3bd4ae',
        }
      },
      fontFamily: {
        sans: ['Manrope', 'sans-serif'],
      },
      borderRadius: {
        'none': '0px',
      }
    }
  }
}
```

---

## Brand Voice

**Tone**: Accessible, Professional, Inspiring, and Clear.

**Voice attributes:**
- Formally educational but creatively open
- Focused on innovation and future-readiness
- Emphasizes community, learning, and technological revolution

**Sample contexts:**
- "El Futuro sí existe"
- "Centro para la Revolución Tecnológica en Industrias Creativas"
- "Innovación tecnológica en el sector creativo"
