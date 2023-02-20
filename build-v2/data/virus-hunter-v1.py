#----------------------------------------------------------------
# DELETTRE Théo | 2023-02-20 | v.1.0 | Main file
#----------------------------------------------------------------

import vt
import os

path1 = ''
path2 = ''
path3 = ''

#----------------------------------------------------------------
# Lecture du fichier de configuration (virus-hunter.cfg)
#----------------------------------------------------------------
f=open('virus-hunter.cfg')
lines=f.readlines()
path1 = lines[0]
path2 = lines[1]
path3 = lines[2]

#----------------------------------------------------------------
# Parcours des répertoires à scanner
#----------------------------------------------------------------
print()
print("Contenu du dossier : "+path1),
path1 = path1.rstrip(path1[-1])
print(os.listdir(path1)) #Affiche le contenu du premier chemin de fichier
print()
print()

print("Contenu du dossier : "+path2),
path2 = path2.rstrip(path2[-1])
print(os.listdir(path2)) #Affiche le contenu du second chemin de fichier
print()
print()

print("Contenu du dossier : "+path3),
print(os.listdir(path3)) #Affiche le contenu du troisième chemin de fichier
print()
print()
print()

#----------------------------------------------------------------
# Scan de chaque fichier
#----------------------------------------------------------------
client = vt.Client("8eb8bd67a99eae271cd71a5f4dbeec6ba98c5e57cb2e0138009476eb7ffff27b") #Clé API client

#----------------------------------------------------------------
# Traitement réponse API
#----------------------------------------------------------------

#----------------------------------------------------------------
# Traitement des alarmes
#----------------------------------------------------------------

#----------------------------------------------------------------
# Fin de traitement, envoi d'un récapitulatif par une API SMS
#----------------------------------------------------------------
