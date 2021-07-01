"""A video player class."""

from src.video_library import VideoLibrary
from src.video import Video
import random
import numpy as np
is_playing = False
is_pause = False
current_playlist=[]
#pause_video = Video(video_title=None, video_id=None, video_tags={})
current_video = Video(video_title=None, video_id=None, video_tags={})


class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()


    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""
        print('Here\'s a list of all available videos: ')
        all_video = self._video_library.get_all_videos()
        all_video.sort(key=lambda x: x.title, reverse=False)
        for i in all_video:
            joining_string = ' '.join(i.tags)
            print( str(i.title) +' (' + str(i.video_id) +') [' + joining_string+']')


    def play_video(self, video_id):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """
        all_video = self._video_library.get_all_videos()
        global is_playing
        global is_pause
        global current_video
        thistitle=[]

        for i in all_video:
            thistitle.append(i.video_id)

        if is_playing == True and (video_id in thistitle):
            print('Stopping video: ' + current_video.title)

        if video_id not in thistitle:
            print('Cannot play video: Video does not exists')

        for i in all_video:
            if video_id == i.video_id:
                current_video = i
                print('Playing video: ' + current_video.title)
                is_playing = True
                is_pause = False

    def stop_video(self):
        """Stops the current video."""
        global is_playing
        global current_video
        global is_pause

        if is_playing == True:
            print('Stopping video: '+current_video.title)
            is_playing = False
        else:
            print('Cannot stop video: No video is currently playing')

    def play_random_video(self):
        """Plays a random video from the video library."""
        global is_playing
        global is_pause
        global current_video
        num_videos = len(self._video_library.get_all_videos())
        i = random.randint(0, num_videos-1)
        all_video = self._video_library.get_all_videos()
        next_video = all_video[i]
        if is_playing == True:
            print('Stopping video: ' + current_video.title)
            print('Playing video: ' + next_video.title)
            current_video = next_video
            is_playing = True
            is_pause = False
        else:
            print('Playing video: ' + next_video.title)
            is_playing = True
            current_video = next_video


    def pause_video(self):
        """Pauses the current video."""
        global is_pause
        global is_playing
        global current_video

        if is_pause==False and is_playing==True:
            print('Pausing video: ' + current_video.title )
            is_pause=True

        elif is_pause==True and is_playing==True:
            print('Video already paused: ' + current_video.title)

        else:
            print('Cannot pause video: No video is currently playing')




    def continue_video(self):
        """Resumes playing the current video."""
        global is_pause
        global is_playing
        global current_video

        if is_pause == True and is_playing == True:
            print('Continuing video: '+ current_video.title)
            is_pause = False
        elif is_pause == False and is_playing == True:
            print('Cannot continue video: Video is not paused')
        else:
            print('Cannot continue video: No video is currently playing')

    def show_playing(self):
        """Displays video currently playing."""
        global is_pause
        global is_playing
        global current_video

        if is_playing==True and is_pause==False:
            print('Currently playing: '+current_video.title+' '+current_video.video_id)
        elif is_playing==True and is_pause==True:
            print('Currently playing: ' + current_video.title + ' '+current_video.video_id +' -PAUSED')
        else:
            print('No video is currently playing')


    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        list_playlist = list(map(lambda x:x.lower(), current_playlist))
        if playlist_name.lower() in list_playlist:
            print('Cannot create playlist: A playlist with the same name already exist')
        else:
            print('Successfully created new playlist')
            playlist_name = []
            current_playlist.append(playlist_name)



    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        print("add_to_playlist needs implementation")

    def show_all_playlists(self):
        """Display all playlists."""
        global current_playlist

        if len(current_playlist)==0:
            print('Showing all playlist: ')
            for i in current_playlist:
                pass


        print("show_all_playlists needs implementation")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("show_playlist needs implementation")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("deletes_playlist needs implementation")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
