import streamlit as st
from presentations.beautifulsoup import get_slides

import bs4

st.title("BeautifulSoup - Parsování HTML v Pythonu")

presentation, text, samples, examples = st.tabs(["Prezentace", "Studijní text", "Ukázky", "Příklady"])

with presentation:
    get_slides()

with text:
    st.header("Co je BeautifulSoup?")
    st.write("""
    BeautifulSoup je Python knihovna, která usnadňuje extrakci dat z HTML a XML souborů. 
    Poskytuje jednoduché metody pro procházení, vyhledávání a modifikaci parsovaného dokumentu.
    Název knihovny je inspirován tagem `<soup>` z populárního HTML editoru z roku 1996.
    """)

    st.header("Instalace a základní použití")
    st.code("""
    # Instalace
    pip install beautifulsoup4

    # Základní použití
    from bs4 import BeautifulSoup

    # Vytvoření soup objektu
    soup = BeautifulSoup(html_doc, 'html.parser')
    """, language="python")

    st.header("Hlavní funkce BeautifulSoup")
    st.markdown("""
    🔍 **Vyhledávání elementů**
    - `find()` - najde první výskyt elementu
    - `find_all()` - najde všechny výskyty elementů
    - `select()` - vyhledávání pomocí CSS selektorů

    🌳 **Navigace v dokumentu**
    - `parent` - rodičovský element
    - `children` - přímí potomci
    - `descendants` - všichni potomci
    - `next_sibling` / `previous_sibling` - sousední elementy

    📝 **Práce s obsahem**
    - `text` - získání textového obsahu
    - `string` - přímý textový obsah
    - `attrs` - práce s atributy
    """)

    st.header("Praktické příklady")

    st.subheader("1. Základní vyhledávání")
    st.code("""
    html_doc = '''
    <div class="content">
        <h1>Hlavní nadpis</h1>
        <p class="text">První odstavec</p>
        <p class="text">Druhý odstavec</p>
    </div>
    '''

    soup = BeautifulSoup(html_doc, 'html.parser')

    # Najít první odstavec
    first_p = soup.find('p')
    print(first_p.text)  # První odstavec

    # Najít všechny odstavce
    all_p = soup.find_all('p')
    for p in all_p:
        print(p.text)
    """, language="python")

    st.subheader("2. CSS selektory")
    st.code("""
    # Najít elementy podle třídy
    text_elements = soup.select('.text')

    # Najít element uvnitř jiného
    content_h1 = soup.select('.content h1')
    """, language="python")

    st.subheader("3. Práce s atributy")
    st.code("""
    # Získání hodnoty atributu
    element = soup.find('p')
    class_name = element['class']

    # Modifikace atributu
    element['class'] = 'new-class'

    # Přidání nového atributu
    element['id'] = 'my-paragraph'
    """, language="python")

    st.header("Pokročilé techniky")
    st.write("""
    BeautifulSoup nabízí několik pokročilých funkcí pro složitější scénáře:
    """)

    st.code("""
    # Vlastní filtrovací funkce
    def has_class_but_no_id(tag):
        return tag.has_attr('class') and not tag.has_attr('id')

    soup.find_all(has_class_but_no_id)

    # Regulární výrazy
    import re
    soup.find_all(text=re.compile("odstavec"))

    # Rekurzivní vyhledávání
    soup.find_all('p', recursive=True)
    """, language="python")

    st.info("""
    💡 **Tip**: Pro lepší výkon při parsování velkých dokumentů použijte parser 'lxml':
    ```python
    soup = BeautifulSoup(html_doc, 'lxml')
    ```
    Nejprve je potřeba nainstalovat lxml: `pip install lxml`
    """)

    st.warning("""
    ⚠️ **Časté problémy**:
    1. **Kódování** - ujistěte se, že používáte správné kódování při čtení HTML
    2. **None hodnoty** - vždy kontrolujte, zda element existuje
    3. **Dynamický obsah** - BeautifulSoup neparsuje JavaScript, pro dynamický obsah použijte Selenium
    4. **Výkon** - pro velké dokumenty zvažte použití lxml parseru nebo CSS selektorů
    """)

    st.header("Užitečné zdroje")
    st.markdown("""
    - [Oficiální dokumentace BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
    - [Tutoriál na Real Python](https://realpython.com/beautiful-soup-web-scraper-python/)
    - [Praktické příklady na GitHub](https://github.com/topics)""")

