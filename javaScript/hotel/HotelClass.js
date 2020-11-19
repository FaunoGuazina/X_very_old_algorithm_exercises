class Hotel {
    
    constructor(nom, habitacions, plantes, superficie) {
        this.data = {
            'nom' : nom || new String,
            'habitacions' : habitacions || new Number,
            'plantes' : plantes || new Number,
            'superficie' : superficie || new Number,
        };
    }

    get nom() {
        return this.data.nom;
    }

    get habitacions() {
        return this.data.habitacions;
    } 

    get plantes() {
        return this.data.plantes;
    }

    get superficie() {
        return this.data.superficie;
    }

    set nom(nom) {
        this.data['nom'] = nom;
    }

    set habitacions(habitacions) {
        this.data['habitacions'] = habitacions;
    } 

    set plantes(plantes) {
        this.data['plantes'] = plantes;
    }

    set superficie(superficie) {
        this.data['superficie'] = superficie;
    }

}

Hotel.prototype.calcularManteniment = function(){
    let rooms = this.habitacions;
    let staff = Math.ceil(rooms/20);
    let cost = staff*1500
    this.expense = {
        'staff' : staff,
        'costMonthly' : cost.toFixed(2)
    }
}

Hotel.prototype.setStatus = function(falseORtrue) {
    this.status = falseORtrue;
}

Hotel.prototype.getStatus = function(falseORtrue) {
    return this.status;
}
