import media
import fresh_tomatoes

dark_night = media.Movie("The Dark Knight Rises", "Bane, an imposing terrorist, attacks Gotham City and disrupts its eight-year-long period of peace.","https://upload.wikimedia.org/wikipedia/en/8/83/Dark_knight_rises_poster.jpg", "https://www.youtube.com/watch?v=g8evyE9TuYk")
titanic = media.Movie("Titanic", " A fictionalized account of the sinking of the RMS Titanic", "https://upload.wikimedia.org/wikipedia/en/2/22/Titanic_poster.jpg", "https://www.youtube.com/watch?v=ZQ6klONCq4s")
avengers = media.Movie("The Avengers", "The Asgardian Loki encounters the Other, the leader of an extraterrestrial race known as the Chitauri", "https://upload.wikimedia.org/wikipedia/en/f/f9/TheAvengers2012Poster.jpg", "https://www.youtube.com/watch?v=eOrNdBpGMv8")
inside_out = media.Movie("Inside Out", "The film is set in the mind of a young girl named Riley Andersen", "https://upload.wikimedia.org/wikipedia/en/0/0a/Inside_Out_%282015_film%29_poster.jpg", "https://www.youtube.com/watch?v=seMwpP0yeu4")
shwashank_redemption = media.Movie("The Shawshank Redemption", "The film tells the story of Andy Dufresne", "https://upload.wikimedia.org/wikipedia/en/8/81/ShawshankRedemptionMoviePoster.jpg", "https://www.youtube.com/watch?v=6hB3S9bIaco")
wolf_of_wall_street = media.Movie("The Wolf of Wall Street", " Thanks to his aggressive pitching style and the high commissions, Jordan makes a small fortune.", "https://upload.wikimedia.org/wikipedia/en/1/1f/WallStreet2013poster.jpg", "https://www.youtube.com/watch?v=iszwuX1AK6A")


list_of_movies = [dark_night, titanic, avengers, inside_out, shwashank_redemption, wolf_of_wall_street]
fresh_tomatoes.open_movies_page(list_of_movies)

