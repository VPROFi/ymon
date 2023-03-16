#!/usr/bin/env python3
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from parsedb import urls
import os, shutil, html

service = Service(executable_path="./chromedriver")

options = webdriver.ChromeOptions()
options.add_argument('--disable-notifications')
options.add_argument("headless")
options.add_argument("--window-size=1920x1080");
options.add_argument("start-maximized")
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")
options.add_argument("--disable-gpu")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--no-sandbox")

driver = webdriver.Chrome(service=service, options=options)
driver.maximize_window()
if os.path.exists('./img'):
    shutil.rmtree('./img')
os.mkdir('./img')

htmlf = open("index.html","wt")
htmlf.write("""
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" lang="en"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<head>
<style>
.collapsible {
  background-color: #777;
  color: white;
  cursor: pointer;
  padding: 18px;
  width: 100%;
  border: none;
  text-align: left;
  outline: none;
  font-size: 15px;
}

.active, .collapsible:hover {
  background-color: #555;
}

.content {
  padding: 0 18px;
  display: none;
  overflow: hidden;
  background-color: #f1f1f1;
}

.container {
  position: relative;
  width: 100%;
  overflow: hidden;
  padding-top: 60%; /* 1:1 Aspect Ratio */
}

.responsive-iframe {
  position: absolute;
  top: 0;
  left: 0;
  bottom: 0;
  right: 0;
  width: 100%;
  height: 100%;
  border: none;
}

* {
  box-sizing: border-box;
}

/* Create four equal columns that floats next to each other */
.column {
  float: left;
  width: 33%;
  height: 350px;
  padding: 5px;
}

/* Clear floats after the columns */
.row:after {
  content: "";
  display: table;
  clear: both;
}

img {
    object-fit: contain;
    width: 100%;
}

</style>
</head><body>
<h1 style="text-align: center;">Youtube</h1>
""")

new = []

for num, item in enumerate(urls):
    driver.get(item)

    title = driver.title
    driver.implicitly_wait(0.5)

    try:
        ytb_link = WebDriverWait(driver, timeout=3).until(lambda d: d.find_element(by=By.ID, value="video-title-link")).get_attribute('href')
        message = WebDriverWait(driver, timeout=3).until(lambda d: d.find_element(by=By.ID, value="video-title"))
        chname = WebDriverWait(driver, timeout=3).until(lambda d: d.find_element(by=By.ID, value="text"))
        value = message.text
        print(num+1, str(value), str(ytb_link))
        if urls[item][0] != ytb_link:
            png = WebDriverWait(driver, timeout=3).until(lambda d: d.find_element(by=By.TAG_NAME, value="ytd-rich-item-renderer"))
            element_png = png.screenshot_as_png
            screenshot = f"./img/{num}screenshot.png"
            driver.save_screenshot(screenshot)
            with open(f"./img/{num}screen.png", "wb") as file:
                file.write(element_png)
                screen = f"./img/{num}screen.png"
                valuehtml = html.escape(value)
                chnamehtml = html.escape(chname.text)
                ytb_link_emb = ytb_link.replace('watch?v=','embed/')
                htmlf.write(f"""
         <div class="row">

             <div class="column" style="background-color:#aaa;width:20%;">
                 <a href="{ytb_link}" rel="nofollow noopener" target="_blank"><img src="{screen}" height="300px"></a>
                 <div style="text-align: center;">
                     <a href="{ytb_link}" rel="nofollow noopener" target="_blank"><strong>{valuehtml}</strong></a>
                 </div>
             </div>

             <div class="column" style="background-color:#bbb;width:30%;">
                 <div class="container"> 
                      <iframe class="responsive-iframe" src="{ytb_link_emb}"></iframe>
                 </div>
             </div>

             <div class="column" style="background-color:#ccc;width:50%;">
                 <a href="{item}"><img src="{screenshot}"height="340px"></a>
             </div>

         </div>
         <div>
                <small>
                    <em>
                        <button type="button" class="collapsible">{chnamehtml}</button>
                        <div class="content">
                            <a href="{item}"><img src="{screenshot}"></a>
                        </div>
                        <a rel="nofollow noopener" target="_blank" href="{item}">{chnamehtml}</a>
                    </em>
                </small>
         </div>
            """)
            new.append(ytb_link)
        urls[item] = (ytb_link,value)
    except:
        pass
with open("parsedb.py","wt") as f:
    f.write("urls = " + str(urls).replace("'), '", "'),\n        '") + "\n")
with open("sites.new","wt") as f:
    f.write("""#!/bin/bash
/usr/bin/google-chrome-stable """)
    f.write(" ".join(new))
    f.write("\n")

os.system('chmod +x sites.new')

htmlf.write("""
<script>
var coll = document.getElementsByClassName("collapsible");
var i;

for (i = 0; i < coll.length; i++) {
  coll[i].addEventListener("click", function() {
    this.classList.toggle("active");
    var content = this.nextElementSibling;
    if (content.style.display === "block") {
      content.style.display = "none";
    } else {
      content.style.display = "block";
    }
  });
}
</script>
</body></html>
""")

htmlf.close()
driver.quit()
