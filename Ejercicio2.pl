padre(jorge, rodrigo).
padre(jorge, daniel).
madre(susana, rodrigo).
madre(susana, daniel).
padres(jorge,susana,rodrigo).
padres(jorge,susana,daniel).
hijos(rodrigo,daniel).

pareja(A,B) :- padre(A,C), madre(B,C).
hermanos(C,D) :- padre(A,C),padre(A,D), madre(B,C),madre(B,D).

hermanos(A,B) :- padres(C,D,A), padres(C,D,B).

