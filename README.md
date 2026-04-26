# Processo Seletivo – Intensivo Maker | IoT

### 👤 Identificação: Gabriel Moreira Tavares Santana

---

## 1️⃣ Visão Geral da Solução

Desenvolvi um sistema embarcado simulado utilizando um ESP32 com o objetivo de representar o funcionamento de um semáforo inteligente com controle de travessia de pedestres.

O sistema controla dois conjuntos de sinais: um para veículos com tres cores e outro para pedestres com duas cores. Se tem interação com o usuário por meio de um botão da solicitação de travessia e ao pressionar o botão, o sistema realiza uma transição respeitando o fluxo do trânsito antes de liberar a passagem para pedestres.

---

## 2️⃣ Arquitetura do Sistema Embarcado

Optei por estruturar o sistema utilizando o conceito de máquina de estados finitos, por ser uma abordagem comum e eficiente em sistemas embarcados.

O fluxo principal do programa segue um loop contínuo, dividido em três etapas principais:

* Leitura das entradas (estado do botão)
* Atualização do estado do sistema
* Controle das saídas (LEDs)

Os estados definidos foram:

* `STATE_CAR_GREEN` – fluxo normal dos veículos
* `STATE_CAR_YELLOW` – transição de parada
* `STATE_CAR_RED_PEDESTRIAN` – parada dos veículos e liberação dos pedestres

A ligação entre os componentes ocorre da seguinte forma:

* O botão altera uma variável de requisição de pedestre
* A lógica de estados decide quando essa requisição será atendida
* Os LEDs refletem o estado atual do sistema

---

## 3️⃣ Componentes Utilizados na Simulação

Os componentes utilizados no `diagram.json` foram:

* **ESP32 DevKit v4** – microcontrolador responsável pela execução do sistema
* **3 LEDs para os veículos** – representam os estados do semáforo de carros
* **2 LEDs para os pedestres** – representam os estados do semáforo de pedestres
* **1 botão para os pedestres** – utilizado para solicitar a travessia

---

## 4️⃣ Decisões Técnicas Relevantes

A utilização de uma máquina de estados, pois facilita a leitura do código e evita comportamentos inesperados em sistemas com múltiplos modos de operação.

Optei por separar o código em funções específicas, como leitura de entrada, atualização de estado e controle de saída, tornando o sistema mais modular.

Para a leitura do botão, implementei detecção de borda, evitando múltiplas leituras de um único pressionamento.

---

## 5️⃣ Resultados Obtidos

O sistema executa perfeitamente no Wokwi. O estado inicial é mantido corretamente e as transições de luzes respeitam os tempos estabelecidos.

A integração com o Wokwi CLI funcionou, e o projeto foi versionado de forma correta.

O código passou na validação automatizada das GitHub Actions, comprovando que o ambiente Python e as execuções de teste em nuvem rodam sem erros.

O fluxo resultante é:

* Inicialmente, o semáforo dos veículos inicia no verde e o dos pedestres no vermelho
* Quando um pedestre pressionar o botão, o sistema registra a solicitação
* O semáforo dos veiculos transita para amarelo e depois vermelho
* Pedestres recebem sinal verde por um período definido
* Após esse período, o sistema retorna ao estado inicial

---

## 6️⃣ Comentários Adicionais

Um desafio técnico foi entender o comportamento do pipeline de CI/CD no GitHub Actions. Realizei a leitura dos no GitHub Actions para entender que a falha inicial ocorria por um erro da chave WOKWI_CLI_TOKEN não presente, já que eu tinha colocado o nome de WOKWI_API_KEY como no READ.ME do repositorio base. Outro foi pelo limite de *timeout* devido ao `expect_text` por conta que eu tinha tirado o print inicial que vinha no codigo.

Uma limitação da solução atual é a ausência de um filtro de click mais robusto para o botão, o que poderia ser melhorado em uma versão futura.

Como aprendizado, esse projeto reforçou a importância de organização lógica em sistemas embarcados e o uso de máquina de estados como ferramenta fundamental para controle de fluxo.



