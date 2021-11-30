import pandas as pd, time, sys                       
from pytrends.request import TrendReq

# Validamos que se han pasado todos los parámetros necesarios
if len(sys.argv) == 6:
    fecha_inicio=sys.argv[1] #format yyyy-mm-dd
    fecha_fin=sys.argv[2] #format yyyy-mm-dd
    geolocalizacion=sys.argv[3] #ES para España 
    fichero_entrada=sys.argv[4]
    fichero_salida=sys.argv[5]
    crawldf = pd.read_csv('entrada.csv')
    nombres= crawldf['consulta'].tolist()
    pytrends = TrendReq(hl='es-ES', tz=60)
    dfFinal= pd.DataFrame()
    cont=0
    for row in nombres:
        kw_list = [row] 
        # build the payload
        pytrends.build_payload(kw_list, timeframe=fecha_inicio+' '+fecha_fin, geo=geolocalizacion)
        # store interest over time information in df
        df = pytrends.interest_over_time()
        if not df.empty:
            df=df.drop(['isPartial'],axis=1) #Eliminamos la columna 'isPartial'
            if cont == 0: 
                dfFinal=df
            else:  
                lista=df[df.columns.values[0]].values
                dfFinal[df.columns.values[0]]=lista
            time.sleep(1)
        cont=cont+1
    dfFinal.to_csv(fichero_salida)
