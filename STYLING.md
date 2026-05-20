# EcoWaste Styling Guide

## Overview
EcoWaste features a modern, polished design system built with Tailwind CSS and custom enhancements for a professional, smooth user experience.

## Design System

### Color Palette
- **Primary (Emerald)**: `#10b981` - Used for main actions, success states
- **Secondary (Teal)**: `#14b8a6` - Complementary accent color
- **Blue**: `#3b82f6` - Collector-specific elements
- **Gray Scale**: From `#f9fafb` to `#1f2937` - Backgrounds and text

### Typography
- **Font Family**: Inter (Google Fonts)
- **Font Weights**: 400 (regular), 500 (medium), 600 (semibold), 700 (bold), 800 (extrabold), 900 (black)
- **Text Rendering**: Optimized with antialiasing for crisp display

## Key Features

### 1. Glass Morphism Effects
Cards and overlays use backdrop blur and transparency for a modern glass effect:
```css
.glass-card {
    background: rgba(255, 255, 255, 0.9);
    backdrop-filter: blur(20px);
}
```

### 2. Smooth Animations
- **Fade In Up**: Elements animate into view on scroll
- **Blob Animation**: Decorative background elements with organic movement
- **Hover Effects**: Cards lift and cast shadows on hover
- **Pulse Effects**: Status indicators and badges

### 3. Responsive Design
- **Mobile-First**: Optimized for all screen sizes
- **Breakpoints**: 
  - sm: 640px
  - md: 768px
  - lg: 1024px
  - xl: 1280px
- **Flexible Grids**: Auto-stacking on mobile devices

### 4. Accessibility Features
- **Focus States**: Clear visual indicators for keyboard navigation
- **Color Contrast**: WCAG AA compliant color combinations
- **Screen Reader Support**: Semantic HTML and ARIA labels
- **Reduced Motion**: Respects user preferences for reduced animations

### 5. Interactive Elements

#### Buttons
- **Primary**: Gradient emerald/teal with shadow
- **Secondary**: White with border
- **Hover**: Lift effect with enhanced shadow
- **Active**: Scale down for press feedback

#### Forms
- **Inputs**: Rounded corners, smooth focus transitions
- **Validation**: Clear error states with red accents
- **Password Toggle**: Eye icon for show/hide functionality

#### Cards
- **Hover Lift**: Subtle elevation on hover
- **Border Glow**: Colored borders on interaction
- **Status Indicators**: Color-coded badges

### 6. Custom Scrollbar
Styled scrollbar matching the emerald theme:
- Track: Light gray background
- Thumb: Emerald gradient
- Hover: Darker emerald

## Page-Specific Styling

### Home Page
- Hero section with gradient background
- Waste classification cards with hover effects
- Animated decorative blobs

### Login/Register
- Centered card with glass effect
- Animated background blobs
- Password visibility toggle
- Form validation styling

### Dashboards

#### Reporter Dashboard
- Sidebar with guidelines
- Report submission form with gradient button
- Waste distribution chart (Chart.js)
- Report history with status badges

#### Collector Dashboard
- Available reports feed
- Collection action forms
- Performance chart
- Status-based color coding

#### Admin Dashboard
- Pending approvals table
- Collection verification cards
- Expandable rejection forms (Alpine.js)
- Confirmation dialogs (SweetAlert2)

### Leaderboard
- Dual-column layout (Reporters vs Collectors)
- Gradient headers
- Medal icons for top 3
- Progress bars showing relative scores
- "YOU" badge for current user

### Profile Page
- Header with gradient background
- Avatar with user initial
- Editable account details
- Status card with account info

## Technologies Used

### CSS Frameworks & Libraries
1. **Tailwind CSS** (CDN) - Utility-first CSS framework
2. **Custom CSS** (`static/css/custom.css`) - Additional polish and animations

