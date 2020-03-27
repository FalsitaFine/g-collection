import requests

def getProject(url):
    response = requests.get(url)
    content = response.text
    repos = content.split('<div class="mt-n1">')
    url_list = []
    for repo in repos:
        if 'Repository&quot;,&quot;url&quot;:&quot;' in repo:
        #if ',"url":"' in repo:

            url_temp = repo.split('url&quot;:&quot;')[1]
            #print(this_url)
            try:
                this_url = url_temp.split('&quot')[0]
                print(this_url)
                url_list.append(this_url)
            except:
                print(url_temp, "HAS SOME PARSING ISSUES")
    return url_list

topic = "server"
fname = topic + ".txt"
languages = ["C%2B%2B", "C"]
fp = open(fname, 'w+')

for page in range(20,30):
    url = 'https://github.com/search?q=machine+learning' + str(page)
    url = "https://github.com/search?l="+languages[1]+ "&p=" + str(page) + "&q=" + topic + "&type=Repositories"
    urls = []
    urls = getProject(url)
    for url_ins in urls:
        fp.write((url_ins + "\n"))
fp.close()