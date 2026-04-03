import requests
import smtplib
import time
from datetime import datetime, timedelta
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# ==========================================
# 1. CONFIGURATION (ENTER YOUR DATA HERE)
# ==========================================
NEWS_API_KEY = 'write your API key'
SENDER_EMAIL = 'youremail@gmail.com'
SENDER_PASSWORD = 'Embedded password from App password'

# Add more emails inside the brackets separated by commas
RECEIVER_EMAILS = ["xxxxxxzz@gmail.com","xxzzzzzz@yahoo.com","xxxzzzz@amazon.com"]

# Channels for Global News at yoir own choice,check channel Id from newsAPI
CHANNELS = ["fox-news", "cnn", "al-jazeera-english", "business-insider"]

# Delivery Time
TARGET_HOUR = 8
TARGET_MINUTE = 30

# ==========================================
# 2. NEWS FETCHING LOGIC
# ==========================================

def fetch_hr_insight():
    """Fetches a strategic article strictly from HBR, SHRM, or CIPD."""
    domains = "shrm.org,hbr.org,peoplemanagement.co.uk"
    url = f"https://newsapi.org/v2/everything?domains={domains}&q=Strategy+OR+Leadership&language=en&sortBy=publishedAt&pageSize=1&apiKey={NEWS_API_KEY}"
    try:
        response = requests.get(url).json()
        articles = response.get('articles', [])
        return articles[0] if articles else None
    except:
        return None

def generate_premium_report():
    """Formats the news into a professional HTML email."""
    hr_feature = fetch_hr_insight()
    date_now = datetime.now().strftime('%d %B %Y')
    
    html = f"""
    <html>
    <body style="font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; color: #2c3e50; background-color: #f8f9fa; padding: 20px;">
        <div style="max-width: 600px; margin: auto; background: white; border-radius: 4px; border: 1px solid #e1e4e8; overflow: hidden; box-shadow: 0 4px 12px rgba(0,0,0,0.05);">
            
            <div style="background: #ffffff; padding: 40px 20px; text-align: center; border-bottom: 3px solid #1a2a6c;">
                <h1 style="margin: 0; font-size: 20px; text-transform: uppercase; letter-spacing: 3px; color: #1a2a6c;">Global Briefing</h1>
                <p style="margin: 10px 0 0 0; font-size: 11px; color: #7f8c8d; text-transform: uppercase; letter-spacing: 1px;">
                    Prepared by your name • {date_now}<br>
                <a href="https://www.linkedin.com/in/xxxxcccccc your web link/"> Connect via Linkedin
                </a>
                </p>
            </div>
            
            <div style="padding: 30px;">
    """

    # Executive HR Highlight
    if hr_feature:
        html += f"""
        <div style="background-color: #f4f7fb; border-left: 4px solid #1a2a6c; padding: 20px; margin-bottom: 40px;">
            <span style="color: #1a2a6c; font-weight: bold; font-size: 10px; text-transform: uppercase; letter-spacing: 1px;">Executive HR Insight | {hr_feature['source']['name']}</span>
            <h3 style="margin: 10px 0; font-size: 17px; line-height: 1.4; color: #1a2a6c;">{hr_feature['title']}</h3>
            <p style="font-size: 14px; color: #5d6d7e; line-height: 1.6;">{hr_feature['description'][:170]}...</p>
            <a href="{hr_feature['url']}" style="color: #1a2a6c; text-decoration: none; font-weight: bold; font-size: 13px;">Review Full Analysis →</a>
        </div>
        """

    # Global News Channels
    for s in CHANNELS:
        url = f"https://newsapi.org/v2/top-headlines?sources={s}&pageSize=5&apiKey={NEWS_API_KEY}"
        try:
            res = requests.get(url).json()
            articles = res.get('articles', [])
            html += f"<h4 style='color: #1a2a6c; border-bottom: 1px solid #f0f0f0; padding-bottom: 10px; margin-top: 30px; font-size: 12px; text-transform: uppercase;'>{s.replace('-', ' ')}</h4>"
            for art in articles:
                html += f"<div style='margin-bottom: 15px;'><a href='{art['url']}' style='color: #34495e; text-decoration: none; font-size: 15px;'>• {art['title']}</a></div>"
        except: continue

    # Minimalist Signature
    html += """
                <div style="margin-top: 60px; padding-top: 30px; border-top: 1px solid #f0f0f0;">
                    <p style="margin-bottom: 5px; color: #95a5a6; font-style: italic; font-size: 14px;">Warm regards,</p>
                    <p style="margin-top: 0; font-size: 22px; color: #2c3e50; font-family: 'Georgia', serif;">your name </p>
                </div>
            </div>
        </div>
    </body>
    </html>
    """
    return html

def send_email(html_body):
    msg = MIMEMultipart()
    msg['From'] = f"Intelligence Briefing <{SENDER_EMAIL}>"
    msg['Subject'] = f"Daily News Briefing & Business Insight | {datetime.now().strftime('%d %b')}"
    msg.attach(MIMEText(html_body, 'html'))
    
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL, RECEIVER_EMAILS, msg.as_string())
        server.quit()
        print(f"✅ Email Sent Successfully: {datetime.now().strftime('%H:%M')}")
    except Exception as e:
        print(f"❌ Error sending email: {e}")

# ==========================================
# 3. SMART SCHEDULER
# ==========================================

if __name__ == "__main__":
    print("🚀 HR and News Briefing Bot started.")
    while True:
        now = datetime.now()
        target = now.replace(hour=TARGET_HOUR, minute=TARGET_MINUTE, second=0, microsecond=0)
        
        if now >= target:
            target += timedelta(days=1)
        
        wait_seconds = (target - now).total_seconds()
        
        print(f"💤 Status: Waiting {wait_seconds/3600:.2f} hours until 08:05 AM delivery.")
        time.sleep(wait_seconds)
        
        print("⏰ Triggering morning report...")
        report_content = generate_premium_report()
        send_email(report_content)
        
        # Buffer to avoid repeating for the same day
        time.sleep(120)