with samples:
    import streamlit as st
    import requests
    from bs4 import BeautifulSoup

    st.title("Interaktivní ukázky BeautifulSoup")

    st.header("1. Základní extrakce dat")
    with st.expander("Jednoduchý příklad extrakce"):
        st.subheader("Vstupní HTML")
        html_input = st.text_area(
            "HTML kód",
            '''
<div class="product">
    <h2>iPhone 14</h2>
    <p class="price">24 990 Kč</p>
    <span class="stock">Skladem</span>
</div>
            ''',
            height=200
        )

        st.subheader("Python kód")
        st.code("""
    from bs4 import BeautifulSoup

    soup = BeautifulSoup(html_input, 'html.parser')
    product = soup.find('div', class_='product')

    nazev = product.h2.text
    cena = product.find('p', class_='price').text
    sklad = product.find('span', class_='stock').text

    print(f"Název: {nazev}")
    print(f"Cena: {cena}")
    print(f"Dostupnost: {sklad}")
            """, language="python")

        if st.button("Spustit extrakci", key="basic_extraction"):
            soup = BeautifulSoup(html_input, 'html.parser')
            try:
                product = soup.find('div', class_='product')
                nazev = product.h2.text
                cena = product.find('p', class_='price').text
                sklad = product.find('span', class_='stock').text

                st.success(f"""
                    Výsledek extrakce:
                    - Název: {nazev}
                    - Cena: {cena}
                    - Dostupnost: {sklad}
                    """)
            except Exception as e:
                st.error(f"Chyba při extrakci: {str(e)}")

    st.header("2. Vyhledávání pomocí různých metod")
    with st.expander("Porovnání metod vyhledávání"):
        html_complex = """
            <div class="container">
                <article class="post">
                    <h2>První článek</h2>
                    <p class="text">Text prvního článku</p>
                    <a href="link1.html">Číst více</a>
                </article>
                <article class="post featured">
                    <h2>Druhý článek</h2>
                    <p class="text">Text druhého článku</p>
                    <a href="link2.html">Číst více</a>
                </article>
            </div>
            """

        st.code(html_complex, language="html")

        method = st.selectbox(
            "Vyberte metodu vyhledávání",
            ["find()", "find_all()", "select()", "select_one()"]
        )

        if method == "find()":
            st.code("""
        soup = BeautifulSoup(html_complex, 'html.parser')
        prvni_clanek = soup.find('article')
        print(prvni_clanek.h2.text)
                """, language="python")

            if st.button("Spustit find()"):
                soup = BeautifulSoup(html_complex, 'html.parser')
                prvni_clanek = soup.find('article')
                st.write(f"Nalezen článek: {prvni_clanek.h2.text}")

        elif method == "find_all()":
            st.code("""
        soup = BeautifulSoup(html_complex, 'html.parser')
        clanky = soup.find_all('article')
        for clanek in clanky:
            print(clanek.h2.text)
                """, language="python")

            if st.button("Spustit find_all()"):
                soup = BeautifulSoup(html_complex, 'html.parser')
                clanky = soup.find_all('article')
                for clanek in clanky:
                    st.write(f"Nalezen článek: {clanek.h2.text}")

        elif method == "select()":
            st.code("""
        soup = BeautifulSoup(html_complex, 'html.parser')
        featured = soup.select('article.featured')
        for clanek in featured:
            print(clanek.h2.text)
                """, language="python")

            if st.button("Spustit select()"):
                soup = BeautifulSoup(html_complex, 'html.parser')
                featured = soup.select('article.featured')
                for clanek in featured:
                    st.write(f"Nalezen zvýrazněný článek: {clanek.h2.text}")

        elif method == "select_one()":
            st.code("""
        soup = BeautifulSoup(html_complex, 'html.parser')
        prvni = soup.select_one('article.post')
        print(prvni.h2.text)
                """, language="python")

            if st.button("Spustit select_one()"):
                soup = BeautifulSoup(html_complex, 'html.parser')
                prvni = soup.select_one('article.post')
                st.write(f"Nalezen první článek: {prvni.h2.text}")

    st.header("3. Navigace v DOM")
    with st.expander("Ukázka navigace"):
        html_nav = '''
            <div class="wrapper">
                <header>
                    <h1>Hlavní nadpis</h1>
                    <nav>
                        <ul>
                            <li>První</li>
                            <li>Druhý</li>
                            <li>Třetí</li>
                        </ul>
                    </nav>
                </header>
                <main>
                    <p>Hlavní obsah</p>
                </main>
            </div>
            '''

        st.code(html_nav, language="html")

        nav_method = st.selectbox(
            "Vyberte způsob navigace",
            ["parent", "children", "next_sibling", "previous_sibling"]
        )

        if nav_method == "parent":
            st.code("""
        soup = BeautifulSoup(html_nav, 'html.parser')
        li = soup.find('li')
        parent_ul = li.parent
        parent_nav = parent_ul.parent
        print(f"Rodič <li>: {parent_ul.name}")
        print(f"Rodič <ul>: {parent_nav.name}")
                """, language="python")

            if st.button("Zobrazit rodiče"):
                soup = BeautifulSoup(html_nav, 'html.parser')
                li = soup.find('li')
                parent_ul = li.parent
                parent_nav = parent_ul.parent
                st.write(f"Rodič <li>: {parent_ul.name}")
                st.write(f"Rodič <ul>: {parent_nav.name}")

        elif nav_method == "children":
            st.code("""
        soup = BeautifulSoup(html_nav, 'html.parser')
        nav = soup.find('nav')
        for child in nav.children:
            if child.name:
                print(f"Potomek <nav>: {child.name}")
                """, language="python")

            if st.button("Zobrazit potomky"):
                soup = BeautifulSoup(html_nav, 'html.parser')
                nav = soup.find('nav')
                for child in nav.children:
                    if child.name:
                        st.write(f"Potomek <nav>: {child.name}")

        elif nav_method == "next_sibling":
            st.code("""
        soup = BeautifulSoup(html_nav, 'html.parser')
        header = soup.find('header')
        main = header.next_sibling.next_sibling
        print(f"Po <header> následuje: {main.name}")
                """, language="python")

            if st.button("Zobrazit následující element"):
                soup = BeautifulSoup(html_nav, 'html.parser')
                header = soup.find('header')
                main = header.next_sibling.next_sibling
                st.write(f"Po <header> následuje: {main.name}")

        elif nav_method == "previous_sibling":
            st.code("""
        soup = BeautifulSoup(html_nav, 'html.parser')
        main = soup.find('main')
        header = main.previous_sibling.previous_sibling
        print(f"Před <main> je: {header.name}")
                """, language="python")

            if st.button("Zobrazit předchozí element"):
                soup = BeautifulSoup(html_nav, 'html.parser')
                main = soup.find('main')
                header = main.previous_sibling.previous_sibling
                st.write(f"Před <main> je: {header.name}")

