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
             ]
         }   
        ]
        ,
        [
         {
            "nombre" : "Asia",
            "paises" : [
                "China",
                "japón",
                "Corea"
                ]
         }   
        ]

        
        
        # [
        # 'Colombia',
        # 'Peru',
        # 'Argentina'
        #  ],
        # [
        # 'España',
        # 'Inglaterra',
        # 'Rusia',
        # ],
        # [
        # 'Irlanda',
        # 'Japón',
        # 'China',
        # ]
        
        
    ]
    
    # longitudAmerica = [ len(paises[0][0]["paises"])
    #             ]
    
    # longitudEuropa = [ len(paises[1][0]["paises"])
    # ]
    
    # longitudAsia = [ len(paises[2][0]["paises"])
                    
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
    
    user = 'Deivi Herrera'
    
    return render_template('paises_listas.html', 
                        user = user,
                        continentes = paises,
                        contador_paises_america = contador_paises_america,
                        contador_paises_europa = contador_paises_europa, 
                        contador_paises_asia = contador_paises_asia)