# =============================================================================
# IMPORT MODULES
# =============================================================================

from selenium import webdriver

import json
import random as rnd

import time

# =============================================================================
# MAIN FUNC
# =============================================================================

def make_meme(count_meme=5, 
                     meme_file='meme_22', 
                     fraze_file='frazes_10000'):
    
    driver = webdriver.Chrome(executable_path='../chrome75_driver_linux_x64/chromedriver')
    
    meme_list = json.load(open('../json/{}.json'.format(meme_file), 'r'))   
    fraze_list = json.load(open('../json/{}.json'.format(fraze_file), 'r'))
    
    for i in range(count_meme):
        
        meme_rnd = rnd.randint(1, len(meme_list))
        
        fraze_rnd_first = rnd.randint(1, len(fraze_list))
        fraze_rnd_second = rnd.randint(1, len(fraze_list))
        
        one_half_rnd = rnd.randint(0, 1)
        
        driver.get('{}'.format(meme_list[meme_rnd]))
        
        if one_half_rnd == 1:
            driver.find_element_by_name('zdata1').click()
            driver.find_element_by_name('zdata1').send_keys('{}'.format(fraze_list[fraze_rnd_first]))
    
        driver.find_element_by_name('zdata2').click()
        driver.find_element_by_name('zdata2').send_keys('{}'.format(fraze_list[fraze_rnd_second]))
    
        driver.find_element_by_name('download').click()
        
        print('= MEME {} WAS MADE'.format(i+1))
        
        time.sleep(1)
        
    driver.close()