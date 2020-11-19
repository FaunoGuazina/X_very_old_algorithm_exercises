
const OUTPUT = document.querySelector('div#outputs')
const BD_USUARIS = [], BD_NUMBERS = [];

informacio = function(){

    const QUEST = confirm("Voleu veure la llista de clients?");

    if (QUEST) {

        listAcounts();

    } 
    else {
        
        let client = selectClient();

        if (client>-1) {

            let positionAcount = selectAcount(client)
    
            if (positionAcount >= 0) {
    
                if (!BD_USUARIS[client].Acounts[positionAcount].Status) {BD_USUARIS[client].Acounts[positionAcount].Status = true;}

                info = "<h3>informació del titular del compte</h3>".toUpperCase();
                info += `<h4>TITULAR: ${BD_USUARIS[client].NomComplet}<br>ID: ${BD_USUARIS[client].Id}</h4>`;
                info += `<p>${BD_USUARIS[client].Acounts[positionAcount].Detall()}</p>`;

                OUTPUT.innerHTML = info;
                
            }
            else {OUTPUT.innerHTML = "";}
    
        } 
        else {OUTPUT.innerHTML = "";}

    }
}

extracte = function(){
    
    let client = selectClient();

    if (client>-1) {

        let positionAcount = selectAcount(client)

        if (positionAcount >= 0) {

            if (!BD_USUARIS[client].Acounts[positionAcount].Status) {BD_USUARIS[client].Acounts[positionAcount].Status = true;}
            
            if (BD_USUARIS[client].Acounts[positionAcount].Transaccions.length > 0) {

                info = "<h3>informació del compte</h3>".toUpperCase();
                info += `<h5>${BD_USUARIS[client].Acounts[positionAcount].Informe()}</h5>`;

                OUTPUT.innerHTML = info;

            } else {

                alert(`no s'ha trobat cap transacció al compte ${BD_USUARIS[client].Acounts[positionAcount].Numero}`);

                OUTPUT.innerHTML = "";
            }
            
        }
        else {OUTPUT.innerHTML = "";}

    }
    else {OUTPUT.innerHTML = "";}

}

ingressar = function(){
    
    let client = selectClient();

    if (client>-1) {

        let positionAcount = selectAcount(client)

        if (positionAcount >= 0) {

            if (!BD_USUARIS[client].Acounts[positionAcount].Status) {BD_USUARIS[client].Acounts[positionAcount].Status = true;}
            
            let QUEST;

            do {
                QUEST = prompt(`${BD_USUARIS[client].NomComplet}, Quina quantitat voleu dipositar?`);
                (QUEST==null) ? QUEST="" : QUEST.trim();
            } while (!QUEST.match(/^[+]?\d+(\.\d+)?$/));

            QUEST = parseFloat(QUEST).toFixed(2);

            BD_USUARIS[client].Acounts[positionAcount].Diposit(QUEST);

            OUTPUT.innerHTML = "";            
        }
        else {OUTPUT.innerHTML = "";}

    }
    else {OUTPUT.innerHTML = "";}
    
}

saldo = function(){
        
    let client = selectClient();

    if (client>-1) {

        let positionAcount = selectAcount(client)

        if (positionAcount >= 0) {

            if (!BD_USUARIS[client].Acounts[positionAcount].Status) {BD_USUARIS[client].Acounts[positionAcount].Status = true;}
         
            info = "<h3>Saldo total</h3>".toUpperCase();
            info += `<h5>TITULAR: ${BD_USUARIS[client].NomComplet}</h4>`;
            info += `<h5>CONPTE: ${BD_USUARIS[client].Acounts[positionAcount].Numero}</h4>`;
            info += `<h4>€ ${BD_USUARIS[client].Acounts[positionAcount].Saldo}</h4>`;

            OUTPUT.innerHTML = info;

            BD_USUARIS[client].Acounts[positionAcount].Transaccions = new Transaccio("Saldo", BD_USUARIS[client].Saldo);
        }
        else {OUTPUT.innerHTML = "";}

    } 
    else {OUTPUT.innerHTML = "";}

}

retirar = function(){
        
    let client = selectClient();

    if (client>-1) {

        let positionAcount = selectAcount(client)

        if (positionAcount >= 0) {

            if (!BD_USUARIS[client].Acounts[positionAcount].Status) {BD_USUARIS[client].Acounts[positionAcount].Status = true;}
            
            let QUEST;

            do {
                QUEST = prompt(`${BD_USUARIS[client].NomComplet}, Quant voleu retirar-vos`);
                (QUEST==null) ? QUEST="" : QUEST.trim();
            } while (!QUEST.match(/^[-+]?\d+(\.\d+)?$/));

            QUEST = parseFloat(QUEST).toFixed(2);

            BD_USUARIS[client].Acounts[positionAcount].Retirar(QUEST);

            OUTPUT.innerHTML = "";

        }
        else {OUTPUT.innerHTML = "";}

    } 
    else {OUTPUT.innerHTML = "";}
    
}

