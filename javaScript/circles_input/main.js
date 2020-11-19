const OUTPUT = document.querySelector('div#outputs');
const CANVAS = document.getElementById('circles');
const X1 = document.querySelector('input#x1');
const Y1 = document.querySelector('input#y1');
const R1 = document.querySelector('input#r1');
const X2 = document.querySelector('input#x2');
const Y2 = document.querySelector('input#y2');
const R2 = document.querySelector('input#r2');


let circle1, circle2;

if (CANVAS.height != CANVAS.width) {CANVAS.height = CANVAS.width};


function begin() {

  OUTPUT.innerHTML = "";
  
  const DRAW = CANVAS.getContext('2d');

  DRAW.clearRect(0, 0, CANVAS.width, CANVAS.height)

  circle1 = definitionCircle(1, parseFloat(R1.value), parseInt(X1.value), parseInt(Y1.value));

  if (circle1 instanceof Cercle) {
    circle2 = definitionCircle(2, parseFloat(R2.value), parseInt(X2.value), parseInt(Y2.value));
  }
  if (circle1 instanceof Cercle && circle2 instanceof Cercle) {

    DRAW.beginPath();
    DRAW.arc(circle1.C.X, circle1.C.Y, circle1.R, 0, 2*Math.PI, true);
    DRAW.fillStyle = '#ff0000ce';
    DRAW.fill();

    DRAW.beginPath();
    DRAW.arc(circle2.C.X, circle2.C.Y, circle2.R, 0, 2*Math.PI, true);
    DRAW.fillStyle = '#ffd900c9';
    DRAW.fill();

    analisisCercles();

  }

}

function analisisCercles() {

  let msg = "<h3>Anàlisi dels cercles</h3>".toUpperCase();
      
      msg += `<h5>Cicle Vermell: radi = ${circle1.R}, latitud = ${circle1.C.X}, longitud = ${circle1.C.Y}<br>` +
        `<h5>Cicle Groc: radi = ${circle2.R}, latitud = ${circle2.C.X}, longitud = ${circle2.C.Y}</h5>`;

      msg += "<p>" + circle1.compare(circle2) + "</p>";

  
  OUTPUT.innerHTML = msg;

}

function definitionCircle(OrderNumber, radius, positionX, positionY) {

  let maximusRadi = CANVAS.width/2, maximusXY = CANVAS.width-radius;

  if (radius < 1 || radius > maximusRadi || isNaN(radius)) {
    alert(`${OrderNumber}º CERCLE: introduïu el valor del radi (1 a ${maximusRadi})`);

  } else {
    
    if (positionX < radius || positionX > maximusXY || isNaN(positionX)) {
      alert(`${OrderNumber}º CERCLE: introduïu la posició X (${radius} a ${maximusXY})`);
    }
    else {
  
      if (positionY < radius || positionY > maximusXY || isNaN(positionY)) {
        alert(`${OrderNumber}º CERCLE: introduïu la posició Y (${radius} a ${maximusXY})`);
  
      } 
      else {
  
        let position =  new Punt(positionX, positionY);

        let circle = new Cercle(position, radius);

        return circle;
      }
    }
  }
}



class Punt {

  constructor (posicioX, posicioY) {

    this.coordenades = { 'posicioX' : posicioX, 'posicioY' :  posicioY}

  }

  get X() {
    return this.coordenades['posicioX'];
  }

  get Y() {
    return this.coordenades['posicioY'];
  }

  set X(posicioX) {
    return this.coordenades['posicioX'] = posicioX;
  }

  set Y(posicioY) {
    return this.coordenades['posicioY'] = posicioY;
  }


}

class Cercle {

  constructor (puntObject, radius) {

    this.atributes = { 'puntObject' : puntObject, 'radius' : radius}
  }

  get R() {
    return parseFloat(this.atributes['radius']);
  }

  get C() {
    return this.atributes.puntObject;
  }

}

