from collections import Counter
import operator
class filereader: 
    def read_movie_file(self):  # function for reading file
        movie_array = []
        with open("/home/hasher/Downloads/movie_recommendation/movie.data", "r") as f:
            for line in f:
                movie_array.append(line)
        movie_dict = {}  # creating movie dictionary for movie.data
        for i in movie_array:
            x = i.split('|')
            inner_dict = {"movie_id":x[0], "title":x[1], "date":x[2], "url":x[4], "avg_rating":"",
                         "unknown": x[5], "action":x[6], "adventure":x[7], "animation":x[8], "children":x[9],
                          "comedy":x[10], "crime":x[11], "documentary":x[12], "drama":x[13], "fantasy":x[14],
                          "Film-Noir":x[15], "Horror":x[16], "musical":x[17], "Mystery":x[18], "Romance":x[19],
                          "Sci-Fi":x[20], "Thriller":x[21], "War":x[22], "Western":x[23]}
            movie_dict[x[0]] = inner_dict
        
        return movie_dict
    def read_rating_file(self):  # function for reading rating file
        rating_array = []  # creating rating list for rating.data
        with open("/home/hasher/Downloads/movie_recommendation/ratings.data", "r") as f:
            for line in f:
                rating_array.append(line)
        rating_list = []
        for i in rating_array:

            x = i.split('\t')
            rating_list.append(x)
        return rating_list
    def most_active_movie(self, rating_list):  # function for calculating most active user
        user_id = []
        for i in rating_list:
            user_id.append(i[0])
        count = Counter(user_id)
        return list(count.most_common()[0])[0]
    
    def most_watched_movie(self, rating_list, movie_dict):  # function for calculating most watched movie
        user_id = []
        for i in rating_list:
            user_id.append(i[1])
        count = Counter(user_id)
        movie_id = (count.most_common()[0])[0]
        return movie_dict.get(movie_id)['title']          
    def most_rated_movie(self, rating_list, movie_dict):  # function for calculating most rated movie
        
        list_movie_id = []
        movie_ratings = {}
        for key in movie_dict:
            list_movie_id.append(key)
        for i in list_movie_id:
            rating_count = 0
            counter = 0
            for j in rating_list: 
                if i in j:
                    counter = float(counter + 1)
                    rating_count = (rating_count + float(j[2]))
            avg_rating = rating_count / counter       
            movie_ratings[i] = avg_rating
            movie_dict.get(i)['avg_rating'] = avg_rating
        movie_key = max(movie_ratings.iteritems(), key=operator.itemgetter(1))[0]
                
        return movie_dict.get(movie_key)['title'] 
    def rated_movie_by_year(self, movie_dict, year):  # function for calculating most rated movie by year
        movie_by_year = {}
        for key in movie_dict:
            if movie_dict.get(key)['date']:
                date = movie_dict.get(key)['date']
                date = date.split('-')
                date = date[2]
                if date == year:
                    movie_by_year[key] = movie_dict.get(key)['avg_rating']
                   
        movie_key = max(movie_by_year.iteritems(), key=operator.itemgetter(1))[0] 
        return movie_dict.get(movie_key)['title']
    def rated_movie_by_gener(self, movie_dict, genre):  # function for calculating most rated movie by genre
        movie_by_genre = {}
        for key in movie_dict:
            if movie_dict.get(key)[genre] == '1':
                movie_by_genre[key] = movie_dict.get(key)['avg_rating'] 
                
                
        movie_key = max(movie_by_genre.iteritems(), key=operator.itemgetter(1))[0] 
        return movie_dict.get(movie_key)['title'] 
    def rated_movie_by_gener_and_year(self, movie_dict, year_filter, gener_filter):  # function for calculating most rated movie by genre
        
        movie_year_filter = {}
        for key in movie_dict:
            if movie_dict.get(key)['date']:
                date = movie_dict.get(key)['date']
                date = date.split('-')
                date = date[2]
                if date == year_filter:
                    movie_year_filter[key] = movie_dict.get(key)
                
        movie_by_genre_filter = {}
        for key in  movie_year_filter:
            if movie_year_filter.get(key)[gener_filter] == '1':
                movie_by_genre_filter[key] = movie_dict.get(key)['avg_rating']             
                
        movie_key = max(movie_by_genre_filter.iteritems(), key=operator.itemgetter(1))[0] 
        return movie_dict.get(movie_key)['title']         
                
                             
     
                   
         
           
    
                         

if __name__ == "__main__":  # main function
    data_read = filereader()
    movie_dict = data_read.read_movie_file() 
    rating_list = data_read.read_rating_file()  
    most_active_user = data_read.most_active_movie(rating_list)
    most_watched_movie = data_read.most_watched_movie(rating_list, movie_dict)
    most_rated_movie = data_read.most_rated_movie(rating_list, movie_dict)
    year = raw_input("Please enter Year: ")
    genre = raw_input("Please enter genre: ")
    year_filter = raw_input("Please enter Year_filter: ")
    genre_filter = raw_input("Please enter genre_filter: ")
    most_rated_movie_by_year = data_read.rated_movie_by_year(movie_dict, year)
    rated_movie_by_gener = data_read.rated_movie_by_gener(movie_dict, genre)
    rated_movie_by_gener_and_year = data_read.rated_movie_by_gener_and_year(movie_dict, year_filter, genre_filter)

    print "Most Active User:" , most_active_user
    print "Most Watched Movie:" , most_watched_movie
    print "Most rated movie:", most_rated_movie
    print "Most rated movie by year:", most_rated_movie_by_year
    print "Most rated movie by genre and year:", rated_movie_by_gener_and_year
    
                

    
                          
                    

