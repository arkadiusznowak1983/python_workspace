from requests import Session
from sqlite3 import connect
from logging import getLogger, DEBUG, StreamHandler


def configuration(titles="Animal", pllimit="max"):
    url = "https://en.wikipedia.org/w/api.php"
    params_links = {
        "action": "query",
        "prop": "links",
        "titles": titles,
        "rvprop": "content",
        "rvslots": "main",
        "formatversion": "2",
        "format": "json",
        "pllimit": f"{pllimit}"
    }
    params_content = {
        "action": "query",
        "prop": "revisions",
        "titles": None,
        "rvprop": "content",
        "rvslots": "main",
        "formatversion": "2",
        "format": "json",
        "rvlimit": 1
    }
    return url, params_links, params_content

def new_database(name=':memory:', reindex=True):
    connection = connect(name)
    cursor = connection.cursor()
    if reindex:
        logger.info('Dropping table pages if exists')
        cursor.execute("drop table if exists pages")
    logger.info('Create table pages if not exists')
    cursor.execute("create table if not exists pages(title text, content text)")
    cursor.execute("select count(1) from pages")
    return connection, cursor, cursor.fetchone()[0] == 0

def get_wiki_links(session, url, params):
    links_titles = []
    request = session.get(url=url, params=params)
    for links_dict in request.json().get("query", {}).get("pages", {}):
        for link in links_dict.get("links", {}):
            links_titles.append(link.get("title"))
    logger.info(f"Found {len(links_titles)} links")
    return links_titles

def set_content(links, session, url, params, cursor):
    for title in links:
        logger.info(f"Get page {title}")
        params["titles"] = title
        request = session.get(url=url, params=params)
        pages = request.json().get("query", {}).get("pages", [])
        if not len(pages):
            continue
        revisions = pages[0].get("revisions", [])
        if not len(revisions):
            continue

        content = revisions[0].get("slots", {}).get("main", {}).get("content", "")
        cursor.execute("insert into pages(title, content) values(?, ?)", (title, content))
    logger.info("Contents inserted")

def create_index(cursor):
    index = {}
    cursor.execute("select title, content from pages")
    for row in cursor.fetchall():
        title = row[0].lower()
        content = row[1].lower()
        content_filtered = ''.join(filter(lambda x: str.isalnum(x) or str.isspace(x), content))
        content_filtered = content_filtered.replace("\n", " ")
        for word in content_filtered.split(' '):
            if word not in index:
                index[word] = [title]
            else:
                index[word].append(title)
    logger.info(f"Index created for {len(index)} words")
    return index

def search(query: str, reindex=True, index_name='wiki_page_rank'):
    url, params_links, params_content = configuration(pllimit="99")
    session = Session()
    links = get_wiki_links(session, url, params_links)
    connection, cursor, reindex = new_database(index_name, reindex)
    if reindex:
        logger.info("No data in table pages. Reindexing.")
        set_content(links, session, url, params_content, cursor)
    connection.commit()
    index = create_index(cursor)
    connection.close()
    query_words = query.lower().split(' ')
    logger.info(f"Words to find: {query_words}")
    search_result = []
    for word in query_words:
        search_result += index.get(word, [])
    existing_words = list(set(search_result))
    logger.info(f"Found pages for words: {existing_words}")
    counted_pages = {key: 0 for key in existing_words}
    for word in search_result:
        counted_pages[word] += 1
    return dict(sorted(counted_pages.items(), key=lambda x: x[1], reverse=True))

if __name__ == '__main__':
    logger = getLogger()
    logger.setLevel(DEBUG)
    logger.addHandler(StreamHandler())

    search_query = "2021ref goodfellow"
    logger.info(f"Query: {search_query}")
    ranked_result = search(search_query, reindex=True)
    logger.info(f"Ranked result for query: {ranked_result}")
