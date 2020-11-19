class Persona {

    constructor (firstName, lastName, numberId) {

        this._info = {
            '_nom' : firstName,
            '_cognom' : lastName,
            '_dni' : numberId.toUpperCase(),

        };

        this._acounts = [];

        this._canvis = [];

    }

    get Nom() {
        return this._info._nom;
    }

    get Cognom() {
        return this._info._cognom;
    }

    get Id() {
        return this._info._dni;
    }

    get NomComplet() {
        return this._info._nom + " " + this._info._cognom;
    }

    get Acounts() {
        return this._acounts;
    }

    get Canvis() {
        return this._canvis;
    }

    set Acounts(AcountObject) {
        if(AcountObject.hasOwnProperty('_compte')) {
            this._acounts.push(AcountObject);
        }
        else {
            alert("Error al registrar la compte!")
        }
    }

    set Canvis(CanviObject) { 
        if(CanviObject.hasOwnProperty('_antic')) {
            this._canvis.push(CanviObject);
        }
        else {
            alert("Error al registrar la compte!")
        }
    }

    set Nom(name) {
        this._info._nom = name;
    }

    set Cognom(surname) {
        this._info._cognom = surname;
    }

    set Id(numberIdAlterated) {
        this._info._dni = numberIdAlterated;
    }

}


class Compte {

    constructor (numCompte) {

        let n = new Date;

        this._compte = {
            '_idCompte' : numCompte.toUpperCase(),
            '_type' : "Compte Corrent",
            '_saldo' : parseFloat(50),
            '_status' : false,
            '_dataAlta' : `${n.toDateString()} - ${n.getHours()}h${n.getMinutes()}m${n.getSeconds()}s`,
            '_transaccions' : []
        }

    }

    get Numero() {
        return this._compte._idCompte;
    }

    set Numero(Valor_Sencer_Sense_Caracters) {
        this._compte._idCompte = Valor_Sencer_Sense_Caracters;
    }

    get Tipus() {
        return this._compte._type;
    }

    set Tipus(Corrent_o_Estalvi) {
        this._compte._type = Corrent_o_Estalvi;
    }

    get Saldo() {
        return parseFloat(this._compte._saldo).toFixed(2);
    }

    get Status() {
        return this._compte._status;
    }

    set Status(StatusBoolean) {
        if (!this.Status && !this._compte.hasOwnProperty('_dataBaixa') && StatusBoolean){
            const QUEST = confirm(`Voleu activar el vostre compte ${this.Numero} ara?`);
            if (QUEST) {
                this._compte._status = true;
                alert(`El compte ${this.Numero} s'ha activat correctament!`);
            } else if (this.Status) {
                alert(`L’estat del compte ${this.Numero} està actiu!`);
            } else {
                alert(`Estat del compte ${this.Numero} encara inactiu!`);
            }
        } else if (this.Status && !StatusBoolean) {
            this._compte._status = false;
        }
        else {
            alert(`Compte ${this.Numero} tancat a la data ${this.DataBaixa}!`);
        }
    }

    get DataAlta() {
        return this._compte._dataAlta
    }

    set DataBaixa(StatusBoolean) {
        let n = new Date;
        if (this.Saldo == 0 && StatusBoolean) {
            const QUEST = confirm("Vol donar-se de baixa ara?");
            if (QUEST && this.Status) {
                this._compte._dataBaixa = `${n.toDateString()} - ${n.getHours()}h${n.getMinutes()}m${n.getSeconds()}s`;
                this.Status = false;
            }
        } else {
            alert(`No podeu tancar el compte, encara teniu un saldo de €${this.Saldo}`);
        }
        
    }

    get DataBaixa() {
        if (this._compte.hasOwnProperty('_dataBaixa') && !this.Status) {
            return this._compte._dataBaixa;
        } else if (this.Status) {
            alert(`Compte encara en estat actiu!`);
        } else {
            alert(`Compte sense data de baixa definida!`);
        }
    }

    get Transaccions() {
        return this._compte._transaccions;
    }

    set Transaccions(transaccio) {
        if(transaccio.hasOwnProperty('_transaccio')) {
            this._compte._transaccions.push(transaccio);
        }
        else {
            alert("Error al registrar la transacció!")
        }
    }

}

