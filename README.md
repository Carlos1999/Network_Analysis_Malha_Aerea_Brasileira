# :mag_right: Introdução

​	Nesse repositório, estaremos realizando um estudo da rede da malha aérea brasileira, em que os nós da rede representam os aeroportos e os links (arestas) representam os voos de um aeroporto para outro. A Análise foi realizada levando em consideração cinco parâmetros: 

1. **Assortatividade**, métrica que avalia o quanto os nós de uma rede tendem a se relacionar com outros nós com características parecidas;

2. **Assortatividade dos graus**, a métrica que indica se os nós de uma rede tendem a se relacionar com os nós de mesmo grau que ele;

3. **Componentes conectados**, subgráfos em que os nós podem ser alcançados por outro através dos links; 

4. **Simulação de uma viajem entre as regiões**, foi simulado uma viagem entre uma cidade da região <u>norte</u> para outra da região <u>sul</u>, desta por sua vez para uma da região <u>nordeste</u>, e desta para uma do <u>centro oeste</u> e por fim dessa última para uma do <u>sudeste</u>. Ao todo foram escolhidas 5 cidades (Uma de cada região) aleatoriamente para a realização do trajeto;

5. **Coeficiente de clustering**,  medida em que podemos verificar se uma rede tende a estar em topologia de estrela, isto é, possui algum nó como "celebridade". 

É possível ter acesso à base de dados que utilizamos através do repositório [dataset-flights-brazil](https://github.com/alvarofpp/dataset-flights-brazil).



# :play_or_pause_button: Passo a Passo Para a Reprodução

1. Entrar no repositório [dataset-flights-brazil ](https://github.com/alvarofpp/dataset-flights-brazil), entrar na pasta **data**, baixar e descompactar   `anac.zip` dentro da pasta do notebook `network_analysis_malha_aerea` ;
2. Executar o script  `cria_grafo.py`;
3. Executar o notebook `network_analysis_malha_aerea` acompanhando as explicações.



# :man_technologist: Autores do projeto

* Carlos Vinícius dos Santos ([@Carlos1999](https://github.com/carlos1999))
* Hugo Felipe dos Santos ([@hugofsantos](https://github.com/hugofsantos))



# :question: Sobre o Projeto

Projeto criado para a disciplina de Análise de Redes (IMD1155), ministrada pelo professor [@ivanovitchm](https://github.com/ivanovitchm), do **Instituto Metrópole Digital - UFRN**, curso de Bacharelado em Tecnologia da Informação.

Para a realização de tal prática foram utilizadas as ferramentas:

- **_Networkx_**;
- **_Jupyter Notebooks_**;
- **_Python_**
