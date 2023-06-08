#Made By Defalt
#This script scan wordpress site users untill 1000

import requests

from termcolor import colored

url = input("Enter the base URL: ")

modified_urls = [url + '/?author=' + str(i) for i in range(1, 1001)]

for modified_url in modified_urls:

    response = requests.get(modified_url)

    status_code = response.status_code

    if status_code == 200:

        print(colored(f"{modified_url}: {status_code}", 'green'))

    else:

        print(colored(f"{modified_url}: {status_code}", 'red'))
