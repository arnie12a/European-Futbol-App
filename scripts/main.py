def getDataForYear(year):
    import pandas as pd
    df = pd.read_html(f'https://fbref.com/en/squads/19538871/{str(year)}-{str(year+1)}/Manchester-United-Stats')[0]
    # df.columns = pd.MultiIndex.from_tuples(
    # [('About' if 'Unnamed' in level_0 else level_0, level_1) 
    #     for level_0, level_1 in df.columns],
    #         names=df.columns.names
    # )
    # df_combined = pd.concat([df['About'], df['Playing Time'], df['Performance']], axis=1)
    # columns_to_keep = ['Player', 'Nation', 'Pos', 'Age', 'MP', 'Min', 'Gls', 'Ast', 'G+A', 'PK']
    # df_combined = df_combined[columns_to_keep]
    return df.head()


def getFranceData():
    return

def getEnglandData():
    return

def getSpainData():
    return

def getGermanyData():
    return

def getItalyData():
    return