import streamlit as st


def home():
    st.title('Web scraping')

def tools():
    st.title("Užitečné nástroje")
    st.write(
        "[Google Colab](https://colab.research.google.com/) - bezplatné webové prostředí ve stylu Jupyter notebooků, které umožňuje psát a spouštět Python kód přímo v prohlížeči s přístupem k výpočetním zdrojům včetně GPU a TPU, což je ideální zejména pro strojové učení a analýzu dat.")


def contact():
    st.title('Kontaktní informace')
    col1, col2 = st.columns(2)

    with col1:
        st.info('Luděk Reif', icon=":material/signature:")
        st.info('+420 720 116 008', icon=":material/call:")
        st.info('luipenox@gmail.com', icon=":material/mail:")
        st.info('https://www.linkedin.com/in/luipenox/', icon=":material/link:")

    with col2:
        st.image('assets/images/luipenox.jpg', width=272)


introduction = st.Page(
    "chapters/introduction.py",
    title="Úvod do webscrapingu",
    icon=":material/counter_0:")

html = st.Page(
    "chapters/html.py",
    title="HTML",
    icon=":material/counter_1:")

beautifulsoup = st.Page(
    "chapters/beautifulsoup.py",
    title="BeautifulSoup",
    icon=":material/counter_2:")

# selections = st.Page(
#     "chapters/selections.py",
#     title="Xpath a CSS selektory",
#     icon=":material/counter_3:")

download = st.Page(
    "chapters/download.py",
    title="Requests",
    icon=":material/counter_3:")

examples = st.Page(
    "chapters/examples.py",
    title="Příklady",
    icon=":material/counter_4:")

project = st.Page(
    "chapters/project.py",
    title="Projekt",
    icon=":material/counter_5:")

page_dict = {'Kapitoly': [
    introduction,
    html,
    beautifulsoup,
    # selections,
    download,
    examples,
    project,
    # api_key,
    # assignments
]}

home_page = st.Page(home, title="O kurzu", icon=":material/info:")
tools_page = st.Page(tools, title="Užitečné nástroje", icon=":material/favorite:")
contact_page = st.Page(contact, title="Kontakt", icon=":material/import_contacts:")

account_pages = [home_page, tools_page, contact_page]

pg = st.navigation({"Informace": account_pages} | page_dict)
pg.run()
