document.addEventListener('DOMContentLoaded', function () {
    const links = document.querySelectorAll('a[href^="#"]');
    for (const link of links) {
        link.addEventListener('click', function (event) {
            event.preventDefault();
            const targetId = this.getAttribute('href').substring(1);
            const targetElement = document.getElementById(targetId);
            if (targetElement) {
                targetElement.scrollIntoView({ behavior: 'smooth' });
            }
        });
    }
});

document.addEventListener('DOMContentLoaded', function () {
    const links = document.querySelectorAll('a');
    links.forEach(link => {
        if (link.hostname !== window.location.hostname) {
            link.setAttribute('target', '_blank');
            link.setAttribute('rel', 'noopener noreferrer');
        }
    });
});

window.addEventListener('load', () => {
    const wordsPerMinute = 275;
    const section = document.querySelector('section');

    if (!section) return;

    const paragraphs = section.querySelectorAll('p');
    const totalWordCount = Array.from(paragraphs).reduce((count, p) =>
        count + p.textContent.trim().split(/\s+/).length, 0);

    if (totalWordCount > 0) {
        const readingTime = Math.ceil(totalWordCount / wordsPerMinute);
        document.getElementById('readingTime').innerHTML = `<i class="fa-solid fa-clock" style="padding-right: 0.3rem;"></i>${readingTime} minutes`;
    }
});

document.addEventListener('DOMContentLoaded', () => {
    const images = document.querySelectorAll('#content .fade-image');
    const observerOptions = {
        root: null,
        rootMargin: '0px',
        threshold: 0.1
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('fade-in');
            }
        });
    }, observerOptions);

    images.forEach(image => observer.observe(image));
});

document.querySelectorAll('details.sd-dropdown').forEach((dropdown) => {
    const summary = dropdown.querySelector('summary');
    const content = dropdown.querySelector('.sd-summary-content');
    content.style.transition = 'max-height 0.5s ease-in-out';
    content.style.overflow = 'hidden';
    content.style.maxHeight = '0';
    summary.addEventListener('click', (event) => {
        event.preventDefault();
        const isOpen = dropdown.hasAttribute('open');
        if (isOpen) {
            content.style.maxHeight = '0';
            setTimeout(() => dropdown.removeAttribute('open'), 500);
        } else {
            dropdown.setAttribute('open', true);
            content.style.maxHeight = content.scrollHeight + 'px';
        }
    });
});

document.addEventListener('DOMContentLoaded', () => {
    document.body.classList.add('page-fade-in');
    const links = document.querySelectorAll('a[href]');
    links.forEach(link => {
        link.addEventListener('click', function (event) {
            const href = this.getAttribute('href');
            if (href && href.startsWith('http')) {
                event.preventDefault();
                document.body.classList.add('page-fade-out');
                setTimeout(() => {
                    window.location.href = href;
                }, 500);
            }
        });
    });
});

var supportedLanguages = ['en', 'es'];

function switchLanguage() {
    var selectedLanguage = document.getElementById('language-selector').value;
    var currentUrl = window.location.href;
    var newUrl;
    var regex = new RegExp('\/(' + supportedLanguages.join('|') + ')\/');
    var currentLanguage = currentUrl.match(regex);

    if (selectedLanguage !== 'en') {
        if (currentLanguage) {
            newUrl = currentUrl.replace(regex, '/' + selectedLanguage + '/');
        } else {
            newUrl = currentUrl.endsWith('/') ? currentUrl + selectedLanguage + '/' : currentUrl + '/' + selectedLanguage + '/';
        }
    } else {
        if (currentLanguage) {
            newUrl = currentUrl.replace(regex, '/');
        }
    }
    if (newUrl) {
        window.location.href = newUrl;
    }
}

window.addEventListener('DOMContentLoaded', function () {
    var regex = new RegExp('\/(' + supportedLanguages.join('|') + ')\/');
    var currentLanguage = window.location.href.match(regex);
    if (currentLanguage) {
        document.getElementById('language-selector').value = currentLanguage[1];
    } else {
        document.getElementById('language-selector').value = 'en';
    }
});

const dropdowns = document.querySelectorAll('.navbar-dropdown');
dropdowns.forEach(dropdown => {
    const button = dropdown.querySelector('.dropbtn');
    button.addEventListener('click', () => {
        dropdowns.forEach(d => d.classList.remove('active'));
        dropdown.classList.toggle('active');
    });
});
document.addEventListener('click', function (event) {
    if (!event.target.closest('.navbar-dropdown')) {
        dropdowns.forEach(dropdown => dropdown.classList.remove('active'));
    }
});
