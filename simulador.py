import random 


class persona:
    infectados  = 0 
    sanos = 0
    muertos = 0
    recuperados = 0
    vacunados = 0
    def __init__(self,state):
        self.state = state 
        self.counter = 0
        if state == "S":
            persona.sanos += 1 
        if state == "I":
            persona.infectados += 1
    def pass_day(self):
        if self.counter == 5:
            number = random.randint(1,10)
            if number <= 8:
                self.to_recuperate()
            else:
                self.to_dead()
        self.counter += 1;
    def infect(self ):
        self.state = "I"
        persona.infectados +=1
        persona.sanos -= 1
    def to_dead(self):
        self.state = "M"
        persona.muertos += 1
        persona.infectados -= 1
    def to_recuperate(self):
        self.state = "R"
        persona.recuperados +=1 
        persona.infectados -= 1
    def vacunado(self):
        self.state = "V"
        persona.vacunados +=1
        persona.sanos -= 1
class simulation:
    def __init__(self,inicial_poblation,days, inicial_infects) :
        self.inicial_poblation = inicial_poblation
        self.days = days
        self.inicial_infests = inicial_infects
        self.list_pearsons = []

    def simulate_day(self):
        counter = 0
        vacunation_decition = random.random()
        number_vacunation = 0
        if vacunation_decition <= 0.2:
            number_vacunation = round(persona.sanos * 0.2)
        counter = persona.infectados * 2
        for i in self.list_pearsons:
            if i.state == "S" and number_vacunation > 0:
                i.vacunado()
                number_vacunation -= 1
            elif counter > 0 and i.state == "S":
                i.infect()
                counter -= 1
            elif i.state == "I":
                i.pass_day()
            
    def start_simulation(self):
        self.list_pearsons = [persona("I")if i< self.inicial_infests else persona("S") for i in range(self.inicial_poblation)]
        dia_pico = 0
        dia_infectados = 0
        for i in range(self.days):
            self.simulate_day()
            if persona.infectados > dia_infectados:
                dia_infectados =  persona.infectados 
                dia_pico = i
            self.print_results(i)
        print("================ results ================")
        print(f"dia_pico: {dia_pico}")
        print(f" numero maximo de infectados al mismo timepo {dia_infectados}")
        print(f"numero de personas sanas: {persona.sanos}")
        print(f"numero de personas infectados: {persona.infectados}")
        print(f"numero de personas recuperados: {persona.recuperados}")
        print(f"numero de personas muertos:  {persona.muertos}")
        print(f"numero de personas vacunados: {persona.vacunados}")
        print(f"muiertos: {persona.muertos}")
        print(f"porcentaje de surpervivencia: {100*(1-(persona.muertos/self.inicial_poblation))}")
        


                
    def print_results(self,day):
        print(f"dia: {day}")
        print(f"numero de personas sanas: {persona.sanos}")
        print(f"numero de personas infectados: {persona.infectados}")
        print(f"numero de personas recuperados: {persona.recuperados}")
        print(f"numero de personas muertos:  {persona.muertos}")
        print(f"numero de personas vacunados: {persona.vacunados}")
            
        
print("bievendio al simulador")
poblacion_inicial = int(input("introduce poblacion inicial: "))
infectados_iniciales = int(input("introduce  infectados inicales: "))
days = int(input("introduce la cantidad de dias: "))
simulacion1 = simulation(poblacion_inicial,days,infectados_iniciales)
simulacion1.start_simulation()