with examples:
    st.title("Cvičení - BeautifulSoup")

    st.info("""
     💡 **Obecné tipy pro řešení úkolů:**
     1. Nejprve si prohlédněte strukturu HTML
     2. Identifikujte klíčové elementy a jejich atributy
     3. Zkuste nejprve jednoduché řešení, potom ho vylepšujte
     4. Nezapomeňte na ošetření chyb
     5. Testujte řešení na různých vstupech
     """)

    st.warning("""
     ⚠️ **Častá úskalí:**
     1. Chybějící elementy
     2. Nekonzistentní struktura
     3. Speciální znaky v textu
     4. Nested elementy
     5. Whitespace v textu
     """)

    st.header("Úkol 1: Extrakce produktů")
    with st.expander("Zobrazit zadání"):
        st.markdown("""
        Z následujícího HTML kódu extrahujte informace o všech produktech (název, cena, dostupnost):
        """)

        html_products = '''
        <div class="eshop">
            <div class="product">
                <h2>iPhone 14</h2>
                <p class="price">24 990 Kč</p>
                <span class="stock">Skladem</span>
            </div>
            <div class="product">
                <h2>Samsung Galaxy S23</h2>
                <p class="price">21 490 Kč</p>
                <span class="stock">Vyprodáno</span>
            </div>
            <div class="product">
                <h2>Xiaomi 13</h2>
                <p class="price">18 999 Kč</p>
                <span class="stock">Skladem</span>
            </div>
        </div>
        '''

        st.code(html_products, language="html")

        if st.button("Zobrazit nápovědu", key="hint1"):
            st.info("""
            1. Použijte `find_all()` pro nalezení všech produktů
            2. Pro každý produkt najděte jeho elementy pomocí:
               - `find('h2')` pro název
               - `find('p', class_='price')` pro cenu
               - `find('span', class_='stock')` pro dostupnost
            3. Použijte `.text` pro získání textu z elementů
            """)

        if st.button("Zobrazit řešení", key="solution1"):
            st.code("""
            from bs4 import BeautifulSoup

            soup = BeautifulSoup(html_products, 'html.parser')
            products = soup.find_all('div', class_='product')

            for product in products:
                name = product.find('h2').text
                price = product.find('p', class_='price').text
                stock = product.find('span', class_='stock').text
                print(f"Produkt: {name}, Cena: {price}, Dostupnost: {stock}")
            """, language="python")

    st.header("Úkol 2: Extrakce odkazů z menu")
    with st.expander("Zobrazit zadání"):
        st.markdown("""
        Extrahujte všechny odkazy z navigačního menu včetně jejich URL:
        """)

        html_menu = '''
        <nav class="menu">
            <ul>
                <li><a href="/" class="active">Domů</a></li>
                <li><a href="/produkty">Produkty</a></li>
                <li><a href="/kontakt">Kontakt</a>
                    <ul class="submenu">
                        <li><a href="/email">Email</a></li>
                        <li><a href="/telefon">Telefon</a></li>
                    </ul>
                </li>
            </ul>
        </nav>
        '''

        st.code(html_menu, language="html")

        if st.button("Zobrazit nápovědu", key="hint2"):
            st.info("""
            1. Najděte všechny odkazy pomocí `find_all('a')`
            2. Pro každý odkaz získejte:
               - Text pomocí `.text`
               - URL pomocí `['href']`
            3. Bonus: Rozlište hlavní menu a submenu pomocí rodičovských elementů
            """)

        if st.button("Zobrazit řešení", key="solution2"):
            st.code("""
            from bs4 import BeautifulSoup

            soup = BeautifulSoup(html_menu, 'html.parser')

            # Základní řešení
            for link in soup.find_all('a'):
                text = link.text
                url = link['href']
                print(f"Odkaz: {text} -> {url}")

            # Pokročilé řešení s rozlišením submenu
            main_menu = soup.select('nav > ul > li > a')
            submenu = soup.select('.submenu a')

            print("Hlavní menu:")
            for link in main_menu:
                print(f"- {link.text}: {link['href']}")

            print("\\nSubmenu:")
            for link in submenu:
                print(f"- {link.text}: {link['href']}")
            """, language="python")

    st.header("Úkol 3: Analýza článku")
    with st.expander("Zobrazit zadání"):
        st.markdown("""
        Analyzujte strukturu článku a extrahujte jeho části:
        """)

        html_article = '''
        <article class="blog-post">
            <header>
                <h1>Průvodce Python programováním</h1>
                <div class="meta">
                    <span class="author">Jan Novák</span>
                    <time datetime="2024-03-15">15.3.2024</time>
                    <span class="category">Python</span>
                </div>
            </header>
            <div class="content">
                <p>První odstavec článku...</p>
                <h2>Podnadpis</h2>
                <p>Druhý odstavec článku...</p>
                <ul class="tags">
                    <li>programování</li>
                    <li>začátečníci</li>
                    <li>tutorial</li>
                </ul>
            </div>
        </article>
        '''

        st.code(html_article, language="html")

        if st.button("Zobrazit nápovědu", key="hint3"):
            st.info("""
            1. Rozdělte extrakci na logické části:
               - Hlavička (titulek, autor, datum, kategorie)
               - Obsah (odstavce, podnadpisy)
               - Tagy
            2. Použijte kombinaci metod:
               - `find()` pro jedinečné elementy
               - `find_all()` pro seznamy
               - `select()` pro složitější CSS selektory
            """)

        if st.button("Zobrazit řešení", key="solution3"):
            st.code("""
            from bs4 import BeautifulSoup

            soup = BeautifulSoup(html_article, 'html.parser')

            # Extrakce hlavičky
            title = soup.h1.text
            author = soup.find('span', class_='author').text
            date = soup.time['datetime']
            category = soup.find('span', class_='category').text

            print(f"Titulek: {title}")
            print(f"Autor: {author}")
            print(f"Datum: {date}")
            print(f"Kategorie: {category}")

            # Extrakce obsahu
            content = soup.find('div', class_='content')
            paragraphs = content.find_all('p')
            subtitles = content.find_all('h2')

            print("\\nObsah:")
            for p in paragraphs:
                print(f"Odstavec: {p.text}")

            # Extrakce tagů
            tags = soup.select('.tags li')
            print("\\nTagy:")
            for tag in tags:
                print(f"- {tag.text}")
            """, language="python")

    st.header("Úkol 4: Tabulková data")
    with st.expander("Zobrazit zadání"):
        st.markdown("""
        Extrahujte data z tabulky do strukturované podoby:
        """)

        html_table = '''
        <table class="data-table">
            <thead>
                <tr>
                    <th>Jméno</th>
                    <th>Věk</th>
                    <th>Město</th>
                    <th>Skóre</th>
                </tr>
            </thead>
            <tbody>
                <tr class="odd">
                    <td>Anna Malá</td>
                    <td>25</td>
                    <td>Praha</td>
                    <td>95</td>
                </tr>
                <tr class="even">
                    <td>Petr Velký</td>
                    <td>32</td>
                    <td>Brno</td>
                    <td>88</td>
                </tr>
                <tr class="odd">
                    <td>Eva Nová</td>
                    <td>28</td>
                    <td>Ostrava</td>
                    <td>92</td>
                </tr>
            </tbody>
        </table>
        '''

        st.code(html_table, language="html")

        if st.button("Zobrazit nápovědu", key="hint4"):
            st.info("""
            1. Nejprve získejte hlavičky sloupců z `thead`
            2. Poté zpracujte řádky z `tbody`
            3. Pro každý řádek získejte hodnoty buněk
            4. Můžete data uložit do:
               - Seznam slovníků
               - Pandas DataFrame
            5. Bonus: Ošetřete typy dat (čísla jako int)
            """)

        if st.button("Zobrazit řešení", key="solution4"):
            st.code("""
            from bs4 import BeautifulSoup
            import pandas as pd

            soup = BeautifulSoup(html_table, 'html.parser')

            # Získání hlaviček
            headers = [th.text for th in soup.find('thead').find_all('th')]

            # Získání dat
            data = []
            for row in soup.find('tbody').find_all('tr'):
                row_data = [td.text for td in row.find_all('td')]
                data.append(dict(zip(headers, row_data)))

            # Převod na DataFrame
            df = pd.DataFrame(data)

            # Konverze typů
            df['Věk'] = df['Věk'].astype(int)
            df['Skóre'] = df['Skóre'].astype(int)

            print(df)
            """, language="python")

