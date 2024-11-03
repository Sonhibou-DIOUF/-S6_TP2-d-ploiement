#####
# Dr Hugo Boisaubert
# hugo.boisaubert@univ-nantes.fr
#####

import genomic as g
import proteomic as p

print("Essayons quelques calculs avec une très grande séquence d'ADN")

for i in range(50):

    ##
    # Partie génétique
    ##

    #On génére un fichier de séquence 
    sequence = g.gen_brins(50000*3)

    # On test la séquence
    if g.is_valid(sequence):
        pass
    else:
        print('\nCette séquence est une séquence invalide')
        exit()

    # On réalise la transcription

    sequence_arn=g.transcription(sequence)

    ##
    # Partie protéique
    ##

    # On réalise la traduction de la séquence
    sequence_aa=p.traduction(sequence_arn)

    # On calcule quelques stats
    
    stats_aa=p.get_nombre_aa(sequence_aa)
    if stats_aa>0:
        print('Sequence N°',i+1,' : Pour cette séquence composée de',stats_aa,'acides aminées, la distribution est la suivante :',p.get_stat_aa(sequence_aa))
        print('Conséquament cette séquence à pour polarité:',p.get_polarite(sequence_aa))




