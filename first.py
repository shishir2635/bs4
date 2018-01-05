from bs4 import BeautifulSoup #this module works upon scraping of the data
import requests #this module requests the data from the page

page = requests.get('http://www.imdb.com/india/top-rated-indian-movies/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=2730173942&pf_rd_r=11ZDVRWYNW8KFBTBJMV5&pf_rd_s=right-4&pf_rd_t=15061&pf_rd_i=homepage&ref_=hm_india_tr_rhs_1')

soup = BeautifulSoup(page.text,'html.parser') #main soup

movie_list = soup.find_all('td',class_='titleColumn') # contain all the movies in the 1. skj(100) form

year_list = list() #list of all year of the movies
movie_list_filter = list() #contain all the movies name modified form

for i in range(len(movie_list)):
	movie_name_com = movie_list[i].get_text() # 1. Ysbdhs(1998)
	mn_len = len(movie_name_com.split()) # ['1.' , 'Ysbdhs','(1998)']
	year = movie_name_com.split()[mn_len-1].strip('()')	#1998 
	movie_name = movie_name_com.split()[1:mn_len-1] # ['ysbdhs']
	movie_list_filter.append(movie_name) 

	year_list.append(year)

input_filter_year = int(input('Please Enter Filter Year : '))

year_filter = input_filter_year #give the filter here
new_count = 0
match_count = 0
filter_list = list() #contain all the list of the movies according to the filter

for x in range(len(year_list)):
	if int(year_list[x]) >= year_filter:
		new_count += 1
	else:
		pass

	if int(year_list[x]) == year_filter:
		match_count += 1
		filter_list.append(movie_list_filter[x])

final_movie_filter_list = list()

def movie_name_defination():
	for i in range(len(filter_list)):
		text = ''
		final_filter = filter_list[i]
		for z in range(len(final_filter)):
			text += " " + final_filter[z]

		final_movie_filter_list.append(text)

	print("")
	
	for mo_name in range(len(final_movie_filter_list)):
		print(final_movie_filter_list[mo_name]) 

	print("")


print('Movies above {0} the list are : {1} movies which accounts for {2} %'.format(input_filter_year ,new_count ,(new_count/len(year_list))*100))
print('No. of movies in year {0} are : {1}'.format(input_filter_year,match_count))
movie_name_defination()





 	
