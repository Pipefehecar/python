from asyncio.windows_events import NULL
from cmath import nan
from datetime import datetime
import math
from tkinter.tix import ROW
from numpy.core.numeric import NaN
import random
import pandas as pd

def alistarData():
    ###bdEstructura = pd.read_excel('xlsxS/BD_CGSM_ESTRUCTURA_LABSIS_2021.12.03.xlsx', sheet_name='BD_Estructura')
    bdEstructura = pd.read_excel('xlsxS/ESTRUCTURA_2022.01.19_LABSIS.xlsx', sheet_name='BD_Estructura')
    bdEstructura.columns = [
    'IDENTIFICADOR','FECHA','AÑO',
    'ESTACION','CÓDIGO_ESTACION',
    'TRANSECTO','PARCELA','ESPECIE',
    'TAG','ROTULO','ESTADO','TIPO',
    'NEW','ALTURA','DAP',
    'CATEGORÍA_DIAMETRICA',
    'OBSERVACIONES','AB'
    ]
    bdEstructura['ESTACION_BD'] = bdEstructura['ESTACION'] + "-" + bdEstructura['TRANSECTO'].map(str) 
    bdEstructura['ESTACION_BD'] = bdEstructura['ESTACION_BD'].str.replace(' ','')
    #Asignamos los id segun la bd
    bdEstructura['ID_ESTACION'] = bdEstructura['ESTACION_BD']
    bdEstructura['ID_ESTACION'] = bdEstructura['ID_ESTACION'].str.replace('AguasNegras-1','45924')
    bdEstructura['ID_ESTACION'] = bdEstructura['ID_ESTACION'].str.replace('AguasNegras-2','45926')
    bdEstructura['ID_ESTACION'] = bdEstructura['ID_ESTACION'].str.replace('AguasNegras-3','45928')
    bdEstructura['ID_ESTACION'] = bdEstructura['ID_ESTACION'].str.replace('CañoGrande-1','45930')
    bdEstructura['ID_ESTACION'] = bdEstructura['ID_ESTACION'].str.replace('CañoGrande-2','45932')
    bdEstructura['ID_ESTACION'] = bdEstructura['ID_ESTACION'].str.replace('CañoGrande-3','45934')
    bdEstructura['ID_ESTACION'] = bdEstructura['ID_ESTACION'].str.replace('Km22-1','45907')
    bdEstructura['ID_ESTACION'] = bdEstructura['ID_ESTACION'].str.replace('Km22-2','45910')
    bdEstructura['ID_ESTACION'] = bdEstructura['ID_ESTACION'].str.replace('Km22-3','45912')
    bdEstructura['ID_ESTACION'] = bdEstructura['ID_ESTACION'].str.replace('Luna-1','45922')
    bdEstructura['ID_ESTACION'] = bdEstructura['ID_ESTACION'].str.replace('Luna-2','47837')
    bdEstructura['ID_ESTACION'] = bdEstructura['ID_ESTACION'].str.replace('Luna-3','47839')
    bdEstructura['ID_ESTACION'] = bdEstructura['ID_ESTACION'].str.replace('Rinconada-1','45914')
    bdEstructura['ID_ESTACION'] = bdEstructura['ID_ESTACION'].str.replace('Rinconada-2','45916')
    bdEstructura['ID_ESTACION'] = bdEstructura['ID_ESTACION'].str.replace('Rinconada-3','45920')
    bdEstructura['ID_ESTACION'] = bdEstructura['ID_ESTACION'].str.replace('Sevillano-1','50089')
    bdEstructura['ID_ESTACION'] = bdEstructura['ID_ESTACION'].str.replace('Sevillano-2','50091')
    bdEstructura['ID_ESTACION'] = bdEstructura['ID_ESTACION'].str.replace('Sevillano-3','50093')
    
    #generamos los id_muestreo
    bdEstructura['ROTULO'] = bdEstructura['ROTULO'].map(int)
    print(bdEstructura.info())
    bdEstructura['FECHA'] = bdEstructura['FECHA'].dt.strftime('%d/%m/%y')
    # bdEstructura['FECHA'] = bdEstructura['FECHA'].dt.date
    bdEstructura['ID_MUESTREO'] =bdEstructura['ID_ESTACION'] + bdEstructura['FECHA'].map(str).str.replace('/','') 
    bdEstructura['ID_MUESTRA'] = bdEstructura['ID_MUESTREO'] + bdEstructura['ROTULO'].map(str)
    bdEstructura['ALTURA'] = bdEstructura['ALTURA'].round(decimals=2)
    bdEstructura['DAP'] = bdEstructura['DAP'].round(decimals=2)
    #bdEstructura = bdEstructura.style.format({"ALTURA": "{:,d}", "DAP": "{:,d}",})
    # bdEstructura['ID_MUESTRA'] = bdEstructura['ID_MUESTRA'].map(int)
    bdEstructura.fillna('',inplace=True)
    # print(bdEstructura['ESTACION_BD'].unique())
    # for row in bdEstructura:
        # row['ESTACION_BD'] = concat(row['ESTACION'], row['TRANSECTO']) 
        
    
    # bdEstructura[['FECHA','AÑO','TRANSECTO','ROTULO','ALTURA','DAP','AB','ID_MUESTRA']] = bdEstructura[['FECHA','AÑO','TRANSECTO','ROTULO','ALTURA','DAP','AB','ID_MUESTRA']].astype(str)
    
    print(bdEstructura.info())
    print(bdEstructura)
    bdEstructura.to_excel('xlsxS/data/BD_2239_3-toUpload(real).xlsx',index=False)