nouCompte = function(){
    
    let client = selectClient(), msgAcount="";

    if (client>-1) {

        let numberAcount = generateNumCompte(client);

        const QUEST = confirm(`S'ha generat el número de compte ${numberAcount}, confirmeu la incorporació al client ${BD_USUARIS[client].NomComplet}?`);

        if (QUEST) {

            BD_USUARIS[client].Acounts = new Compte(numberAcount);

            BD_NUMBERS[numberAcount] = BD_USUARIS[client].Id;

            msgAcount += `<h4>S'ha creat i afegit el compte ${numberAcount} amb èxit al client ${BD_USUARIS[client].NomComplet}.</h4>`;

            msgAcount += "<p>Compte creat en estat inactiu i que es pot activar amb una primera transacció!</p>";

        }
        else {
            msgAcount += "<h4>Es va descartar el número de compte i no es va canviar res del client!</h4>";
        }

        OUTPUT.innerHTML = msgAcount;
    }
    else {OUTPUT.innerHTML = "";}

}

tancarCompte = function(){
        
    let client = selectClient();

    if (client>-1) {

        let positionAcount = selectAcount(client)

        if (positionAcount >= 0) {
        
            BD_USUARIS[client].Acounts[positionAcount].DataBaixa = true;

            BD_USUARIS[client].Acounts[positionAcount].Transaccions = new Transaccio("Baixa", BD_USUARIS[client].Saldo);

        }

        else {OUTPUT.innerHTML = "";}

    } 
    else {OUTPUT.innerHTML = "";}
    
}

altaClient = function(){

    OUTPUT.innerHTML = "<h3>emplena les dades per registrar-se</h3>".toUpperCase();
    
    let nom = document.createElement('input');
        nom.type = "text";
        nom.id = "nom";
        nom.placeholder = "primer nom";

    let cognom = document.createElement('input');
        cognom.type = "text";
        cognom.id = "cognom";
        cognom.placeholder = "segon nom i cognoms";

    let idUsuari = document.createElement('input');
        idUsuari.type = "text";
        idUsuari.id = "idUsuari";
        idUsuari.placeholder = "nº d’identificació";

    let btnRegister = document.createElement('input');
        btnRegister.type = "button";
        btnRegister.value = "Registre";
        btnRegister.id = "btnRegister";
        btnRegister.onclick = btnRegisterDatas;


    OUTPUT.appendChild(nom);
    OUTPUT.innerHTML += "<br>";
    OUTPUT.appendChild(cognom);
    OUTPUT.innerHTML += "<br>";
    OUTPUT.appendChild(idUsuari);
    OUTPUT.innerHTML += "<br>";
    OUTPUT.appendChild(btnRegister);
   
}

infoClients = function(){

    let quantitatComptes, listClients = "";
    
    do {
        quantitatComptes = prompt("voleu seleccionar un nombre mínim de comptes per client?");
        if (quantitatComptes!=null){
            (quantitatComptes!="") ? quantitatComptes.replace(/([^\d])+/gim, '') : quantitatComptes="0";
        } else {quantitatComptes="99999"}
    } while (quantitatComptes.match(/[^\d]/));

    if (quantitatComptes!=99999) {
            const QUEST = confirm(`Voleu veure clients amb més de ${quantitatComptes} comptes?`);
        

        if (QUEST) {

            for (let i=0; i<BD_USUARIS.length; i++) {
                if (BD_USUARIS[i].Acounts.length >= quantitatComptes) {
                    listClients += BD_USUARIS[i].NomComplet + " - ";
                    listClients += BD_USUARIS[i].Id + " - ";
                    listClients += BD_USUARIS[i].Acounts.length + "<br>";
                }
            }

        }
        else {

            for (let i=0; i<BD_USUARIS.length; i++) {
                if (BD_USUARIS[i].Acounts.length == quantitatComptes) {
                    listClients += BD_USUARIS[i].NomComplet + " - ";
                    listClients += BD_USUARIS[i].Id + " - ";
                    listClients += BD_USUARIS[i].Acounts.length + "<br>";
                }
            }
        }

        OUTPUT.innerHTML = "<h3>fitxa de clients</h3>".toUpperCase() +
                        "<h5>Nom Complet _ Identificació _ Nº Comptes</h5>" + "<p>";
        (listClients != "") ? OUTPUT.innerHTML += listClients : OUTPUT.innerHTML += "cap client compleix els requisits";
    } 
    else {OUTPUT.innerHTML = "";}
}

