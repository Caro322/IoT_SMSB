window.addEventListener('load', () => {
//El evento se dispara cuando la ventana ha terminado de cargar 
    
    //Se obtienen los parametros através de la consulta
    const name = sessionStorage.getItem('NAME');
    const surname = sessionStorage.getItem('SURNAME');
    
    //Se obtienen los parámetros através del almacenamiento local
    document.getElementById('result-name').innerHTML = name;
    document.getElementById('result-surname').innerHTML = surname;
    
})