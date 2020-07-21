

import sqlalchemy as sql
import pandas as pd

from sqlalchemy import create_engine
engine = create_engine('mysql+pymysql://luca:pelliccioli@localhost/ASSURAUTO')



# Pour ce projet on ne remplira que les tables clients.
data = pd.read_sql_query('select * from ASSURAUTO.CLIENT;', engine) 

idClientMax = pd.read_sql_query('SELECT MAX(CL_ID) FROM CLIENT;', engine) 
print(idClientMax)

clientmax = idClientMax.iloc[0, 0]
CL_ID = clientmax + 1
print(CL_ID)

# Vous devrais utiliser la méthode engine.execute() pour exécuter du
# script SQL et insérer des données
CL_NOM =input('veuillez entrer le nom : ').upper()
CL_PRENOM=input('veuillez entrer le prénom : ')
CL_ADRESSE=input("veuillez entrer l'adresse' : ")
CL_CODEPOSTAL=input('veuillez entrer le code postal : ')
while not CL_CODEPOSTAL.isdigit() :
    print('Attention, il ne faut que des chiffres')
    CL_CODEPOSTAL=input('veuillez entrer le code postal : ')    
CL_VILLE=input('veuillez entrer la ville : ')
CL_TELEPHONE=input('veuillez entrer le numéro de téléphone : ')
CL_FAX=input('veuillez entrer votre fax : ')
CL_MAIL=input('veuillez entrer votre mail : ')

engine.execute('INSERT INTO ASSURAUTO.CLIENT (CL_ID, CL_NOM, CL_PRENOM, CL_ADRESSE, CL_CODEPOSTAL, CL_VILLE, CL_TELEPHONE, CL_FAX, CL_MAIL) VALUES ("%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s");' %(CL_ID, CL_NOM, CL_PRENOM, CL_ADRESSE, CL_CODEPOSTAL, CL_VILLE, CL_TELEPHONE, CL_FAX, CL_MAIL))



# Pour ce projet on ne remplira que les tables contrat.
data = pd.read_sql_query('select * from ASSURAUTO.CONTRAT;', engine) 
print(data)

idMaxContrat = pd.read_sql_query('SELECT MAX(CO_ID) FROM CONTRAT;', engine) 
print(idMaxContrat)

contratMax = idMaxContrat.iloc[0, 0]
CO_ID = contratMax + 1
print(CO_ID)

# Vous devrais utiliser la méthode engine.execute() pour exécuter du
# script SQL et insérer des données
CO_NUMERO=input('veillez entrer le numéro contrat : ')
CO_DATE=input('AAAA-MM-JJ') 
CO_CATEGORIE=input('veuillez entrer le contrat categorie : ')
CO_BONUS=input('veuillez entrer le contrat bonus: ')
CO_MALUS=input('veuillez entrer le contrat malus: ')
CO_AG_ID_FK=1
CO_CL_ID_FK=CL_ID
CO_VT_ID_FK=1
CO_VU_ID_FK=1


engine.execute('INSERT INTO ASSURAUTO.CONTRAT (CO_ID, CO_NUMERO, CO_DATE, CO_CATEGORIE, CO_BONUS, CO_MALUS, CO_AG_ID_FK, CO_CL_ID_FK, CO_VT_ID_FK, CO_VU_ID_FK) VALUES ("%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s");' %(CO_ID, CO_NUMERO, CO_DATE, CO_CATEGORIE, CO_BONUS, CO_MALUS, CO_AG_ID_FK, CO_CL_ID_FK, CO_VT_ID_FK, CO_VU_ID_FK))





