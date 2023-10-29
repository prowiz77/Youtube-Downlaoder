import customtkinter
from PIL import Image
import os
import requests
from yt_dlp import YoutubeDL
import subprocess

customtkinter.set_appearance_mode("dark")

class App(customtkinter.CTk):
    width = 600
    height = 600

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("CeNtis - Youtube Downloader")
        self.geometry(f"{self.width}x{self.height}")
        self.resizable(False, False)

        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "images")

        # load and create background image
        current_path = os.path.dirname(os.path.realpath(__file__))
        self.bg_image = customtkinter.CTkImage(Image.open(current_path + "/images/darkgrey.jpg"),
                                               size=(self.width, self.height))
        self.bg_image_label = customtkinter.CTkLabel(self, image=self.bg_image)
        self.bg_image_label.grid(row=0, column=0)

        # create login frame
        self.login_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color ='#333333')
        self.login_frame.grid(row=0, column=0, sticky="ns")
        self.large_test_image = customtkinter.CTkImage(Image.open(current_path + "/images/youtube2.png"), 
                                                size=(300, 100))#size=(300, 100))                                                
        self.large_test_image_label = customtkinter.CTkLabel(self.login_frame, image=self.large_test_image, text="")
        self.large_test_image_label.grid(row=0, column=0, padx=30 , pady=(100, 15))

        self.username_entry = customtkinter.CTkEntry(self.login_frame, width=200, placeholder_text="enter youtube link", fg_color="#ff0000", border_color="#ff0000", placeholder_text_color="white")
        self.username_entry.grid(row=1, column=0, padx=30, pady=(175, 15))
        self.login_button = customtkinter.CTkButton(self.login_frame, text="Download", command=self.login_event, width=200, fg_color = "#ff0000", hover_color = "#ff4c4c")
        self.login_button.grid(row=3, column=0, padx=30, pady=(15, 15))

    def login_event(self):
        def download_link_func():
            url = self.username_entry.get()
            if len(url) == 0:
                print("No input found...")
            else:
                print("Download Button Pressed - link:", self.username_entry.get())

                ydl_opts = {
                    'format': 'bv*[ext=mp4]+ba[ext=m4a]/b[ext=mp4] / bv*+ba/b',         
                }
                with YoutubeDL(ydl_opts) as ydl:
                    ydl.download(url)

        download_link_func()        


if __name__ == "__main__":
    app = App()
    app.mainloop()