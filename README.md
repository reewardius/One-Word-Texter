# One-Word-Texter

This is a script that can send any big file word by word on WhatsApp. By default it's the script to Bee Movie.

# Compatibility

The script is written in Python, but currently is only compatibile with Linux devices or with Termux on android.

# How does it work?

It sends post requests with cURL to Chat-API, so you need to have an account there and have it connected with your WhatsApp Web.
You can create a Chat-API account on https://chat-api.com. Then copy your API-URL and paste it into the script.

# Installation

To install the script type this into the Terminal or Termux:

    apt update && apt upgrade
    apt install python3 python3-pip
    git clone https://github.com/BossLPczNWM/One-Word-Texter.git
    cd One-Word-Texter
    pip3 install -r requirements.txt

# Usage

To open and use this script, just type this into the Terminal or Termux:

    python3 texter.py

and make sure you are in the folder where you downloaded it.

# Disclaimer

Please, do not distribute without a proper credit.
