
function selectAcount(client) {

    let positionAcount;

    switch (BD_USUARIS[client].Acounts.length) {
        case 0:
            positionAcount = -1;
            break;
    
        case 1:
            positionAcount = 0;
            break;
    
        default:
            positionAcount = witchPositionAcount(BD_USUARIS[client].Acounts);
            break;
    }

    if (positionAcount == -1){

        alert(`Sembla que el client ${BD_USUARIS[client].NomComplet} no té cap compte registrat!`);

    }

    return positionAcount;
}

function witchPositionAcount(clientAcounts) {

    let i, numbersAcounts = [];
    let msgConfirm = "el client té aquests comptes, quin voleu seleccionar?\n".toUpperCase();
    
    for (i=0; i<clientAcounts.length; i++) {
        msgConfirm += clientAcounts[i].Numero + "\n";
        numbersAcounts.push(clientAcounts[i].Numero);
    }
    
    numbersAcounts.push(null);

    let QUEST;

    do {
        QUEST = prompt(msgConfirm);
        if (QUEST!=null) {
            QUEST = treatAcount(QUEST);
        }
    } while(!numbersAcounts.includes(QUEST))

    if (QUEST == null) {i = -2}
    else {i = numbersAcounts.indexOf(QUEST)}

    return i;

}

function selectClient() {
    
    let QUEST, client, info;

    do {
        QUEST = prompt("Voleu seleccionar un client per:\n1 - Número de compte\n2 - Nom complet\n3 - Document d’identificació");
        (QUEST==null || QUEST=="") ? QUEST="0" : QUEST = QUEST.trim().charAt(0);
    } while (!QUEST.match(/[0-3]/));

    switch (QUEST) {
        case "1":
            do {
                info = prompt('Quin número de compte amb guionet i lletra de comprovació?');
                (info==null) ? info="" : info=treatAcount(info);
            } while(!isNaN(info));
            client = findClient(info,0,0);
            break;
        
        case "2":
            do {
                info = prompt('Quin nom complet del client?');
                (info==null) ? info="" : info=treatNames(info.trim());
            } while(!isNaN(info));
            client = findClient(0,info,0);
            break;

        case "3":
            do {
                info = prompt('Quin número d’identificació del client?');
                (info==null) ? info="" : info=treatId(info);
            } while(!isNaN(info));
            client = findClient(0,0,info);
            break;
        
        case "0":
            client = -3;
            break;
    }

    
    if (client == -1) {
        alert(`És impossible trobar un client amb aquestes dades:\n${info}!`)
    }
    else if (client == -2) {
        alert(`hi ha més d’un client amb aquest nom ${info}, seleccioneu una altra manera d’identificar el client!`)
    }
    else if (client == -3) {
        //l'usuari ha cancel·lat l'acció
    }

    return client
    
}

function findClient(acount, name, id) {

    let client = -1, i=0, verify=false;

    if (name==0 && id==0) {

        if (BD_NUMBERS.hasOwnProperty(acount)) {

            let idCliente = BD_NUMBERS[acount];

            client = findClient(0, 0, idCliente);
        }
    } 
    else if (acount==0 && id==0) {

        let count = 0;

        while (i<BD_USUARIS.length) {
            if (BD_USUARIS[i].NomComplet == name) {
                verify = true;
                client = i;
                count++;
            }
            i++
        }

        if (count>1) {
            client = -2;
        }

    } 
    else if (acount==0 && name==0) {

        while (i<BD_USUARIS.length && !verify) {
            if (BD_USUARIS[i].Id == id) {
                verify = true;
                client = i;
            } 
            else if (BD_USUARIS[i].Canvis.length > 0) {
                for (let j=0; j<BD_USUARIS[i].Canvis.length; j++){
                    if (BD_USUARIS[i].Canvis[j].Id == id) {
                        verify = true;
                        client = i;
                    }
                }
            }
            i++
        }

    }

    return client;

}

