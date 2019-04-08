from music_library import Song, Playlist
import unittest

class TestSong(unittest.TestCase):

    def test_validation_when_title_is_not_str_then_raise_type_error(self):
        with self.assertRaises(TypeError):
            Song.validate_parameters(title=1, artist='OneRepublic', album='Native', length='3:44')

    def test_validation_when_artist_is_not_str_then_raise_type_error(self):
        with self.assertRaises(TypeError):
            Song.validate_parameters(title='Love Runs Out', artist=1, album='Native', length='3:44')

    def test_validation_when_album_is_not_str_then_raise_type_error(self):
        with self.assertRaises(TypeError):
            Song.validate_parameters(title='Love Runs Out', artist='OneRepublic', album=True, length='3:44')

    def test_validation_when_length_is_not_str_then_raise_type_error(self):
        with self.assertRaises(TypeError):
            Song.validate_parameters(title='Love Runs Out', artist='OneRepublic', album='Native', length=3)

    def test_validation_when_length_is_not_in_hh_mm_ss_format_then_return_value_error(self):
        with self.assertRaises(ValueError):
            Song.validate_parameters(title='Love Runs Out', artist='OneRepublic', album='Native', length='3-44')

    def test_string_dunder(self):
        test_song = Song(title='Love Runs Out', artist='OneRepublic', album='Native', length='3:44')
        expected_result = 'OneRepublic - Love Runs Out from Native - 3:44'
        self.assertEqual(str(test_song), expected_result)

    def test_equal_dunder(self):
        test_song1 = Song(title='Love Runs Out', artist='OneRepublic', album='Native', length='3:44')
        test_song2 = Song(title='Love Runs Out', artist='OneRepublic', album='Native', length='3:44')
        self.assertTrue(test_song1 == test_song2)

    def test_get_length_when_seconds_is_true(self):
        test_song = Song(title='Love Runs Out', artist='OneRepublic', album='Native', length='3:44')
        expected_result = 224
        self.assertEqual(test_song.get_length(seconds=True), expected_result)

    def test_get_length_when_minutes_is_true(self):
        test_song = Song(title='Love Runs Out', artist='OneRepublic', album='Native', length='3:44')
        expected_result = 3
        self.assertEqual(test_song.get_length(minutes=True), expected_result)

    def test_get_length_when_hours_is_true(self):
        test_song = Song(title='Love Runs Out', artist='OneRepublic', album='Native', length='3:44')
        expected_result = 0
        self.assertEqual(test_song.get_length(hours=True), expected_result)

    def test_get_length_when_default(self):
        test_song = Song(title='Love Runs Out', artist='OneRepublic', album='Native', length='3:44')
        expected_result = '3:44'
        self.assertEqual(test_song.get_length(), expected_result)


