# video_manager.py
class VideoManager:
    def __init__(self):
        self.videos = {
            "Спина": {
                "Упражнение 1": "video_url_1",
                "Упражнение 2": "video_url_2",
            },
            "Руки": {
                "Упражнение 1": "video_url_3",
                "Упражнение 2": "video_url_4",
            },
            "Грудь": {
                "Упражнение 1": "video_url_5",
                "Упражнение 2": "video_url_6",
            },
            "Ноги": {
                "Упражнение 1": "video_url_7",
                "Упражнение 2": "video_url_8",
            },
            "Плечи": {
                "Упражнение 1": "video_url_9",
                "Упражнение 2": "video_url_10",
            },
            # Добавьте другие категории и упражнения
        }

    def get_categories(self):
        return list(self.videos.keys())

    def get_exercises(self, category):
        return self.videos.get(category, {})

    def get_video_url(self, category, exercise):
        return self.videos.get(category, {}).get(exercise)