function listAcounts() {
    
    let listAcounts;

    const QUEST = confirm("Voleu veure una llista de només comptes actius?");
    
    if (QUEST) {

        listAcounts = "<h3>llista de comptes actius</h3>".toUpperCase();
        listAcounts += "<h5>Qant. Comptes _ Nom Complet _ Identificació</h5>" + "<p>";

        for(let i=0; i<BD_USUARIS.length; i++){
            if (BD_USUARIS[i].Acounts.length > 0) {

                listAcounts += BD_USUARIS[i].Acounts.length + " - ";
                listAcounts += BD_USUARIS[i].NomComplet + " - ";
                listAcounts += BD_USUARIS[i].Id + "<br>";

                listAcounts += "<i>Nº de Comptes" + "<br>";
                for (let j=0; j<BD_USUARIS[i].Acounts.length; j++) {
                    if (BD_USUARIS[i].Acounts[j].Status) {
                        listAcounts += BD_USUARIS[i].Acounts[j].Numero + "<br>";
                    }
                }
                listAcounts += "</i><br>";
            }
        }

        listAcounts += "</p>";

        OUTPUT.innerHTML = listAcounts;

    } 
    else {
        
        listAcounts = "<h3>llista de tots els comptes</h3>".toUpperCase();
        listAcounts += "<h5>Qant. Comptes _ Nom Complet _ Identificació</h5>" + "<p>";

        for(let i=0; i<BD_USUARIS.length; i++){
            if (BD_USUARIS[i].Acounts.length > 0) {
                listAcounts += BD_USUARIS[i].Acounts.length + " - "
                listAcounts += BD_USUARIS[i].NomComplet + " - "
                listAcounts += BD_USUARIS[i].Id + "<br>"
            
                listAcounts += "<i>Nº de Compte _ Status" + "<br>";
                for (let j=0; j<BD_USUARIS[i].Acounts.length; j++) {
                    listAcounts += BD_USUARIS[i].Acounts[j].Numero;
                    (BD_USUARIS[i].Acounts[j].Status) ? listAcounts += " - Actiu<br>" : listAcounts += " - Inactiu<br>";
                }
                listAcounts += "</i><br>";
            }
        }

        listAcounts += "</p>";

        OUTPUT.innerHTML = listAcounts;

    }
}

canviClient = function(){

    let client = selectClient();
    
    if (client>-1) {
        
        let nom = document.createElement('input');
            nom.type = "text";
            nom.id = "nom";
            nom.placeholder = BD_USUARIS[client].Nom;

        let cognom = document.createElement('input');
            cognom.type = "text";
            cognom.id = "cognom";
            cognom.placeholder = BD_USUARIS[client].Cognom;

        let idUsuari = document.createElement('input');
            idUsuari.type = "text";
            idUsuari.id = "idUsuari";
            idUsuari.placeholder = BD_USUARIS[client].Id;

        let btnRegister = document.createElement('input');
            btnRegister.type = "button";
            btnRegister.value = "Canviar";
            btnRegister.id = "btnRegister";
            btnRegister.onclick = btnChangeDatas;

        OUTPUT.innerHTML = "<h3>ompliu només els camps que vulgueu canviar</h3>".toUpperCase();
        OUTPUT.appendChild(nom);
        OUTPUT.innerHTML += "<br>";
        OUTPUT.appendChild(cognom);
        OUTPUT.innerHTML += "<br>";
        OUTPUT.appendChild(idUsuari);
        OUTPUT.innerHTML += "<br>";
        OUTPUT.appendChild(btnRegister);
    }
    else {OUTPUT.innerHTML = "";}


function btnChangeDatas() {

    let msgChange = "", verifyName = false, verifyId = false;

    let NOM = treatNames(document.getElementById('nom').value.trim());
    let COGNOM = treatNames(document.getElementById('cognom').value.trim());
    let IDUSUARI = treatId(document.getElementById('idUsuari').value.trim());

    (NOM=="") ? NOM = BD_USUARIS[client].Nom : verifyName=true;
    (COGNOM=="") ? COGNOM = BD_USUARIS[client].Cognom : verifyName=true;
    (IDUSUARI=="") ? IDUSUARI = BD_USUARIS[client].Id : verifyId=true;

    if (!isNaN(NOM) || !isNaN(COGNOM) || !isNaN(IDUSUARI)) {
        alert('Errada! Dades incorrectes!')
    } 
    else if (!verifyId && !verifyName) {
        alert(`No s’ha canviat cap dada de ${BD_USUARIS[client].NomComplet}!`);
        OUTPUT.innerHTML = "";
    }
    else {

        if (verifyName) {
            msgChange += `NOM ABANS: ${BD_USUARIS[client].NomComplet}\nNOM CANVIAT: ${NOM + " " + COGNOM}`;
            if (verifyId) {msgChange += "\n\n"};
        }
        if (verifyId) {
            msgChange += `ID ABANS: ${BD_USUARIS[client].Id}\nID CANVIAT: ${IDUSUARI}`;
        }
        
        const QUEST = confirm("confirmeu els canvis?\n\n".toUpperCase() + `${msgChange}`)

        if (QUEST) {
            BD_USUARIS[client].Canvis = new CanviCadastral((BD_USUARIS[client].NomComplet), BD_USUARIS[client].Id)
            BD_USUARIS[client].Nom = NOM;
            BD_USUARIS[client].Cognom = COGNOM;
            BD_USUARIS[client].Id = IDUSUARI;
            alert("El client s'ha canviat correctament");
            
            OUTPUT.innerHTML = "";
        }
        else {
            const QUEST = confirm("Voleu canviar alguna informació d’aquest canvi de registre?");
            if (!QUEST) {
                OUTPUT.innerHTML = "";
            }
        }
    }
    

}
   
}

