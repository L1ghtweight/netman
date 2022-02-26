# IUT-net-manager
We know how shitty IUT internet is. To survive, we need to have someone managing our net IDs.
This script will notify the total internet usage of the user.

---

##### Requirements and Installation
1. Install `python 3.x` and `pip`
2. `ChromeDriver` is needed. \
    Download it for [windows](https://chromedriver.chromium.org/downloads). \
    For Linux: 

    * ChromeDriver is available in AUR. Run: `sudo paru -S chromedriver`
    * Available in apt: Run `sudo apt-get install chromium-chromedriver` 
    * Or download from the official repo. \
    Run: `wget https://chromedriver.storage.googleapis.com/2.35/chromedriver_linux64.zip && unzip chromedriver_linux64.zip && ./chromedriver`
3. Run `git clone https://github.com/L1ghtweight/netman.git && cd netman`
4. Run: `pip install -r requirements.txt`
5. You'll need a gmail account so that this script can use it for sending mail. 
Using throwaway mail is highly recommended.
Log into that account and enable less secure apps from [here](https://myaccount.google.com/lesssecureapps).
6. Now, set the email and password variable in `secrets.py` to the address and password of that gmail account. 
To be absolutely sure, go through the code and understand what this script is doing with your password.
7. Now add IUT internet credentials in `credentials.json`
8. Now run `python netman.py`
9. Schedule the script to run after certain period to
get update about your internet usage.
10. Make sure that `credentials.json` and `secrets.py` is
safe from prying eyes.

