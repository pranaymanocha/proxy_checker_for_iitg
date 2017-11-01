function proxy(){
f=~/Proxy_list2.txt
while IFS='' read -r line || [[ -n "$line" ]]; do
#     echo "$line"
    value=$(curl -sx http://$line --connect-timeout .025 --max-time 1 -L www.google.com/humans.txt)
    # echo "$value"
    if [[ "$value" ==  "Google is built by a large team of engineers"
]]; then
            echo "$line"
    fi
    value=""
done < "$f"
}

export -f proxy
