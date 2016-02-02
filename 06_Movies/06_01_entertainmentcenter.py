import media
import fresh_tomatoes

black_mirror = media.Movie("Black Mirror", "A satire on humans and technology", "https://upload.wikimedia.org/wikipedia/en/2/24/BlackMirrorTitleCard.jpg", "https://www.youtube.com/watch?v=jROLrhQkK78")

sherlock_holmes = media.Movie("Sherlock Holmes", "A detective series", "http://images.christianpost.com/full/74899/sherlock.jpg", "https://www.youtube.com/watch?v=7hjPxUfV32Q")

# print (black_mirror.storyline)
# print (sherlock_holmes.storyline)
#
# black_mirror.show_trailer()

school_of_rock = media.Movie("School of rock", "school of rock", "http://images.christianpost.com/full/74899/sherlock.jpg", "https://www.youtube.com/watch?v=7hjPxUfV32Q")

movies = [black_mirror, sherlock_holmes, school_of_rock]
fresh_tomatoes.open_movies_page(movies)
print (media.Movie.VALID_RATINGS)
print (media.Movie.__doc__)