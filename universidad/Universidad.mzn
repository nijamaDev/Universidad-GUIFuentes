int: n;
int: m;
array[1..m,1..2] of int: ciudades;

%array[0..n,0..n] of var 0..m: mapa;
array[1..2] of var 0..n: posUniversidad;
array[1..m] of var int: distances;
var int: largestDistance;

%constraint forall(i in 1..m)(
  %mapa[n-ciudades[i,2],ciudades[i,1]]=i);
   
constraint forall(i in 1..m)(
  distances[i] = pow(abs(posUniversidad[1]-ciudades[i,1]),2)+pow(abs(posUniversidad[2]-ciudades[i,2]),2));
  
constraint largestDistance = max(distances);

solve minimize largestDistance;