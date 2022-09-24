#!/usr/bin/env bash
read -p 'username: ' username
read -s -p 'password: ' password

cookie=$(curl -i -s -k -X $'GET' \
    -H $'Host: 10.220.20.12' -H $'Upgrade-Insecure-Requests: 1' -H $'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.5195.102 Safari/537.36' -H $'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9' -H $'Accept-Encoding: gzip, deflate' -H $'Accept-Language: en-US,en;q=0.9' -H $'Connection: close' \
    $'http://10.220.20.12/' | grep Cookie | tr ';' ' ' | cut -d ' ' -f2 | cut -d '=' -f2)

curl -i -s -k -X $'POST' \
    -H $'Host: 10.220.20.12' -H $'Cache-Control: max-age=0' -H $'Upgrade-Insecure-Requests: 1' -H $'Origin: http://10.220.20.12' -H $'Content-Type: application/x-www-form-urlencoded' -H $'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.5195.102 Safari/537.36' -H $'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9' -H $'Referer: http://10.220.20.12/index.php/home/login' -H $'Accept-Encoding: gzip, deflate' -H $'Accept-Language: en-US,en;q=0.9' -H $'Connection: close' \
    -b $'ci_session='${cookie} \
    --data-binary $'username='${username}'&password='${password}'' \
    $'http://10.220.20.12/index.php/home/loginProcess' > /dev/null

response="$(curl -i -s -k -X $'GET' \
    -H $'Host: 10.220.20.12' -H $'Cache-Control: max-age=0' -H $'Upgrade-Insecure-Requests: 1' -H $'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.5195.102 Safari/537.36' -H $'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9' -H $'Referer: http://10.220.20.12/index.php/home/login' -H $'Accept-Encoding: gzip, deflate' -H $'Accept-Language: en-US,en;q=0.9' -H $'Connection: close' \
    -b $'ci_session='${cookie} \
    $'http://10.220.20.12/index.php/home/dashboard' | tail -n 49 | head -n 28)"

echo ""
echo "Full Name     :" "$(echo "$response" | awk '/Full Name:/{getline; print}' | cut -d '>' -f2 | cut -d '<' -f1)"
echo "Student ID    :" "$(echo "$response" | awk '/Student ID:/{getline; print}' | cut -d '>' -f2 | cut -d '<' -f1)"
echo "Total Use     :" "$(echo "$response" | awk '/Total Use:/{getline; print}' | cut -d '>' -f2 | cut -d '<' -f1)"
echo "Extra Use     :" "$(echo "$response" | awk '/Extra Use:/{getline; print}' | cut -d '>' -f2 | cut -d '<' -f1)"
echo "Estimated Bill:" "$(echo "$response" | awk '/Estimated Bill:/{getline; print}' | cut -d '>' -f2 | cut -d '<' -f1)"