# GENERAR MUESTRAS
def generarAGD_MUESTRAS():
    bdEstructura = pd.read_excel('xlsxS/data/BD_2239_3-toUpload(real).xlsx')
    muestras = pd.DataFrame(columns = ['ID_MUESTRA','ID_MUESTREO','NOTAS'])
    muestras['ID_MUESTRA'] = bdEstructura['ID_MUESTRA'].map(str)
    muestras['ID_MUESTREO'] = bdEstructura['ID_MUESTREO'].map(str)
    muestras['NOTAS'] = bdEstructura['OBSERVACIONES']
    #muestras['ES_REPLICA'] = 1 #siempre es 1??
    print(muestras.info())
    print(muestras)
    muestras.to_excel('xlsxS/data/BD_2239_3-ToUpload(muestras).xlsx',index=False)
    
# GENERAR MUESTREOS
def generarAGD_MUESTREOS():
    bdEstructura = pd.read_excel('xlsxS/data/BD_2239_3-toUpload(real).xlsx')
    muestreos = pd.DataFrame(columns = ['ID_MUESTREO','ID_ESTACION','ID_PROYECTO','ID_METODOLOGIA','ID_TEMATICAS','FECHA','NOTAS'])
    result_bdEstructura = bdEstructura.drop_duplicates(subset=['ID_MUESTREO'])
    muestreos['ID_MUESTREO'] = result_bdEstructura['ID_MUESTREO'].map(str)
    muestreos['ID_ESTACION'] = result_bdEstructura['ID_ESTACION'].map(str)
    muestreos['ID_PROYECTO'] = 1513 #2239
    muestreos['ID_METODOLOGIA'] = 3 #3
    muestreos['ID_TEMATICAS'] = 224
    muestreos['FECHA'] = result_bdEstructura['FECHA']
    muestreos['NOTAS'] = 'MUESTREO GENERADO A PARTIR DE BD HISTORICA DE MANGLAR'
   # muestreos['FECHASIS'] = datetime.now().date() #no es necesario, dejar asignacion de la bd
    print(muestreos.info())
    print(muestreos)
    muestreos.to_excel('xlsxS/data/BD_2239_3-ToUpload(muestreos).xlsx',index=False)
    #muestreos.to_excel('xlsxS/data/BD_2239_3-toUpload(muestreos).xlsx',index=False)
    
        
