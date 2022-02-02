
import pandas as pd

global excel 
global mang_estrc_bd 
# mang_estrc_bd = pd.read_excel('sigma_estructura_bd.xlsx',sheet_name='db')
# mang_estrc_excel = pd.read_excel('sigma_estructura_excel.xlsx',sheet_name='excel_db')

def alistarData():
    excel = pd.read_excel('sigma_estructura_bd - copia.xlsx',sheet_name='DATA_EXCEL')
    bd = pd.read_excel('sigma_estructura_bd - copia.xlsx',sheet_name='DATA_BD')
    print(">-----------------------------------------------------------------------------------")
    print("CANT REGISTROS ORIGINALES EN LA BD: ",bd.shape[0])
    print("CANT REGISTROS ORIGINALES EN EL EXCEL: ",excel.shape[0])


    #quitar espacios en blanco y cañoa del identificador para los datos de la bd
    bd['IDENTIFICADOR'] = bd['IDENTIFICADOR'].str.replace(' ', '')
    bd['IDENTIFICADOR'] = bd['IDENTIFICADOR'].str.replace('Cañoa', 'Caño')

    #quitar espacios en blanco y cañoa del identificador para los datos del excel
    excel['IDENTIFICADOR'] = excel['IDENTIFICADOR'].str.replace(' ', '')
    excel['IDENTIFICADOR'] = excel['IDENTIFICADOR'].str.replace('Cañoa', 'Caño')
    excel['IDENTIFICADOR'] = excel['IDENTIFICADOR'].str.replace('Km', 'Kilómetro')

    #eliminar reg con identificadores vacios
    excel.dropna(subset=['IDENTIFICADOR'], inplace=True)
    bd.dropna(subset=['IDENTIFICADOR'], inplace=True)

    # excel['IDENTIFICADOR'] = excel['IDENTIFICADOR'].dropna()
    # bd['IDENTIFICADOR'] = bd['IDENTIFICADOR'].dropna()

    #guardar copia
    bd.to_excel("sigma_estructura_bd.xlsx", sheet_name='DATA_BD',index=False)
    excel.to_excel("sigma_estructura_excel.xlsx", sheet_name='DATA_EXCEL',index=False)
    print(">-----------------------------------------------------------------------------------")
    print("CANT REGISTROS EN LA COPIA DE LA BD: ",bd.shape[0])
    print("CANT REGISTROS EN LA COPIA DEL EXCEL: ",excel.shape[0])





def abrirExcels(verTambien):
    excel = pd.read_excel("sigma_estructura_bd.xlsx", sheet_name='DATA_BD')
    bd = pd.read_excel("sigma_estructura_excel.xlsx", sheet_name='DATA_EXCEL')
    if ('34930Rinconada21101' in list(bd['IDENTIFICADOR'])):
        print("present")
    else:
        print("no present en bd")
    
    if verTambien:
        print(">>>EXCEL: \n\n",excel)
        print(">>>BASE DE DATOS: \n\n",bd)
        
def verExcels():
    abrirExcels()
    print(">>>EXCEL: \n\n",excel)
    print(">>>BASE DE DATOS: \n\n",bd)
    
    
def verificar_coincidencias():
    #cargamos las hojas excel
    bd = pd.read_excel("sigma_estructura_bd.xlsx", sheet_name='DATA_BD')
    excel = pd.read_excel("sigma_estructura_excel.xlsx", sheet_name='DATA_EXCEL')
    excel = excel.where(excel.AÑO < 2019)
    i = 0
    p = 0
    print("CANT REGISTROS EN LA COPIA DEL EXCEL: ",excel.shape[0])
    for item in excel['IDENTIFICADOR']:
        if (item in list(bd['IDENTIFICADOR'])):
            #print(i," -",item)
            p=p+1
        else:
            print(i," -",item,"no present en bd")
            i=i+1
    print("cant registros no presentes : ",i)  
    print("cant registros presentes : ",p)  
    
    
    # datos['IDENTIFICADOR'].unique()
    
    # var1 = df.loc[df['IDENTIFICADOR'] == identificador, :]
    # var2 = df2.loc[df2['IDENTIFICADOR'] == identificador, :]

    
