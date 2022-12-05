arch=`uname -m`
if [[ ("$arch" == *'arm'*) || ("$arch" == *'Android'*) ]]; then
   wget 'https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-arm' > /dev/null 2>&1
   chmod +x cloudflared-linux-arm
   mv cloudflared-linux-arm server/cloudflared
elif [[ "$arch" == *'x86_64'* ]]; then
   wget 'https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64' > /dev/null 2>&1
   chmod +x cloudflared-linux-amd64
   mv cloudflared-linux-amd64 server/cloudflared
else
   wget 'https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-386' > /dev/null 2>&1
   chmod +x cloudflared-linux-386
   mv cloudflared-linux-386 server/cloudflared
fi
