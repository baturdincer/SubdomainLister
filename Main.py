import requests
# target_input=input("enter your target website")
target_input="google.com"
with open("subdomainlist.txt", "r") as subdomain_list:
    for word in subdomain_list:
        word= word.strip()
        url="http://"+word+"."+target_input
        try:
            response=requests.get(url)
            if response:
                print(url+ " is avaible")
        except requests.exceptions.ConnectionError:
            # print(url+" is not exist")
            pass
        #print(response.json())