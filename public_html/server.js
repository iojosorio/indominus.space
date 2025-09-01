const express = require('express');
const bodyParser = require('body-parser');
const mysql = require('mysql2');

const app = express();
app.use(bodyParser.json());

// MySQL connection
const db = mysql.createPool({
    host: 'localhost',
    user: 'root',
    password: 'qwas7a1Cf322',
    database: 'logs'
});

// --- /api/static ---
app.post('/api/static', (req, res) => {
    const d = req.body;
    const sql = `
        INSERT INTO static_info
        (session, userAgent, userLanguage, cookiesEnabled, jsEnabled,
         imagesEnabled, cssEnabled, screenWidth, screenHeight,
         windowWidth, windowHeight, networkConnectionType)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    `;
    const values = [
        d.session,
        d.userAgent,
        d.userLanguage,
        d.cookiesEnabled,
        d.jsEnabled,
        d.imagesEnabled,
        d.cssEnabled,
        d.screenDimensions?.width,
        d.screenDimensions?.height,
        d.windowDimensions?.width,
        d.windowDimensions?.height,
        d.networkConnectionType
    ];
    db.query(sql, values, (err) => {
        if (err) {
            console.error(err);
            res.status(500).json({ success: false, error: err });
        } else {
            res.json({ success: true });
        }
    });
});

// --- /api/performance ---
app.post('/api/performance', (req, res) => {
    const d = req.body;
    const sql = `
        INSERT INTO performance_info
        (session, performanceTiming, pageLoadStart, pageLoadEnd, totalLoadTime)
        VALUES (?, ?, ?, ?, ?)
    `;
    const values = [
        d.session,
        JSON.stringify(d.performanceTiming || {}),
        d.pageLoadStart,
        d.pageLoadEnd,
        d.totalLoadTime
    ];
    db.query(sql, values, (err) => {
        if (err) {
            console.error(err);
            res.status(500).json({ success: false, error: err });
        } else {
            res.json({ success: true });
        }
    });
});

app.listen(3000, () => {
    console.log('API running on http://localhost:3000');
});
