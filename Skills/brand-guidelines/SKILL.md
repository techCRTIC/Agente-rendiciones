---
name: brand-guidelines
description: Applies InfiniteBoard's official brand colors, typography, and design system to any artifact. Use when creating or styling InfiniteBoard-related interfaces, documentation, presentations, or any visual content that should reflect the InfiniteBoard brand identity (tech-modern, dark theme, orange accents).
license: Complete terms in LICENSE.txt
---

# InfiniteBoard Brand Guidelines

## Overview

InfiniteBoard's brand identity reflects its core purpose: a powerful, infinite canvas for creative professionals. The visual language combines **tech-modern minimalism** with **creative energy**, using a dark foundation with vibrant orange accents.

**Brand Essence**: Professional. Infinite. Vibrant. Modern.

**Keywords**: branding, InfiniteBoard, dark theme, tech aesthetic, orange accent, infinite canvas, design system, visual identity

---

## Color System

### Primary Colors

**Dark Foundation:**
- `#1a1a1a` - Primary background (tech-panel)
- `#141413` - Deep black for emphasis
- `#0a0a0a` - True black for overlays

**Orange Accent System:**
- `#FF6B00` - Primary accent (tech-orange) - Main interactive elements
- `#d97757` - Warm orange - Hover states, secondary accents
- `#ff8533` - Bright orange - Highlights, active states

### Neutral Grays

**Structured Hierarchy:**
- `#faf9f5` - Light text on dark backgrounds
- `#e5e5e5` - High contrast text
- `#9ca3af` - Secondary text (gray-400)
- `#71717a` - Tertiary text (zinc-500)
- `#52525b` - Subtle text (zinc-600)
- `#3f3f46` - Borders (zinc-700)
- `#27272a` - Subtle borders (zinc-800)
- `#18181b` - Card backgrounds (zinc-900)

### Semantic Colors

**Status & Feedback:**
- Success: `#22c55e` (green-500)
- Warning: `#eab308` (yellow-500)
- Error: `#ef4444` (red-500)
- Info: `#3b82f6` (blue-500)

### Grid & Canvas

**Visual Helpers:**
- Grid dots/lines: `#444444` at 30% opacity
- Anchor points: `#FF6B00` with white stroke
- Selection: `#FF6B00` at 20% opacity

---

## Typography

### Font Stack

**Primary Font Family:**
```css
font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Oxygen', 'Ubuntu', 'Cantarell', 'Fira Sans', 'Droid Sans', 'Helvetica Neue', sans-serif;
```

**Monospace (for code/technical):**
```css
font-family: 'Courier New', Courier, monospace;
```

### Type Scale

**Headings:**
- H1: 2rem (32px) - Bold, tech-orange
- H2: 1.5rem (24px) - Semibold
- H3: 1.25rem (20px) - Semibold
- H4: 1rem (16px) - Medium

**Body:**
- Large: 1rem (16px)
- Base: 0.875rem (14px)
- Small: 0.75rem (12px)
- Tiny: 0.625rem (10px) - Status bar, labels

### Font Weights
- Regular: 400
- Medium: 500
- Semibold: 600
- Bold: 700

---

## Design Patterns

### Glass Morphism (Tech-Modern)

**Panel Effects:**
```css
background: rgba(26, 26, 26, 0.8);
backdrop-filter: blur(12px);
border: 1px solid rgba(63, 63, 70, 0.5);
```

**Toolbar/StatusBar:**
```css
background: rgba(10, 10, 10, 0.9);
backdrop-filter: blur(16px);
border: 1px solid #27272a;
```

### Neon Glow Effects

**Orange Glow (Interactive Elements):**
```css
box-shadow: 0 0 20px rgba(255, 107, 0, 0.3);
```

**Strong Glow (Active/Selected):**
```css
box-shadow: 0 0 30px rgba(255, 107, 0, 0.5),
            0 0 60px rgba(255, 107, 0, 0.2);
```

### Button Styles

**Primary (Orange):**
```css
background: linear-gradient(135deg, #FF6B00 0%, #d97757 100%);
color: white;
padding: 0.75rem 1.5rem;
border-radius: 0.5rem;
transition: all 0.3s ease;
box-shadow: 0 0 20px rgba(255, 107, 0, 0.3);
```

**Secondary (Ghost):**
```css
background: transparent;
color: #FF6B00;
border: 1px solid #FF6B00;
padding: 0.75rem 1.5rem;
border-radius: 0.5rem;
transition: all 0.3s ease;
```

**Icon Buttons:**
```css
background: rgba(255, 107, 0, 0.1);
color: #FF6B00;
padding: 0.5rem;
border-radius: 0.375rem;
transition: all 0.2s ease;
```

### Cards & Panels

