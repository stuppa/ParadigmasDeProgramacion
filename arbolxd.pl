%Arbol genealogico
%varon(X): X es un varon
varon(carlos).
varon(nahum).
varon(jesus).
varon(sergio).
varon(mario).
varon(rafael).
%mujer (X): X es una mujer
mujer(rosario).
mujer(coral).
mujer(susi).
mujer(obdulia).

%relacion de padre
%padre(X,Y): X es padre de Y
padre(sergio,carlos).
padre(carlos,rafael).
padre(carlos,jesus).
padre(carlos,jesus).

%realcion de madre
%madre(X,Y): X es madre de Y
madre(rosario,coral).
madre(coral,susi).
madre(coral,rafael).
madre(coral,jesus).
madre(coral,nahum).


%relacion de abuelo
%abuelo(X,Y): X es abuelo de Y
%
abuelo(X,Y):-padre(X,Z), (madre(Z,Y);padre(Z,Y))




