
//constants that capture html elements ----------------------------------------------------------------------------------------------------

const OUTPUT = document.getElementById('outputs')
const HOTELS = new Array;



//Main methods ----------------------------------------------------------------------------------------------------

function crearHotel() {
    
    OUTPUT.innerHTML = "<h3>Registrar un Nou Hotel</h3>".toUpperCase();
    basicFormHotel(treatInformation);
    

}

function veureHotel() {
    
        let p = positionHotelArray();

        if (p>-1) {
            let msg = "<h3>Consulta d'hotel</h3>".toUpperCase();
            msg += `<p>Nom: ${HOTELS[p].nom}<br>`+
                    `Habitacions: ${HOTELS[p].habitacions}<br>`+
                    `Plantes: ${HOTELS[p].plantes}<br>`+
                    `Superficie: ${HOTELS[p].superficie}m²</p>`;
        
            OUTPUT.innerHTML = msg;
        }
        
    
}

function costHotel(){
    let p = positionHotelArray();
    
    if (p>-1) {
        HOTELS[p].calcularManteniment();

        let msg = "<h3>Consulta d'hotel</h3>".toUpperCase();
        msg += `<h4>HOTEL: ${HOTELS[p].nom}</h4>`;
        msg += `<p>Habitacions: ${HOTELS[p].habitacions}<br>`+
                `Plantes: ${HOTELS[p].plantes}<br>`+
                `Superficie: ${HOTELS[p].superficie}m²</p>`;
        msg += `<p>Equipo de ${HOTELS[p].expense.staff} personas<br>`+
                `Costo Mensual: €${HOTELS[p].expense.costMonthly}</p>`;
        
        
        OUTPUT.innerHTML = msg;
    }
}

function modificarHotel(){

    let p = positionHotelArray();

    if (p>-1) {
        const QUEST = confirm(`Confirma que voleu modificar la informació de l’hotel ${HOTELS[p].nom}`);

        if (QUEST) {

            OUTPUT.innerHTML = "<h3>modificar la informació de l’hotel</h3>".toUpperCase()
            OUTPUT.innerHTML += `<p>Nom: ${HOTELS[p].nom}<br>`+
                                `Habitacions: ${HOTELS[p].habitacions}<br>`+
                                `Plantes: ${HOTELS[p].plantes}<br>`+
                                `Superficie: ${HOTELS[p].superficie}m²</p>`;
            
            
            basicFormHotel(replaceInformation);

            }
    }

    function replaceInformation() {
        const NAME = document.getElementById('name').value;
        const ROOMS = parseInt(document.getElementById('rooms').value);
        const FLOORS = parseInt(document.getElementById('floors').value);
        const AREA = parseFloat(document.getElementById('area').value).toFixed(2);
    
        if (NAME == "" || !isNaN(NAME) || isNaN(ROOMS) || isNaN(FLOORS) || isNaN(AREA)) {
            alert('Errada! falten dades o incorrectes')
        }
        else {
            const QUEST = confirm(
                "Confirma el canvi de dades?\n\n".toUpperCase()+
                `Nom: ${NAME}\n`+
                `Habitacions: ${ROOMS}\n`+
                `Plantes: ${FLOORS}\n`+
                `Superficie: ${AREA}\n\n`+
                "confirmar tota la informació?".toUpperCase()
            );
    
            if (QUEST) {
                let T = new Hotel(NAME, ROOMS, FLOORS, AREA);
                console.log(T);
                HOTELS[p] = T;
                
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
    

}

function donarDeBaixaHotel(){

    let p = positionHotelArray();
    
    if (p>-1) {
        const QUEST = confirm(`Confirma que voleu donar-vos de baixa de l'hotel ${HOTELS[p].nom}`);

        (QUEST) ? HOTELS.splice(p,1) : alert("No heu suprimit cap informació!")
    }
    

}


// TEST DATABASE ---------------------------------------------------------------------------------------------------

HOTELS.push(new Hotel("Acta Voraport", 30, 3, 600));
HOTELS.push(new Hotel("BCN 1882", 20, 2, 400));
HOTELS.push(new Hotel("REC", 90, 4, 1000));
HOTELS.push(new Hotel("One", 45, 5, 1000));