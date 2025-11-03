import news
import os
from kivymd.app import MDApp
from kivy.uix.image import AsyncImage
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.label import MDLabel
from kivymd.uix.toolbar import MDTopAppBar
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.pagelayout import PageLayout
from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDTextButton,MDFillRoundFlatButton
    
class news_app(MDApp):
    def build(self):
        global news
        self.manager = MDScreenManager()
        self.home = MDScreen(name = 'home')
        self.artical = MDScreen(name = 'artical') 
        self.home_main = BoxLayout()
        self.home_main.orientation = 'vertical'
        self.home_title = MDTopAppBar(title = 'Epoch')
        self.home_title.anchor_title = 'left'
        self.home_main.add_widget(self.home_title)
        self.home.add_widget(self.home_main)
        self.manager.add_widget(self.home)
        self.manager.add_widget(self.artical)
        self.scrollview = MDScrollView()
        self.scroll_item = BoxLayout()
        self.scroll_item.padding = '25dp'
        self.scroll_item.spacing = '25dp'
        self.scroll_item.height = '50dp'
        self.scroll_item.size_hint_y = None
        self.scroll_item.bind(minimum_height=self.scroll_item.setter('height'))
        self.scroll_item.orientation = 'vertical'
        self.scrollview.add_widget(self.scroll_item)
        self.scrollview.do_scroll_x = False
        self.scrollview.do_scroll_y = True
        self.website = MDBoxLayout()
        self.website.spacing = '3dp'
        self.website.height = '20dp'
        field = ['mumbai','tech','delhi','sports','viral','india','entertainment','business','education','hollywood','bollywood','movie-review']
        self.website.size_hint_y = None
        for i in field:
            self.website.add_widget(MDFillRoundFlatButton(text = i.upper(),on_release = self.search))
        self.scroll_item.add_widget(self.website)
        self.home_main.add_widget(self.scrollview)
        self.news =news.news()
        self.init()
        self.artical_init()
        return self.manager
    def init(self):
        self.news.ready()
        data =self.news.get()
        for i in range(0,len(data['titles'])):
            self.create_news(data['images'][i],data['titles'][i],data['links'][i])
    def artical_init(self):
        self.artical_Head1 = MDLabel()
        self.artical_Head1.height = '130dp'
        self.artical_Head1.size_hint_y = None
        self.artical_head2 = MDLabel()
        self.artical_head2.height = '130dp'
        self.artical_head2.size_hint_y = None
        self.box_of_art = BoxLayout()
        self.box_of_art.padding = '10dp'
        self.box_of_art.spacing = '10dp'
        self.box_of_art.size_hint_y = None
        self.artical_title = MDTopAppBar(title = 'Artical')
        self.artical_title.size_hint_y = None
        self.artical_title.right_action_items = [['home',self.go_home]]
        self.box_of_art.add_widget(self.artical_title)
        self.box_of_art.add_widget(self.artical_Head1)
        self.box_of_art.add_widget(self.artical_head2)
        self.artical_image = AsyncImage(height = '600dp')
        self.artical_image.size_hint_y = None
        self.box_of_art.add_widget(self.artical_image)
        self.p1 = MDLabel()
        self.p1.height = '75dp'
        self.p1.size_hint_y = None
        self.p2 = MDLabel()
        self.p2.height = '75dp'
        self.p2.size_hint_y = None
        self.p3 = MDLabel()
        self.p3.height = '75dp'
        self.p3.size_hint_y = None
        self.box_of_art.orientation = 'vertical'
        self.box_of_art.add_widget(self.p1)
        self.box_of_art.add_widget(self.p2)
        self.box_of_art.add_widget(self.p3)
        self.box_of_art.bind(minimum_height=self.box_of_art.setter('height'))
        scroll = MDScrollView()
        scroll.do_scroll_y = True
        scroll.do_scroll_x = False
        scroll.add_widget(self.box_of_art)

        self.artical.add_widget(scroll)
    def go_home(self,*args):
        self.manager.current = 'home'
    def search(self,button):
        self.news.city =button.text.lower()
        try:
            self.news.ready()
            self.news.get()
            self.scroll_item.clear_widgets()
            self.scroll_item.add_widget(self.website)
        except:
            pass
        
        self.init()
    def create_news(self,image,title,link):
        main = BoxLayout()
        print(image)
        imagebox = AsyncImage(source = image,size_hint_y = None,height = '160dp')
        main.add_widget(imagebox)
        about = BoxLayout()
        about.size_hint_y = None
        main.size_hint_y = None
        main.height = '50dp'
        about.orientation = 'vertical'
        about.add_widget(MDLabel(text = title,size_hint_y= None))        
        about.add_widget(MDFillRoundFlatButton(text= 'More...',size_hint_y=None,on_release = lambda x:self.article(link)))
        main.add_widget(about)
        main.bind(minimum_height=main.setter('height'))  
        self.scroll_item.add_widget(main)
    def article(self,link):
        self.manager.current = 'artical'
        articl =news.article(link)
        articl.ready()
        try:
            self.artical_Head1.text = articl.title
            self.artical_Head1.font_style = 'H4'
            self.artical_head2.font_style = 'H5'
            self.artical_head2.text = articl.heading
            self.artical_image.source = articl.image
            self.p1.text = articl.p1
            self.p2.text = articl.p2
            self.p3.text = articl.p3
        except:
            pass
news_app().run()