# GENERAR MUESTRAS VARIABLES(ID_PARAMETRO ID_METODOLOGIA ID_UNIDAD_MEDIDA ID_MUESTRA ID_METODO VALOR QUALITY_FLAG PRECISION)
def generarAGD_MUESTRAS_VARIABLES():
#     270	Altura	663	Regla
#     270	Altura	48	Hipsómetro--
#     270	Altura	633	Estimación visual directa
#     270	Altura	47	Clinómetro----
#     372	Circunferencia altura pecho	615	Cinta métrica
#     263	Diametro altura pecho	614	Cinta diamétrica
#     263	Diametro altura pecho	744	Forcípula
    bdEstructura = pd.read_excel('xlsxS/data/BD_2239_3-toUpload(real).xlsx')
    muestras_variables = pd.DataFrame(columns = ['ID_PARAMETRO','ID_METODOLOGIA','ID_UNIDAD_MEDIDA','ID_MUESTRA','ID_METODO','VALOR','QUALITY_FLAG','PRECISION'])
    for i, row in bdEstructura.iterrows():
        id_muestraa = str(row['ID_MUESTRA'])
        # row['NEW'] = str(row['NEW'])
        #ID
        if not(math.isnan(row['ROTULO'])):
            muestras_variables = muestras_variables.append({'ID_PARAMETRO':249, 'ID_METODOLOGIA':3,'ID_UNIDAD_MEDIDA':100,'ID_MUESTRA':id_muestraa,'ID_METODO':732, 'VALOR':row['ROTULO'],'QUALITY_FLAG':2,'PRECISION':NaN}, ignore_index=True)
        
            #Diametro altura pecho ¿ID METODO? 614 o 633
        if not(math.isnan(row['DAP'])):
            # print(id_muestraa,row['DAP'])
            muestras_variables = muestras_variables.append({'ID_PARAMETRO':263, 'ID_METODOLOGIA':3,'ID_UNIDAD_MEDIDA':10,'ID_MUESTRA':id_muestraa,'ID_METODO':614, 'VALOR':row['DAP'],'QUALITY_FLAG':2,'PRECISION':NaN}, ignore_index=True)
        if not(math.isnan(row['ALTURA']) ):
            #Altura (m) ¿ID METODO? 633 estimacion visual o 47 clinometro
            muestras_variables = muestras_variables.append({'ID_PARAMETRO':270, 'ID_METODOLOGIA':3,'ID_UNIDAD_MEDIDA':11,'ID_MUESTRA':id_muestraa,'ID_METODO':633, 'VALOR':row['ALTURA'],'QUALITY_FLAG':2,'PRECISION':NaN}, ignore_index=True)
        
        #Estado arbol valor = id_estado () AG_LOVE -> TABLA 1
        if (row['ESTADO'] != ""):
            if row['ESTADO'] == 'CA':
                muestras_variables = muestras_variables.append({'ID_PARAMETRO':252, 'ID_METODOLOGIA':3,'ID_UNIDAD_MEDIDA':100,'ID_MUESTRA':id_muestraa,'ID_METODO':732, 'VALOR':1,'QUALITY_FLAG':2,'PRECISION':NaN}, ignore_index=True)
            if row['ESTADO'] == 'CO':
                muestras_variables = muestras_variables.append({'ID_PARAMETRO':252, 'ID_METODOLOGIA':3,'ID_UNIDAD_MEDIDA':100,'ID_MUESTRA':id_muestraa,'ID_METODO':732, 'VALOR':2,'QUALITY_FLAG':2,'PRECISION':NaN}, ignore_index=True)
            if row['ESTADO'] == 'ME':
                muestras_variables = muestras_variables.append({'ID_PARAMETRO':252, 'ID_METODOLOGIA':3,'ID_UNIDAD_MEDIDA':100,'ID_MUESTRA':id_muestraa,'ID_METODO':732, 'VALOR':3,'QUALITY_FLAG':2,'PRECISION':NaN}, ignore_index=True)
            if row['ESTADO'] == 'MU':
                muestras_variables = muestras_variables.append({'ID_PARAMETRO':252, 'ID_METODOLOGIA':3,'ID_UNIDAD_MEDIDA':100,'ID_MUESTRA':id_muestraa,'ID_METODO':732, 'VALOR':4,'QUALITY_FLAG':2,'PRECISION':NaN}, ignore_index=True)
            if row['ESTADO'] == 'PA':
                muestras_variables = muestras_variables.append({'ID_PARAMETRO':252, 'ID_METODOLOGIA':3,'ID_UNIDAD_MEDIDA':100,'ID_MUESTRA':id_muestraa,'ID_METODO':732, 'VALOR':5,'QUALITY_FLAG':2,'PRECISION':NaN}, ignore_index=True)
            if row['ESTADO'] == 'VI':
                muestras_variables = muestras_variables.append({'ID_PARAMETRO':252, 'ID_METODOLOGIA':3,'ID_UNIDAD_MEDIDA':100,'ID_MUESTRA':id_muestraa,'ID_METODO':732, 'VALOR':6,'QUALITY_FLAG':2,'PRECISION':NaN}, ignore_index=True)
            if row['ESTADO'] == 'NE': 
                muestras_variables = muestras_variables.append({'ID_PARAMETRO':252, 'ID_METODOLOGIA':3,'ID_UNIDAD_MEDIDA':100,'ID_MUESTRA':id_muestraa,'ID_METODO':732, 'VALOR':7,'QUALITY_FLAG':2,'PRECISION':NaN}, ignore_index=True)
            if row['ESTADO'] == 'NA': 
                muestras_variables = muestras_variables.append({'ID_PARAMETRO':252, 'ID_METODOLOGIA':3,'ID_UNIDAD_MEDIDA':100,'ID_MUESTRA':id_muestraa,'ID_METODO':732, 'VALOR':8,'QUALITY_FLAG':2,'PRECISION':NaN}, ignore_index=True)
        
        #REVISAR ESTADO NA no asignado? QUE PASA CON LOS VACIOS PARA ESTADO????????
        #else: #PA ERROR CDG SIN DEFINIR	7 -CO ERROR CDG SIN DEFINIR	8 ***************************
            #muestras_variables = muestras_variables.append({'ID_PARAMETRO':252, 'ID_METODOLOGIA':3,'ID_UNIDAD_MEDIDA':100,'ID_MUESTRA':id_muestraa,'ID_METODO':732, 'VALOR':"-",'QUALITY_FLAG':2,'PRECISION':NaN}, ignore_index=True)
        
        
        #Tipo (vivo o muerto)
        if (row['TIPO'] != ""):
            if row['TIPO'] == "T":
                muestras_variables = muestras_variables.append({'ID_PARAMETRO':281, 'ID_METODOLOGIA':3,'ID_UNIDAD_MEDIDA':100,'ID_MUESTRA':id_muestraa,'ID_METODO':732, 'VALOR':8,'QUALITY_FLAG':2,'PRECISION':NaN}, ignore_index=True)
            if row['TIPO'] == "R":
                muestras_variables = muestras_variables.append({'ID_PARAMETRO':281, 'ID_METODOLOGIA':3,'ID_UNIDAD_MEDIDA':100,'ID_MUESTRA':id_muestraa,'ID_METODO':732, 'VALOR':7,'QUALITY_FLAG':2,'PRECISION':NaN}, ignore_index=True)
            #si no es ni T ni R queda vacio igual? o no asignado? ******************************
            #else:
            #    muestras_variables = muestras_variables.append({'ID_PARAMETRO':281, 'ID_METODOLOGIA':3,'ID_UNIDAD_MEDIDA':100,'ID_MUESTRA':id_muestraa,'ID_METODO':732, 'VALOR':'N/a','QUALITY_FLAG':2,'PRECISION':NaN}, ignore_index=True)
            
            
        #TAG
        if ((row['TAG']) != ""):
            muestras_variables = muestras_variables.append({'ID_PARAMETRO':282, 'ID_METODOLOGIA':3,'ID_UNIDAD_MEDIDA':100,'ID_MUESTRA':id_muestraa,'ID_METODO':732, 'VALOR':row['TAG'],'QUALITY_FLAG':2,'PRECISION':NaN}, ignore_index=True)
       
        #ESPECIE ¿ID METODO? 95(ICTPM (SAMP)) 629(Entrevista) 732(Observación directa)? **********************
        #if (row['ESPECIE'] != '' or not(row['ESPECIE'].isnull()) or not(len(str(row['ESPECIE']))) == 0):
        if not(str(row['ESPECIE']) == 'nan' ):
            print(len(str(row['ESPECIE'])),row['ESPECIE'])
            muestras_variables = muestras_variables.append({'ID_PARAMETRO':585, 'ID_METODOLOGIA':3,'ID_UNIDAD_MEDIDA':100,'ID_MUESTRA':id_muestraa,'ID_METODO':732, 'VALOR':row['ESPECIE'],'QUALITY_FLAG':2,'PRECISION':NaN}, ignore_index=True)
        # if row['NEW']=='':
        #     print("New vacio")
        if i % 100 == 0:
            print("muestra numero: ",i)
        # if i % 20000 == 0:
        #     muestras_variables.to_excel('xlsxS/2239_3-toUpload/BD_2239_3-ToUpload(muestras_variables)-'+i+'.xlsx',index=False)
        #     muestras_variables.drop(muestras_variables.index[:i],inplace=True)
       
    print(muestras_variables.info())
    print(muestras_variables)
    muestras_variables.to_excel('xlsxS/data/BD_2239_3-ToUpload(muestras_variables).xlsx',index=False)
    