**Standard Panel:**
```css
background: #18181b;
border: 1px solid #27272a;
border-radius: 0.75rem;
padding: 1.5rem;
```

**Elevated Panel:**
```css
background: rgba(26, 26, 26, 0.95);
border: 1px solid #3f3f46;
border-radius: 0.75rem;
box-shadow: 0 10px 40px rgba(0, 0, 0, 0.5);
```

---

## Component Styling

### Toolbar

**Structure:**
- Dark background (`#0a0a0a` at 90% opacity)
- Backdrop blur (16px)
- Bottom border (`#27272a`)
- Height: 60px
- Padding: 1rem horizontal

**Tool Buttons:**
- Size: 40x40px
- Border-radius: 0.5rem
- Active state: Orange background (#FF6B00)
- Hover: Orange background at 10% opacity

### Status Bar

**Layout:**
- Fixed bottom
- Dark background with blur
- Text: Small (12px), monospace
- Color: Zinc-400 (#9ca3af)
- Orange highlights for important metrics

### Context Menu

**Style:**
- Dark panel (#18181b)
- Border: Zinc-800
- Border-radius: 0.5rem
- Shadow: Neon orange glow
- Items: Hover with orange accent

### Transformer/Selection

**Visual Feedback:**
- Border: `#FF6B00` (2px)
- Handles: Orange circles with white stroke
- Selection box: Orange at 20% opacity

---

## Animations & Transitions

### Timing Functions

**Standard Ease:**
```css
transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
```

**Bounce (Playful):**
```css
transition: all 0.4s cubic-bezier(0.68, -0.55, 0.265, 1.55);
```

**Smooth (Elegant):**
```css
transition: all 0.5s cubic-bezier(0.16, 1, 0.3, 1);
```

### Common Animations

**Fade In:**
```css
@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}
```

**Slide Up:**
```css
@keyframes slideUp {
  from {
    opacity: 0;
    transform: translateY(10px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}
```

**Glow Pulse:**
```css
@keyframes glowPulse {
  0%, 100% { box-shadow: 0 0 20px rgba(255, 107, 0, 0.3); }
  50% { box-shadow: 0 0 40px rgba(255, 107, 0, 0.6); }
}
```

---

## Iconography

### Style Guidelines
- **Line weight**: 2px for clarity
- **Size**: 16px, 20px, 24px (consistent sizing)
- **Color**: Inherit from parent or use zinc-400
- **Active state**: tech-orange (#FF6B00)

### Icon Usage
- Lucide React library for consistency
- Always include alt text/labels
- Use contextual colors (orange for active/selected)

---

## Best Practices

### Do's ✅
- Use dark backgrounds with orange accents
- Apply glass morphism for panels
- Include subtle neon glows for interactive elements
- Maintain consistent spacing (multiples of 4px)
- Use monospace fonts for technical data
- Provide clear visual feedback for interactions

### Don'ts ❌
- Avoid light themes (InfiniteBoard is dark-first)
- Don't use other accent colors (stick to orange)
- Avoid sharp, harsh shadows (use soft glows)
- Don't mix font families unnecessarily
- Avoid cluttered interfaces (embrace whitespace)

---

## Technical Implementation

### Tailwind Configuration

Key custom values used in InfiniteBoard:

```javascript
colors: {
  'tech-orange': '#FF6B00',
  'tech-panel': '#1a1a1a',
  'tech-dark': '#0a0a0a',
}

boxShadow: {
  'neon-orange': '0 0 30px rgba(255, 107, 0, 0.5)',
}

backdropBlur: {
  'tech': '12px',
}
```

### CSS Variables

```css
:root {
  --color-primary: #FF6B00;
  --color-bg-dark: #1a1a1a;
  --color-bg-darker: #0a0a0a;
  --color-text-light: #faf9f5;
  --spacing-unit: 4px;
  --border-radius: 0.5rem;
}
```

---

## Examples

### Hero Section
- Large H1 in tech-orange
- Subtitle in zinc-400
- CTA button with orange gradient
- Dark background with subtle grain

### Feature Card
- Dark panel (#18181b)
- Border zinc-800
- Icon in tech-orange (24px)
- Title semibold
- Description in zinc-400

### Interactive Element
- Base state: Ghost style (transparent + orange border)
- Hover: Orange background at 10% opacity + subtle glow
- Active: Full orange background + strong glow
- Transition: 0.3s ease

---

## Brand Voice

**Tone**: Professional yet approachable, creative, empowering

**Voice attributes:**
- Clear and direct
- Tech-savvy but not jargon-heavy
- Encouraging creativity
- Confident without arrogance

**Sample copy:**
- "Infinite possibilities, infinite canvas"
- "Create without boundaries"
- "Your ideas, amplified"
