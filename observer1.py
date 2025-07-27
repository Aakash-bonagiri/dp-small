class YouTubeChannel:
    
    def __init__(self):
        self.subscribers = []
        self.video_title = None
    
    def subscribe(self, subscriber):
        self.subscribers.append(subscriber)
    
    def unsubscribe(self, subscriber):
        self.subscribers.remove(subscriber)
        
    def upload_video(self, video_value):
        self.video_title = video_value
        print(f'\nUploaded the video: {video_value}')
        self.notifyall()
    
    def notifyall(self):
        for s in self.subscribers:
            s.notify(self.video_title)

class Subscriber:
    def __init__(self, name):
        self.name = name

    def notify(self, video_title):
        print(f'{self.name} got notified with: {video_title}')

# ----------------------------
if __name__ == "__main__":
    channel = YouTubeChannel()

    # Correct: Pass Subscriber objects, not strings
    s1 = Subscriber("Aakash")
    s2 = Subscriber("Alice")
    s3 = Subscriber("Bob")

    channel.subscribe(s1)
    channel.subscribe(s2)

    channel.upload_video("Observer Pattern")

    channel.subscribe(s3)

    channel.upload_video("Design Patterns")
