import streamlit as st

st.title("Projekt: Scraping žebříčku knih")

# Zadání projektu
with st.expander("📋 Zadání projektu", expanded=True):
    st.markdown("""
    #### Cíl projektu
    Vytvořte skript, který bude stahovat data z žebříčku 100 nejlépe hodnocených knih na webu databazeknih.cz.

    #### URL stránky
    `https://www.databazeknih.cz/zebricky/100-nejlepe-hodnocenych-knih`

    #### Požadované informace pro každou knihu:
    1. Pořadí v žebříčku
    2. Název knihy
    3. Autor knihy
    4. Počet hodnocení
    5. Procento hodnocení

    #### Výstup:
    - Data uložte do JSON souboru
    - Formát: seznam objektů, kde každý objekt reprezentuje jednu knihu
    - Soubor pojmenujte `nejlepsi_knihy.json`

    #### Technické požadavky:
    - Použijte knihovnu `requests` pro stažení stránky
    - Použijte `BeautifulSoup` pro parsování HTML
    - Implementujte proper HTTP hlavičky
    - Ošetřete možné chyby
    - Přidejte komentáře vysvětlující klíčové části kódu
    """)

# Nápověda
with st.expander("💡 Nápověda"):
    st.markdown("""
    #### 1. Struktura dat
    - Knihy jsou v tabulce/seznamu na stránce
    - HTML elementy mají specifické třídy pro:
        - Pořadí knihy
        - Název knihy
        - Autora
        - Hodnocení a počet hodnocení

    #### 2. Postup řešení
    1. **Příprava requestu:**
        ```python
        headers = {
            'User-Agent': 'Mozilla/5.0...',
            'Accept': 'text/html...'
        }
        response = requests.get(url, headers=headers)
        ```

    2. **Parsování HTML:**
        ```python
        soup = BeautifulSoup(response.text, 'html.parser')
        ```

    3. **Nalezení knih:**
        - Použijte `find_all()` pro nalezení všech elementů s knihami
        - Hledejte podle třídy nebo struktury

    4. **Extrakce dat:**
        - Pro každou knihu najděte požadované informace
        - Použijte metody jako:
            - `find()`
            - `text` nebo `get_text()`
            - `strip()`

    5. **Uložení do JSON:**
        ```python
        import json

        with open('nejlepsi_knihy.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        ```

    #### 3. Užitečné tipy
    - Prozkoumejte strukturu stránky v DevTools prohlížeče
    - Ošetřete chybějící data pomocí podmínek
    - Zkontrolujte kódování textu
    - Přidejte zpoždění mezi requesty při vývoji
    - Testujte na menším vzorku dat

    #### 4. Kontrola výstupu
    - Ověřte, že JSON obsahuje všechny požadované informace
    - Zkontrolujte správnost formátu dat
    - Validujte JSON pomocí online nástrojů
    """)

st.info("""
💡 **Pro prozkoumání HTML struktury:**
1. Otevřete stránku v prohlížeči
2. Stiskněte F12 pro otevření DevTools
3. Použijte nástroj pro výběr elementů (🔍)
4. Klikněte na požadovaný element pro zobrazení jeho HTML
""")

st.warning("""
⚠️ **Nezapomeňte na:**
- Ošetření chyb při stahování
- Správné hlavičky requestu
- Kódování textu (UTF-8)
- Formátování výstupního JSONu
""")