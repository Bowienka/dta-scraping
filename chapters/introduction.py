import streamlit as st
from presentations.introductions import get_slides


st.title("Úvod do Web Scrapingu")
presentation, text = st.tabs(["Prezentace", "Studijní text"])

with presentation:
    get_slides()

with text:
    st.header("Co je web scraping?")
    st.write("""
    Web scraping je technika automatizovaného získávání dat z webových stránek. Umožňuje efektivně extrahovat 
    informace z HTML kódu a zpracovat je do strukturované podoby.
    """)

    st.header("Základní technologie")

    st.subheader("1. HTML - Základ webových stránek")
    st.write("""
    HTML (HyperText Markup Language) tvoří strukturu webových stránek:
    - Definuje elementy stránky (nadpisy, odstavce, odkazy...)
    - Určuje hierarchii obsahu
    - Poskytuje metadata o stránce
    """)

    st.subheader("2. CSS - Vzhled a selektory")
    st.write("""
    CSS (Cascading Style Sheets) kromě stylování nabízí:
    - Způsob identifikace elementů pomocí selektorů
    - Hierarchické vyhledávání elementů
    - Filtrování podle tříd a ID
    """)

    st.header("Nástroje pro web scraping")

    st.write("""
    V Pythonu máme k dispozici několik základních knihoven:
    
    📥 **Stahování stránek**
    - **Requests** - základní HTTP požadavky
    - Selenium - pro dynamické stránky
    - aiohttp - asynchronní stahování
    
    🔍 **Parsování HTML**
    - **BeautifulSoup** - jednoduchý a populární parser
    - lxml - rychlý XML/HTML parser
    - html5lib - nejpřesnější HTML parser
    
    🤖 **Komplexní řešení**
    - Scrapy - framework pro škálovatelný scraping
    - Playwright - automatizace prohlížeče
    - Puppeteer - Node.js nástroj pro Chrome
    """)

    st.header("Etické aspekty")
    st.warning("""
    ⚠️ Při scrapingu je nutné:
    1. Neposílat příliš mnoho požadavků
    2. Dodržovat podmínky použití webu
    3. Chránit osobní údaje
    """)

    st.header("Tipy pro začátek")
    st.info("""
    💡 **Doporučený postup:**
    1. Prozkoumejte strukturu stránky v DevTools
    2. Identifikujte klíčové elementy
    3. Začněte s jednoduchými statickými stránkami
    4. Postupně přidávejte pokročilejší funkce
    5. Vždy ošetřujte chybové stavy
    """)

    st.success("""
    ✨ **Výhody web scrapingu:**
    - Automatizace sběru dat
    - Monitoring konkurence
    - Analýza trhu
    - Agregace obsahu
    - Výzkum a analýza
    """)