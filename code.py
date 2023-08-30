# Import instaloader package
import instaloader

# creating an Instaloader() object
ig=instaloader.Instaloader()

# Taking the instagram username as input from user
usrname=input("Enter username:")

#Fetching the details of provided useraname using instaloder object
profile=instaloader.Profile.from_username(ig.context, usrname)

# Printing the fetched details and storing the profile pic of that account
print("Your Username is: ", profile.username)
print("Total Number of Posts Uploaded: ", profile.mediacount)
print(profile.username+" is having " + str(profile.followers)+' followers.')
print(profile.username+" is following " + str(profile.followees)+' people')
print("Bio: ", profile.biography)
instaloader.Instaloader().download_profile(usrname,profile_pic_only=True)