baixaClient = function(){
           
    let client = selectClient();

    if (client>-1) {

        if (BD_USUARIS[client].Acounts.length == 1) {

            BD_USUARIS[client].Acounts[0]._compte._status = false;

            BD_USUARIS[client].Acounts[0].Transaccions = new Transaccio("Inactivar", BD_USUARIS[client].Acounts[0].Saldo);

        }
        else if (BD_USUARIS[client].Acounts.length > 1) {
            for (let i=0; i<BD_USUARIS[client].Acounts.length; i++) {
                if (BD_USUARIS[client].Acounts[i].Status) {
                    BD_USUARIS[client].Acounts[i]._compte._status = false;
                    BD_USUARIS[client].Acounts[i].Transaccions = new Transaccio("Inactivar", BD_USUARIS[client].Acounts[i].Saldo);
                }
            }
        }
        else {OUTPUT.innerHTML = "";}    

    }
    else {OUTPUT.innerHTML = "";}

}

// DATABASE TESTS ---------------------------------------- positionin array

BD_USUARIS.push(new Persona("Fauno", "Guazina", "123F"));        // 0
BD_USUARIS.push(new Persona("Fauno", "Güazina", "123G"));       // 1
BD_USUARIS.push(new Persona("Diana", "Vile", "123D"));         // 2
BD_USUARIS.push(new Persona("Robert", "Garcia", "123R"));     // 3
BD_USUARIS.push(new Persona("Conxi", "Cozar", "123C"));      // 4
BD_USUARIS.push(new Persona("Clara", "Murcia", "123M"));    // 5

BD_USUARIS[0].Acounts = new Compte(generateNumCompte(0));                   // 0
// BD_USUARIS[0].Acounts[0]._compte._status = true;
BD_NUMBERS[BD_USUARIS[0].Acounts[0].Numero] = BD_USUARIS[0].Id;

BD_USUARIS[0].Acounts = new Compte(generateNumCompte(0));                   // 1
BD_USUARIS[0].Acounts[1]._compte._status = true;
BD_NUMBERS[BD_USUARIS[0].Acounts[1].Numero] = BD_USUARIS[0].Id;

BD_USUARIS[1].Acounts = new Compte(generateNumCompte(1));                   // 0
BD_USUARIS[1].Acounts[0]._compte._status = true;
BD_NUMBERS[BD_USUARIS[1].Acounts[0].Numero] = BD_USUARIS[1].Id;

BD_USUARIS[2].Acounts = new Compte(generateNumCompte(2));                   // 0
// BD_USUARIS[2].Acounts[0]._compte._status = true;
BD_NUMBERS[BD_USUARIS[2].Acounts[0].Numero] = BD_USUARIS[2].Id;

BD_USUARIS[2].Acounts = new Compte(generateNumCompte(2));                   // 1
BD_USUARIS[2].Acounts[1]._compte._status = true;
BD_NUMBERS[BD_USUARIS[2].Acounts[1].Numero] = BD_USUARIS[2].Id;

BD_USUARIS[3].Acounts = new Compte(generateNumCompte(3));                   // 0
// BD_USUARIS[3].Acounts[0]._compte._status = true;
BD_NUMBERS[BD_USUARIS[3].Acounts[0].Numero] = BD_USUARIS[3].Id;

BD_USUARIS[3].Acounts = new Compte(generateNumCompte(3));                   // 1
BD_USUARIS[3].Acounts[1]._compte._status = true;
BD_NUMBERS[BD_USUARIS[3].Acounts[1].Numero] = BD_USUARIS[3].Id;

BD_USUARIS[3].Acounts = new Compte(generateNumCompte(3));                   // 2
BD_USUARIS[3].Acounts[2]._compte._status = true;
BD_NUMBERS[BD_USUARIS[3].Acounts[2].Numero] = BD_USUARIS[3].Id;

BD_USUARIS[4].Acounts = new Compte(generateNumCompte(4));                   // 0
// BD_USUARIS[4].Acounts[0]._compte._status = true;
BD_NUMBERS[BD_USUARIS[4].Acounts[0].Numero] = BD_USUARIS[4].Id;

BD_USUARIS[4].Acounts = new Compte(generateNumCompte(4));                   // 1
BD_USUARIS[4].Acounts[1]._compte._status = true;
BD_NUMBERS[BD_USUARIS[4].Acounts[1].Numero] = BD_USUARIS[4].Id;

BD_USUARIS[4].Acounts = new Compte(generateNumCompte(4));                   // 2
BD_USUARIS[4].Acounts[2]._compte._status = true;
BD_NUMBERS[BD_USUARIS[4].Acounts[2].Numero] = BD_USUARIS[4].Id;

BD_USUARIS[4].Acounts = new Compte(generateNumCompte(4));                   // 3
BD_USUARIS[4].Acounts[3]._compte._status = true;
BD_NUMBERS[BD_USUARIS[4].Acounts[3].Numero] = BD_USUARIS[4].Id;