def alistarIdentificadores():
    #cargamos hojas de excel
    p=0
    i=0
    bd = pd.read_excel("sigma_estructura_bd.xlsx", sheet_name='DATA_BD')
    excel = pd.read_excel("sigma_estructura_excel.xlsx", sheet_name='DATA_EXCEL')
    
    #quitar espacios en blanco y cañoa del identificador para los datos de la bd
    bd['NOM_ESTACION'] = bd['NOM_ESTACION'].str.replace(' ', '')
    bd['NOM_ESTACION'] = bd['NOM_ESTACION'].str.replace('Cañoa', 'Caño')
    bd['NOM_ESTACION'] = bd['NOM_ESTACION'].str.replace('CañoGrandeE', 'CañoGrande')

    #quitar espacios en blanco y cañoa del ESTACION para los datos del excel
    excel['ESTACION'] = excel['ESTACION'].str.replace('Cañoa', 'Caño')
    excel['ESTACION'] = excel['ESTACION'].str.replace('Km', 'Kilómetro')
    
    #creamoos nueva col estacion-transecto para comparar con la BD
    excel['NOM_ESTACION'] = excel['ESTACION'] +" -"+ excel['TRANSECTO'].map(str)
    excel['NOM_ESTACION'] = excel['NOM_ESTACION'].str.replace(' ', '')
    
    
    #creamoos nueva col IDENTIFICADOR(FECHA-ESTACION-TRANSECTO-ROTULO ÁRBOL(ID)) para comparar con la BD
    #bd['FECHA'] =pd.to_datetime(bd['FECHA'])
    excel['ROTULO ÁRBOL        (ID)'] = list(map(int,excel['ROTULO ÁRBOL        (ID)']))
    excel['IDENTIFICADOR'] = excel['FECHA'].map(str) + excel['ESTACION'].map(str) + excel['TRANSECTO'].map(str) + excel['ROTULO ÁRBOL        (ID)'].map(str)
    excel['IDENTIFICADOR'] = excel['IDENTIFICADOR'].str.replace(' ', '')
    excel['IDENTIFICADOR'] = excel['IDENTIFICADOR'].str.replace('-', '')
    excel['IDENTIFICADOR'] = excel['IDENTIFICADOR'].str.replace('00:00:00', '')
    
    #creamoos nueva col IDENTIFICADOR(FECHA-NOM_ESTACION-ROTULO_ARBOL_ID) para comparar con el excel
    #bd['FECHA'] =pd.to_datetime(bd['FECHA']).dt.normalize()
    bd['ROTULO_ARBOL_ID'] = list(map(int,bd['ROTULO_ARBOL_ID']))
    bd['IDENTIFICADOR'] = bd['FECHA'].map(str) + bd['NOM_ESTACION'].map(str) + bd['ROTULO_ARBOL_ID'].map(str)
    bd['IDENTIFICADOR'] = bd['IDENTIFICADOR'].str.replace(' ', '')
    bd['IDENTIFICADOR'] = bd['IDENTIFICADOR'].str.replace('-', '')
    bd['IDENTIFICADOR'] = bd['IDENTIFICADOR'].str.replace('00:00:00', '')
    
  
    print("ESTACIONES BD\n\n",bd.info())
    print("ESTACIONES EXCEL\n\n",excel.info()) 
    print("ESTACIONES BD\n\n",bd)
    print("ESTACIONES EXCEL\n\n",excel) 
    #guardar copia
    bd.to_excel("sigma_estructura_bd.xlsx", sheet_name='DATA_BD',index=False)
    excel.to_excel("sigma_estructura_excel.xlsx", sheet_name='DATA_EXCEL',index=False)
    
def verificar_estaciones():
    p=0
    i=0
    bd = pd.read_excel("sigma_estructura_bd.xlsx", sheet_name='DATA_BD')
    excel = pd.read_excel("sigma_estructura_excel.xlsx", sheet_name='DATA_EXCEL')
    print("CANT REGISTROS EN LA COPIA DEL EXCEL: ",excel.shape[0])
    print("CANT REGISTROS EN LA COPIA DE BD: ",bd.shape[0])
    
    estacion_bd = list(bd.NOM_ESTACION.unique())
    estacion_excel = list(excel.NOM_ESTACION.unique())
    for item in estacion_excel:
        if (item in estacion_bd):
            #print(i," -",item)
            p=p+1
        else:
            print(i," -",item,"no coincide con la bd")
            i=i+1
    print("estaciones que coinciden con la bd: ",p)  
    print("estaciones que no coinciden con la bd: ",i)     
    print("ESTACIONES BD\n\n",estacion_bd)
    print("ESTACIONES EXCEL\n\n",estacion_excel)
 
 
#-------------------------------------------------------------------v 
bd = pd.read_excel("sigma_estructura_bd.xlsx", sheet_name='DATA_BD')
excel = pd.read_excel("sigma_estructura_excel.xlsx", sheet_name='DATA_EXCEL')
#borramos col no necesarias
del bd['ID_MUESTREOTX']
del bd['ID_MUESTRA']
#igualamos la col de estado
excel['ESTADO'] = excel['ESTADO'].str.replace('CA','1')
excel['ESTADO'] = excel['ESTADO'].str.replace('CO','2')
excel['ESTADO'] = excel['ESTADO'].str.replace('ME','3')
excel['ESTADO'] = excel['ESTADO'].str.replace('MU','4')
excel['ESTADO'] = excel['ESTADO'].str.replace('PA','5')
excel['ESTADO'] = excel['ESTADO'].str.replace('VI','6')


#igualamos la estructura de los dataframes en
excel.columns = [
'FECHA',
'AÑO',
'IDENTIFICADOR',
'ESTACION',
'CÓDIGO_ESTACIÓN',
'TRANSECTO',
'PARCELA',
'ESPECIE',
'ROTULO_ARBOL_ID',
'TAG',
'ESTADO',
'TIPO_DES',
'NEW_TAG',
'ALTURA_METROS',
'DAP',
'CATEGORÍA DIAMÉTRICA',
'OBSERVACIONES',
'AB',
'NOM_ESTACION'
]

