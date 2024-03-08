const puppeteer = require('puppeteer');

async function captureScreenshot(url) {
    const browser = await puppeteer.launch();
    const page = await browser.newPage();

    try {
        // Increase the navigation timeout (e.g., 60 seconds)
        await page.goto(url, { timeout: 60000 });

        // Capture a screenshot as a Buffer
        const screenshotBuffer = await page.screenshot();

        // Convert the Buffer to a data URL
        const dataUrl = `data:image/png;base64,${screenshotBuffer.toString('base64')}`;

        return dataUrl;
    } catch (error) {
        console.error('Error during navigation:', error.message);
        return null;
    } finally {
        await browser.close();
    }
}

// Example URL
const url = 'https://imgtext-placeholder.onrender.com/?font=merriweather';

// Call the captureScreenshot function
captureScreenshot(url)
    .then(dataUrl => {
        if (dataUrl) {
            console.log('Generated Data URL:', dataUrl);
        } else {
            console.log('Failed to generate Data URL.');
        }
    })
    .catch(error => {
        console.error('Unexpected error:', error);
    });
