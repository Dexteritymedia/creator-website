// Previous video control script
        document.addEventListener('DOMContentLoaded', function() {
            const video = document.getElementById('heroVideo');
            const muteBtn = document.getElementById('muteBtn');
            const pauseBtn = document.getElementById('pauseBtn');
            
            // Previous video controls code...

            // New Intersection Observer for perk cards
            const perkCards = document.querySelectorAll('.perk-card');
            
            const observerOptions = {
                root: null,
                rootMargin: '0px',
                threshold: 0.1
            };

            const observer = new IntersectionObserver((entries, observer) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        entry.target.classList.add('visible');
                        // Optional: stop observing after animation
                        observer.unobserve(entry.target);
                    }
                });
            }, observerOptions);

            perkCards.forEach(card => {
                observer.observe(card);
            });
        });
   
   
  // Function to show the loading indicator
  function showLoadingIndicator() {
    const loadingContainer = document.querySelector('.loading-container');
    loadingContainer.style.display = 'flex';
  }

  // Function to hide the loading indicator
  function hideLoadingIndicator() {
    const loadingContainer = document.querySelector('.loading-container');
    loadingContainer.style.display = 'none';
  }

  // Show the loading indicator on page load
  window.addEventListener('load', hideLoadingIndicator);

  // Show the loading indicator on link clicks
  document.querySelectorAll('a').forEach(link => {
    link.addEventListener('click', (event) => {
      event.preventDefault();
      showLoadingIndicator();

      // Navigate to the new page after a short delay
      setTimeout(() => {
        window.location.href = event.target.href;
      }, 500);
    });
  });

// Handle infinite scroll
        const containers = document.querySelectorAll('.review-container');
        containers.forEach(container => {
            container.addEventListener('animationend', () => {
                container.style.animation = 'none';
                container.offsetHeight; // Trigger reflow
                container.style.animation = null;
            });
        });

document.addEventListener('DOMContentLoaded', function() {
    // Update Subscribe button
    const heroButton = document.querySelector('.content-wrapper .btn-primary');
    if (heroButton) {
        heroButton.classList.add('subscribe-btn');
    }
    
    // Update Send Message button color
    const sendMessageBtn = document.querySelector('.form-control .btn');
    if (sendMessageBtn) {
        sendMessageBtn.className = 'btn btn-primary w-full';
    }
    
    // Number counting animation
    const numberElements = {
        subscribers: {
            element: document.querySelector('.text-3xl:contains("450")'),
            end: 450,
            suffix: ' million+'
        },
        views: {
            element: document.querySelector('.text-3xl:contains("54")'),
            end: 54,
            suffix: ' billion+'
        },
        engagement: {
            element: document.querySelector('.text-3xl:contains("15")'),
            end: 15,
            suffix: '%'
        }
    };
    
    // Intersection Observer for triggering count animation
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const element = entry.target;
                const key = element.dataset.counterKey;
                if (key && numberElements[key]) {
                    animateValue(element, 0, numberElements[key].end, 2000, numberElements[key].suffix);
                }
            }
        });
    }, { threshold: 0.5 });
    
    // Setup counter elements and observers
    Object.keys(numberElements).forEach(key => {
        const { element } = numberElements[key];
        if (element) {
            element.dataset.counterKey = key;
            element.style.opacity = '0';
            observer.observe(element);
        }
    });
    
    function animateValue(element, start, end, duration, suffix = '') {
        element.style.opacity = '1';
        let startTimestamp = null;
        const step = (timestamp) => {
            if (!startTimestamp) startTimestamp = timestamp;
            const progress = Math.min((timestamp - startTimestamp) / duration, 1);
            const currentValue = Math.floor(progress * (end - start) + start);
            element.innerHTML = `<span class="counter-value">${currentValue}${suffix}</span>`;
            if (progress < 1) {
                window.requestAnimationFrame(step);
            }
        };
        window.requestAnimationFrame(step);
    }
});

