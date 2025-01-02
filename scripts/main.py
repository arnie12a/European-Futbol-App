def getDataForYear(year):
    
    # getEnglandData(year)
    # getGermanyData(year)
    # getSpainData(year)
    # getItalyData(year)
    

    return getFranceData(year)

def getFranceData(year):
    import pandas as pd
    url = f'https://fbref.com/en/comps/13/{str(year)}-{str(year+1)}/{str(year)}-{str(year+1)}-Ligue-1-Stats'
    dfs = pd.read_html(url)
    return squadShooting(dfs)

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
    df = dfs[0]
    columns = ['Rk', 'Squad', 'MP', 'W', 'L', 'GF', 'GA', 'GD', 'Pts', 'Pts/MP', 'Top Team Scorer']
    filtered_df = df[columns]
    return filtered_df

def squadStandardStats(dfs):
    import pandas as pd
    df = dfs[2]
    df.columns = pd.MultiIndex.from_tuples(
    [('About' if 'Unnamed' in level_0 else level_0, level_1) 
        for level_0, level_1 in df.columns],
            names=df.columns.names
    )

    df_combined = pd.concat([df['About'], df['Performance']], axis=1)
    columns_to_keep = ['Squad', '# Pl', 'Age', 'Gls', 'Ast', 'G+A', 'PK', 'PKatt', 'CrdY', 'CrdR']
    return df_combined[columns_to_keep]

def squadShooting(dfs):
    import pandas as pd
    df = dfs[8]
    df.columns = pd.MultiIndex.from_tuples(
    [('About' if 'Unnamed' in level_0 else level_0, level_1) 
        for level_0, level_1 in df.columns],
            names=df.columns.names
    )
    df_combined = pd.concat([df['About'], df['Standard']], axis=1)
    columns_to_keep = ['Squad', 'Gls', 'Sh', 'SoT', 'SoT%', 'Sh/90', 'SoT/90', 'G/Sh', 'G/SoT', 'Dist', 'FK', 'PK', 'PKatt']
    return df_combined[columns_to_keep]

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