class TestPlaylist(unittest.TestCase):
    
    def test_validation_when_name_is_not_str_then_raise_type_error(self):
        with self.assertRaises(TypeError):
            Playlist.validate_parameters(1)

    def test_validation_when_shuffle_is_not_bool_then_raise_type_error(self):
        with self.assertRaises(TypeError):
            Playlist.validate_parameters('OneRepublic', shuffle=0)

    def test_validation_when_repeat_is_not_bool_then_raise_type_error(self):
        with self.assertRaises(TypeError):
            Playlist.validate_parameters('OneRepublic', repeat='True')

    def test_validation_when_songs_list_is_not_list_then_raise_type_error(self):
        with self.assertRaises(TypeError):
            Playlist.validate_parameters('OneRepublic', songs_list=())

    def test_validation_when_song_in_songs_list_is_not_instance_of_class_song_then_raise_type_error(self):
        with self.assertRaises(TypeError):
            Playlist.validate_parameters('OneRepublic', songs_list=[('Love Runs Out', 'OneRepublic', 'Native', '3:44')])

    def test_add_song_when_song_is_not_instance_of_class_song_then_raise_type_error(self):
        with self.assertRaises(TypeError):
            Playlist('OneRepublic').add_song(('Love Runs Out', 'OneRepublic', 'Native', '3:44'))

    def test_add_song_when_song_is_instance_of_class_song_then_add_song_to_playlist(self):
        test_playlist = Playlist('OneRepublic')
        test_playlist.add_song(Song(title='Love Runs Out', artist='OneRepublic', album='Native', length='3:44'))
        expected_result = [Song(title='Love Runs Out', artist='OneRepublic', album='Native', length='3:44')]
        self.assertEqual(test_playlist.songs_list, expected_result)

    def test_remove_song_when_song_is_not_instance_of_class_song_then_raise_type_error(self):
        test_playlist = Playlist('OneRepublic', songs_list=[Song(title='Love Runs Out', artist='OneRepublic', album='Native', length='3:44')])
        with self.assertRaises(TypeError):
            test_playlist.remove_song(('Love Runs Out', 'OneRepublic', 'Native', '3:44'))

    def test_remove_song_when_song_is_not_present_in_songs_list_then_raise_value_error(self):
        test_playlist = Playlist('OneRepublic', songs_list = [])
        with self.assertRaises(ValueError):
            test_playlist.remove_song(Song(title='Counting Stars', artist='OneRepublic', album='Native', length='3:50'))

    def test_remove_song_when_song_is_present_in_songs_list_then_remove_song_from_playlist(self):
        test_playlist = Playlist('OneRepublic', songs_list=[Song(title='Love Runs Out', artist='OneRepublic', album='Native', length='3:44')])
        test_playlist.remove_song(Song(title='Love Runs Out', artist='OneRepublic', album='Native', length='3:44'))
        expected_result = []
        self.assertEqual(test_playlist.songs_list, expected_result)

    def test_add_songs_when_songs_is_not_list_then_raise_type_error(self):
        with self.assertRaises(TypeError):
            Playlist('OneRepublic').add_songs((Song(title='Love Runs Out', artist='OneRepublic', album='Native', length='3:44')))

    def test_add_songs_when_a_song_in_songs_is_not_an_instance_of_class_song_then_raise_type_error(self):
        with self.assertRaises(TypeError):
            Playlist('OneRepublic').add_songs([('Love Runs Out', 'OneRepublic', 'Native', '3:44')])

    def test_add_songs_when_songs_are_instances_of_class_song_and_are_in_a_list_then_add_songs_to_playlist(self):
        test_playlist = Playlist('OneRepublic', songs_list = [])
        test_playlist.add_songs([Song(title='Love Runs Out', artist='OneRepublic', album='Native', length='3:44'), Song(title='Counting Stars', artist='OneRepublic', album='Native', length='3:50')])
        expected_result = [Song(title='Love Runs Out', artist='OneRepublic', album='Native', length='3:44'), Song(title='Counting Stars', artist='OneRepublic', album='Native', length='3:50')]
        self.assertEqual(test_playlist.songs_list, expected_result)

    def test_total_length_when_songs_do_not_add_up_to_a_full_hour_then_return_length_in_mm_ss_format(self):
        test_playlist = Playlist('OneRepublic', songs_list = [Song(title='Love Runs Out', artist='OneRepublic', album='Native', length='3:44'), Song(title='Counting Stars', artist='OneRepublic', album='Native', length='3:50')])
        expected_result = '7:34'
        self.assertEqual(test_playlist.total_length(), expected_result)
        
    def test_total_length_when_songs_add_up_to_a_full_hour_the_return_length_in_format_hh_mm_ss(self):
        test_playlist = Playlist('OneRepublic', songs_list = [Song(title='Love Runs Out', artist='OneRepublic', album='Native', length='33:44'), Song(title='Counting Stars', artist='OneRepublic', album='Native', length='33:50')])
        expected_result = '1:07:34'
        self.assertEqual(test_playlist.total_length(), expected_result)
        
    def test_artists_return_histogram_of_artists_in_playlist(self):
        test_playlist = Playlist('OneRepublic', songs_list = [Song(title='Love Runs Out', artist='OneRepublic', album='Native', length='3:44'), Song(title='Counting Stars', artist='OneRepublic', album='Native', length='3:50')])
        expected_result = {'OneRepublic': 2}
        self.assertEqual(test_playlist.artists(), expected_result)

if __name__ == '__main__':
    unittest.main()