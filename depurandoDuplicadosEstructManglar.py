import pandas as pd
import numpy as np
import math as math

def prepararExcel():
    dataDuplicados = pd.read_excel('DUPLICADOS_EstructuraDc_AC1+JC-RAE - copia.xlsx', sheet_name='Exportar Hoja de Trabajo')
    dataDuplicados['Acciones tomadas'] = dataDuplicados['Acciones tomadas'].map(str) #volvemos la columna str
    
    updateTerms =  ['Se eliminó', 'Se corrigió', 'Se corrigio', 'Corrección', 'Se dejo Sin', 'Se dejó sin', 'Se modificó']

    dataDuplicados['Acciones tomadas'] = dataDuplicados['Acciones tomadas'].str.replace('Se eliminó', 'update')
    for i in updateTerms:
            # print(type(i))
            dataDuplicados['Acciones tomadas'] = dataDuplicados['Acciones tomadas'].str.replace(i, 'update')
          
    dataDuplicados.to_excel("dataDuplicadosEsctructuraManglar.xlsx", sheet_name='DATA',index=False)
    
# print (dataDuplicados)
def generarQuerys():
    dataDuplicados = pd.read_excel('dataDuplicadosEsctructuraManglar.xlsx', sheet_name='DATA')
    dataDuplicados['Acciones tomadas'] = dataDuplicados['Acciones tomadas'].map(str)
    # .astype('string') #volvemos la columna str
    word = 'update'
    updEstacion = 0
    updTAG = 0
    updID = 0
    updParcela = 0
    updEspecie = 0
    text = ''
    f= open("updatesTAG.sql","w+")
    
    for i, row in dataDuplicados.iterrows():
        #CORRECIONES IDENTIFICABLES: TAG, ID, estación, parcela, especie
        #ACCIONES IDENTIFICABLES para update: [se eliminó, se corrigió, Correción, se dejo sin, se dejó sin, se modificó]
        # if str.isin(row['Acciones tomadas']).any():
        # if not(np.isnan(row['Acciones tomadas'])):
        if word in row['Acciones tomadas']:
        # a = str(row['Acciones tomadas'])
        # a = np.format_float_positional(row['Acciones tomadas'])
            # print(i,"]",row['Acciones tomadas'])
            
            if 'estación' in row['Acciones tomadas'] or 'estacion' in row['Acciones tomadas']:
                # print("UPDATE datosdecampo.AGD_MUESTRAS_VARIABLES SET ID_ESTACION =","'",row['ID_ESTACION'],"'","WHERE ID_MUESTRA =",row['ID_MUESTRA'],";")
                updEstacion +=1
                
            if 'parcela' in row['Acciones tomadas'] :
                # print("UPDATE datosdecampo.AGD_MUESTRAS_VARIABLES SET ID_ESTACION =","'",row['ID_ESTACION'],"'","WHERE ID_MUESTRA =",row['ID_MUESTRA'],";")
                updParcela +=1
            
            if 'tag' in row['Acciones tomadas']  or 'TAG' in row['Acciones tomadas']:#UPDATE ON MUESTRAS_VARIABLES CUANDO EL PARAMETRO ES (282 = Tag)
                # print("UPDATE datosdecampo.AGD_MUESTRAS_VARIABLES SET VALOR =","'",row['TAG_ARBOL'],"'","WHERE ID_MUESTRA =",row['ID_MUESTRA'],"AND ID_PARAMETRO= 282",";")
                text = ("UPDATE datosdecampo.AGD_MUESTRAS_VARIABLES SET VALOR ="+"'"+str(row['TAG_ARBOL'])+"'"+"WHERE ID_MUESTRA ="+str(row['ID_MUESTRA'])+"AND ID_PARAMETRO= 282"+";")
                f.write(text+"\n")
                updTAG +=1
                
            if 'ID' in row['Acciones tomadas'] :#UPDATE ON MUESTRAS_VARIABLES CUANDO EL PARAMETRO ES (249 = ID)
                # print("UPDATE datosdecampo.AGD_MUESTRAS_VARIABLES SET VALOR =","'",row['ID_ARBOL'],"'","WHERE ID_MUESTRA =",row['ID_MUESTRA'],"AND ID_PARAMETRO= 249",";")
                # f.write("UPDATE datosdecampo.AGD_MUESTRAS_VARIABLES SET VALOR =","'",row['ID_ARBOL'],"'","WHERE ID_MUESTRA =",row['ID_MUESTRA'],"AND ID_PARAMETRO= 249",";")
                updID +=1
                
            if 'especie' in row['Acciones tomadas'] :#UPDATE ON MUESTRAS_VARIABLES CUANDO EL PARAMETRO ES (585 = Especie)
                # print("UPDATE datosdecampo.AGD_MUESTRAS_VARIABLES SET VALOR =","'",row['ID_ESPECIE'],"'","WHERE ID_MUESTRA =",row['ID_MUESTRA'],"AND ID_PARAMETRO= 585",";")
                # f.write("UPDATE datosdecampo.AGD_MUESTRAS_VARIABLES SET VALOR =","'",row['ID_ESPECIE'],"'","WHERE ID_MUESTRA =",row['ID_MUESTRA'],"AND ID_PARAMETRO= 585",";")
                updEspecie +=1
    f.close()            
    print("CANT UPDATES:\n")
    print("ESTACION: ",updEstacion)
    print("PARCELA: ",updParcela)
    print("TAG: ",updTAG)               
    print("ID: ",updID)
    print("ESPECIE: ",updEspecie)               
                
                
# prepararExcel()
generarQuerys()
# dataDuplicados = pd.read_excel('dataDuplicadosEsctructuraManglar.xlsx', sheet_name='DATA')
# dataDuplicados['Acciones tomadas'] = dataDuplicados['Acciones tomadas'].map(str) #volvemos la columna str
# for i, row in dataDuplicados.iterrows():
#     print(type(row['Acciones tomadas']))