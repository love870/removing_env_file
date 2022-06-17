#import modules
#instaloader is a python library for downloading instagram posts
import instaloader

#import profile_pic_only
from instaloader import Profile, Post

#instaloader.Instaloader is used to download instagram posts
instance = instaloader.Instaloader()

#Taking Inputs From User
#enter username
user_name = input("Please enter your username: ")
#enter password
password = input("Please enter your password: ")

#logging in to instagram profile
instance.login(user=user_name,passwd=password)

#instagram profile of the user from which you want to download stories
name = input("please enter your username to get story: ")

#pass the username to get profile
profile = Profile.from_username(instance.context, username=name)

#download the stories
instance.download_stories(userids=[profile.userid],filename_target='{}/stories'.format(profile.username))