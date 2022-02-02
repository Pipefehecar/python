import pandas as pd 

def importarDatos():
    excel = pd.read_excel('sigma_estructura_bd - copia.xlsx',sheet_name='DATA_EXCEL')
    bd = pd.read_excel('sigma_estructura_bd - copia.xlsx',sheet_name='DATA_BD')
    bd.to_excel("sigmaEstructura_bd.xlsx", sheet_name='DATA_BD',index=False)
    excel.to_excel("sigmaEstructura_excel.xlsx", sheet_name='DATA_EXCEL',index=False)
    
def igualarColumnas():#col deben tener el mismo nombre y los registros deben estar descritos de la misma forma
    bd = pd.read_excel("sigmaEstructura_bd.xlsx", sheet_name='DATA_BD')
    excel = pd.read_excel("sigmaEstructura_excel.xlsx", sheet_name='DATA_EXCEL')
    #cambiamos la descripcion de los registros
    #igualamos la col de estado
    excel['ESTADO'] = excel['ESTADO'].str.replace('CA','1')
    excel['ESTADO'] = excel['ESTADO'].str.replace('CO','2')
    excel['ESTADO'] = excel['ESTADO'].str.replace('ME','3')
    excel['ESTADO'] = excel['ESTADO'].str.replace('MU','4')
    excel['ESTADO'] = excel['ESTADO'].str.replace('PA','5')
    excel['ESTADO'] = excel['ESTADO'].str.replace('VI','6')
    excel['ID_TIPO'] = excel['ID_TIPO'].str.replace('R','7')
    excel['ID_TIPO'] = excel['ID_TIPO'].str.replace('T','8')
    #cambiamos los nombres de las colas de la misma
    excel.columns['FECHA','AÑO','IDENTIFICADOR','ESTACION','CÓDIGOESTACIÓN','TRANSECTO','PARCELA','ESPECIE','ROTULO_ARBOL_ID','TAG','ESTADO','ID_TIPO','NEW TAG o INDIV','ALTURA_METROS','DAP','CATEGORÍA DIAMÉTRICA','OBSERVACIONES','AB']
    bd.to_excel("sigmaEstructura_bd.xlsx", sheet_name='DATA_BD',index=False)
    excel.to_excel("sigmaEstructura_excel.xlsx", sheet_name='DATA_EXCEL',index=False)
def armarIdentificador():
    

importarDatos()