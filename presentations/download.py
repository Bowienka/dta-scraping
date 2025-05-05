import reveal_slides as rs


def get_slides():
    slides = """
    # Requests
    HTTP pro lidi

    ---
    <!-- .slide: data-background-color="#283747" -->
    ## Co je Requests?

    **Python knihovna pro snadnou práci s HTTP požadavky**

    ---
    <!-- .slide: data-background-color="#283747" -->
    ## Hlavní výhody Requests

    - Jednoduchá syntaxe 🎯
    - Automatické zpracování JSON 📦
    - Podpora sessions 🔄
    - Zpracování cookies 🍪
    - Správa hlaviček 📝

    ---

    ## Instalace a import

    ```python
    # Instalace
    pip install requests

    # Import
    import requests
    ```

    ---
    <!-- .slide: data-background-color="#285747" -->
    ### HTTP Metody

    ```python
    # GET požadavek
    requests.get('https://api.example.com/data')

    # POST požadavek
    requests.post('https://api.example.com/submit')

    # PUT požadavek
    requests.put('https://api.example.com/update')

    # DELETE požadavek
    requests.delete('https://api.example.com/remove')
    ```

    ---
    <!-- .slide: data-background-color="#285747" -->
    ### Parametry požadavku

    ```python
    # URL parametry
    params = {'key': 'value', 'search': 'python'}
    requests.get('https://api.example.com/search',
                params=params)

    # POST data
    data = {'username': 'user', 'password': 'pass'}
    requests.post('https://api.example.com/login',
                 data=data)

    # JSON data
    json_data = {'name': 'John', 'age': 30}
    requests.post('https://api.example.com/user',
                 json=json_data)
    ```

    ---

    ### Odpovědi

    **Stavový kód**     <!-- .element: class="fragment" data-fragment-index="0" -->
    ```python
    response = requests.get('https://example.com')
    print(response.status_code)  # 200
    ```
    <!-- .element: class="fragment" data-fragment-index="1" -->

    **Obsah**     <!-- .element: class="fragment" data-fragment-index="2" -->
    ```python
    print(response.text)        # Text
    print(response.json())      # JSON
    print(response.content)     # Binární data
    ```
    <!-- .element: class="fragment" data-fragment-index="3" -->

    ---

    ### Hlavičky a Cookies

    ```python
    # Vlastní hlavičky
    headers = {
        'User-Agent': 'Mozilla/5.0',
        'Accept': 'text/html'
    }
    response = requests.get(url, headers=headers)

    # Přístup k cookies
    cookies = response.cookies

    # Vlastní cookies
    cookies = {'session': '123456'}
    response = requests.get(url, cookies=cookies)
    ```

    ---

    ### Sessions

    ```python
    # Vytvoření session
    session = requests.Session()

    # Přihlášení
    session.post('https://example.com/login',
                data={'user': 'name', 'pass': '123'})

    # Další požadavky se stejnou session
    response = session.get('https://example.com/data')

    # Ukončení session
    session.close()
    ```

    ---

    ### Zpracování chyb

    ```python
    try:
        response = requests.get('https://example.com')
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Chyba: {e}")
    ```

    ---

    ### Pokročilé možnosti

    1. **Timeout**     <!-- .element: class="fragment" data-fragment-index="0" -->
    2. **Proxy**     <!-- .element: class="fragment" data-fragment-index="1" -->
    3. **Streaming**     <!-- .element: class="fragment" data-fragment-index="2" -->
    4. **SSL Verifikace**     <!-- .element: class="fragment" data-fragment-index="3" -->

    ---

    ## Časté problémy a řešení

    - **Timeout** - nastavte časový limit
    - **SSL** - ověřte certifikáty
    - **Encoding** - zkontrolujte kódování
    - **Rate limiting** - implementujte zpoždění

    ---

    ## Děkuji za pozornost

    💡 **Tip**: Dokumentace Requests je dostupná na:
    [https://requests.readthedocs.io/](https://requests.readthedocs.io/)
    """

    config = {
        "title": "Requests",
        "theme": "dracula",
        "width": 1000,
        "height": 500,
        "plugins": ["highlight", "katex", "mathjax2", "mathjax3", "notes", "search", "zoom"]
    }

    return rs.slides(slides, config=config, markdown_props={"data-separator-vertical":"^--$"}, key="foo")