# GENERAR MUESTREOS PARAMETROS (ID_MUESTREO ID_PARAMETRO ID_METODOLOGIA ID_UNIDAD_MEDIDA VALOR) 
# REEMPLAAZDO POR MUESTREOS PARAMETORS AREAS
def generarAGD_MUESTREOS_PARAMETROS():
    bdEstructura = pd.read_excel('xlsxS/data/BD_2239_3-toUpload(real).xlsx')
    muestreos_parametros = pd.DataFrame(columns = ['ID_MUESTREO','ID_PARAMETRO','ID_METODOLOGIA','ID_UNIDAD_MEDIDA','VALOR'])
    result_bdEstructura = bdEstructura.drop_duplicates(subset=['ID_MUESTREO'])
    result_bdEstructura['ID_MUESTREO'] = result_bdEstructura['ID_MUESTREO'].map(str)
    for i, row in result_bdEstructura.iterrows():
        #Area
        muestreos_parametros = muestreos_parametros.append({'ID_MUESTREO':row['ID_MUESTREO'], 'ID_PARAMETRO':860,'ID_METODOLOGIA':3, 'ID_UNIDAD_MEDIDA':109,'VALOR':100}, ignore_index=True)
        # muestreos_parametros = muestreos_parametros.append({'ID_MUESTREO':row['ID_MUESTREO'], 'ID_PARAMETRO':860,'ID_METODOLOGIA':3, 'ID_UNIDAD_MEDIDA':109,'VALOR':100}, ignore_index=True)
    
    print(muestreos_parametros.info())
    print(muestreos_parametros)
    muestreos_parametros.to_excel('xlsxS/data/2239_3-toUpload/BD_2239_3-ToUpload(muestreos_parametros).xlsx',index=False)

