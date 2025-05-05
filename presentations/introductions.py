import reveal_slides as rs

def get_slides():
    slides = """
    # Web Scraping
    Úvod do automatizovaného získávání dat

    ---
    <!-- .slide: data-background-color="#283747" -->
    ## Co je Web Scraping?

    **Technika automatizovaného získávání dat z webových stránek pomocí extrakce informací z HTML kódu.**

    ---
    <!-- .slide: data-background-color="#283747" -->
    ## Využití Web Scrapingu

    - Analýza a výzkum trhu 📊
    - Agregace obsahu 📰
    - Obchodní intelligence 💼
    - Datová analýza 📈
    - Monitoring webů 🔍

    ---

    ## Základní technologie

    1. **HTML** - struktura stránky 
    2. **CSS** - styly a selektory  
    3. **Python knihovny** - nástroje  

    ---
    <!-- .slide: data-background-color="#285747" -->
    ### Dostupné nástroje

    --

    **Stahování stránek**
    ```python
    # Requests - základní HTTP požadavky
    # Selenium - pro dynamické stránky
    # aiohttp - asynchronní stahování
    ```

    --

    **Parsování HTML**
    ```python
    # BeautifulSoup - populární parser
    # lxml - rychlý XML/HTML parser
    # html5lib - přesný HTML parser
    ```

    --

    **Komplexní řešení**
    ```python
    # Scrapy - framework pro scraping
    # Playwright - automatizace prohlížeče
    # Puppeteer - Node.js nástroj
    ```

    ---

    ### Praktický postup

    1. Analýza stránky   
    2. Výběr nástrojů    
    3. Implementace scraperu   
    4. Testování a ladění  

    ---

    ## Tipy pro začátek

    1. **Začněte jednoduše**   
    2. **Používejte DevTools**    
    3. **Ošetřujte chyby**    
    4. **Testujte na malých datech**  

    ---

    💡 **Tip**: Pro analýzu stránek používejte DevTools v prohlížeči
    """

    config = {
        "title": "Web Scraping",
        "theme": "dracula",
        "width": 1000,
        "height": 500,
        "plugins": ["highlight", "katex", "mathjax2", "mathjax3", "notes", "search", "zoom"]
    }

    return rs.slides(slides, config=config, markdown_props={"data-separator-vertical":"^--$"}, key="foo")