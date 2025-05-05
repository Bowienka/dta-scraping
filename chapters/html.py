import streamlit as st

from presentations.html import get_slides



st.title("Úvod do HTML")

presentation, text = st.tabs(["Prezentace", "Studijní text"])

with presentation:
    get_slides()

with text:
    st.header("Co je HTML?")
    st.write("""
        HTML (HyperText Markup Language) je značkovací jazyk používaný pro tvorbu webových stránek. 
        Definuje strukturu webového dokumentu pomocí značek (tagů), které určují, jak se má obsah zobrazit v prohlížeči.

        HTML je základním stavebním kamenem webových stránek a společně s CSS (pro styling) a JavaScriptem (pro interaktivitu)
        tvoří základní technologie pro tvorbu webu.
    """)

    st.header("Základní struktura HTML dokumentu")
    st.code("""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>Název stránky</title>
    </head>
    <body>
        <h1>Hlavní nadpis</h1>
        <p>Obsah stránky</p>
    </body>
    </html>
    """, language="html")

    st.header("Nejdůležitější HTML značky")
    st.markdown("""
    📝 **Textové elementy**
    - `<h1>` až `<h6>` - nadpisy
    - `<p>` - odstavec
    - `<span>` - inline text
    - `<strong>` - tučný text
    - `<em>` - kurzíva

    🎯 **Strukturální elementy**
    - `<div>` - blokový element pro rozdělení obsahu
    - `<header>` - hlavička stránky/sekce
    - `<nav>` - navigace
    - `<main>` - hlavní obsah
    - `<footer>` - patička

    📋 **Seznamy**
    - `<ul>` - nečíslovaný seznam
    - `<ol>` - číslovaný seznam
    - `<li>` - položka seznamu

    🔗 **Odkazy a obrázky**
    - `<a>` - odkaz
    - `<img>` - obrázek
    """)

    st.header("Atributy HTML elementů")
    st.write("""
    Atributy poskytují elementům dodatečné informace nebo vlastnosti:
    """)
    st.code("""
    <a href="https://www.example.com" target="_blank">Odkaz</a>
    <img src="obrazek.jpg" alt="Popis obrázku" width="300" height="200">
    <div class="container" id="hlavni">Obsah</div>
    """, language="html")

    st.write("""
    Nejčastější atributy:
    - `class` - CSS třída pro styling
    - `id` - unikátní identifikátor elementu
    - `href` - URL odkazu
    - `src` - zdroj obrázku nebo skriptu
    - `alt` - alternativní text pro obrázky
    - `style` - inline CSS styly
    """)

    st.header("Formuláře v HTML")
    st.code("""
    <form action="/odeslat" method="POST">
        <label for="jmeno">Jméno:</label>
        <input type="text" id="jmeno" name="jmeno" required>

        <label for="email">Email:</label>
        <input type="email" id="email" name="email">

        <input type="submit" value="Odeslat">
    </form>
    """, language="html")

    st.write("""
    Typy vstupních polí (`<input type="...">`):
    - text - textové pole
    - email - emailová adresa
    - password - heslo
    - number - číslo
    - checkbox - zaškrtávací pole
    - radio - přepínač
    - file - nahrání souboru
    """)

    st.header("Sémantický HTML")
    st.info("""
    💡 **Tip**: Sémantický HTML kód používá značky, které jasně popisují svůj význam a účel.
    To zlepšuje přístupnost, SEO a udržitelnost kódu.
    """)

    st.code("""
    <header>
        <nav>
            <ul>
                <li><a href="#home">Domů</a></li>
                <li><a href="#about">O nás</a></li>
            </ul>
        </nav>
    </header>
    <main>
        <article>
            <h1>Hlavní článek</h1>
            <p>Obsah článku...</p>
        </article>
        <aside>
            <h2>Související obsah</h2>
            <p>Doplňující informace...</p>
        </aside>
    </main>
    <footer>
        <p>&copy; 2024 Moje stránka</p>
    </footer>
    """, language="html")

    st.warning("""
    ⚠️ **Pozor**: Při tvorbě HTML dokumentů je důležité:
    - Používat správnou strukturu dokumentu
    - Dodržovat sémantiku značek
    - Zajistit přístupnost pro všechny uživatele
    - Validovat kód pomocí W3C validátoru
    """)