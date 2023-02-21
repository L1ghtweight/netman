
<p align="center">
    <a href="" target="_blank"><img src="assets/netman-logo-2-cropped-reduced.png" width="400"></a>
</p>
<p align="center">
    <a href=""><img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54" alt="python badge" style="display:block;padding:5px"></a>
    
</p>


## About NETMAN
Manually keeping track of the internet usage in IUT is tedious work. Netman is a small tool that does that dull job for us, saving us a few extra minutes to focus on more productive things.
We can add our credentials and netman will send us our internet usage report via email.

---
##  Requirements and Installation
1. Install [python 3.x](https://www.python.org/downloads/), [pip](https://pip.pypa.io/en/stable/installation/) and [git](https://git-scm.com/downloads) if you don't have them already.
2. Clone and install the dependencies:
```bash
git clone --depth 1 https://github.com/L1ghtweight/netman.git
cd netman
pip install -r requirements.txt
```
>NOTE: Administrative privileges may be needed to install pip packages in windows.
4. We'll need a gmail account to send mails. To set up the email:
* First, enable 2FA from [here](https://myaccount.google.com/security).
* Then, go to `App Passwords`, select `Mail` and `Windows computer` and hit `Generate`.
* You will be given a password, copy it.

Google's official guide regarding this step can be found [here](https://support.google.com/accounts/answer/185833?hl=en).
>NOTE: Using a throwaway mail is highly recommended.
5. Store your email and password you just copied in the `netman/secrets.py` file.
6. Add your IUT internet credentials inside the `netman/credentials.json` file.
* Follow the structure given in the file.
* Setting the `us` variable to `true` means you will get notified about all of the users' usage through email. Otherwise, you'll get usage of yourself only.
7. We can now run the script with the command `python netman.py`.
>NOTE: You need to be connected to IUT internet so that the [iusers](http://10.220.20.12/index.php/home/login) page is accessible.

## Scheduling
We can schedule the script to get a periodic update.
#### Windows:
* For windows we can use the pre-installed `Task Scheduler`. 

#### Linux:
* For Linux we can use `crontab`. 

## Issues
As `secrets.py` and `credentials.py` files are not encrypted, it is necessary to keep them safe from prying eyes.
#### Possible solutions (and why they aren't implemented)
**Using a database:** Seems like an overkill for such a simple task. <br>
**Password protecting the files:** Password would be required whenever an instance is run. If used as a scheduled task, this would become a hassle.
