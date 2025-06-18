// Echo Bridge Manual v2 - Retro, Flat, DIY Aesthetic with Fun Background Animations
// LUFS Audio - Brand Aligned

document.addEventListener('DOMContentLoaded', function() {
    initializeStickyHeader();
    initializeRetroEffects();
    initializeScrollEffects();
    initializeRetroButtons();
    initializeAnimatedBackground();
});

// Animated Background with Floating Shapes
function initializeAnimatedBackground() {
    const background = document.getElementById('animated-background');
    if (!background) return;
    
    // Create floating shapes
    createFloatingShapes(background);
    createPulsingElements(background);
}

function createFloatingShapes(container) {
    const shapes = ['square', 'circle', 'triangle', 'diamond'];
    const animations = ['floatAround', 'floatSlow', 'floatFast'];
    
    // Create 15 floating shapes
    for (let i = 0; i < 15; i++) {
        const shape = document.createElement('div');
        const shapeType = shapes[Math.floor(Math.random() * shapes.length)];
        const animation = animations[Math.floor(Math.random() * animations.length)];
        
        shape.className = `floating-shape ${shapeType}`;
        
        // Random size between 8px and 25px
        const size = Math.random() * 17 + 8;
        if (shapeType !== 'triangle') {
            shape.style.width = size + 'px';
            shape.style.height = size + 'px';
        }
        
        // Random position
        shape.style.left = Math.random() * 100 + '%';
        shape.style.top = Math.random() * 100 + '%';
        
        // Random animation duration and delay
        const duration = Math.random() * 10 + 10; // 10-20 seconds
        const delay = Math.random() * 5; // 0-5 seconds delay
        
        shape.style.animation = `${animation} ${duration}s ease-in-out infinite`;
        shape.style.animationDelay = delay + 's';
        
        container.appendChild(shape);
    }
}

function createPulsingElements(container) {
    // Create 5 pulsing background elements
    for (let i = 0; i < 5; i++) {
        const pulse = document.createElement('div');
        pulse.className = 'pulse-element';
        
        // Random size between 50px and 150px
        const size = Math.random() * 100 + 50;
        pulse.style.width = size + 'px';
        pulse.style.height = size + 'px';
        
        // Random position
        pulse.style.left = Math.random() * 100 + '%';
        pulse.style.top = Math.random() * 100 + '%';
        
        // Random animation delay
        const delay = Math.random() * 8;
        pulse.style.animationDelay = delay + 's';
        
        container.appendChild(pulse);
    }
}

// Add interactive background effects
function addInteractiveBackgroundEffects() {
    const background = document.getElementById('animated-background');
    if (!background) return;
    
    // Add mouse interaction for fun
    document.addEventListener('mousemove', function(e) {
        const shapes = background.querySelectorAll('.floating-shape');
        const mouseX = e.clientX / window.innerWidth;
        const mouseY = e.clientY / window.innerHeight;
        
        shapes.forEach((shape, index) => {
            if (index % 3 === 0) { // Only affect every 3rd shape for performance
                const offsetX = (mouseX - 0.5) * 20;
                const offsetY = (mouseY - 0.5) * 20;
                shape.style.transform += ` translate(${offsetX}px, ${offsetY}px)`;
            }
        });
    });
}

// Sticky Header Functionality
function initializeStickyHeader() {
    const stickyHeader = document.getElementById('sticky-header');
    const mainHeader = document.querySelector('.main-header');
    let lastScrollTop = 0;
    let headerVisible = false;

    function updateStickyHeader() {
        const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
        const mainHeaderBottom = mainHeader.offsetTop + mainHeader.offsetHeight;
        
        // Show sticky header when scrolled past main header
        if (scrollTop > mainHeaderBottom && !headerVisible) {
            stickyHeader.classList.add('visible');
            headerVisible = true;
        } else if (scrollTop <= mainHeaderBottom && headerVisible) {
            stickyHeader.classList.remove('visible');
            headerVisible = false;
        }
        
        lastScrollTop = scrollTop;
    }

    // Throttled scroll handler for performance
    let ticking = false;
    function handleScroll() {
        if (!ticking) {
            requestAnimationFrame(function() {
                updateStickyHeader();
                ticking = false;
            });
            ticking = true;
        }
    }

    window.addEventListener('scroll', handleScroll);
    
    // Smooth scroll to top functionality
    const logoLinks = document.querySelectorAll('.logo-link');
    logoLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
        });
    });
}

// Retro Effects and Animations
function initializeRetroEffects() {
    addPixelatedHoverEffects();
    initializeRetroTableEffects();
    addRetroGlitchEffects();
}

// Pixelated hover effects for retro feel
function addPixelatedHoverEffects() {
    const headers = document.querySelectorAll('.manual-content h1, .manual-content h2, .manual-content h3');
    
    headers.forEach(header => {
        header.addEventListener('mouseenter', function() {
            this.style.textShadow = '2px 2px 0 #78BEBA, 4px 4px 0 #2069af';
            this.style.transition = 'text-shadow 0.1s ease';
        });
        
        header.addEventListener('mouseleave', function() {
            this.style.textShadow = '1px 1px 0 #111111';
        });
    });
}

// Retro table effects
function initializeRetroTableEffects() {
    const tables = document.querySelectorAll('.manual-content table');
    
    tables.forEach(table => {
        const rows = table.querySelectorAll('tr');
        
        rows.forEach(row => {
            row.addEventListener('mouseenter', function() {
                this.style.transform = 'translateX(2px)';
                this.style.transition = 'transform 0.1s ease';
            });
            
            row.addEventListener('mouseleave', function() {
                this.style.transform = '';
            });
        });
    });
}

