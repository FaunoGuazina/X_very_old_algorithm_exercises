
//Auxiliary methods ----------------------------------------------------------------------------------------------------

function basicFormHotel(_function) {

    let name = document.createElement('input');
        name.type = "text";
        name.placeholder = "nou nom d'hotel";
        name.id = "name";

    let rooms = document.createElement('input');
        rooms.type = "text";
        rooms.placeholder = "nombre d’habitacions";
        rooms.id = "rooms";

    let floors = document.createElement('input');
        floors.type = "text";
        floors.placeholder = "nombre de plantes";
        floors.id = "floors";

    let area = document.createElement('input');
        area.type = "text";
        area.placeholder = "mida de l’àrea";
        area.id = "area";

    let register = document.createElement('input');
        register.type = "button";
        register.value = "registre";
        register.onclick = _function;

    OUTPUT.appendChild(name);
    OUTPUT.innerHTML += "<br>";
    OUTPUT.appendChild(rooms);
    OUTPUT.innerHTML += "<br>";
    OUTPUT.appendChild(floors);
    OUTPUT.innerHTML += "<br>";
    OUTPUT.appendChild(area);
    OUTPUT.innerHTML += "<br>";
    OUTPUT.appendChild(register);
}

function treatInformation() {
    const NAME = document.getElementById('name').value;
    const ROOMS = parseInt(document.getElementById('rooms').value);
    const FLOORS = parseInt(document.getElementById('floors').value);
    const AREA = parseFloat(document.getElementById('area').value).toFixed(2);

    if (NAME == "" || !isNaN(NAME) || isNaN(ROOMS) || isNaN(FLOORS) || isNaN(AREA)) {
        alert('Errada! falten dades o incorrectes!')
    }
    else if (alreadyExists(NAME)) {
        alert('Errada! aquest hotel ja està registrat!')
    }
    else {
        const QUEST = confirm(
            "confirmeu un nou hotel??:\n\n".toUpperCase()+
            `Nom: ${NAME}\n`+
            `Habitacions: ${ROOMS}\n`+
            `Plantes: ${FLOORS}\n`+
            `Superficie: ${AREA}\n\n`+
            "confirmeu tota la informació?".toUpperCase()
        );

        if (QUEST) {
            let T = new Hotel(NAME, ROOMS, FLOORS, AREA);
            
            HOTELS.push(T);
            
            OUTPUT.innerHTML = "";
        } 
        else {
            const QUEST = confirm("voleu canviar alguna informació?");
            if (!QUEST) {
                OUTPUT.innerHTML = "";
            }
        }
    }
}

function positionHotelArray() {

    let consulting = whichHotel();
    
    if (consulting=="NULL") {consultList();}
    
    else if (consulting!="NULL") {
    
         
        let find = false;

        let position = -1;

        let i = 0;
        while(i<HOTELS.length && !find) {
            if (consulting.toLocaleUpperCase() == HOTELS[i].nom.toUpperCase()) {
                find = true;
                position = i;
            }
            i++
        }

        (!find) ? consultList() : OUTPUT.innerHTML="";
        
        return position;
    }
}

function consultList() {
    const QUEST = confirm("Voleu veure una llista d'hotels registrats?");
    if (QUEST){
        let msg = "<h3>llista d'hotels</h3>".toUpperCase()
        for (let i=0; i<HOTELS.length; i++) {
            msg += HOTELS[i].nom + "<br>";
        }
        OUTPUT.innerHTML = msg;
    } else {OUTPUT.innerHTML = "";}
}

function whichHotel() {
    let whichHotel;
    
    do {
        whichHotel = prompt("quin hotel voleu consultar?");
        if (whichHotel==null) {whichHotel="NULL"}
    } while(!isNaN(whichHotel))

    return whichHotel;
}

function alreadyExists(nameHotel) {
    let answer = false;

    for (let i=0; i<HOTELS.length; i++) {
        if (nameHotel.toUpperCase() == HOTELS[i].nom.toUpperCase()) {
            answer = true;
        }
    }

    return answer;
}
