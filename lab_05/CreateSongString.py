# coding=utf-8
# DO NOT REMOVE THE LINE ABOVE, OTHERWISE YOUR CODE WILL FAIL IN THE AUTOGRADER!


def create_song_string():
    pass


def main():
    """
    Just an example. Feel free to try your own.
    """
    title = "Groovy!"
    artist = "Hirose, Koumi"
    album = "Cardcaptor Sakura OST"
    bpm = 123
    length_in_seconds = 267.0

    formatted_song_string = create_song_string(title, artist, album, bpm, length_in_seconds)
    print(formatted_song_string)

if __name__ == '__main__':
    main()