# bd.columns = [
#         'ID_MUESTREOTX',
#     	'ID_MUESTRA',
#     	'FECHA',
#     	'IDENTIFICADOR',
#      	'NOM_ESTACION',
#     	'ESTACION',
#     	'TRANSECTO',
#     	'SUBPARCELA',
#     	'SECTOR',
#     	'ESPECIE',
#     	'ESPECIE_DES',
#     	'ROTULO_ARBOL_ID',
#     	'TAG',
#     	'ESTADO',
#     	'ESTADO_DES',
#     	'ID_TIPO',
#     	'TIPO_DES',
#     	'ALTURA_METROS',
#     	'CAP',
#     	'DAP']


identificadores = list(excel['IDENTIFICADOR'])
compareDf = pd.DataFrame(columns=['IDENTIFICADOR','COMPARACION'])
compareDf['IDENTIFICADOR'] = identificadores
# print(compareDf)
data = pd.DataFrame (columns= ['FECHA','IDENTIFICADOR','ESTACION','TRANSECTO','ESPECIE','ROTULO_ARBOL_ID','TAG','ESTADO','ALTURA_METROS','DAP'])
for identificador in identificadores:
    excelRegister = bd.loc[bd['IDENTIFICADOR'] == identificador, [
    'FECHA',
    'IDENTIFICADOR',
    'ESTACION',
    'TRANSECTO',
    'ESPECIE',
    'ROTULO_ARBOL_ID',
    'TAG',
    'ESTADO',
    'ALTURA_METROS',
    'DAP'
    ]]
    data = data.append(excelRegister)
print(data)


    
#print("corre codigo...\n")
#print("bd\n\n",bd)
#print("\n",bd.info())
#print("excel\n\n",excel,
#print("\n",excel.info())

#PREPARAMOS LOS DATAFRAMES
#alistarData()
#alistarIdentificadores()

#VERIFICAMOS LOS IDENTIFICADORES
# verificar_coincidencias()

#VERIFICAMOS ESTACIONES
# verificar_estaciones()

#abrirExcels(1)
#verExcels()

#bd = pd.read_excel("sigma_estructura_bd.xlsx", sheet_name='DATA_BD')
# print(bd)
#print(list(bd.NOM_ESTACION.unique()))





"""
#miramos los registros generados
bd = pd.read_excel('sigma_estructura_bd.xlsx',sheet_name='DATA_BD')
excel = pd.read_excel('sigma_estructura_excel.xlsx',sheet_name='DATA_EXCEL')

print("ANTES excel\n\n",excel[excel['IDENTIFICADOR'].isnull()])
print("ANTES bd\n\n",bd[bd['IDENTIFICADOR'].isnull()])
excel = excel.dropna()
bd = bd.dropna()
print("DESPUES excel\n\n",excel[excel['IDENTIFICADOR'].isnull()])
print("DESPUES bd\n\n",bd[bd['IDENTIFICADOR'].isnull()])

"""


"""
#print(">>>DB1: \n\n",bd)

#del bd['IDENTIFICADOR']
#print (">>>before deleting blank spaces\n",bd)
#print (">>>previus info\n",bd.info())
#bd['ID_MUESTREOTX'] = bd['ID_MUESTREOTX'].astype(str)
#print (">>>new info\n",bd.info())
#bd['IDENTIFICADOR'] = bd['IDENTIFICADOR'].str.replace(' ', '')
#bd['IDENTIFICADOR'] = bd['IDENTIFICADOR'].str.replace('Cañoa', 'Caño')
#bd.to_excel("sigma_estructura_bd.xlsx", sheet_name='db',index=False)
#excel.to_excel("sigma_estructura_bd.xlsx", sheet_name='db',index=False)
#print (">>>after deleting blank spaces\n",bd)
#print(bd.info())

# #FILTRAR POR MUERTOS
# excel['ESTADO'] = excel['ESTADO'].astype(str)#conversion de estado
# print(excel.info())
# df1 = excel[excel['ESTADO'].str.contains("MU")]#nuevo dataframe que solo contiene registros de estado MU
# print(df1)
#convert cañoa to caño
i=0
print("ANTES\n\n",excel[excel['IDENTIFICADOR'].isnull()])
print("ANTES\n\n",bd[bd['IDENTIFICADOR'].isnull()])
excel = excel.dropna()
bd = bd.dropna()
print("DESPUES\n\n",excel[excel['IDENTIFICADOR'].isnull()])
print("DESPUES\n\n",bd[bd['IDENTIFICADOR'].isnull()])
# for item in excel['IDENTIFICADOR']:
#     if (item in list(bd['IDENTIFICADOR'])):
#         #print(i," -",item)
#         i=i+1
#     else:
#         print(i," -",item,"no present excel")
    #i=i+1
print("cant registros presentes: ",i)    
#print(">>>DB:\n\n ",bd)
#rslt_df = bd[bd['ALTURA_METROS'] > 3]
#print(">>>after filtering:\n\n",rslt_df)
#print(">>>EXCEL:\n\n ",excel)
#print("Iguales?\n",bd.equals(excel))"""