import streamlit as st
import requests
import time

st.title("Úvod do knihovny Requests")

st.header("Stahování webových stránek")
st.write("""
Knihovna Requests je nejpoužívanější Python knihovnou pro stahování webových stránek. 
Pro začátek si vystačíme s metodou `GET`, která slouží k získání obsahu stránky.
""")

st.subheader("1. Instalace a import")
st.code("""
# Instalace přes pip
pip install requests

# Import v Python kódu
import requests
""", language="python")

st.subheader("2. Základní použití")
url_input = st.text_input(
    "Zadejte URL adresu k otestování:",
    "https://example.com"
)

if st.button("Stáhnout stránku"):
    try:
        response = requests.get(url_input)

        st.success(f"Stránka úspěšně stažena! (Status kód: {response.status_code})")

        with st.expander("Zobrazit hlavičky odpovědi"):
            st.json(dict(response.headers))

        with st.expander("Zobrazit HTML kód"):
            st.code(response.text[:1000] + "...", language="html")

    except requests.RequestException as e:
        st.error(f"Chyba při stahování: {str(e)}")

st.subheader("3. Praktický kód")
st.code("""
import requests

def stahni_stranku(url):
    try:
        # Přidání User-Agent hlavičky
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }

        # Stažení stránky s timeoutem
        response = requests.get(url, headers=headers, timeout=10)

        # Kontrola úspěšnosti
        response.raise_for_status()

        # Nastavení správného kódování
        response.encoding = response.apparent_encoding

        return response.text

    except requests.RequestException as e:
        print(f"Chyba při stahování: {e}")
        return None
""", language="python")

st.subheader("4. Pokročilejší příklad")
st.write("""
Při scrapingu více stránek je důležité:
1. Používat správné hlavičky
2. Implementovat zpoždění mezi požadavky
3. Ošetřovat chyby
""")

st.code("""
import requests
import time

def stahni_vice_stranek(urls):
    # Nastavení hlaviček
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
        'Accept': 'text/html,application/xhtml+xml',
        'Accept-Language': 'cs,en-US;q=0.7,en;q=0.3'
    }

    vysledky = []

    for url in urls:
        try:
            # Stažení stránky
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()

            # Přidání výsledku
            vysledky.append({
                'url': url,
                'status': response.status_code,
                'content': response.text
            })

            # Zpoždění mezi požadavky
            time.sleep(1)

        except requests.RequestException as e:
            print(f"Chyba při stahování {url}: {e}")
            continue

    return vysledky
""", language="python")

st.subheader("5. Demo s více stránkami")
urls_demo = st.text_area(
    "Zadejte URL adresy (jedna na řádek):",
    "https://example.com\nhttps://httpbin.org/get"
)

if st.button("Stáhnout více stránek"):
    urls = [url.strip() for url in urls_demo.split('\n') if url.strip()]

    progress_bar = st.progress(0)
    status_text = st.empty()

    results = []
    for i, url in enumerate(urls):
        try:
            status_text.write(f"Stahuji {url}...")
            response = requests.get(url, timeout=10)
            results.append({
                'url': url,
                'status': response.status_code,
                'length': len(response.text)
            })
            time.sleep(1)  # Zpoždění mezi požadavky

            # Aktualizace progress baru
            progress_bar.progress((i + 1) / len(urls))

        except requests.RequestException as e:
            results.append({
                'url': url,
                'status': 'ERROR',
                'error': str(e)
            })

    status_text.write("Stahování dokončeno!")
    st.write("Výsledky:")
    st.table(results)

st.info("""
💡 **Tipy pro stahování stránek:**
1. Vždy přidávejte User-Agent hlavičku
2. Implementujte timeouty
3. Používejte zpoždění mezi požadavky
4. Ošetřujte chyby a výjimky
5. Respektujte robots.txt
""")

st.warning("""
⚠️ **Časté problémy:**
1. Blokování IP adresy při příliš častých požadavcích
2. Problémy s SSL certifikáty
3. Timeouty při pomalém připojení
4. Nesprávné kódování textu
""")