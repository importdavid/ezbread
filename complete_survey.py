from selenium import webdriver
# from selenium.webdriver.common.keys import Keys

def complete_survey(code):
    # URL = 'https://marcoscsatsurvey.survey.marketforce.com/?languageId=1&sc='
    # driver = webdriver.Firefox()
    # driver.get(URL)

    # UNCOMMENT this block to run on Linux with Chrome headless, turn off above block
    URL = 'https://marcoscsatsurvey.survey.marketforce.com/?languageId=1&sc='
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get(URL)

    # First Page
    elem = driver.find_element_by_id('sc-timeofvisit')
    elem.send_keys(code[0:4])
    elem = driver.find_element_by_id('sc-storenum')
    elem.send_keys(code[4:8])
    elem = driver.find_element_by_id('sc-dateofvisit')
    elem.send_keys(code[8:16])
    elem = driver.find_element_by_id('sc-ordernumber')
    elem.send_keys(code[16:20])
    start = driver.find_element_by_id('startButton')
    start.click()

    # Next Page
    begin = driver.find_element_by_css_selector('.ui-btn > input:nth-child(1)')
    begin.click()

    # Next Page
    # First two groups of radio buttons
    # Answers here will alter appearance of 'How long did you wait' question later
    for group in driver.find_elements_by_css_selector('div.ui-controlgroup-controls ')[0:2]:
        radio = group.find_elements_by_css_selector('div.ui-radio')[0]
        radio.click()
    next = driver.find_element_by_css_selector('div.ui-btn:nth-child(2) > input:nth-child(1)')
    next.click()

    # Next Page
    elem = driver.find_element_by_css_selector('label.ui-last-child')
    elem.click()
    next = driver.find_element_by_css_selector('div.ui-btn:nth-child(2) > input:nth-child(1)')
    next.click()
    # Popup created, verify
    #confirm = driver.find_element_by_id('scaleConfirmed')
    confirm = driver.find_element_by_css_selector('.ui-simpledialog-container > nav:nth-child(2) > div:nth-child(1) > div:nth-child(1) > a:nth-child(1)')
    confirm.click()

    # Next Page
    # Ordered CheezyBread only, to simplify survey, second box
    cheezybread = driver.find_elements_by_css_selector('div.ui-checkbox')[1]
    cheezybread.click()
    next = driver.find_element_by_css_selector('div.ui-btn:nth-child(2) > input:nth-child(1)')
    next.click()

    # Next Page
    # 'Please rate your satisfaction with...'
    body = driver.find_element_by_css_selector('tbody')
    for row in body.find_elements_by_css_selector('tr'):
        radio = row.find_elements_by_css_selector('div.ui-radio')[-1]
        radio.click()
    next = driver.find_element_by_css_selector('div.ui-btn:nth-child(2) > input:nth-child(1)')
    next.click()

    # Next Page
    # 'Please rate your satisfaction with...'
    body = driver.find_element_by_css_selector('tbody')
    for row in body.find_elements_by_css_selector('tr'):
        radio = row.find_elements_by_css_selector('div.ui-radio')[-1]
        radio.click()
    next = driver.find_element_by_css_selector('div.ui-btn:nth-child(2) > input:nth-child(1)')
    next.click()

    # Next Page
    # 'Please rate your satisfaction with...'
    body = driver.find_element_by_css_selector('tbody')
    for row in body.find_elements_by_css_selector('tr'):
        radio = row.find_elements_by_css_selector('div.ui-radio')[-1]
        radio.click()
    next = driver.find_element_by_css_selector('div.ui-btn:nth-child(2) > input:nth-child(1)')
    next.click()

    # Next Page
    # 'Did you have any problems with your purchase?'
    no = driver.find_element_by_css_selector('label.ui-last-child')
    no.click()
    next = driver.find_element_by_css_selector('div.ui-btn:nth-child(2) > input:nth-child(1)')
    next.click()

    # Next Page
    # 'Based on this visit, what is the likelihood that you will…'
    body = driver.find_element_by_css_selector('tbody')
    for row in body.find_elements_by_css_selector('tr'):
        radio = row.find_elements_by_css_selector('div.ui-radio')[-1]
        radio.click()
    next = driver.find_element_by_css_selector('div.ui-btn:nth-child(2) > input:nth-child(1)')
    next.click()

    # Next Page
    # 'Please tell us in three or more sentences why you were Extremely Satisfied with your Marco's Pizza experience.'
    next = driver.find_element_by_css_selector('div.ui-btn:nth-child(2) > input:nth-child(1)')
    next.click()

    # Next Page
    # 'Please indicate Yes or No to the following.'
    body = driver.find_element_by_css_selector('tbody')
    finalRowComplete = False
    for row in body.find_elements_by_css_selector('tr')[::-1]:
        if finalRowComplete:
            radio = row.find_elements_by_css_selector('div.ui-radio')[0]
            radio.click()
        else:
            radio = row.find_elements_by_css_selector('div.ui-radio')[1]
            radio.click()
            finalRowComplete = True
    next = driver.find_element_by_css_selector('div.ui-btn:nth-child(2) > input:nth-child(1)')
    next.click()

    # Next Page
    # 'How long did it take for you to receive your order after having placed it?'
    # This question does not appear when "dine-in" option is chosen on page 3
    tentotwenty = driver.find_elements_by_css_selector('div.ui-radio')[1]
    tentotwenty.click()
    next = driver.find_element_by_css_selector('div.ui-btn:nth-child(2) > input:nth-child(1)')
    next.click()

    # Next Page
    # 'Please select your primary reasons for visiting this Marco's Pizza.'
    convenience = driver.find_elements_by_css_selector('div.ui-checkbox')[0]
    convenience.click()
    next = driver.find_element_by_css_selector('div.ui-btn:nth-child(2) > input:nth-child(1)')
    next.click()

    # Next Page
    # 'Which of the following Marco's Pizza advertisements have you seen or heard in the past 30 days?'
    choices = driver.find_elements_by_css_selector('div.ui-checkbox')
    choices[1].click() # Print
    choices[5].click() # Email
    next = driver.find_element_by_css_selector('div.ui-btn:nth-child(2) > input:nth-child(1)')
    next.click()

    # Next Page
    # 'Based on the advertising I saw or heard, this Marco's Pizza experience met my expectations.'
    rating = driver.find_elements_by_css_selector('div.ui-radio')[-1]
    rating.click()
    next = driver.find_element_by_css_selector('div.ui-btn:nth-child(2) > input:nth-child(1)')
    next.click()

    # Next Page
    # Two groups of radio buttons
    for group in driver.find_elements_by_css_selector('div.ui-controlgroup-controls ')[0:2]:
        radio = group.find_elements_by_css_selector('div.ui-radio')[0]
        radio.click()
    next = driver.find_element_by_css_selector('div.ui-btn:nth-child(2) > input:nth-child(1)')
    next.click()

    # Next Page
    # 'Was this your first time ordering from Marco's Pizza?'
    no = driver.find_elements_by_css_selector('div.ui-radio')[1]
    no.click()
    next = driver.find_element_by_css_selector('div.ui-btn:nth-child(2) > input:nth-child(1)')
    next.click()

    # Next Page
    # 'Have you ordered dine-in, carryout, or delivery from any other pizza delivery restaurants in the past 30 days?'
    no = driver.find_elements_by_css_selector('div.ui-radio')[1]
    no.click()
    next = driver.find_element_by_css_selector('div.ui-btn:nth-child(2) > input:nth-child(1)')
    next.click()

    # Next Page
    # Four groups of radio buttons
    # "Prefer not to answer" for each choice
    for group in driver.find_elements_by_css_selector('div.ui-controlgroup-controls ')[0:4]:
        radio = group.find_elements_by_css_selector('div.ui-radio')[-1]
        radio.click()
    next = driver.find_element_by_css_selector('div.ui-btn:nth-child(2) > input:nth-child(1)')
    next.click()

    # Final Page
    coupon = driver.find_element_by_css_selector('.main-content > section:nth-child(1) > h2:nth-child(1) > p:nth-child(1) > span:nth-child(7) > span:nth-child(1)')
    coupon = coupon.text
    tellcode = driver.find_element_by_css_selector('.main-content > section:nth-child(1) > h2:nth-child(1) > p:nth-child(2) > span:nth-child(2) > span:nth-child(1)')
    tellcode = tellcode.text
    print(coupon)
    print(f'TellCode: {tellcode}')
    driver.close()

    return coupon, tellcode


if __name__ == '__main__':
    code = input('Enter coupon code (i.e. 18281052201912060565): ')
    complete_survey(code)