# Expressive code

> Notez les 3 principales idées à retenir à propos du Mob Programming ?

1. Il faut communiquer sinon (le rédacteur par exemple) on peut louper des éléments.
2. Plus on est nombreux, plus cela prend de temps pour mettre en place.
3. On finit par enlever du code (donc on simplifie)

Pendant le Mob :

Changements effectués :
- Dans **bank.py**, les variables `currency1` et `currency2` qui n'étaient pas assez explicites ont été renommées respectivement en `from_currency` et `to_currency`.
- Refactor de la fonction `convert()`.
- Money Calculator -> Changement de tous les paramètres