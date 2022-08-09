<p align="center">
    <a href="" target="_blank"><img src="assets/netman-logo.jpg" width="400"></a>
</p>
<p align="center">
    <a href=""><img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54" alt="python badge"></a>
</p>



## About NETMAN
We know how shitty IUT internet is. To survive, we need to have someone managing out net IDs.
This script will notify the total internet usage of the user.

---

## Requirements and Installation
1. Install `python 3.x` and `pip`
2. `ChromeDriver` is needed. \
    Download it for [windows](https://chromedriver.chromium.org/downloads). \
    For Linux: 
    * ChromeDriver is available in AUR. Run: `paru -S chromedriver`
    * Available in apt: Run `sudo apt-get install chromium-chromedriver` 
    * Or download from the official repo. \
    Run: `wget https://chromedriver.storage.googleapis.com/2.35/chromedriver_linux64.zip && unzip chromedriver_linux64.zip && ./chromedriver`
3. Run `git clone --depth 1 https://github.com/L1ghtweight/netman.git && cd netman`
4. Run: `pip install -r requirements.txt`
5. You'll need a gmail account so that this script can use it for sending mail. 
Using a throwaway mail is highly recommended.
~~Log into that account and enable less secure apps from [here](https://myaccount.google.com/lesssecureapps).~~
 Google has stopped lesssecureapps service.  You need to enable 2FA from [here](https://myaccount.google.com/u/3/security). Then create a password for an app for sending mail. You will be given a password for that app.
6. Now, set the email and password variable in `secrets.py` to the gmail address and the password you got from the last step. 
To be absolutely sure, kindly go through the code and understand what this script is doing with your password.
7. Now add IUT internet credentials in `credentials.json`. Make sure you maintain the format.
8. Now run `python netman.py`.
> **Note:** You need to be connected to IUT internet so that iusers page is accessible
10. Schedule the script to run after certain period to
get update about your internet usage.
11. Make sure that `credentials.json` and `secrets.py` is
safe from prying eyes.
