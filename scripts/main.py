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
    return squadMiscellaneousStats(dfs)

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
    import pandas as pd
    df = dfs[10]
    df.columns = pd.MultiIndex.from_tuples(
        [
            (
                'About' if 'Unnamed' in level_0 else level_0,  # Add 'About' for unnamed columns
                f"{level_0}_{level_1}" if level_0 in ['Short', 'Medium', 'Long'] else level_1  # Rename lower-level names for specific top-level names
            )
            for level_0, level_1 in df.columns
        ],
        names=df.columns.names
    )

    df_combined = pd.concat([df['About'], df['Total'], df['Short'], df['Medium'], df['Long']], axis=1)
    columns_to_keep = ['Squad', 'Cmp', 'Att', 'Cmp%', 'TotDist', 'PrgDist', 'Short_Cmp', 'Short_Att', 'Short_Cmp%', 'Medium_Cmp', 'Medium_Att', 'Medium_Cmp%', 'Long_Cmp', 'Long_Att', 'Long_Cmp%']
    return df_combined[columns_to_keep]

def squadPassType(dfs):
    import pandas as pd
    df = dfs[12]
    df.columns = pd.MultiIndex.from_tuples(
    [('About' if 'Unnamed' in level_0 else level_0, level_1) 
        for level_0, level_1 in df.columns],
            names=df.columns.names
    )
    df_combined = pd.concat([df['About'], df['Pass Types'], df['Corner Kicks'], df['Outcomes']], axis=1)
    columns_to_keep = ['Squad', 'Att', 'Live', 'Dead', 'FK', 'TB', 'Sw', 'Crs', 'TI', 'CK', 'In', 'Out', 'Str', 'Cmp', 'Off', 'Blocks']
    return df_combined[columns_to_keep]

def squadDefensiveActions(dfs):
    import pandas as pd
    df = dfs[16]
    df.columns = pd.MultiIndex.from_tuples(
        [('About' if 'Unnamed' in level_0 else level_0, level_1) 
            for level_0, level_1 in df.columns],
                names=df.columns.names
        )
    df_combined = pd.concat([df['About'], df['Tackles'], df['Challenges'], df['Blocks']], axis=1)
    columns_to_exclude = ['# Pl', '90s']
    final_df = df_combined.drop(columns_to_exclude, axis=1)
    final_df
    return final_df

def squadPossession(dfs):
    import pandas as pd
    df = dfs[18]
    df.columns = pd.MultiIndex.from_tuples(
        [('About' if 'Unnamed' in level_0 else level_0, level_1) 
            for level_0, level_1 in df.columns],
                names=df.columns.names
        )
    df_combined = pd.concat([df['About'], df['Touches'], df['Take-Ons'], df['Carries'], df['Receiving']], axis=1)
    columns_to_exclude = ['# Pl', '90s']
    final_df = df_combined.drop(columns_to_exclude, axis=1)
    return final_df

def squadMiscellaneousStats(dfs):
    import pandas as pd
    df = dfs[22]
    df.columns = pd.MultiIndex.from_tuples(
        [('About' if 'Unnamed' in level_0 else level_0, level_1) 
            for level_0, level_1 in df.columns],
                names=df.columns.names
        )

    df_combined = pd.concat([df['About'], df['Performance'], df['Aerial Duels']], axis=1)
    columns_to_exclude = ['# Pl', '90s']
    final_df = df_combined.drop(columns_to_exclude, axis=1)
    return final_df

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

def saveData(country, year, metric, data):
    import os
    BASE_DIR = '../FootballData'
    league_dir = os.path.join(BASE_DIR, country, str(year))
    os.makedirs(league_dir, exist_ok=True)

    csv_path = os.path.join(league_dir, )