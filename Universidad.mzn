% Parametros
int: n; % Numero de Kilometros en la region
int: m; % Numero de ciudades en la region
array[1..m,1..2] of int: ciudades; % Posiciones de cada una de las m ciudades de la region

% Variables
%array[0..n,0..n] of var 0..m: mapa; % Arreglo que representa graficamente la region
array[1..2] of var 0..n: posUniversidad; % Cordenadas donde s deberia construir la Universidad
array[1..m] of var int: distances; % Arreglo de las distancias de las ciaudades a la Universidad
var int: largestDistance; % Distancia mas larga de la Universidad a una de las ciudades

% Restricciones
% Pinta un tablero a modo de mapa de acuerdo a las ciudades, esto ayuda a ver el problema graficamente
%constraint forall(i in 1..m)(
  %mapa[n-ciudades[i,2],ciudades[i,1]]=i);

% Establece la distancia de la universidad a cada una de las ciudades  
constraint forall(i in 1..m)(
  distances[i] = pow((posUniversidad[1]-ciudades[i,1]),2)+pow((posUniversidad[2]-ciudades[i,2]),2));

% Selecciona la distancia mas larga de la universidad a las ciudades
constraint largestDistance = max(distances);

% Funcion Objetivo
solve minimize largestDistance;