# 860	Area	A
# 901	Subparcelas muestreadas	SuPM
# 1055	Versión plantilla	1055
# 1170	Archivo fuente	1170

# GENERAR MUESTREOS PARAMETROS (areas de parcelas)(ID_MUESTREO ID_PARAMETRO ID_METODOLOGIA ID_UNIDAD_MEDIDA VALOR)
def generarAGD_MUESTREOS_PARAMETROS_AREAS(): #ACA CREAMOS LOS PARAMETROS DE LOS MUESTREOS, LOS MUESTREOS SON GENERADOS MAS ABAJO EN documentarNO_MUESTREADOS()
    bdEstructura = pd.read_excel('xlsxS/data/BD_2239_3-toUpload(real).xlsx')
    #bdAREAS = pd.read_excel('xlsxS/BD_2239_3_areas-toUpload.xlsx')
    muestreos_parametros = pd.DataFrame(columns = ['ID_MUESTREO','ID_PARAMETRO','ID_METODOLOGIA','ID_UNIDAD_MEDIDA','VALOR'])
    areas_resumen = pd.read_excel('xlsxS/BD_2239_3-ToUpload(somedataa).xlsx')
    # muestreos_parametros = pd.read_excel('xlsxS/2239_3-toUpload/BD_2239_3-ToUpload(muestreos_parametros).xlsx')
    
    result_bdEstructura = bdEstructura.drop_duplicates(subset=['ID_MUESTREO'])
    result_bdEstructura['ID_MUESTREO'] = result_bdEstructura['ID_MUESTREO'].map(str)
    areas_resumen['N_PARCELAS'] = areas_resumen['N_PARCELAS'].map(str)
    for p, muestreo in result_bdEstructura.iterrows():
        
        for i, areas in areas_resumen.iterrows():
            if muestreo['ID_ESTACION'] == areas['ID_ESTACION'] and muestreo['AÑO'] == areas['AÑO']:
                print('muestreo:',p)
                #parametros -> 901 = subparcelas muestreadas 860 = Area
                muestreos_parametros = muestreos_parametros.append({'ID_MUESTREO':muestreo['ID_MUESTREO'], 'ID_PARAMETRO':860,'ID_METODOLOGIA':3, 'ID_UNIDAD_MEDIDA':109,'VALOR':areas['AREA']}, ignore_index=True)
                # print({'ID_MUESTREO':muestreo['ID_MUESTREO'], 'ID_PARAMETRO':860,'ID_METODOLOGIA':3, 'ID_UNIDAD_MEDIDA':109,'VALOR':areas['AREA']})
                #muestreos_parametros = muestreos_parametros.append({'ID_MUESTREO':muestreo['ID_MUESTREO'], 'ID_PARAMETRO':901,'ID_METODOLOGIA':3, 'ID_UNIDAD_MEDIDA':100,'VALOR':800}, ignore_index=True)
                # print({'ID_MUESTREO':muestreo['ID_MUESTREO'], 'ID_PARAMETRO':901,'ID_METODOLOGIA':3, 'ID_UNIDAD_MEDIDA':100,'VALOR':areas['N_PARCELAS']})
                muestreos_parametros = muestreos_parametros.append({'ID_MUESTREO':muestreo['ID_MUESTREO'], 'ID_PARAMETRO':901,'ID_METODOLOGIA':3, 'ID_UNIDAD_MEDIDA':100,'VALOR':areas['N_PARCELAS']}, ignore_index=True)
                #
                muestreos_parametros = muestreos_parametros.append({'ID_MUESTREO':muestreo['ID_MUESTREO'], 'ID_PARAMETRO':1170,'ID_METODOLOGIA':3, 'ID_UNIDAD_MEDIDA':100,'VALOR':'Datos rescatados de BD EXCEL con informacion historica de estructura de maglar'}, ignore_index=True)
        
        #print(muestreos_parametros.info())
        #print(muestreos_parametros)
    muestreos_parametros.to_excel('xlsxS/data/BD_2239_3-ToUpload(muestreos_parametros).xlsx',index=False)
    print(muestreos_parametros.info())
