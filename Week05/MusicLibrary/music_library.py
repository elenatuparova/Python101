import re
import os.path
from math import floor
import json
from random import shuffle


class Jsonable:
    def to_json(self):
        return json.dumps(self, default=lambda o: {'type': o.__class__.__name__, 'dict': o.__dict__})


class Song(Jsonable):

    def __init__(self, title, artist, album, length):
        self.validate_parameters(title, artist, album, length)
        self.title = title
        self.artist = artist
        self.album = album
        self.length = length

    def __str__(self):
        return '{} - {} from {} - {}'.format(self.artist, self.title, self.album, self.length)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __hash__(self):
        return hash((self.title, self.artist, self.album, self.song_length))

    def get_length(self, seconds=False, minutes=False, hours=False):
        song_length_list = [int(length) for length in self.length.split(':')]

        if seconds == True:
            if len(song_length_list) == 2:
                return song_length_list[1] + song_length_list[0] * 60
            if len(song_length_list) == 3:
                return song_length_list[2] + song_length_list[1] * 60 + song_length_list[0] * 3600

        if minutes == True:
            if len(song_length_list) == 2:
                return song_length_list[0]
            if len(song_length_list) == 3:
                return song_length_list[1] + song_length_list[0] * 60

        if hours == True:
            if len(song_length_list) == 2:
                return 0
            if len(song_length_list) == 3:
                return song_length_list[0]

        return self.length

    @staticmethod
    def validate_parameters(title, artist, album, length):
        if not isinstance(title, str):
            raise TypeError('Title attribute must be string!')

        if not isinstance(artist, str):
            raise TypeError('Artist attribute must be string!')
        
        if not isinstance(album, str):
            raise TypeError('Album attribute must be string!')
        
        if not isinstance(length, str):
            raise TypeError('Length attribute must be string!')
        length_pattern = re.compile('^([0-9]{1,2}:)?[0-9]{1,2}:[0-9]{1,2}$')
        if not length_pattern.match(length):
            raise ValueError('Length is not in suitable format!')


class Playlist(Jsonable):

    def __init__(self, name, repeat=False, shuffle=False, songs_list=[]):
        self.validate_parameters(name, repeat, shuffle, songs_list)
        self.name = name
        self.repeat = repeat
        self.shuffle = shuffle
        self.songs_list = songs_list
        self.current_song_index = 0

    def add_song(self, song):
        if not isinstance(song, Song):
            raise TypeError('Song should be an instance of class Song!')
        self.songs_list.append(song)

    def remove_song(self, song):
        if not isinstance(song, Song):
            raise TypeError('Song should be an instance of class Song!')

        if song not in self.songs_list:
            raise ValueError('Song doesn\'t exist in playlist!')

        self.songs_list.remove(song)

    def add_songs(self, songs):
        if not isinstance(songs, list):
            raise TypeError('Songs should be in a list!')

        for song in songs:
            if not isinstance(song, Song):
                raise TypeError('Every song must be an instance of class Song!')

        self.songs_list += songs

    def total_length(self):
        total_length = 0
        for song in self.songs_list:
            total_length += song.get_length(seconds=True)
        hours = floor(total_length / 3600)
        minutes = floor((total_length % 3600) / 60)
        seconds = total_length % 60
        total_length_str = ''
        if hours > 0:
            total_length_str += str(hours) + ':'
            if minutes < 10:
                total_length_str += '0'
        total_length_str += str(minutes) + ':' + str(seconds)
        return total_length_str

    def artists(self):
        artists = {}
        for song in self.songs_list:
            if song.artist not in artists.keys():
                artists[song.artist] = 0
            artists[song.artist] += 1
        return artists

    def next_song(self):
        pass

    def pprint_playlist(self):
        pass

    def save(self):
        file_name = [char for char in self.name]
        for char in file_name:
            if char == ' ':
                char = '-'
        file_name_str = ''.join(file_name) + '.json'
        directory = '/home/osboxes/Documents/PythonProjects/playlist-data/'
        complete_file_name = os.path.join(directory, file_name_str)

        json_content_str = self.to_json()
        json_dict = json.loads(json_content_str)

        with open(complete_file_name, 'w') as json_file:
            json.dump(json_dict, json_file, indent=4)

    @staticmethod
    def load(path):
        directory = '/home/osboxes/Documents/PythonProjects/playlist-data/'
        complete_path = directory + path
        with open(complete_path) as json_file:
            playlist_dict = json.load(json_file)['dict']
        new_playlist = Playlist(playlist_dict['name'])
        new_playlist.repeat = playlist_dict['repeat']
        new_playlist.shuffle = playlist_dict['shuffle']
        new_playlist.songs_list = [Song(**song['dict']) for song in playlist_dict['songs_list']]
        return new_playlist

    @staticmethod
    def validate_parameters(name, repeat=False, shuffle=False, songs_list=[]):
        if not isinstance(name, str):
            raise TypeError('Name attribute must be string!')

        if not isinstance(repeat, bool):
            raise TypeError('Repeat attribute must be boolean!')

        if not isinstance(shuffle, bool):
            raise TypeError('Shuffle attribute must be boolean!')

        if not isinstance(songs_list, list):
            raise TypeError('Songs must be in a list!')
        for song in songs_list:
            if not isinstance(song, Song):
                raise TypeError('Each song must be an instance of class Song!')


class MusicCrawler:
    def __init__(self, path):
        pass

    def generate_playlist(self):
        pass

if __name__ == '__main__':
    song1 = Song(title='Love Runs Out', artist='OneRepublic', album='Native', length='3:44')
    song2 = Song(title='Counting Stars', artist='OneRepublic', album='Native', length='3:50')
    song3 = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="3:44")
    playlist = Playlist('OneRepublic')
    playlist.add_songs([song1, song2, song3])
    print(playlist.songs_list)
    print(song1)
    playlist.save()
    json_str = playlist.to_json()
    p1 = Playlist.load('OneRepublic.json')
    print(p1.__dict__)
    print(p1.artists())
    print(p1.songs_list)
    random_p1 = p1.songs_list
    shuffle(random_p1)
    print(random_p1)