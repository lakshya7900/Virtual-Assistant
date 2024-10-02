def getSitesList():
    file = open('D:\Virtual Assistant\Database\Sites.json', 'r')
    sites = []
    sites = file.readlines()
    nsites = []
    for site in sites:
        nsites.append(site.split())
    return nsites
    file.close()
