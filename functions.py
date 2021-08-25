def makaan_scraper_v1():
    '''scrapes the popular real estate website makaan.com to get data such as coordinates, property type, locality, area'''
    import requests
    from bs4 import BeautifulSoup
    import numpy as np
    import pandas as pd
    import json
    url = 'https://www.makaan.com/hyderabad-residential-property/rent-property-in-hyderabad-city'
    response = requests.get(url)
    if response.ok:
        soup = BeautifulSoup(response.text, "lxml")
        pagenav = soup.select(".pagination > :nth-of-type(1) >:nth-of-type(7)>:nth-of-type(1)")
        num_pages = int(pagenav[0].text)
        mainlist=[]
    for i in range(1,num_pages):
        url1 = 'https://www.makaan.com/hyderabad-residential-property/rent-property-in-hyderabad-city' + '?page='+str(i)
        response = requests.get(url1)
        if response.ok:
            soup = BeautifulSoup(response.text, "lxml")
            cards = soup.select(".cardWrapper > script")
            for j in range(len(cards)):
                attrs = json.loads(cards[j].text)
                mylist=[attrs['latitude'],attrs['longitude'],attrs['bedrooms'],attrs['sellerType'],attrs['propertyType'],attrs['localityName'],attrs['suburbName'],attrs['size'].split()[0],('').join(attrs['size'].split()[1:]),attrs['price']]
                mainlist.append(mylist)
        print(i)        

            
    
    columns = ('latitude','longitude','bedrooms','seller','property_type','locality','suburb','area','units','rent')
    df = pd.DataFrame(mainlist,columns=columns)
    return df





def model_maker(df):
    import pandas as pd
    import numpy as np
    from sklearn.preprocessing import OneHotEncoder, StandardScaler
    from sklearn.pipeline import Pipeline
    from sklearn.compose import ColumnTransformer
    from sklearn.ensemble import RandomForestRegressor
    from sklearn.cluster import KMeans
    #Remove outliers
    df['area']= df['area'].apply(lambda x: int(x.replace(',','')))
    df_shortened = df[(df['latitude']>17.1) & (df['latitude']<17.7) & (df['longitude']>78.1) & (df['longitude']<78.8) & (df['bedrooms']<=6) & (df['area']<=2400)]
    df = df_shortened
    #clustering
    coords= list(zip(df['latitude'],df['longitude']))
    kmeans = KMeans(n_clusters = 100, random_state=0) #arbitrary number, we shall optimise later
    coords = kmeans.fit_predict(coords)
    df['cluster_center']=coords
    df = df[['latitude','longitude','bedrooms','area','seller','property_type','cluster_center','rent']]
    #training
    X = df.drop('rent',axis=1)
    y=df['rent']
    num_pipeline = Pipeline([('std_scaler',StandardScaler())])
    cat_pipeline = Pipeline([('one_hot',OneHotEncoder())])
    num_attribs = ['latitude','longitude','bedrooms','area']
    cat_attribs=['seller','property_type','cluster_center']
    full_pipeline = ColumnTransformer([('num',num_pipeline,num_attribs),('cat',cat_pipeline,cat_attribs),])
    X_prepared = full_pipeline.fit_transform(X)
    rfr = RandomForestRegressor(n_estimators = 200)
    rfr.fit(X_prepared,y)
    mylist = [kmeans,rfr,full_pipeline]
    return mylist


  