### JavaScript Libraries
1. **AOS (Animate On Scroll)** - Scroll-triggered animations
2. **Chart.js** - Data visualization for analytics
3. **SweetAlert2** - Beautiful alert/confirmation dialogs
4. **Alpine.js** - Lightweight JavaScript for UI interactions

### Fonts & Icons
1. **Inter Font** (Google Fonts) - Modern, readable typeface
2. **Heroicons** (SVG) - Clean, consistent icon set

## Animation Details

### Scroll Animations (AOS)
```javascript
AOS.init({
    duration: 800,
    once: true,
    easing: 'ease-out-quint',
});
```

### Custom Animations
- **Blob**: 7s infinite organic movement
- **Pulse**: 2s infinite subtle opacity change
- **Shimmer**: 2s infinite loading effect
- **Spin**: 1s infinite rotation for loaders

## Best Practices

### Performance
- Lazy loading for images
- Optimized animations with `transform` and `opacity`
- Minimal repaints and reflows
- CDN-hosted libraries for caching

### Maintainability
- Consistent naming conventions
- Reusable utility classes
- Modular component structure
- Well-commented custom CSS

### Browser Support
- Modern browsers (Chrome, Firefox, Safari, Edge)
- Graceful degradation for older browsers
- Fallbacks for backdrop-filter

## Customization Guide

### Changing Primary Color
Update these values in `base.html`:
```javascript
tailwind.config = {
    theme: {
        extend: {
            colors: {
                emerald: {
                    // Update these values
                }
            }
        }
    }
}
```

### Adding New Animations
Add to `static/css/custom.css`:
```css
@keyframes yourAnimation {
    /* keyframes */
}

.your-class {
    animation: yourAnimation 1s ease;
}
```

### Modifying Card Styles
Update `.glass-card` class in custom CSS or add Tailwind utilities directly in templates.

## Responsive Breakpoints

### Mobile (< 640px)
- Single column layouts
- Full-width buttons
- Stacked navigation
- Reduced font sizes

### Tablet (640px - 1024px)
- Two-column grids
- Adjusted spacing
- Responsive tables

### Desktop (> 1024px)
- Multi-column layouts
- Sidebar navigation
- Full feature set
- Optimal spacing

## Color Coding System

### Status Colors
- **Pending**: Yellow (`#fbbf24`)
- **Collected**: Blue (`#3b82f6`)
- **Verified**: Emerald (`#10b981`)
- **Rejected**: Red (`#ef4444`)

### Role Colors
- **Reporter**: Emerald gradient
- **Collector**: Blue gradient
- **Admin**: Emerald gradient

## Future Enhancements

### Planned Features
1. Dark mode toggle
2. Custom theme builder
3. More chart types
4. Advanced animations
5. Micro-interactions
6. Loading skeletons

### Accessibility Improvements
1. Enhanced keyboard navigation
2. More ARIA labels
3. Screen reader testing
4. High contrast mode

## Troubleshooting

### Common Issues

**Animations not working:**
- Check if AOS is loaded
- Verify `data-aos` attributes
- Check browser console for errors

**Styles not applying:**
- Clear browser cache
- Check if custom.css is loaded
- Verify Tailwind CDN connection

**Responsive issues:**
- Test on actual devices
- Use browser dev tools
- Check viewport meta tag

## Resources

- [Tailwind CSS Documentation](https://tailwindcss.com/docs)
- [AOS Library](https://michalsnik.github.io/aos/)
- [Chart.js Documentation](https://www.chartjs.org/docs/)
- [SweetAlert2 Documentation](https://sweetalert2.github.io/)
- [Alpine.js Documentation](https://alpinejs.dev/)

## Credits

Design System: Modern, eco-friendly aesthetic
Color Palette: Nature-inspired greens and blues
Typography: Inter font family
Icons: Heroicons SVG library

---

**Last Updated**: May 2026
**Version**: 1.0
**Maintained by**: EcoWaste Development Team
