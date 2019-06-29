# =============================================================================
# IMPORT MUDULES
# =============================================================================

from bs4 import BeautifulSoup
import requests
import json

# =============================================================================
# MAIN FUNC
# =============================================================================

def parser_img(start_page=1, 
               end_page=22, 
               site_meme_img='http://risovach.ru/mem-generators/', 
               site_meme_img_main='http://risovach.ru/', 
               file_img='meme'):    
    
    href_list = []

    for pg in range(start_page, end_page + 1):
        if pg == 1:
            page = ''
        else:
            page = str(pg)
            
        print('= PAGE IS {} FROM {}'.format(pg, end_page))
    
        page_main_img = requests.get('{}{}'.format(site_meme_img, page), headers = {'User-agent': 'Andy, just Andy'})
        soup = BeautifulSoup(page_main_img.text, 'html.parser')
        squares = soup.find_all('div', class_='square')
        
        for sq in squares:
            a_tag = sq.find('a')
            href = a_tag['href']
            href = href[1:]
            href_list.append('{}{}'.format(site_meme_img_main, href))
            
    unique_href_list = []

    for hr in href_list:
        if hr not in unique_href_list:
            unique_href_list.append(hr)
            
    json.dump(unique_href_list, open('../json/{}_{}.json'.format(file_img, end_page), 'w'))
    
    return unique_href_list