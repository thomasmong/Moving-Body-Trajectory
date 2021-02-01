Trajectoire d'un mobile - Interface graphique

Requirements : -tkinter
	       -matplotlib
	       -numpy

Le bouton 'Mettre à jour l'affichage' permet de redimensionner les axes et la grille lorsque la fenêtre a changé de taille.
Il est possible de faire translater le graphe en avec le clic gauche de la souris appuyé.
Le bouton 'Reset' supprime la trace de la trajectoire et repositionne le mobile en x=0.
Le bouton 'Exporter' crée deux fichiers :
- une image pdf matplotlib de la trajectoire avec les paramètres utilisés ;
- un fichier texte contenant la position du mobile.
Il est nécessaire d'avoir reset le graphe pour pouvoir à nouveau modifier les paramètres.
Le bouton 'Reset' ne supprime pas les listes de position --> vous pouvez exporter une trajectoire même si vous avez reset le graphe.


Il est assez simple de modifier les valeurs limites des curseurs dans le code, cependant la taille du graphe est adaptée pour que toutes les trajectoires possibles avec ces jeux de paramètres ne dépassent pas les axes du graphe (sauf avec la force du vent, x<0 possible).


Le code est très peu commenté, j'en suis désolé.