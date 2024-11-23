# Organize, Prioritize, and Boost Your Productivity with Smart Assistance

<!-- Convenção: O caminho da imagem será a url da imagem no github, ao invés de ser o caminho do repositório local. Desse modo, evita o problema da imagem não carregar no github. -->
<!--
![Imagem de Capa](https://github.com/jeffersonrafael/projrto_to_do_list/blob/master/Images/DALL%C2%B7E-2024-11-23-09.36.png)
-->

<div align="center">
  <img src="https://github.com/jeffersonrafael/projrto_to_do_list/blob/master/Images/DALL%C2%B7E-2024-11-23-09.36.png" alt="Imagem de capa" width="600"/>
</div>

<div align="center">
  <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="MIT License"/>
  <img src="https://img.shields.io/badge/License-GPLv3-blue.svg" alt="GPLv3 License"/>
  <img src="https://img.shields.io/badge/python-3.11-green.svg" alt="Python 3.11"/>
  <img src="https://img.shields.io/badge/Flet-1.0-orange.svg" alt="Flet"/>
</div>


## Indice
<!--
- [Licença](#licença) -->
- [Descrição](#descrição)
- [Contribuidores](#contribuidores)

---

<!--
# Licença
![MIT License](https://img.shields.io/badge/License-MIT-yellow.svg) ![GPLv3 License](https://img.shields.io/badge/License-GPLv3-blue.svg) 
-->


## Descrição

Empenhado em aprimorar a minha produtividade e insatisfeito com os aplicativos disponíveis no mercado, decidi transformar minha frustração em inovação. Identifiquei todas as falhas no principal app de organização e rotina e, com isso, criei uma solução própria e revolucionária. O resultado? Um app de código aberto, construido em ![Python 3.11](https://img.shields.io/badge/python-3.11-green.svg) usando a biblioteca ![Flet](https://img.shields.io/badge/Flet-1.0-orange.svg)
 e que realmente entende suas necessidades e potencializa sua rotina como nunca antes!

Este app é para um usuário que busca:  

1. **Melhorar a produtividade**: Quer gerenciar melhor seu tempo e realizar mais tarefas no dia.  
2. **Organização**: Deseja uma ferramenta que facilite a organização de suas atividades diárias, com listas de tarefas claras e objetivos definidos.  
3. **Manter o foco**: Procura evitar distrações e se concentrar no que realmente importa, utilizando técnicas como o Pomodoro.  
4. **Gestão do tempo**: Deseja planejar o dia de forma eficiente, combinando alarmes e cronômetros para acompanhar prazos.  
5. **Assistência personalizada**: Busca um suporte prático e intuitivo, como uma assistente virtual, para lembrar compromissos, sugerir estratégias e oferecer dicas úteis.  
6. **Equilíbrio entre produtividade e descanso**: Valorizam ferramentas que promovem pausas estratégicas para evitar o esgotamento.  

No geral, o objetivo principal é ter uma vida mais organizada e produtiva, sem comprometer a saúde mental.


## Contribuidores
<!-- ![Minha Foto de Perfil](https://avatars.githubusercontent.com/u/65470846?v=4) -->

<img src="https://avatars.githubusercontent.com/u/65470846?v=4" alt="Minha Foto de Perfil" width="150"/>

[Jefferson Rafael](https://github.com/jeffersonrafael)



# Aba em inglês

<div>
  <style>
    .tab {
      display: none;
    }
    .tab-header {
      display: flex;
      cursor: pointer;
      padding: 10px;
      background-color: #f1f1f1;
      border-bottom: 1px solid #ccc;
    }
    .tab-header div {
      margin-right: 10px;
      padding: 10px;
      border: 1px solid #ccc;
      background-color: #e1e1e1;
    }
    .tab-header div.active {
      background-color: #fff;
      border-bottom: none;
    }
    .tab-content {
      padding: 10px;
      border: 1px solid #ccc;
      display: none;
    }
    .tab-content.active {
      display: block;
    }
  </style>

  <div class="tab-header">
    <div onclick="openTab('tab1')">Aba 1</div>
    <!-- <div onclick="openTab('tab2')">Aba 2</div>
    <div onclick="openTab('tab3')">Aba 3</div> -->
  </div>

  <div id="tab1" class="tab-content">
    <h2>Conteúdo da Aba 1</h2>
    <p>Este é o conteúdo da primeira aba.</p>
  </div>
  <!-- <div id="tab2" class="tab-content">
          <h2>Conteúdo da Aba 2</h2>
          <p>Este é o conteúdo da segunda aba.</p>
       </div>
  <div id="tab3" class="tab-content">
    <h2>Conteúdo da Aba 3</h2>
    <p>Este é o conteúdo da terceira aba.</p>
  </div> -->

  <script>
    function openTab(tabId) {
      var i, tabContent, tabHeader;
      tabContent = document.getElementsByClassName("tab-content");
      for (i = 0; i < tabContent.length; i++) {
        tabContent[i].classList.remove("active");
      }
      tabHeader = document.querySelectorAll(".tab-header div");
      for (i = 0; i < tabHeader.length; i++) {
        tabHeader[i].classList.remove("active");
      }
      document.getElementById(tabId).classList.add("active");
      event.target.classList.add("active");
    }
  </script>
</div>
