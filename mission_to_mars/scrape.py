from splinter import Browser
from bs4 import BeautifulSoup as bs
import time

def init_browser():
    executable_path = {"executable_path": "/chromedriver.exe"}
    return Browser("chrome", **executable_path)
    

def scrape():

    browser = init_browser

    dict = {}

    news_title, news_p = news()

    dict["title"] = news_title
    dict["content"] = news_p
    dict["main_image"] = image()
    dict["facts"] = facts()
    dict["hemisphere"] = hemisphere()

    browser.quit
    return dict

def news():
    browser = init_browser()

    #Visit URL
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)

    time.sleep(1)

    html = browser.html
    soup = bs(html, "html.parser")

    #news_title
    news_title = soup.find("div", class_="content_title")

    #news paragraph
    news_p = soup.find("div", class_="article_teaser_body").text

    broswer.quit()

    return news_title, news_p

def image():

    browser = init_browser()

    jpl_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"

    browser.visit(jpl_url)

    time.sleep(1)

    browser.quit()

def facts():

    broswer = init_browser()

    mars_facts_url = "https://space-facts.com/mars/"

    tables = pd.read_html(mars_facts_url)
    df = tables[0]

    df.columns = ['Fact', 'Value']
    df.set_index('Fact', inplace=True)
    html_table = df.to_html()
    html_table

    browser.quit()

    return html_table

def hemisphere():

    browser = init_browser()

    jpl_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"

    browser.visit(jpl_url)

    time.sleep(1)

    browser.quit()
