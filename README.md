# 4Atro_Random_Meme_Generator

## This is random meme-generator

You need just write count of memes you want and wait time :)

### MODULES
1. BeautifulSoup
2. Selenium

### FOLDERS
1. chrome75_driver_linux_x64 — WebDriver Chrome for Selenium with Linux x64 | Ubuntu 18.02
2. examples — Just some examples
3. examples_best — Ones of the bests examples
4. json — Saved json-files with lists of frazes and meme_href's
5. parsers — Two files, wich can parse sites with meme-frazes and meme-links
6. selenium_clicker — Selenium files to use WebDriver Chrome

### How it works?
I Chose two sites:
1. mr-mem.ru — with frazes of meme
2. risovach.ru — can create meme, but need frazes

I made a parser for mr-mem.ru and get a 10'000 fraze-pages of memes
Saved it in frazes_10000.json

After then, I parse risovach.ru and get meme-links for future Selenium work
And I get 22 href-pages of memes and saved it in meme_22.json

I concatenate both of this processes in Selenium-part and with WebDriver start to making memes
