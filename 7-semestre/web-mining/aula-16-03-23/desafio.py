from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Lucas da Silva Santos 1904209
# Larissa Yonaha 1903166
# Arthur Vinicius Santos Silva 1903665

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

navegador = webdriver.Chrome(service=Service(ChromeDriverManager().install()), chrome_options=chrome_options)
navegador.get('http://www.ssp.sp.gov.br/transparenciassp/')

navegador.find_element(By.ID, 'cphBody_btnRouboVeiculo').click()

navegador.find_element(By.XPATH, '//*[@id="cphBody_lkAno22"]').click()

for i in range(1, 13):
    item_mes = f'//*[@id="cphBody_lkMes{i}"]'
    print("mes  --------------------------- " + item_mes)
   
    try:
        navegador.find_element(By.XPATH, item_mes).click()
        botao_exportar = WebDriverWait(navegador, 6000).until(EC.presence_of_element_located((By.XPATH, '//*[@id="cphBody_ExportarBOLink"]')))
    finally:
        botao_exportar.click()
        print("cabô")