Cercle.prototype.distanciaCentres = function(altreCercle) {

  let x = (this.C.X - altreCercle.C.X)*(this.C.X - altreCercle.C.X),
      y = (this.C.Y - altreCercle.C.Y)*(this.C.Y - altreCercle.C.Y),
  
      distancia = parseInt(Math.sqrt(x + y));

  if (distancia < 0) {distancia*-1}

  return distancia;

}

Cercle.prototype.equals = function(altreCercle) {

  let center, radius, both;

  (this.C.X == altreCercle.C.X && this.C.Y == altreCercle.C.Y) 
  ? center = true : center = false;

  (this.R == altreCercle.R) 
  ? radius = true : radius = false;

  (center && radius) 
  ? both = true : both = false;

  return both;

}

Cercle.prototype.concentrics = function(altreCercle) {

  let center;

  (this.C.X == altreCercle.C.X && this.C.Y == altreCercle.C.Y) 
  ? center = true : center = false;

  return center;

}

Cercle.prototype.equalRadi = function(altreCercle) {

  let radius;

  (this.R == altreCercle.R) 
  ? radius = true : radius = false;

  return radius;

}

Cercle.prototype.secants = function(altreCercle) {

  let verify, distancia = this.distanciaCentres(altreCercle);
  
  
  (distancia < (this.R + altreCercle.R) && distancia > (this.R - altreCercle.R)) 
  ? verify = true : verify = false;
  

  return verify;

}


Cercle.prototype.tangents = function(altreCercle) {

  let verify, distancia = this.distanciaCentres(altreCercle);

  (distancia == (this.R + altreCercle.R) || distancia == (this.R - altreCercle.R)) 
  ? verify = true : verify = false;
  

  return verify;

}

Cercle.prototype.noEsToquen = function(altreCercle) {

  let verify;

  let distancia = this.distanciaCentres(altreCercle);

  (distancia > (this.R + altreCercle.R))
  ? verify = true : verify = false;

  return verify;

}


Cercle.prototype.dins = function(altreCercle) {

  let verify, distancia = this.distanciaCentres(altreCercle);
  let petit = this.R, grand = altreCercle.R;
  if (grand < petit) {petit=altreCercle.R; grand = this.R}
  
  (distancia <= (grand-petit)) 
  ? verify = true : verify = false;

  return verify;

}


Cercle.prototype.compare = function(altreCercle) {

  let msg = `La distància entre el centre dels cercles és ${this.distanciaCentres(altreCercle)} pixels`;

  msg += "<br><br>";

  if (this.equals(altreCercle)) {
    msg += "els cercles són idèntics"; //, mateixos radi i centre
  }
  else {
    msg += "Els cercles no són idèntics"; //, diferents radis o centres
  }

  msg += "<br><br>";

  if (this.concentrics(altreCercle)) {
    msg += "Els cercles són concèntrics"; //, tenen el mateix centre
  } 
  else {
    msg += "Els cercles no són concèntrics"; //, tenen diferents centres
  }

  msg += "<br><br>";

  if (this.equalRadi(altreCercle)) {
    msg += "Els cercles tenen el mateix ràdi";
  } 
  else {
    msg += "Els cercles tenen diferents ràdis";
  }

  msg += "<br><br>";

  if (this.tangents(altreCercle)) {
    msg += "Els cercles són tangents";
  }
  else {
    msg += "Els cercles no són tangents";
  }

  msg += "<br><br>";

  if (this.secants(altreCercle)) {
    msg += "Els cercles són secants";
  }
  else {
    msg += "Els cercles no són secants";
  }

  msg += "<br><br>";

  if (this.noEsToquen(altreCercle)) {
    msg += "Els cercles no es toquen";
  }
  else {
    msg += "Els cercles es toquen";
  }

  msg += "<br><br>";

  if (this.dins(altreCercle)) {
    msg += "Un cercle es troba dins de l’altre";
  }

  return msg;

}
