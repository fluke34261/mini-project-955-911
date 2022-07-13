library(rvest)
library(dplyr)
library(stringr)

pg = read_html('web1.html')

tag <- pg %>% html_nodes(xpath='//img[@class="image"]') %>% html_attr('src')
for (blob in 1:length(tag)) {
  #error missng url coz start with blob instead of  http
  download.file(tag[blob], sprintf("img_%s.jpg", blob))
}