document.addEventListener('DOMContentLoaded', function() {
    // Get all section headers
    const headers = [
        "About us",
        "AWESOME PERKS",
        "Latest Content",
        "Frequently Asked Questions",
        "Get in Touch"
    ];
    
    // Function to update header with zigzag SVG
    function updateHeader(headerText) {
        const header = document.querySelector(`h1:contains("${headerText}")`);
        if (header) {
            // Keep existing classes but add zigzag-header
            const classes = header.className;
            header.innerHTML = `
                ${headerText}
                <svg class="zigzag-line" viewBox="0 0 200 20" preserveAspectRatio="xMidYMid meet">
                    <path class="zigzag-path" d="M0,10 L20,2 L40,10 L60,2 L80,10 L100,2 L120,10 L140,2 L160,10 L180,2 L200,10"/>
                </svg>
            `;
            header.className = `${classes} zigzag-header`;
        }
    }
    
    // Update all headers
    headers.forEach(updateHeader);
});

// Add contains selector support if needed
if (!Element.prototype.matches) {
    Element.prototype.matches = Element.prototype.msMatchesSelector || Element.prototype.webkitMatchesSelector;
}

if (!document.querySelector(':contains')) {
    jQuery.expr[':'].contains = function(a, i, m) {
        return jQuery(a).text().toUpperCase().indexOf(m[3].toUpperCase()) >= 0;
    };
}


    // Theme toggle functionality
    document.addEventListener('DOMContentLoaded', function() {
        const themeToggle = document.getElementById('themeToggle');
        const html = document.documentElement;
        
        // Check for saved theme preference
        const savedTheme = localStorage.getItem('theme');
        if (savedTheme) {
            html.setAttribute('data-theme', savedTheme);
            updateThemeIcon(savedTheme);
        }
        
        themeToggle.addEventListener('click', function() {
            const currentTheme = html.getAttribute('data-theme');
            const newTheme = currentTheme === 'light' ? 'dark' : 'light';
            
            html.setAttribute('data-theme', newTheme);
            localStorage.setItem('theme', newTheme);
            updateThemeIcon(newTheme);
        });
        
        function updateThemeIcon(theme) {
            themeToggle.innerHTML = theme === 'light' 
                ? '<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20.354 15.354A9 9 0 018.646 3.646 9.003 9.003 0 0012 21a9.003 9.003 0 008.354-5.646z" /></svg>'
                : '<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z" /></svg>';
        }
    });

        document.addEventListener('DOMContentLoaded', function() {
            const video = document.getElementById('heroVideo');
            const muteBtn = document.getElementById('muteBtn');
            const pauseBtn = document.getElementById('pauseBtn');
            
            // Handle mute/unmute
            muteBtn.addEventListener('click', function() {
                if (video.muted) {
                    video.muted = false;
                    muteBtn.innerHTML = `
                        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
                            <path d="M11 5L6 9H2v6h4l5 4V5zM15.54 8.46a5 5 0 0 1 0 7.07M19 12a9 9 0 0 1-1.5 5"/>
                        </svg>`;
                } else {
                    video.muted = true;
                    muteBtn.innerHTML = `
                        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
                            <path d="M11 5L6 9H2v6h4l5 4V5zM23 9l-6 6M17 9l6 6"/>
                        </svg>`;
                }
            });

            // Handle play/pause
            pauseBtn.addEventListener('click', function() {
                if (video.paused) {
                    video.play();
                    pauseBtn.innerHTML = `
                        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
                            <path d="M6 4h4v16H6zm8 0h4v16h-4z"/>
                        </svg>`;
                } else {
                    video.pause();
                    pauseBtn.innerHTML = `
                        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
                            <path d="M8 5v14l11-7z"/>
                        </svg>`;
                }
            });

            // Ensure video plays on mobile devices
            video.play().catch(function(error) {
                console.log("Video autoplay failed:", error);
            });
        });