Compte.prototype.Diposit = function(valor) {
    let temp = this.Saldo;
    if (valor > 0) {
        const QUEST = confirm(`El vostre saldo actual és de €${temp} euros, confirmeu l’ingrés de €${valor}?`);
        if (QUEST) {
            this._compte._saldo = parseFloat(this._compte._saldo) + parseFloat(valor);
            this.Transaccions = new Transaccio("Dipòsit", valor);
            alert(`Dipòsit fet! El vostre saldo era €${temp} i l’actual és €${this.Saldo}`);
        }  else {
            alert(`Dipòsit no realitzat! el vostre saldo es manté a €${this.Saldo}`);
        }
    } else {alert("No es poden dipositar valors negatius!")}
}

Compte.prototype.Retirar = function(valor) {
    let temp = this.Saldo;
    if (this.Saldo >= valor) {
        const QUEST = confirm(`El vostre saldo actual és de €${temp} euros, confirmeu la retirada de €${valor}?`);
        if (QUEST) {
            this._compte._saldo = parseFloat(this._compte._saldo) - parseFloat(valor);
            this.Transaccions = new Transaccio("Retirada", valor);
            alert(`Retirada fet! El vostre saldo era €${temp} i l’actual és €${this.Saldo}`);
        } else {
            alert(`Retirada no realitzat! el vostre saldo es manté a €${this.Saldo}`);
        }
    } else {
        alert("Saldo de compte insuficient per dur a terme aquesta operació!");
    }
}

Compte.prototype.Informe = function() {
    let _informe = "";

    for (let i=0; i<this.Transaccions.length; i++) {

        _informe += `${this.Transaccions[i].Type} | `;
        _informe += `${this.Transaccions[i].Data} `;
        _informe += `${this.Transaccions[i].Hores} | `;
        _informe += `${this.Transaccions[i].Value}<br>`;
    }

    return _informe;
}

Compte.prototype.Detall = function() {
    
    
    let s="<strong>", S="</strong>";
    
    let _detall = `${s}Nº:${S} ${this.Numero} | ${s}Tipus:${S} ${this.Tipus}<br>`;

    _detall += `${s}Total de transaccions:${S} ${this.Transaccions.length}<br>`;
    
    _detall += `${s}Data Alta:${S} ${this.DataAlta}<br>`;
    
    _detall += `${s}Estat Actual:${S} `;
    (this.Status) ? _detall += 'ACTIU<br>' : _detall += 'INACTIU<br>';
    
    if (this._compte.hasOwnProperty('_dataBaixa') && !this.Status) {
        _detall += `${s}Data Baixa:${S} ${this.DataBaixa}<br>`;
    };

    return _detall;

}


class Transaccio {

    constructor(transaccio, valor){

        let n = new Date, xValor;

        if (transaccio == "Dipòsit") {
            xValor = `+ ${valor}`;
        } else if (transaccio == "Retirada") {
            xValor = `- ${valor}`;
        } else {
            xValor = `${valor}`;
        }

        this._transaccio = {
            '_date' : `${n.toDateString()}`,
            '_hour' : `${n.getHours()}h${n.getMinutes()}m${n.getSeconds()}s`,
            '_type' : transaccio,
            '_value' : xValor
        }

    }

    get Type() {
        return this._transaccio._type;
    }

    get Data() {
        return this._transaccio._date;
    }

    get Hores() {
        return this._transaccio._hour;
    }

    get Value() {
        return this._transaccio._value;
    }

}

class CanviCadastral {


    constructor(nomCompletAntic, numberIdAntic){

        let n = new Date;

        this._antic = {
            '_nomComplet' : nomCompletAntic,
            '_dni' : numberIdAntic,
            '_date' : `${n.toDateString()}`,
            '_hour' : `${n.getHours()}h${n.getMinutes()}m${n.getSeconds()}s`
        }

    }

    get NomComplet() {
        return this._antic._nomComplet;
    }

    get Id() {
        return this._antic._dni;
    }

    get Data() {
        return this._antic._date;
    }

    get Hores() {
        return this._antic._hour;
    }

}