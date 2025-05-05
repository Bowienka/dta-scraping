import streamlit as st
from presentations.selections import get_slides

st.title("XPath a CSS Selektory")

presentation, text = st.tabs(["Prezentace", "Studijní text"])

with presentation:
    get_slides()

with text:
    st.header("CSS Selektory")
    st.write("""
    CSS selektory jsou způsob, jak vybrat HTML elementy na základě jejich vlastností.
    Jsou primárně používány pro stylování webových stránek, ale jsou také velmi užitečné pro web scraping.
    """)

    st.subheader("Základní CSS selektory")
    st.markdown("""
    🏷️ **Základní selektory**
    - `element` - výběr podle typu elementu (např. `p`, `div`)
    - `.trida` - výběr podle třídy
    - `#id` - výběr podle ID
    - `[atribut=hodnota]` - výběr podle atributu

    🔗 **Kombinátory**
    - `mezera` - potomek (kdekoliv uvnitř)
    - `>` - přímý potomek
    - `+` - následující sourozenec
    - `~` - všichni následující sourozenci

    🎯 **Pseudo-třídy**
    - `:first-child` - první potomek
    - `:last-child` - poslední potomek
    - `:nth-child(n)` - n-tý potomek
    - `:hover` - element při najetí myší
    """)

    st.header("XPath")
    st.write("""
    XPath je jazyk pro navigaci v XML dokumentech, který lze použít i pro HTML.
    Nabízí více možností než CSS selektory, ale má složitější syntaxi.
    """)

    st.subheader("Základní koncepty XPath")
    st.markdown("""
    🛣️ **Cesty**
    - `/` - absolutní cesta od kořene
    - `//` - relativní cesta (kdekoliv v dokumentu)
    - `.` - aktuální uzel
    - `..` - rodičovský uzel

    🎯 **Predikáty**
    - `[]` - podmínky pro výběr uzlů
    - `@` - reference na atribut

    🌳 **Osy**
    - `ancestor` - předci
    - `descendant` - potomci
    - `following-sibling` - následující sourozenci
    - `preceding-sibling` - předchozí sourozenci
    """)

    st.header("Praktické příklady")

    st.subheader("HTML struktura")
    st.code("""
    <div class="container">
        <nav>
            <ul class="menu">
                <li><a href="#home">Domů</a></li>
                <li><a href="#about">O nás</a></li>
            </ul>
        </nav>
        <main>
            <article id="hlavni">
                <h1>Hlavní článek</h1>
                <p class="text">První odstavec</p>
                <p class="text highlight">Druhý odstavec</p>
            </article>
            <aside>
                <h2>Boční panel</h2>
                <p>Doplňující informace</p>
            </aside>
        </main>
    </div>
    """, language="html")

    st.subheader("CSS Selektory")
    st.code("""
    /* Všechny odkazy v menu */
    .menu a

    /* První odstavec v článku */
    #hlavni p:first-child

    /* Odstavce s oběma třídami */
    p.text.highlight

    /* Nadpisy h2 v bočním panelu */
    aside h2
    """, language="css")

    st.subheader("XPath Selektory")
    st.code("""
    # Všechny odkazy v menu
    //ul[@class='menu']//a

    # První odstavec v článku
    //article[@id='hlavni']/p[1]

    # Odstavce s třídou text a highlight
    //p[@class='text highlight']

    # Nadpisy h2 v bočním panelu
    //aside/h2
    """, language="xpath")

    st.header("Pokročilé techniky")

    st.subheader("CSS")
    st.code("""
    /* Sudé položky seznamu */
    li:nth-child(2n)

    /* Element obsahující text */
    [title*="hledaný text"]

    /* První písmeno */
    p::first-letter

    /* Prázdné elementy */
    p:empty
    """, language="css")

    st.subheader("XPath")
    st.code("""
    # Elementy obsahující text
    //p[contains(text(), 'hledaný text')]

    # Poslední element svého typu
    //p[last()]

    # Element s více podmínkami
    //p[@class='text' and contains(@id, 'hlavni')]

    # Předchozí sourozenec
    //p/preceding-sibling::h1
    """, language="xpath")

    st.info("""
    💡 **Tip**: Pro testování CSS selektorů v prohlížeči použijte:
    ```javascript
    document.querySelector('.selektor')  // první nalezený
    document.querySelectorAll('.selektor')  // všechny nalezené
    ```
    """)

    st.warning("""
    ⚠️ **Časté problémy**:
    1. **Příliš specifické selektory** - mohou se snadno rozbít při změně struktury
    2. **Nedostatečně specifické selektory** - mohou vybrat nechtěné elementy
    3. **Dynamický obsah** - selektory nefungují na dynamicky generovaný obsah
    4. **Výkon** - složité selektory mohou být pomalé na velkých dokumentech
    """)

    st.header("Kdy použít který selektor?")
    st.markdown("""
    **CSS Selektory**
    - ✅ Jednoduchá navigace v dokumentu
    - ✅ Výběr elementů podle tříd a ID
    - ✅ Základní filtrování elementů
    - ❌ Pohyb nahoru ve struktuře
    - ❌ Složité podmínky

    **XPath**
    - ✅ Komplexní navigace v dokumentu
    - ✅ Pohyb nahoru ve struktuře
    - ✅ Složité podmínky a filtry
    - ❌ Složitější syntaxe
    - ❌ Může být pomalejší
    """)