import json
from scholarly import scholarly

def main():
    author = scholarly.search_author_id('2WFd9foAAAAJ')
    author = scholarly.fill(author)
    publications = author['publications']
    publications = [scholarly.fill(pub) for pub in publications]
    publications.sort(key=lambda pub: int(pub["bib"]["pub_year"]), reverse=True)

    data = {"publications": publications, "author": author}
    with open("data.json", 'w') as data_fp:
        json.dump(data, data_fp)

if __name__ == "__main__":
    main()