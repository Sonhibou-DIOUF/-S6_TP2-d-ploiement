#####
# Dr Hugo Boisaubert
# hugo.boisaubert@univ-nantes.fr
#####

import genomic as g
import proteomic as p

print("Essayons quelques calculs avec une séquence d'ADN de 150 bases")
##
# Partie génétique
##

#On génére un fichier de séquence 
fragment = g.gen_brins(50*3)

# On conserve ce fragment dans un fichier
g.write_file(fragment)
 
#On ouvre le fichier de séquence
sequence=g.read_adn("brin.dat")

#On affiche la séquence
print("\nLa séquence est : ",sequence)

# On test la séquence
if g.is_valid(sequence):
    print('\nCette séquence est une séquence valide')
else:
    print('\nCette séquence est une séquence invalide')
    exit()

#On calcule quelques statistiques
stats=g.get_stat_base(sequence)
print('\nPour cette séquence la distribution des bases est la suivante :')
print(stats)

# On réalise la transcription

sequence_arn=g.transcription(sequence)

print("\nLa séquence : ",sequence)
print("\nA été transcrite en la séquence d'ARN suivante : ",sequence)

##
# Partie protéique
##

# On réalise la traduction de la séquence
sequence_aa=p.traduction(sequence_arn)
print("\nLa séquence  d'ARN : ",sequence_arn)
print("\nA été transcrite en la séquence protéique suivante : ",sequence_aa)


# On calcule quelques stats

stats_aa=p.get_nombre_aa(sequence_aa)
print('\nPour cette séquence composée de',stats_aa,'acides aminées, la distribution est la suivante :')
print(p.get_stat_aa(sequence_aa))

print('\nConséquament cette séquence à pour polarité:',p.get_polarite(sequence_aa))




