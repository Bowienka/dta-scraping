import reveal_slides as rs


def get_slides():
    slides = """
    # HTML
    Základy značkovacího jazyka

    ---
    <!-- .slide: data-background-color="#283747" -->
    ## Co je HTML?

    **HTML (HyperText Markup Language) je značkovací jazyk používaný pro strukturování a prezentaci obsahu na webu.**

    ---
    <!-- .slide: data-background-color="#283747" -->
    ## K čemu slouží HTML?

    - Vytváření webových stránek 🌐
    - Definice struktury obsahu 📑
    - Propojování dokumentů 🔗
    - Vkládání multimédií 🎬
    - Tvorba formulářů 📝

    ---

    ## Základní struktura HTML

    `<!DOCTYPE html>`     <!-- .element: class="fragment" data-fragment-index="0" -->  
    **Definice typu dokumentu**               <!-- .element: class="fragment" data-fragment-index="1" -->  

    `<html lang="cs">`     <!-- .element: class="fragment" data-fragment-index="2" -->  
    **Kořenový element**          <!-- .element: class="fragment" data-fragment-index="3" -->  

    `<head>, <body>`  <!-- .element: class="fragment" data-fragment-index="4" -->  
    **Meta informace a obsah**          <!-- .element: class="fragment" data-fragment-index="5" -->  

    ---
    <!-- .slide: data-background-color="#285747" -->
    ### Příklad struktury
    ```html
    <!DOCTYPE html>
    <html lang="cs">
      <head>
        <meta charset="UTF-8">
        <title>Moje stránka</title>
      </head>
      <body>
        <h1>Vítejte</h1>
        <p>Toto je obsah stránky.</p>
      </body>
    </html>
    ```

    ---
    <!-- .slide: data-background-color="#285747" -->
    ### Základní HTML značky

    --

    **Textové elementy**
    ```html
    <h1>Hlavní nadpis</h1>
    <p>Odstavec textu</p>
    <strong>Důležitý text</strong>
    <em>Zvýrazněný text</em>
    ```

    --

    **Odkazy a obrázky**
    ```html
    <a href="https://example.com">
        Odkaz na stránku
    </a>
    <img src="obrazek.jpg" 
         alt="Popis obrázku">
    ```

    ---

    ### Seznamy

    **Nečíslovaný seznam**     <!-- .element: class="fragment" data-fragment-index="0" -->
    ```html
    <ul>
        <li>První položka</li>
        <li>Druhá položka</li>
    </ul>
    ```
    <!-- .element: class="fragment" data-fragment-index="1" -->

    **Číslovaný seznam**     <!-- .element: class="fragment" data-fragment-index="2" -->
    ```html
    <ol>
        <li>První položka</li>
        <li>Druhá položka</li>
    </ol>
    ```
    <!-- .element: class="fragment" data-fragment-index="3" -->

    ---

    ### Tabulky

    ```html
    <table>
        <tr>
            <th>Hlavička 1</th>
            <th>Hlavička 2</th>
        </tr>
        <tr>
            <td>Data 1</td>
            <td>Data 2</td>
        </tr>
    </table>
    ```

    ---

    ### Formuláře

    ```html
    <form action="/odeslat" method="POST">
        <label for="jmeno">Jméno:</label>
        <input type="text" 
               id="jmeno" 
               name="jmeno" 
               required>

        <label for="email">Email:</label>
        <input type="email" 
               id="email" 
               name="email">

        <button type="submit">
            Odeslat
        </button>
    </form>
    ```

    ---

    ### Sémantické elementy HTML5

    ```html
    <header>
        <nav>Menu webu</nav>
    </header>

    <main>
        <article>
            <h1>Článek</h1>
            <p>Obsah článku</p>
        </article>

        <aside>
            Boční panel
        </aside>
    </main>

    <footer>
        Patička webu
    </footer>
    ```

    ---

    ## Atributy HTML elementů

    1. **class** - CSS třídy     <!-- .element: class="fragment" data-fragment-index="0" -->
    2. **id** - unikátní ID     <!-- .element: class="fragment" data-fragment-index="1" -->
    3. **src** - zdroj médií     <!-- .element: class="fragment" data-fragment-index="2" -->
    4. **href** - odkazy     <!-- .element: class="fragment" data-fragment-index="3" -->
    5. **alt** - alternativní text     <!-- .element: class="fragment" data-fragment-index="4" -->

    ---

    ## Důležité zásady

    1. Validní kód     <!-- .element: class="fragment" data-fragment-index="0" -->
    2. Správná sémantika     <!-- .element: class="fragment" data-fragment-index="1" -->
    3. Přístupnost     <!-- .element: class="fragment" data-fragment-index="2" -->
    4. Responzivita     <!-- .element: class="fragment" data-fragment-index="3" -->

    ---

    ## Děkuji za pozornost

    💡 **Tip**: Pro validaci HTML kódu používejte [W3C validátor](https://validator.w3.org/)
    """

    config = {
        "title": "HTML",
        "theme": "dracula",
        "width": 1000,
        "height": 500,
        "plugins": ["highlight", "katex", "mathjax2", "mathjax3", "notes", "search", "zoom"]
    }

    return rs.slides(slides, config=config, markdown_props={"data-separator-vertical":"^--$"}, key="foo")