// Retro glitch effects (subtle)
function addRetroGlitchEffects() {
    const logo = document.querySelector('.main-header .logo');
    
    if (logo) {
        logo.addEventListener('click', function() {
            this.style.animation = 'retroGlitch 0.3s ease';
            setTimeout(() => {
                this.style.animation = '';
            }, 300);
        });
    }
}

// Scroll Effects
function initializeScrollEffects() {
    initializeScrollReveal();
    initializeRetroProgressBar();
}

// Simple scroll reveal for retro feel
function initializeScrollReveal() {
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };
    
    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, observerOptions);
    
    // Observe elements for scroll reveal
    const elementsToReveal = document.querySelectorAll('.manual-content h2, .manual-content h3, .manual-content table');
    
    elementsToReveal.forEach(element => {
        element.style.opacity = '0';
        element.style.transform = 'translateY(10px)';
        element.style.transition = 'all 0.3s ease';
        observer.observe(element);
    });
}

// Retro-style progress bar
function initializeRetroProgressBar() {
    const progressBar = document.createElement('div');
    progressBar.style.cssText = `
        position: fixed;
        top: 0;
        left: 0;
        width: 0%;
        height: 3px;
        background: linear-gradient(90deg, #78BEBA, #2069af, #E7B225, #D35233);
        z-index: 1001;
        transition: width 0.1s ease;
        image-rendering: pixelated;
    `;
    document.body.appendChild(progressBar);
    
    window.addEventListener('scroll', function() {
        const scrollTop = window.pageYOffset;
        const docHeight = document.body.scrollHeight - window.innerHeight;
        const scrollPercent = (scrollTop / docHeight) * 100;
        progressBar.style.width = scrollPercent + '%';
    });
}

// Retro Button Effects
function initializeRetroButtons() {
    const buttons = document.querySelectorAll('.webring-button');
    
    buttons.forEach(button => {
        // Add retro click effect
        button.addEventListener('mousedown', function() {
            this.style.transform = 'translate(2px, 2px)';
            this.style.boxShadow = 'none';
        });
        
        button.addEventListener('mouseup', function() {
            this.style.transform = '';
            this.style.boxShadow = '2px 2px 0 #888888';
        });
        
        button.addEventListener('mouseleave', function() {
            this.style.transform = '';
            this.style.boxShadow = '2px 2px 0 #888888';
        });
        
        // Add retro sparkle animation
        button.addEventListener('mouseenter', function() {
            const sparkles = this.querySelectorAll('.sparkle');
            sparkles.forEach(sparkle => {
                sparkle.style.animationPlayState = 'running';
            });
        });
    });
}

// Retro keyboard navigation
document.addEventListener('keydown', function(e) {
    // Arrow key navigation for retro feel
    if (e.key === 'ArrowUp' && e.ctrlKey) {
        e.preventDefault();
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    }
    
    if (e.key === 'ArrowDown' && e.ctrlKey) {
        e.preventDefault();
        window.scrollTo({
            top: document.body.scrollHeight,
            behavior: 'smooth'
        });
    }
});

// CSS animations added via JavaScript for retro effects
const style = document.createElement('style');
style.textContent = `
    @keyframes retroGlitch {
        0% { transform: translateX(0); }
        20% { transform: translateX(-2px); }
        40% { transform: translateX(2px); }
        60% { transform: translateX(-1px); }
        80% { transform: translateX(1px); }
        100% { transform: translateX(0); }
    }
    
    @keyframes retroBlink {
        0%, 50% { opacity: 1; }
        51%, 100% { opacity: 0; }
    }
    
    @keyframes retroFloat {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-1px); }
    }
    
    /* Pixelated image rendering */
    img, svg {
        image-rendering: pixelated;
        image-rendering: -moz-crisp-edges;
        image-rendering: crisp-edges;
    }
`;
document.head.appendChild(style);

// Console easter egg - retro style
console.log(`
╔══════════════════════════════════════╗
║  ECHO BRIDGE MANUAL v2.0             ║
║  ────────────────────────────────     ║
║  LUFS Audio - Retro Edition          ║
║                                      ║
║  Features:                           ║
║  • Flat, DIY aesthetic              ║
║  • Sticky header navigation          ║
║  • Retro webpage buttons             ║
║  • Brand-aligned LUFS colors         ║
║                                      ║
║  Keyboard shortcuts:                 ║
║  Ctrl + ↑  : Scroll to top           ║
║  Ctrl + ↓  : Scroll to bottom        ║
╚══════════════════════════════════════╝

Built with ♥ by LUFS Audio
Retro vibes, modern functionality!
`);

// Performance optimization for retro effects
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

// Optimized scroll handler
const optimizedScrollHandler = debounce(function() {
    // Additional scroll-based retro effects can go here
}, 16); // ~60fps

window.addEventListener('scroll', optimizedScrollHandler);

document.addEventListener('DOMContentLoaded', function() {
    initializeStickyHeader();
    initializeRetroEffects();
    initializeScrollEffects();
    initializeRetroButtons();
    initializeAnimatedBackground();
    setCurrentYear();
});

// Set current year dynamically
function setCurrentYear() {
    const yearElement = document.getElementById('current-year');
    if (yearElement) {
        yearElement.textContent = new Date().getFullYear();
    }
}