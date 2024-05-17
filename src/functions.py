from py1337x import py1337x

engine = py1337x(proxy="1337x.to")


def search_torrents(query, page=1):
    torrents = engine.search(query=query, page=page, sortBy='seeders', order='desc')
    result = []
    for torrent in torrents['items']:
        result.append(enhance_torrent(torrent['link']))
    torrents['items'] = result
    return torrents


def enhance_torrent(link):
    return engine.info(link)