# 860	Area	A
# 901	Subparcelas muestreadas	SuPM
# 1055	Versión plantilla	1055
# 1170	Archivo fuente	1170

    """
    10->Parcela desmontada / sin montar
    20->Parcela sin vegetación
    30->Parcela NO monitoreada
    40->Parcela visitada con vegetacion	
    
    """
#procedimiento para ordenar registros por año por transecto
def ordenarAreas_parcelas():
    NO_MONTADA = 0
    NO_MONITOREADA = 0
    SIN_VEGETACION = 0
    N_PARCELAS = 0
    DATA = {}
    bdAREAS = pd.read_excel('xlsxS/BD_2239_3_areas-toUpload.xlsx', sheet_name='REAL')
    print(bdAREAS)
    #bdAREAS.sort_values(by=['AÑO'], inplace=True)
    # bdAREAS.sort_values(by=['ESTACION'], inplace=True)
    
    areas_resumen = pd.DataFrame(columns = ['ID_ESTACION','ESTACION','AÑO','AREA','N_PARCELAS','NO_MONTADA','NO_MONITOREADA','SIN_VEGETACION'])
    # ID_ESTACION1 = bdAREAS.loc[0, 'ID_ESTACION']
    # AÑO1 = bdAREAS.loc[0, 'AÑO']
  
    # ESTACIONES = (
    #     45924, 45926, 45928, 45930, 45932, 45934,45907, 45910, 45912, 42400, 42396, 42398, 45922, 47837, 47839, 45914, 45916, 45920, 50093, 50091, 50089    
    # )
    ESTACIONES = { 
            'Aguas Negras -1' : 45924,
            'Aguas Negras -2' : 45926,
            'Aguas Negras -3' : 45928,
            'Caño Grande -1' : 45930,
            'Caño Grande -2' : 45932,
            'Caño Grande -3' : 45934,
            'Kilometro 22 -1' : 45907,
            'Kilometro 22 -2' : 45910,
            'Kilometro 22 -3' : 45912,
            'Luna -1' : 45922,
            'Luna -2' : 47837,
            'Luna -3' : 47839,
            'Rinconada -1' : 45914,
            'Rinconada -2' : 45916,
            'Rinconada -3' : 45920,
            'Sevillano -3' : 50093,
            'Sevillano -2' : 50091,
            'Sevillano -1' : 50089
    }
    # print(bdAREAS)
    for año in range(1995, 2022):
        NO_MONTADA = 0
        NO_MONITOREADA = 0
        SIN_VEGETACION = 0
        N_PARCELAS = 0
        print(año)
        for estacion in ESTACIONES:
            NO_MONTADA = 0
            NO_MONITOREADA = 0
            SIN_VEGETACION = 0
            N_PARCELAS = 0
            # print(estacion)
            for i, row in bdAREAS.iterrows():

                    
                # print(estacion,año, ESTACIONES[estacion])
                if row['ID_ESTACION'] == ESTACIONES[estacion] and row['AÑO'] == año:
                    #print (row['ID_ESTACION'], row['AÑO'])
                    if row['VALOR'] == 10:
                        NO_MONTADA = NO_MONTADA + 1
                    if row['VALOR'] == 20:
                        
                        SIN_VEGETACION = SIN_VEGETACION + 1
                    if row['VALOR'] == 30:
                        
                        NO_MONITOREADA = NO_MONITOREADA + 1
                    if row['VALOR'] == 40 or row['VALOR'] == 20:
                        N_PARCELAS = N_PARCELAS + 1
                        
                    if año == 2020:
                        print(año)
                        NO_MONITOREADA = NO_MONITOREADA + 1
                  
            DATA = {'ID_ESTACION':ESTACIONES[estacion],'ESTACION':estacion, 'AÑO':año,'AREA':N_PARCELAS*100,'N_PARCELAS':N_PARCELAS,'NO_MONTADA':NO_MONTADA,'NO_MONITOREADA':NO_MONITOREADA,'SIN_VEGETACION':SIN_VEGETACION}
            # print(DATA)
            areas_resumen = areas_resumen.append(DATA, ignore_index=True)
    # areas_resumen = areas_resumen.append(DATA, ignore_index=True)
     
    areas_resumen.to_excel('xlsxS/BD_2239_3-ToUpload(somedataa).xlsx',index=False)
    
