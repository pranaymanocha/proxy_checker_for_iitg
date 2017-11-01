# proxy_checker_for_iitg

This is a bash tool written in bash. You need to add the following lines of code to your bashrc so that everytime you open your terminal, it automatically loads up and you just need to call the function name then. It checks from a list of proxies which you give to it.

Step1

Open .bashrc by doing vim ~/.bashrc. Add the following lines of code at the end of the file

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

Step2
Do source ~/.bashrc and then on the terminal run proxy. It will show you the list of proxies one by one by trying out each of them one by one.
