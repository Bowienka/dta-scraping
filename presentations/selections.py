import reveal_slides as rs


def get_slides():
    slides = """
    # XPath a CSS Selektory
    Nástroje pro navigaci v HTML dokumentech

    ---
    <!-- .slide: data-background-color="#283747" -->
    ## CSS Selektory

    **Jednoduchý a efektivní způsob výběru HTML elementů pomocí jejich vlastností**

    ---
    <!-- .slide: data-background-color="#283747" -->
    ## XPath

    **Jazyk pro adresování částí XML dokumentu, použitelný i pro HTML**

    ---

    ## CSS Selektory - Základy

    1. **Elementy** `p`     <!-- .element: class="fragment" data-fragment-index="0" -->
    2. **Třídy** `.trida`     <!-- .element: class="fragment" data-fragment-index="1" -->
    3. **ID** `#identifikator`     <!-- .element: class="fragment" data-fragment-index="2" -->
    4. **Atributy** `[attr=hodnota]`     <!-- .element: class="fragment" data-fragment-index="3" -->

    ---
    <!-- .slide: data-background-color="#285747" -->
    ### CSS Kombinátory

    ```css
    /* Potomek (kdekoliv uvnitř) */
    div p

    /* Přímý potomek */
    div > p

    /* Následující sourozenec */
    div + p

    /* Všichni následující sourozenci */
    div ~ p
    ```

    ---
    <!-- .slide: data-background-color="#285747" -->
    ### CSS Pseudo-třídy

    ```css
    /* První element svého typu */
    p:first-of-type

    /* Poslední potomek */
    p:last-child

    /* Sudé elementy */
    p:nth-child(even)

    /* Prázdné elementy */
    p:empty
    ```

    ---

    ## XPath - Základy

    1. **Absolutní cesta** `/html/body/div`     <!-- .element: class="fragment" data-fragment-index="0" -->
    2. **Relativní cesta** `//div`     <!-- .element: class="fragment" data-fragment-index="1" -->
    3. **Aktuální uzel** `.`     <!-- .element: class="fragment" data-fragment-index="2" -->
    4. **Rodičovský uzel** `..`     <!-- .element: class="fragment" data-fragment-index="3" -->

    ---
    <!-- .slide: data-background-color="#285747" -->
    ### XPath Predikáty

    ```xpath
    # Element s atributem
    //div[@class='container']

    # N-tý element
    //div[2]

    # Element s textem
    //p[text()='Hledaný text']

    # Obsahuje text
    //p[contains(text(), 'část textu')]
    ```

    ---
    <!-- .slide: data-background-color="#285747" -->
    ### XPath Osy

    ```xpath
    # Všichni potomci
    //div/descendant::p

    # Předci
    //p/ancestor::div

    # Následující sourozenci
    //div/following-sibling::p

    # Předchozí sourozenci
    //div/preceding-sibling::p
    ```

    ---

    ### Praktické příklady

    HTML struktura:
    ```html
    <div class="container">
        <article id="hlavni">
            <h1>Nadpis</h1>
            <p class="text">Odstavec 1</p>
            <p class="text">Odstavec 2</p>
        </article>
    </div>
    ```

    ---

    ### CSS řešení

    ```css
    /* Všechny odstavce v article */
    article p

    /* Odstavce s třídou text */
    .text

    /* První odstavec v article */
    article p:first-child

    /* Article s ID hlavni */
    #hlavni
    ```

    ---

    ### XPath řešení

    ```xpath
    # Všechny odstavce v article
    //article//p

    # Odstavce s třídou text
    //p[@class='text']

    # První odstavec v article
    //article/p[1]

    # Article s ID hlavni
    //article[@id='hlavni']
    ```

    ---

    ## Srovnání CSS a XPath

    **CSS Selektory**
    - Jednodušší syntaxe 📝
    - Lepší čitelnost 👀
    - Omezené možnosti ⚠️

    **XPath**
    - Složitější syntaxe 🤔
    - Větší flexibilita 💪
    - Pohyb "nahoru" ve stromu 🔝

    ---

    ## Doporučení pro použití

    1. **Začněte s CSS selektory**     <!-- .element: class="fragment" data-fragment-index="0" -->
    2. **XPath pro složité případy**     <!-- .element: class="fragment" data-fragment-index="1" -->
    3. **Testujte v prohlížeči**     <!-- .element: class="fragment" data-fragment-index="2" -->
    4. **Udržujte selektory aktuální**     <!-- .element: class="fragment" data-fragment-index="3" -->

    ---

    ## Děkuji za pozornost

    💡 **Tip**: Pro testování selektorů použijte DevTools v prohlížeči
    """

    config = {
        "title": "Selektory",
        "theme": "dracula",
        "width": 1000,
        "height": 500,
        "plugins": ["highlight", "katex", "mathjax2", "mathjax3", "notes", "search", "zoom"]
    }

    return rs.slides(slides, config=config, markdown_props={"data-separator-vertical":"^--$"}, key="foo")