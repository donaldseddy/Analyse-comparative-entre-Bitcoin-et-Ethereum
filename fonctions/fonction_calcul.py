'''fonction permetant de calculer le score et retourne la colonne du datafame calcule
    parameter: df:dataframe
                value: selection de la colonne a calculer
                period :period d'analyse
'''
def calcul_z_scrore(df,value:str,period:int):
    rolling_mean=df[value].rolling(window=period).mean()
    rolling_std=df[value].rolling(window=period).std()
    z_scrore=(df[value] - rolling_mean)/rolling_std
    df['Z_SCRORE']=z_scrore
    return df