function btnRegisterDatas() {
    const NOM = treatNames(document.getElementById('nom').value.trim());
    const COGNOM = treatNames(document.getElementById('cognom').value.trim());
    const IDUSUARI = treatId(document.getElementById('idUsuari').value.trim());
    const CLIENT = findClient(0,0,IDUSUARI);

    if ((NOM == "" || !isNaN(NOM) || COGNOM == "" || !isNaN(COGNOM)) || IDUSUARI == "" || !isNaN(IDUSUARI)) {
        alert('Errada! falten dades o incorrectes!')
    } 
    else if (CLIENT > -1) {
        alert(`ERROR! ${BD_USUARIS[CLIENT].NomComplet} ja està registrat!`)
    }
    else {
        
        const QUEST = confirm(
            "confirmeu tota la informació?\n\n".toUpperCase() +
            `Nom Complet: ${NOM} ${COGNOM}\n` +
            `Document d’Identificació: ${IDUSUARI}\n`
        )

        if (QUEST) {
            let newUser = new Persona(NOM, COGNOM, IDUSUARI);
            BD_USUARIS.push(newUser);
            alert("El client s'ha registrat correctament");
            
            
            OUTPUT.innerHTML = "";
        }
        else {
            const QUEST = confirm("voleu canviar alguna informació d’aquest nou registre?");
            if (!QUEST) {
                OUTPUT.innerHTML = "";
            }
        }
    }
    

}

function generateNumCompte(positionClient) {

    let digit = "-";

    ((BD_USUARIS[positionClient].Cognom)[1].match(/[a-zA-Z]/))
    ? digit += (BD_USUARIS[positionClient].Cognom)[1].toUpperCase()
    : digit += "X";
    
    let numCompte = Math.ceil(Math.random()*10000)+digit;
    
    let verify = true;
    
    while (verify) {

        if (numCompte.length<6) {
            numCompte = "0".repeat(6-numCompte.length) + numCompte;
        }

        (BD_NUMBERS.hasOwnProperty(numCompte)) 
        ? numCompte = Math.ceil(Math.random()*10000)+digit 
        : verify = false;

    }

    return numCompte;

}

function treatNames(Name_String) {
    let nameArray = (Name_String.replace(/[^a-zA-Z\u00C0-\u00FF\u0027\u00B7\u0020]/g, "")).split(" "), nameTreated = "";

    for (let i=0; i<nameArray.length; i++) {
        if (!nameArray[i].includes("\'")) {
            nameTreated += nameArray[i].charAt(0).toUpperCase() + nameArray[i].slice(1).toLowerCase();
        }
        else {
            let temp = nameArray[i].split("\'");
            nameTreated += temp[0].charAt(0).toUpperCase() + temp[0].slice(1).toLowerCase() + "\'";
            nameTreated += temp[1].charAt(0).toUpperCase() + temp[1].slice(1).toLowerCase();            
        }
        if (i<(nameArray.length-1)) {nameTreated += " "}
    }

    return nameTreated;
}

function treatId(Id_String) {
    let idTreated = (Id_String.toUpperCase()).replace(/\W|\s/g, "");

    return idTreated;
}

function treatAcount(Acount_String) {
    let acountTreated = (Acount_String.toUpperCase()).replace(/[^0-9A-Z\u002D]/g, "");

    if (acountTreated.length<6) {
        acountTreated = "0".repeat(6-acountTreated.length) + acountTreated;
    }

    return acountTreated;
}