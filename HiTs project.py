import requests
from lxml import html
import json


def main():
    PMID = input("PMID:")
    page = requests.get('https://www.ncbi.nlm.nih.gov/pubmed/'+PMID)
    tree = html.fromstring(page.content)
    abstract = tree.xpath('//*[@id="maincontent"]/div/div[5]/div/div[4]/div/p/abstracttext/text()')
    abst='.'.join(abstract)
    print(abst)
    datatext={'text': abst}
    url='http://agathon.sista.arizona.edu:8080/odinweb/api/text'
    data=requests.post(url,data=datatext)
    with open(PMID+'.json', 'w') as fp:
        json.dump(data.text, fp)

if __name__ == "__main__":
    main()