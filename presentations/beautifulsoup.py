import reveal_slides as rs


def get_slides():
    slides = """
    # BeautifulSoup
    Knihovna pro parsování HTML a XML

    ---
    <!-- .slide: data-background-color="#283747" -->
    ## Co je BeautifulSoup?

    **BeautifulSoup je Python knihovna pro extrakci dat z&nbsp;HTML a XML souborů.**

    ---
    <!-- .slide: data-background-color="#283747" -->
    ## Hlavní výhody BeautifulSoup

    - Jednoduchá syntaxe 🔍
    - Flexibilní vyhledávání 🎯
    - Robustní parsování 💪
    - Podpora různých parserů 🛠
    - Snadná navigace v DOM 🗺

    ---

    ## Instalace a import

    ```python
    # Instalace pomocí pip
    pip install beautifulsoup4

    # Import v Pythonu
    from bs4 import BeautifulSoup
    ```

    ---
    <!-- .slide: data-background-color="#285747" -->
    ### Základní použití

    ```python
    # Vytvoření instance BeautifulSoup
    html_doc = '''
    <html>
      <body>
        <h1>Titulek</h1>
        <p class="text">Obsah</p>
      </body>
    </html>
    '''
    soup = BeautifulSoup(html_doc, 'html.parser')
    ```

    ---
    <!-- .slide: data-background-color="#285747" -->
    ### Metody pro vyhledávání

    --

    **Základní metody**
    ```python
    # Najde první výskyt
    soup.find('p')

    # Najde všechny výskyty
    soup.find_all('p')

    # CSS selektor
    soup.select('.text')
    ```

    --

    **Pokročilé vyhledávání**
    ```python
    # Hledání podle atributů
    soup.find('p', class_='text')

    # Hledání podle více kritérií
    soup.find_all(['h1', 'p'])

    # Regulární výrazy
    import re
    soup.find_all(text=re.compile('Obsah'))
    ```

    ---

    ### Navigace v DOM

    **Procházení elementů**     <!-- .element: class="fragment" data-fragment-index="0" -->
    ```python
    element.parent          # Rodičovský element
    element.children       # Přímí potomci
    element.descendants    # Všichni potomci
    ```
    <!-- .element: class="fragment" data-fragment-index="1" -->

    **Sourozenci**     <!-- .element: class="fragment" data-fragment-index="2" -->
    ```python
    element.next_sibling   # Další sourozenec
    element.previous_sibling # Předchozí sourozenec
    ```
    <!-- .element: class="fragment" data-fragment-index="3" -->

    ---

    ### Extrakce dat

    ```python
    # Získání textu
    element.text       # Veškerý text
    element.string     # Přímý text

    # Získání atributů
    element['class']   # Hodnota atributu
    element.attrs      # Slovník všech atributů

    # Modifikace
    element.string = "Nový text"
    element['class'] = "new-class"
    ```

    ---

    ### Praktický příklad

    ```python
    from bs4 import BeautifulSoup
    import requests

    # Stažení stránky
    url = "https://example.com"
    page = requests.get(url)

    # Parsování HTML
    soup = BeautifulSoup(page.content, 'html.parser')

    # Vyhledání elementů
    articles = soup.find_all('article')

    # Extrakce dat
    for article in articles:
        title = article.find('h2').text
        link = article.find('a')['href']
        print(f"{title}: {link}")
    ```

    ---

    ### Pokročilé techniky

    1. Vlastní filtry     <!-- .element: class="fragment" data-fragment-index="0" -->
    2. Rekurzivní vyhledávání     <!-- .element: class="fragment" data-fragment-index="1" -->
    3. Parsování částečného HTML     <!-- .element: class="fragment" data-fragment-index="2" -->
    4. Práce s XML     <!-- .element: class="fragment" data-fragment-index="3" -->

    ---

    ## Časté problémy a řešení

    - **Kódování textu** - použijte správné charset
    - **Chybějící elementy** - ošetřete None
    - **Dynamický obsah** - zvažte Selenium
    - **Výkon** - použijte lxml parser

    ---

    ## Děkuji za pozornost

    💡 **Tip**: Dokumentace BeautifulSoup je výborným zdrojem informací:
    [https://www.crummy.com/software/BeautifulSoup/bs4/doc/](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
    """

    config = {
        "title": "BeautifulSoup",
        "theme": "dracula",
        "width": 1000,
        "height": 500,
        "plugins": ["highlight", "katex", "mathjax2", "mathjax3", "notes", "search", "zoom"]
    }

    return rs.slides(slides, config=config, markdown_props={"data-separator-vertical":"^--$"}, key="foo")