def documentarNO_MUESTREADOS():#FUNCION PARA GENERAR REGISTROS SOBRE LOS TRANSECTOS NO MUESTREADOS EN SU TOTALIDAD, LA INFORMACION DE LOS MUESTREADOS TOTAL O PARCIALMENTE ASIGNA EN LA FUNCION generarAGD_MUESTREOS_PARAMETROS_AREAS()
    muestreos= pd.read_excel('xlsxS/data/BD_2239_3-ToUpload(muestreos).xlsx')
    muestreos['ID_MUESTREO'] = muestreos['ID_MUESTREO'].map(str)
    muestras= pd.read_excel('xlsxS/data/BD_2239_3-ToUpload(muestras).xlsx')
    muestras['ID_MUESTRA'] = muestras['ID_MUESTRA'].map(str)
    muestreos_parametros= pd.read_excel('xlsxS/data/BD_2239_3-ToUpload(muestreos_parametros).xlsx')
    # muestreos_parametros = pd.DataFrame(columns = ['ID_MUESTREO','ID_PARAMETRO','ID_METODOLOGIA','ID_UNIDAD_MEDIDA','VALOR'])
    EEESTACIONES = {
        'Sevillano' : 40996,
        'Caño Grande' : 42271,
        'Aguas Negras' : 42316,
        'Kilometro 22' : 42395,
        'Luna' : 43442,
        'Rinconada' : 44175,
        'Luna' : 49423
    }
    areas_resumen = pd.read_excel('xlsxS/BD_2239_3-ToUpload(somedataa).xlsx')        
    for i, row in areas_resumen.iterrows():#ITERAMOS LAS AREAS MONITOREADAS POR ESTACION-AÑO
      
        if row['NO_MONITOREADA'] == 5 or row['NO_MONTADA'] == 5:
            FECHA = (f'3012{row["AÑO"]}')
            ID_ESTACIONN = EEESTACIONES[row["ESTACION"][0:-3]]
            ID_MUESTREO = (f'{FECHA}{ID_ESTACIONN}')
            if not muestras['ID_MUESTRA'].str.contains((f'{ID_MUESTREO}{row["ID_ESTACION"]}'), regex=False).any() : 
                muestras = muestras.append({'ID_MUESTRA':(f'{ID_MUESTREO}{row["ID_ESTACION"]}'), 'ID_MUESTREO':ID_MUESTREO,'NOTAS':(f'El Transecto {row["ESTACION"]} (id: {row["ID_ESTACION"]}) no fue monitoreado en el año {row["AÑO"]}'),'ES_REPLICA':1}, ignore_index=True)
                print({'ID_MUESTRA':(f'{ID_MUESTREO}{row["ID_ESTACION"]}'), 'ID_MUESTREO':ID_MUESTREO,'NOTAS':(f'El Transecto {row["ESTACION"]} (id: {row["ID_ESTACION"]}) no fue monitoreado en el año {row["AÑO"]}'),'ES_REPLICA':1})
           
            if not muestreos['ID_MUESTREO'].str.contains(ID_MUESTREO, regex=False).any() :
                
                muestreos = muestreos.append({'ID_MUESTREO':ID_MUESTREO, 'ID_ESTACION':row['ID_ESTACION'],'ID_PROYECTO':2239,'ID_METODOLOGIA':3,'ID_TEMATICAS':224, 'FECHA':(f'30-12-{row["AÑO"]}'),'NOTAS':'Muestreo generado para documentar monitoreos no realizados','FECHASIS':NaN}, ignore_index=True)
                print({'ID_MUESTREO':ID_MUESTREO, 'ID_ESTACION':row['ID_ESTACION'],'ID_PROYECTO':2239,'ID_METODOLOGIA':3,'ID_TEMATICAS':224, 'FECHA':(f'30-12-{row["AÑO"]}'),'NOTAS':'Muestreo generado para documentar monitoreos no realizados','FECHASIS':NaN})
                muestreos_parametros = muestreos_parametros.append({'ID_MUESTREO':ID_MUESTREO, 'ID_PARAMETRO':1170,'ID_METODOLOGIA':3, 'ID_UNIDAD_MEDIDA':100,'VALOR':'Datos rescatados de BD EXCEL con informacion historica de estructura de maglar (transectos no monitoreados)'}, ignore_index=True)
                print({'ID_MUESTREO':ID_MUESTREO, 'ID_PARAMETRO':1170,'ID_METODOLOGIA':3, 'ID_UNIDAD_MEDIDA':100,'VALOR':'Datos rescatados de BD EXCEL con informacion historica de estructura de maglar (transectos no monitoreados)'})
              
    print(muestreos.info())
    print(muestreos)
    print(muestras.info())
    print(muestras)
    print(muestreos_parametros.info())
    print(muestreos_parametros)
    
    muestras.to_excel('xlsxS/data/BD_2239_3-ToUpload(muestras).xlsx',index=False)
    muestreos.to_excel('xlsxS/data/BD_2239_3-ToUpload(muestreos).xlsx',index=False)
    muestreos_parametros.to_excel('xlsxS/data/BD_2239_3-ToUpload(muestreos_parametros).xlsx',index=False)
    # muestrasppp = muestrasppp.drop_duplicates(subset=['ID_MUESTREO'])
    # for i, row in muestrasppp.iterrows():
    #     muestreos = muestreos.append({'ID_MUESTREO':ID_MUESTREO, 'ID_ESTACION':row['ID_ESTACION'],'ID_PROYECTO':2239,'ID_METODOLOGIA':3,'ID_TEMATICAS':224, 'FECHA':(f'30-12-{row["AÑO"]}'),'NOTAS':'Muestreo generado para documentar monitoreos no realizados','FECHASIS':NaN}, ignore_index=True)
    # GENERAR AUTORIAS (ID_FUNCIONARIO  ID_TAREA  ORDEN  FECHA  FECHASIS  ID_MUESTRA  ENTIDAD)

