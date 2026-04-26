from machine import Pin
import time

# Adicionado apenas para o GitHub Actions validar o código
print("Teste") 

# Semáforo dos Carros
car_red = Pin(15, Pin.OUT)
car_yellow = Pin(2, Pin.OUT)
car_green = Pin(4, Pin.OUT)

# Semáforo dos Pedestres
ped_red = Pin(17, Pin.OUT)
ped_green = Pin(16, Pin.OUT)

# Configuração do Botão 
btn_pedestrian = Pin(12, Pin.IN, Pin.PULL_UP)

# Variável global para registrar se o botão foi apertado
pedestrian_request = False

# Função para quando o botão é pressionado
def handle_button(pin):
    global pedestrian_request
    pedestrian_request = True

# Detecta o estado do botão
btn_pedestrian.irq(trigger=Pin.IRQ_FALLING, handler=handle_button)

# Função para alterar todos os LEDs de uma vez
def set_lights(cr, cy, cg, pr, pg):
    car_red.value(cr)
    car_yellow.value(cy)
    car_green.value(cg)
    ped_red.value(pr)
    ped_green.value(pg)



# Estado inicial padrão com carros passando e pedestres parados.
set_lights(0, 0, 1, 1, 0)
print("Sistema Iniciado. Fluxo de carros normal. Aguardando pedestre.")

while True:
    # Verifica se teve o pedido do pedestre
    if pedestrian_request:
        print("Botão pressionado! Iniciando ciclo de travessia.")
        time.sleep(1) # Atraso para segurança
        
        # Etapa 1 (Amarelo carros)
        print("Sinal Amarelo para os carros.")
        set_lights(0, 1, 0, 1, 0)
        time.sleep(2)
        
        # Etapa 2 (Vermelho carros/Verde pedestres)
        print("Sinal Vermelho para carros. Travessia liberada!")
        set_lights(1, 0, 0, 0, 1)
        time.sleep(5) # Tempo para os pedestre
        
        # Etapa 3 (Verde carros/Vermelho pedestres)
        print("Sinal Vermelho para pedestre. Tempo de travessia acabando.")
        for _ in range(4):
            set_lights(1, 0, 0, 1, 0) # Apaga verde, liga vermelho
            time.sleep(0.3)
            set_lights(1, 0, 0, 0, 0) # Apaga vermelho
            time.sleep(0.3)
            
        # Etapa 4 (Tudo vermelho)
        set_lights(1, 0, 0, 1, 0)
        time.sleep(1) # Apenas um 1 segundo para segurança
        
        # Etapa 5 (Volta ao fluxo normal)
        print("Travessia encerrada. Fluxo de carros liberado.")
        set_lights(0, 0, 1, 1, 0)
        
        # Etapa 5 (tempo de recarga para evitar spam do botão)
        pedestrian_request = False
        time.sleep(3)
        print("Aguardando novo pedestre.")

    # Delay no loop principal para evitat sobrecarregar a CPU do ESP32
    time.sleep(0.1)