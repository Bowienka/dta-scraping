import streamlit as st
import requests
from bs4 import BeautifulSoup
import time

st.title("Cvičení - Web Scraping")


# Společné funkce
def get_headers():
    return {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }


# Cvičení 1: Stažení a extrakce titulku
st.header("Cvičení 1: Extrakce titulku stránky")

with st.expander("Zobrazit zadání"):
    st.markdown("""
    **Úkol**: Napište program, který stáhne webovou stránku a vypíše její titulek (`<title>` tag).

    **Cíl**: Naučit se základní práci s requests a BeautifulSoup pro extrakci jednoduchých dat.
    """)

with st.expander("Zobrazit nápovědu"):
    st.markdown("""
    1. Použijte `requests.get()` pro stažení stránky
    2. Vytvořte BeautifulSoup objekt z `response.text`
    3. Najděte element title pomocí `soup.title`
    """)

url_title = st.text_input(
    "Zadejte URL adresu pro extrakci titulku:",
    "https://example.com"
)

if st.button("Získat titulek", key="btn_title"):
    with st.spinner("Stahuji stránku..."):
        try:
            response = requests.get(url_title, headers=get_headers(), timeout=10)
            soup = BeautifulSoup(response.text, 'html.parser')

            if soup.title:
                st.success(f"Titulek stránky: {soup.title.text.strip()}")
            else:
                st.warning("Stránka nemá titulek")

            with st.expander("Zobrazit zdrojový kód"):
                st.code("""
def get_page_title(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup.title.text.strip() if soup.title else None
""", language="python")

        except Exception as e:
            st.error(f"Chyba při stahování: {str(e)}")

# Cvičení 2: Extrakce všech odkazů
st.header("Cvičení 2: Extrakce odkazů")

with st.expander("Zobrazit zadání"):
    st.markdown("""
    **Úkol**: Vytvořte program, který stáhne stránku a vypíše seznam všech unikátních odkazů.

    **Cíl**: Naučit se pracovat s HTML atributy a zpracovávat více elementů najednou.
    """)

with st.expander("Zobrazit nápovědu"):
    st.markdown("""
    1. Použijte `find_all('a')` pro nalezení všech odkazů
    2. Pro každý odkaz získejte atribut 'href' pomocí `get()`
    3. Použijte `set()` pro odstranění duplicit
    4. Filtrujte neplatné odkazy (None, prázdné, #)
    """)

url_links = st.text_input(
    "Zadejte URL adresu pro extrakci odkazů:",
    "https://example.com"
)

if st.button("Získat odkazy", key="btn_links"):
    with st.spinner("Stahuji stránku..."):
        try:
            response = requests.get(url_links, headers=get_headers(), timeout=10)
            soup = BeautifulSoup(response.text, 'html.parser')

            links = set()
            for a in soup.find_all('a'):
                href = a.get('href')
                if href and not href.startswith('#'):
                    links.add(href)

            if links:
                st.success(f"Nalezeno {len(links)} unikátních odkazů:")
                for link in sorted(links):
                    st.write(f"- {link}")
            else:
                st.warning("Nebyly nalezeny žádné odkazy")

            with st.expander("Zobrazit zdrojový kód"):
                st.code("""
def get_all_links(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    links = set()
    for a in soup.find_all('a'):
        href = a.get('href')
        if href and not href.startswith('#'):
            links.add(href)

    return sorted(links)
""", language="python")

        except Exception as e:
            st.error(f"Chyba při stahování: {str(e)}")

st.info("""
💡 **Tipy pro scraping:**
1. Vždy používejte User-Agent hlavičky
2. Implementujte timeouty
3. Ošetřujte chyby
4. Respektujte robots.txt
5. Přidejte zpoždění mezi požadavky při scrapování více stránek
""")