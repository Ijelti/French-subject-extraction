import json
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 import Features, CategoriesOptions
import codecs

contenu=[]
contenue=[]
resultat=[]


###################################### fonction pour recupurer le label sous forme liste #######################################
def topic_ibm(content):
    natural_language_understanding = NaturalLanguageUnderstandingV1(
            version='2018-11-16',
            iam_apikey="MpIV_8-gUahq8R3WzNh7C0g1JgDZGueVrUzq8441rQVb",
            url="https://gateway-lon.watsonplatform.net/natural-language-understanding/api"
            )
    response = natural_language_understanding.analyze(
            text=content,    
            features=Features(categories=CategoriesOptions(limit=3))).get_result()

    fichier=json.dumps(response, indent=2)
    print(fichier)
    data_dict_02 = json.loads(fichier)
    
    if len(data_dict_02["categories"])>2:
        category1=data_dict_02["categories"][0]["label"]
        category2=data_dict_02["categories"][1]["label"]
        resultat1=category1.split("/")
        resultat2=category2.split("/")
        print('resultat1 ',resultat1)
        print('resultat2 ',resultat2)
        resultat=[]
        resultat.append(resultat1[1])
        resultat.append(resultat2[1])
        print(resultat)
    return resultat
    
    
print(topic_ibm('''La discussion demande un effort de réflexion. Vous y montrez la pertinence de votre travail et son apport original dans le domaine scientifique concerné. Elle permet à la science d’avancer
 '''))
"""
########################################### lecture et application du api sur notre data ############################################
def open_csv(path):
    dic1={}
    mon_fichier = open(path, encoding="utf8")
    contenu = mon_fichier.read()
    contenue=contenu.split(".")
    for i in contenue[330001:432000]:
        i=i.replace('\n',' ')
        #print(i)
        if len(i.split(" "))>7:
            try:
               liste=topic_ibm(i)
               dic1[i]=liste 
            except Exception:
               continue
             
    return dic1


###################################### ecriture dans csv ############################################################
def writterCsv(my_dict,pathoutput):
    with codecs.open(str(pathoutput),"w+", encoding="utf8") as f:
        key1="phrase"
        value1="domaine1"
        value2="domaine2"
        f.write('{0};{1};{2}\n'.format(key1,value1,value2))
        for key,value in my_dict.items():
            if len(value)>0:
                f.write('{0};{1};{2}\n'.format(key,value[0],value[1]))
                #print(value[0])
                #print(value[1])    
            

################################################### affichage #######################################################"
path="C:/Users/Dell 7470/Desktop/stage pfe/1 idee/datafr.txt"
dic1=open_csv(path)
print(dic1)
writterCsv(dic1,"C:/Users/Dell 7470/Desktop/stage pfe/1 idee/donnee_multiclasse3.csv")

"""