def generarAGD_AUTORIAS():
    bdEstructura = pd.read_excel('xlsxS/BD_2239_3-toUpload.xlsx')



#GENERAR SQLS
"""
def generate_sqls():
    muestreos = pd.read_excel('xlsxS/2239_3-toUpload/BD_2239_3-ToUpload(muestreos).xlsx')
    muestreos['ID_PROYECTO'] = muestreos['ID_PROYECTO'].map(str)
    muestreos['ID_METODOLOGIA'] = muestreos['ID_METODOLOGIA'].map(str)
    muestreos['ID_TEMATICAS'] = muestreos['ID_TEMATICAS'].map(str)
    print(muestreos.info())
    columns = list(muestreos)
    query = "INSERT INTO datosdecampo.AGD_MUESTREOS ("
    values = ""
    for i, row in muestreos.iterrows():
        for col in columns:
            query = query + col +","
           
        query=" INSERT INTO datosdecampo.AGD_MUESTREOS (ID_MUESTREO,ID_ESTACION,ID_PROYECTO,ID_METODOLOGIA,ID_TEMATICAS,FECHA,NOTAS,FECHASIS) VALUES ("+row['ID_MUESTREO']+","+row['ID_ESTACION']+","+row['ID_PROYECTO']+","+row['ID_METODOLOGIA']+","+row['ID_TEMATICAS']+","+row['FECHA']+","+row['NOTAS']+","+row['FECHASIS']+");"
        
        
        print(query,"\n")
"""   
#    ID_MUESTREO ID_ESTACION  ID_PROYECTO  ID_METODOLOGIA  ID_TEMATICAS       FECHA NOTAS    FECHASIS
    


# alistarData()
# generarAGD_MUESTRAS()
# generarAGD_MUESTREOS()
# generarAGD_MUESTRAS_VARIABLES()
# # generarAGD_MUESTREOS_PARAMETROS() #aca solo se registraba el parametro Area 
ordenarAreas_parcelas()
generarAGD_MUESTREOS_PARAMETROS_AREAS() #se asigna PLANTILLA, AREA, N_SUBPARCELAS
documentarNO_MUESTREADOS()