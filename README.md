<h1 align="center"> <strong align="center"> Code Challenge - Bibicí Níus </strong> </h1>

<p align="center">
    <img src="./img/Bibici_Nius.png" width=200px/>
</p>

<br>

<h2><img src="./img/descricao.svg" width=50px/> Descrição </h2>

<div>
<p> Bibici Nius is my solution to a coding challenge. </p>

<br>

<p><b> Coding challenge statement </b></p>

<br>

<p> This page consists a coding challenge for Data Engineering roles. </p>

<br>

<p><b> Purpose </b></p>

<br>

<p> Aim of this test is three fold:
    <ul>
        <li>Evaluate your coding abilities;</li>
        <li>Judge your technical experince;</li>
        <li>Understand how you design a solution</li>
    </ul>
</p>

<br>

<p><b> How you will be judged? </b></p>

<br>

<p> You will be scored on:
    <ul>
        <li>Coding standard, comments and style;</li>
        <li>Overall solution design;</li>
        <li>Appropriate use of source control</li>
    </ul>
</p>

<br>

<p><b> Intructions </b></p>

<br>

<p> Please create a free account in <a href="https://cloud.google.com/free" target="_blank"> GCP </a>

<p> Candidate should put their test results on a public code repository hosted on Github. </p>

<p> Once test is completed please share the Github repository URL to hiring team so they can review your work.</p>

<p> You are building a backend application and <u>no UI is required</u>, input can be provided using a configuration file or command line </p>

<br>

<p><b> Challenge - News Content Collect and Store </b></p>

<br>

<p> Create a solution that crawls for articles from a news website, cleanses the response, stores in BigQuery (bonus) then makes it available to search via an API. </p>

<br>

<p><b> Details </b></p>

<br>

<p> Write an application to crawl an online news website, e.g. <a href="https://www.theguardian.com/au" target="_blank"> The Guardian </a> or <a href="https://www.bbc.com" target="_blank"> BBC </a> using a crawler framework such as <a href="http://scrapy.org/" target="_blank"> Scrapy </a>. You can use a crawl framework of your choice and build the application in Python. </p>

<br>

<p> The appliction should cleanse the articles to obtain only information relevant to the news story, e.g. article text, author, headline, article url, etc. Use a framework such as Readability to cleanse the page of superfluous content such as advertising and html. </p>

<br>

<p> Store the data in BigQuery, for subsequent search and retrieval. Ensure the URL of the article is included to enable comparison to the original. </p>

<br>

<p><b> Bonus </b></p>

<br>

<p> Write an API that provides access to the content in BigQuery database. The user should be able to search for articles by keyword. </p>

</div>

<br>

<div>
  <p>
    <sub>
      <adress>
        Icons made by (from <a href="https://www.flaticon.com/br/" target="_blank" title="Flaticon"> www.flaticon.com</a> and <a href="https://icon-icons.com/pt/" target="_blank" title="Icon-Icons">www.icon-icons.com/pt/</a>):
        <ul>
          <li><a href="https://www.pngfuel.com/free-png/wmpfw" target="_blank" title="pngfuel">Free-png</a>;</li>
          <li><a href="https://www.flaticon.com/br/autores/freepik" target="_blank" title="Freepik">Freepik</a>;</li>
        </ul>
      </adress>
    <sub>
  </p>
</div>

<br>

<h2><img src="./img/user_guide.png" width=50px/> How to use? </h2>
<div>
  <ul>
    <li> Download the repo and run <code>app.py</code></li>
    <li> Click on the link that appears in the terminal output </li>
    <li> In the search bar, add on the end of the URL <code>/Article/*KEYWORD*</code> (to search for a specific keyword) or <code>/AllArticles</code> (to search all articles in the database - around 30 articles).
    </li>
  </ul>
</div>

<br>

<h2><img src="./img/melhorias.png" width=50px/> Improvment opportunities </h2>

<br>

<div>
  <p> I didn't have enough time to learn how to:</p>
    <ul>
      <li> <s> Improve data access control in BigQuery. </s> </li>
      <li> Implement the input using a configuration file or command line: </li>
    </ul>
  <p> I believe these would be the improvements for the next steps. </p>
</div>

<br>

<h2><img src="./img/autor.svg" width=50px/> Autor </h2>

<a href="https://www.linkedin.com/in/vini-antunes/" target="_blank"><img src="https://avatars0.githubusercontent.com/u/57882903?s=460&u=caee8cc76060b036952e169feba0449f2d43519e&v=4" width="140px;" alt="foto do autor"/>
<br>
<sub><b>Vini Antunes</b></sub>
</a>
