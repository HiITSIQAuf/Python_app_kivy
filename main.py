import os

os.environ['KIVY_VIDEO'] = "ffpyplayer"
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import StringProperty
from kivy.uix.behaviors import ButtonBehavior
from kivymd.uix.label import MDIcon
from kivy.animation import Animation
from kivy.core.window import Window
from kivy.uix.carousel import Carousel
from kivy.uix.video import Video

Window.size = (400, 710)


class Hello(MDApp):
    dialog = None
    l = StringProperty()

    def send_data(self, email, password):
        from firebase import firebase

        # firebaza chaqrvollik
        firebase = firebase.FirebaseApplication('https://center-a530c-default-rtdb.firebaseio.com/', None)

        # Data import qilamiz

        data = {
            'Email': email,
            'Password': password,
        }

        # fire bazadagi post

        firebase.post('https://center-a530c-default-rtdb.firebaseio.com/Users', data)

    def build(self):
        self.theme_cls.material_style = "M3"
        self.l = "assets/hello.png"
        return Builder.load_file("Main.kv")

    def email(self):
        self.l = "assets/Nice.png"

    def password(self):
        self.l = "assets/Nics.png"

    def login(self, widget, widget1, widget2, widget3, widget4, widget5):
        self.l = "assets/hello.png"
        anim = Animation(opacity=0, duration=0.5)
        anim.start(widget)
        anim1 = Animation(opacity=0, duration=0.5)
        anim1.start(widget1)
        anim2 = Animation(opacity=0, duration=0.5)
        anim2.start(widget2)
        anim3 = Animation(pos_hint={"center_x": .5, "center_y": .05}, size_hint=(.3, .3), duration=1.5)
        anim3 += Animation(pos_hint={"center_x": .5, "center_y": .86}, size_hint=(.4, .4), duration=1.5)
        anim3.start(widget3)
        anim3 = Animation(pos_hint={"center_x": .5, "center_y": .64}, duration=3)
        anim3.start(widget4)
        anim4 = Animation(pos_hint={"center_x": .5, "center_y": .55}, duration=3)
        anim4.start(widget5)

    def video_state(self):
        state = 'play'
        return state


# Add_videos
# class MenuScreen(Screen):
#     pass
# https://www.youtube.com/watch?v=r-sLPRdlMd4

class Heoo(Screen, Carousel):
    def __init__(self, **kwargs):
        super(Heoo, self).__init__(**kwargs)
        global source

        source = ["", "assets/edit.mp4", "assets/hello.mp4", "assets/hello_world.mp4", "assets/hepuay.mp4"]
        j = 0
        for i in source:
            j += 1
            vid = Video(source=i, state="stop")
            vid.options = {'eos': 'loop'}
            vid.allow_stretch = True
            self.add_widget(vid)
            self.ids[f"video{j}"] = vid
        self.ids["video1"].state = "play"

    def r(self, args):
        for i in range(len(source)):
            if args == i:
                self.ids[f"video{i + 1}"].state = "play"
            else:
                self.ids[f"video{i + 1}"].state = "stop"

    def ro(self, button):
        if button.icon == "play":
            button.icon = "pause"
            self.root.ids.video.state = "play"
        else:
            button.icon = "play"
            self.root.ids.video.state = "pause"


class Videos(Video):
    pass


class IconButton(ButtonBehavior, MDIcon):
    pass


class AddVideo(Screen):
    pass


sm = ScreenManager()
sm.add_widget(Heoo(name='screen 1'))
sm.add_widget(AddVideo(name='video'))

if __name__ == "__main__":
    Hello().run()
