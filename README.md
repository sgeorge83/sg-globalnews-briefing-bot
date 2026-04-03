# sg-globalnews-briefing-bot
An automated Python assistant that curates premium HR insights and global news into a daily executive briefing. 

### 💡 The Vision: Global News Automation & Stay Informed
In a fast-paced corporate environment, staying informed on leadership trends and workplace culture is a competitive necessity. This project was developed by an **HR professional** to solve the problem of "information overload."
Instead of manual searching, this bot uses Python to curate high-level framework from elite sources like **Harvard Business Review (HBR)** and **SHRM**, delivering a "Daily Kick Start" of intelligence directly to your inbox. It transitions the HR function from a reactive role to a tech-driven, proactive strategic partner.
**Not in HR? Adapt in Seconds:**
The code is modular and industry-agnostic. You can pivot the "Executive Insight" section to any field by simply updating the domains and q (query) variables in the script:
 * **Tech Leaders:** Use domains = "techcrunch.com, wired.com" and q = "AI+Innovation".
 * **Finance Experts:** Use domains = "wsj.com, bloomberg.com" and q = "Market+Trends".
 * **Marketing Directors:** Use domains = "adweek.com, marketingweek.com" and q = "Consumer+Behavior".
### 🔧 How to Customize the Code
To personalize this bot for your own use or your team, follow these three steps to replace the placeholders in the script:
#### 1. Personalize the Identity & Links
Use **Find & Replace (Ctrl+H)** in your code editor to quickly swap these values:
 * **Your Name:** Search for the placeholder text your name. You will find it in the "Prepared by" header and the "Warm regards" signature at the bottom. Replace both with your actual name.
 * **LinkedIn Profile:** Look for the URL https://www.linkedin.com/in/xxxxcccccc your web link/. Replace this entire link with your personal LinkedIn or portfolio URL.
   * *Pro Tip:* You can also change the text Connect via Linkedin to something like View My Professional Insights.
#### 2. Secure Your API Key
The bot requires a "key" to fetch news from the web.
 * Register for a free account at **NewsAPI.org**.
 * Copy your unique API Key.
 * In the code, find the line NEWS_API_KEY = 'write your API key' and paste your key inside the quotes.
#### 3. Set Up Email Delivery
 * **Sender Email:** Use the Gmail address you want the bot to send from.
 * **App Password:** For security, Google requires an **App Password** rather than your standard login password.
   1. Go to your Google Account Security settings.
   2. Search for "App Passwords."
   3. Generate one for "Mail" and "Other (Python Bot)."
   4. Copy the 16-character code into the SENDER_PASSWORD variable in the script.
#### 4. Define Your Sources
If you want to track specific professional journals, edit this line:
domains = "shrm.org,hbr.org,peoplemanagement.co.uk"
Add any reputable industry websites, separated by commas, to ensure the "Executive Insight" section remains relevant to your specific career goals.
This framing highlights your technical skills and strategic mindset without bringing in specific industry sectors. 
You can set the time and keep python running, so everyday it will send the briefing at the same time.
