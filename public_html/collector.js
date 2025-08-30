let sessionId = null;

window.addEventListener('load', function() {

    //Session Identifier
    function generateSessionId() {
        return 'sess-' + Date.now() + '-' + Math.random().toString(36).substr(2, 9);
    }

    sessionId = generateSessionId();

    //Helper methods
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

    //Static Information
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

    //Performance Information
    let performanceTiming = performance.timing;
    let pageLoadStart = performance.timing.loadEventStart;
    let pageLoadEnd = performance.timing.loadEventEnd;
    let totalLoadTime = pageLoadEnd - pageLoadStart;

    // Packet
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

//Activity Information

//All thrown errors
window.onerror = function(message, source, lineno, colno, error) {
    fetch('/logger.php?error=' + encodeURIComponent(message) +
          '&source=' + encodeURIComponent(source) +
          '&line=' + lineno +
          '&col=' + colno +
          '&session=' + sessionId);
};

//All mouse activity
document.addEventListener('mousemove', function(event) {
    let x = event.clientX;
    let y = event.clientY;
    fetch('/logger.php?mousemove&x=' + x + '&y=' + y + '&session=' + sessionId);
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
    fetch('/logger.php?scroll&x=' + scrollX + '&y=' + scrollY + '&session=' + sessionId);
});

//All keyboard activity
document.addEventListener('keydown', function(event) {
    let key = event.key;
    let code = event.code;
    fetch('/logger.php?keydown&key=' + key + '&code=' + code + '&session=' + sessionId);
});

document.addEventListener('keyup', function(event) {
    let key = event.key;
    let code = event.code;
    fetch('/logger.php?keyup&key=' + key + '&code=' + code + '&session=' + sessionId);
});

//When the user entered the page
window.addEventListener('load', function() {
    let entryTime = Date.now();
    fetch('/logger.php?entryTime=' + entryTime + '&session=' + sessionId);
});

//When the user left the page
window.addEventListener('beforeunload', function() {
    let exitTime = Date.now();
    //Which page the user was on
    let page = window.location.href;
    fetch('/logger.php?exitTime=' + exitTime + '&page=' + encodeURIComponent(page) + '&session=' + sessionId);
});

//Idle Detection
let idleStart = null;
let lastActivity = Date.now();
let idleTimeout = null;

function activityHandler() {
    let now = Date.now();
    if (idleStart !== null) {
        let idleEnd = now;
        let idleDuration = idleEnd - idleStart;
        console.log('Idle ended:', idleEnd, 'Duration:', idleDuration);
        //Record when the break ended
        //Record how long it lasted
        fetch('/logger.php?idleEnd=' + idleEnd + '&idleDuration=' + idleDuration + '&session=' + sessionId);
        idleStart = null;
    }
    lastActivity = now;
    clearTimeout(idleTimeout);
    idleTimeout = setTimeout(function() {
        idleStart = Date.now();
        console.log('Idle started:', idleStart);
        fetch('/logger.php?idleStart=' + idleStart + '&session=' + sessionId);
    }, 2000);
}

['mousemove', 'keydown', 'scroll', 'click'].forEach(function(event) {
    document.addEventListener(event, activityHandler, true);
});

activityHandler();