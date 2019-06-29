# =============================================================================
# IMPORT MODULES
# =============================================================================

from bs4 import BeautifulSoup

import requests
import json

# =============================================================================
# MAIN FUNC
# =============================================================================

def parser_frazes(start_page=1, 
                  end_page=1000, 
                  json_file_name='frazes', 
                  site_meme_descr='https://mr-mem.ru/published/feed?page='):
    
    frazes_list = []
    
    for page in range(start_page, end_page + 1):
        print('= PAGE IS {} FROM {}'.format(page, end_page))
        page_main_descr = requests.get('{}{}'.format(site_meme_descr, page), 
                                       headers = {'User-agent': 'Andy, just Andy'})
        
        page_main_descr.encoding = 'utf-8'
        soup = BeautifulSoup(page_main_descr.text, 'html.parser')
    
        for link in soup.find_all('div', class_='quote'):
            for l in link.find_all('p'):
                text = l.text
                text_split = text.split('@')
                try:
                    text_split = text_split[1]
                except IndexError:
                    break
                text_split = text_split.lstrip()
                text_split = text_split.rstrip()
                
                if text_split not in frazes_list:
                    if '\n' not in text_split:
                        text_split = text_split.lower()
                        frazes_list.append(text_split)

    print('\n= = = =\n= ALL PAGES DONE\n= = = =\n') 
    uniq_frazes_list = []
    len_fraze_list = len(frazes_list)
    
    print('\n= MAKE UNIQUE FRAZES LIST')
    i = 1
    for fraze in frazes_list:
        print('ITER IS {} FROM {}'.format(i, len_fraze_list))
        if fraze not in uniq_frazes_list:
            uniq_frazes_list.append(fraze)
        
        i += 1
    
    print('\n= = = =\n= UNIQUE LIST WAS MADE\n= = = =\n') 
    
    json.dump(uniq_frazes_list, open('../json/{}_{}.json'.format(json_file_name, end_page), 'w'))
    
    print('\n= = = =\n= JSON SAVED\n= = = =\n') 
    
    return uniq_frazes_list