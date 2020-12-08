# Errors

### CRITICAL:root:twint.get:User:

This error is related to the twint installation/module on your device.

Fix:-

```bash
pip3 install --upgrade -e git+https://github.com/twintproject/twint.git@origin/master#egg=twint
```

### ERROR: Unable to extract JS player URL

This error is related to the youtube downloader function.

Fix:- update youtube-dl using pip

```bash
sudo pip3 -U youtube-dl
```

