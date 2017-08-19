import media
import fresh_tomatoes

#Contains the information about each movie to be displayed on the website
def main():
    spider_man = media.Movie("Spider-Man: Homecoming",
                            "Thrilled by his experience with the Avengers, young Peter Parker returns home to live with his Aunt May. Under the watchful eye of mentor Tony Stark, Parker starts to embrace his newfound identity as Spider-Man. He also tries to return to his normal daily routine -- distracted by thoughts of proving himself to be more than just a friendly neighborhood superhero. Peter must soon put his powers to the test when the evil Vulture emerges to threaten everything that he holds dear.",
                            "https://upload.wikimedia.org/wikipedia/en/thumb/f/f9/Spider-Man_Homecoming_poster.jpg/220px-Spider-Man_Homecoming_poster.jpgc",
                            "https://www.youtube.com/watch?v=rk-dF1lIbIg",
                            "7 July 2017")
    print(spider_man.storyline)

    transformers = media.Movie("Transformers: The Last Knight",
                         "Humans are at war with the Transformers, and Optimus Prime is gone. The key to saving the future lies buried in the secrets of the past and the hidden history of Transformers on Earth. Now, it's up to the unlikely alliance of inventor Cade Yeager, Bumblebee, an English lord and an Oxford professor to save the world.",
                         "https://upload.wikimedia.org/wikipedia/en/2/26/Transformers_The_Last_Knight_poster.jpg",
                         "https://youtu.be/yCOvcyfRPRk",
                         "23 June 2017 ")

    thor = media.Movie("Thor: Ragnarok",
                        "Imprisoned on the other side of the universe, the mighty Thor finds himself in a deadly gladiatorial contest that pits him against the Hulk, his former ally and fellow Avenger. Thor's quest for survival leads him in a race against time to prevent the all-powerful Hela from destroying his home world and the Asgardian civilization.",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/7/7d/Thor_Ragnarok_poster.jpg/220px-Thor_Ragnarok_poster.jpg",
                        "https://youtu.be/TTgNlfAht4I",
                        "3 November 2017")

    won_women = media.Movie("Wonder Woman",
                          "Before she was Wonder Woman (Gal Gadot), she was Diana, princess of the Amazons, trained to be an unconquerable warrior. Raised on a sheltered island paradise, Diana meets an American pilot (Chris Pine) who tells her about the massive conflict that's raging in the outside world. Convinced that she can stop the threat, Diana leaves her home for the first time. Fighting alongside men in a war to end all wars, she finally discovers her full powers and true destiny.",
                          "https://upload.wikimedia.org/wikipedia/en/e/ed/Wonder_Woman_%282017_film%29.jpg",
                          "https://youtu.be/VSB4wGIdDwo",
                          "2 June 2017")

    gaurdians = media.Movie("Guardians of the Galaxy Vol. 2",
                           "Peter Quill and his fellow Guardians are hired by a powerful alien race, the Sovereign, to protect their precious batteries from invaders. When it is discovered that Rocket has stolen the items they were sent to guard, the Sovereign dispatch their armada to search for vengeance. As the Guardians try to escape, the mystery of Peter's parentage is revealed.",
                           "https://upload.wikimedia.org/wikipedia/en/thumb/9/95/GotG_Vol2_poster.jpg/220px-GotG_Vol2_poster.jpg",
                           "https://youtu.be/duGqrYw4usE",
                           "19 April 2017")

    pirates = media.Movie("Pirates of the Caribbean: Dead Men Tell No Tales",
                          "Thrust into an all-new adventure, a down-on-his-luck Capt. Jack Sparrow feels the winds of ill-fortune blowing even more strongly when deadly ghost sailors led by his old nemesis, the evil Capt. Salazar, escape from the Devil's Triangle. Jack's only hope of survival lies in seeking out the legendary Trident of Poseidon, but to find it, he must forge an uneasy alliance with a brilliant and beautiful astronomer and a headstrong young man in the British navy.",
                          "https://upload.wikimedia.org/wikipedia/en/2/21/Pirates_of_the_Caribbean%2C_Dead_Men_Tell_No_Tales.jpg",
                          "https://youtu.be/XibzC-e_s5M",
                          "26 May 2017")

    movies = [thor, spider_man, gaurdians, pirates, won_women, transformers]

    # Open the movie website in the user's browser, featuring the movies above.
    fresh_tomatoes.open_movies_page(movies)
    print("__doc__ : "+media.Movie.__doc__ +"\n__module__ : "+ media.Movie.__module__)

if __name__ == '__main__':
    main()
