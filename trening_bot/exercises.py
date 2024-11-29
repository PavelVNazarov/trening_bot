# exercises.py
from video_manager import VideoManager

video_manager = VideoManager()

def get_exercise_categories():
    return video_manager.get_categories()

def get_exercise_video(category, exercise):
    return video_manager.get_video_url(category, exercise)