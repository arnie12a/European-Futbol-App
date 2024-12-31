def getDataForYear(year):
    getFranceData(year)
    # getEnglandData(year)
    # getGermanyData(year)
    # getSpainData(year)
    # getItalyData(year)
    

    return 

def getFranceData(year):
    import pandas as pd
    url = f'https://fbref.com/en/comps/13/{str(year)}-{str(year+1)}/{str(year)}-{str(year+1)}-Ligue-1-Stats'
    dfs = pd.read_html(url)
    print(dfs)
    print(len(dfs))
    getMetrics(dfs)
    return 

def getEnglandData(year):
    url = f'https://fbref.com/en/comps/9/{str(year)}-{str(year+1)}/{str(year)}-{str(year+1)}-Premier-League-Stats'
    print("England" + str(year))

    return

def getSpainData(year):
    url = f'https://fbref.com/en/comps/12/{str(year)}-{str(year+1)}/{str(year)}-{str(year+1)}-La-Liga-Stats'
    print("Spain" + str(year))
    
    return

def getGermanyData(year):
    url = f'https://fbref.com/en/comps/20/{str(year)}-{str(year+1)}/{str(year)}-{str(year+1)}-Bundesliga-Stats'
    print("Germany" + str(year))
    
    return

def getItalyData(year):
    url = f'https://fbref.com/en/comps/11/{year}-{year+1}/{year}-{year+1}-Serie-A-Stats'
    print("Italy" + str(year))
    
    return


def getGeneralData(dfs):
    return dfs[0]


def squadStandardStats(dfs):
    return dfs[1]

def squadShooting(dfs):
    return dfs[4]

def squadPassing(dfs):
    return dfs[5]

def squadPassType(dfs):
    return dfs[6]

def squadDefensiveActions(dfs):
    return dfs[8]

def squadPossession(dfs):
    return dfs[9]

def squadMiscellaneousStats(dfs):
    return dfs[11]

def getMetrics(dfs):
    getGeneralData(dfs)
    squadStandardStats(dfs)
    squadShooting(dfs)
    squadPassing(dfs)
    squadPassType(dfs)
    squadDefensiveActions(dfs)
    squadPossession(dfs)
    squadMiscellaneousStats(dfs)
    return