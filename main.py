from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def index():
    return 'Ariza riko'+' Moreno hermoso'


@app.route('/paises')
def prueba():
    
    ''' Lista en Python'''
    
    
    
    paises = [
        
        [
         {
             "nombre" : "América",
             "paises" : [
                 "Colombia",
                 "peru"
             ],
             "capital" : [
                "Bogotá",
                "Lima"
             ],
             "moneda" : [
                 "Peso",
                 "Sol"
             ],
             "población" : [
                 "51.049.000",
                 "33 630 948"
             ],
             
             "superficie" :[
                 "1,142,000 km²",
                 "1,285,220 km²"
             ]
             
         }
        ]
        ,
        [
         {
             "nombre" : "Europa",
             "paises" : [
                 "Francia",
                 "Irlanda",
                 "España"
             ],
             "capital" : [
                "París",
                "Dublín",
                "Madrid"
             ],
             "moneda" : [
                 "Euro de Francia",
                 "Euro de Irlanda",
                 "Euro de España"
             ],
             "población" : [
                 "67.221.943",
                 "4 581 269",
                 "47,615,034"
             ],
             
             "superficie" :[
                 "675,417 km²",
                 "70.273 km²",
                 "505.990 km²"
             ]
             
         }
        ]
        ,
        [
         {
             "nombre" : "Asia",
             "paises" : [
                 "China",
                 "Japón",
                 "Corea"
             ],
             "capital" : [
                "Pekín",
                "Tokio",
                "Seúl"
            
             ],
             "moneda" : [
                 "Renminbi",
                 "Yen",
                 "Won surcoreano"
             ],
             "población" : [
                 "1.395.380.000",
                 "126.529.100",
                 "51.301.193"
             ],
             
             "superficie" :[
                 "9,596,960 km²",
                 "377,975 km²",
                 "100,363 km²"
             ]
             
         }
        ]
        
        
        
    ]
    

    # PAISES

                    
    contador_paises_america = 0
    for paisesAmerica in paises[0][0]["paises"]:
        contador_paises_america = contador_paises_america + 1
    print (contador_paises_america)
        
    contador_paises_europa = 0
    for paisesEuropa in paises[1][0]["paises"]:
        contador_paises_europa = contador_paises_europa + 1
        
    contador_paises_asia = 0
    for paisesAsia in paises[2][0]["paises"]:
        contador_paises_asia = contador_paises_asia + 1
    
    # CAPITAL
    
    contador_capitales_america = 0 
    for capitalAmerica in paises[0][0]["capital"]:
        contador_capitales_america += 1
    print(contador_capitales_america)
    
    contador_capitales_europa = 0 
    for capitalEuropa in paises[1][0]["capital"]:
        contador_capitales_europa += 1
    print(contador_capitales_europa)
    
    contador_capitales_asia = 0 
    for capitalAsia in paises[2][0]["capital"]:
        contador_capitales_asia += 1
    print(contador_capitales_asia)
    
    
    # MONEDA
    
    contador_moneda_america = 0 
    for monedaAmerica in paises[0][0]["moneda"]:
        contador_moneda_america += 1
    print(contador_moneda_america)
    
    contador_moneda_europa = 0 
    for monedaEuropa in paises[1][0]["moneda"]:
        contador_moneda_europa += 1
    print(contador_moneda_europa)
    
    contador_moneda_asia = 0 
    for monedaAsia in paises[2][0]["moneda"]:
        contador_moneda_asia += 1
    print(contador_moneda_asia)
    
    
    # POBLACIÓN
    
    contador_poblacion_america = 0 
    for poblacionAmerica in paises[0][0]["población"]:
        contador_poblacion_america += 1
    print(contador_poblacion_america)
    
    contador_poblacion_europa = 0 
    for poblacionEuropa in paises[0][0]["población"]:
        contador_poblacion_europa += 1
    print(contador_poblacion_europa)
    
    contador_poblacion_asia = 0 
    for poblacionAsia in paises[0][0]["población"]:
        contador_poblacion_asia += 1
    print(contador_poblacion_asia)
    
    # SUPERFICIE
    
    contador_superificie_america = 0 
    for superficieAmerica in paises[0][0]["superficie"]:
        contador_superificie_america += 1
    print(contador_superificie_america)
    
    contador_superificie_europa = 0 
    for superficieEuropa in paises[0][0]["superficie"]:
        contador_superificie_europa += 1
    print(contador_superificie_europa)
    
    contador_superificie_asia = 0 
    for superficieAsia in paises[0][0]["superficie"]:
        contador_superificie_asia += 1
    print(contador_superificie_asia)
    user = 'Deivi Herrera'
    
    return render_template('paises_listas.html', 
                        user = user,
                        continentes = paises,
                        contador_paises_america = contador_paises_america,
                        contador_paises_europa = contador_paises_europa, 
                        contador_paises_asia = contador_paises_asia,
                        contador_moneda_america = contador_moneda_america,
                        contador_moneda_europa = contador_moneda_europa,
                        contador_moneda_asia = contador_moneda_asia,
                        contador_capitales_america = contador_capitales_america,
                        contador_capitales_europa = contador_capitales_europa,
                        contador_capitales_asia = contador_capitales_asia,
                        contador_poblacion_america = contador_poblacion_america,
                        contador_poblacion_europa = contador_poblacion_europa,
                        contador_poblacion_asia = contador_poblacion_asia,
                        contador_superificie_america = contador_superificie_america,
                        contador_superificie_europa = contador_superificie_europa,
                        contador_superificie_asia = contador_superificie_asia)