window.addEventListener('load', function() {

    function generateSessionId() {
        return 'sess-' + Date.now() + '-' + Math.random().toString(36).substr(2, 9);
    }

    function checkImagesEnabled(callback) {
        let img = new Image();
        img.onload = function() { callback(true); };
        img.onerror = function() { callback(false); };
        img.src = "/members/osorio/_icons/pikachu.ico";
    }

    function checkCssEnabled() {
        let div = document.createElement('div');
        div.className = 'test-css';
        document.body.appendChild(div);
        let style = window.getComputedStyle(div);
        let cssEnabled = style.color === 'rgb(255, 0, 0)';
        document.body.removeChild(div);
        return cssEnabled;
    }

    let sessionId = generateSessionId();

    let userAgent = navigator.userAgent;

    let userLanguage = navigator.language;

    let cookiesEnabled = navigator.cookieEnabled;

    let screenDimensions = { 
        width: screen.width, 
        height: screen.height 
    };

    let windowDimensions = { 
        width: window.innerWidth, 
        height: window.innerHeight 
    };

    let networkConnectionType = navigator.connection ? navigator.connection.effectiveType : "unknown";

    let performanceTiming = performance.timing;

    let pageLoadStart = performance.timing.loadEventStart;

    let pageLoadEnd = performance.timing.loadEventEnd;

    let totalLoadTime = pageLoadEnd - pageLoadStart;

    // Collect all static and performance data, then send as one packet
    checkImagesEnabled(function(imagesEnabled) {
        let cssEnabled = checkCssEnabled();
        let data = {
            session: sessionId,
            userAgent: userAgent,
            userLanguage: userLanguage,
            cookiesEnabled: cookiesEnabled,

            jsEnabled: true,
            imagesEnabled: imagesEnabled,
            cssEnabled: cssEnabled,

            screenDimensions: screenDimensions,
            windowDimensions: windowDimensions,
            networkConnectionType: networkConnectionType,
            performanceTiming: performanceTiming,
            pageLoadStart: pageLoadStart,
            pageLoadEnd: pageLoadEnd,
            totalLoadTime: totalLoadTime
        };
        fetch('/logger.php', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
        });
    });
});

window.onerror = function(message, source, lineno, colno, error) {
    fetch('/logger.php?error=' + encodeURIComponent(message) +
          '&source=' + encodeURIComponent(source) +
          '&line=' + lineno +
          '&col=' + colno);
};

document.addEventListener('mousemove', function(event) {
    let x = event.clientX;
    let y = event.clientY;
    fetch('/logger.php?mousemove&x=' + x + '&y=' + y);
});

document.addEventListener('click', function(event) {
    let x = event.clientX;
    let y = event.clientY;
    let button = event.button; // 0: left, 1: middle, 2: right
    fetch('/logger.php?click&x=' + x + '&y=' + y + '&button=' + button);
});

window.addEventListener('scroll', function() {
    let scrollX = window.scrollX;
    let scrollY = window.scrollY;
    fetch('/logger.php?scroll&x=' + scrollX + '&y=' + scrollY);
});

document.addEventListener('keydown', function(event) {
    let key = event.key;
    let code = event.code;
    fetch('/logger.php?keydown&key=' + key + '&code=' + code);
});

document.addEventListener('keyup', function(event) {
    let key = event.key;
    let code = event.code;
    fetch('/logger.php?keyup&key=' + key + '&code=' + code);
});

window.addEventListener('load', function() {
    let entryTime = Date.now();
});

window.addEventListener('beforeunload', function() {
    let exitTime = Date.now();
    let page = window.location.href;
});


let idleStart = null;
let lastActivity = Date.now();
let idleTimeout = null;

function activityHandler() {
    let now = Date.now();
    if (idleStart !== null) {
        let idleEnd = now;
        let idleDuration = idleEnd - idleStart;
        console.log('Idle ended:', idleEnd, 'Duration:', idleDuration);
        fetch('/logger.php?idleEnd=' + idleEnd + '&idleDuration=' + idleDuration);
        idleStart = null;
    }
    lastActivity = now;
    clearTimeout(idleTimeout);
    idleTimeout = setTimeout(function() {
        idleStart = Date.now();
        console.log('Idle started:', idleStart);
        fetch('/logger.php?idleStart=' + idleStart);
    }, 2000);
}

['mousemove', 'keydown', 'scroll', 'click'].forEach(function(event) {
    document.addEventListener(event, activityHandler, true);
});

activityHandler();