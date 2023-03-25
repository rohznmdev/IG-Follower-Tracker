import codecs
import os
from bs4 import BeautifulSoup

followingIG = codecs.open("./followers_and_following/following.html", "r", "utf-8")
followersIG = codecs.open("./followers_and_following/followers_1.html", "r", "utf-8")


if os.path.exists("followers.txt"):
    os.remove("followers.txt")
if os.path.exists("following.txt"):
    os.remove("following.txt")
if os.path.exists("notfollowingme.txt"):
    os.remove("notfollowingme.txt")
if os.path.exists("notfollowingback.txt"):
    os.remove("notfollowingback.txt")

followers = open("followers.txt", "x")
following = open("following.txt", "x")
notfollowing = open("notfollowingme.txt", "x")
notfollowingback = open("notfollowingback.txt", "x")

followingList = []
followerList = []
notFollowingMeList = []
notFollowingBackList = []


def findFollowing():
    soup = BeautifulSoup(followingIG, "html.parser")
    for i in soup.find_all('a'):
        following.write(f"{i.text}\n")
        followingList.append(f"{i.text}\n")


def findFollowers():
    soup = BeautifulSoup(followersIG, "html.parser")
    for i in soup.find_all('a'):
        followers.write(f"{i.text}\n")
        followerList.append(f"{i.text}\n")

def findNotFollowing(): 
    for i in followingList: 
        if i not in followerList:
            notFollowingMeList.append(i)

def findNotFollowingBack():
    for i in followerList:
        if i not in followingList:
            notFollowingBackList.append(i)
        
def createNotFollowing():
    for i in notFollowingMeList:
        notfollowing.write(i)

def createNotFollowingBack():
    for i in notFollowingBackList:
        notfollowingback.write(i)

def flow():
    findFollowing()
    findFollowers()
    findNotFollowing()
    createNotFollowing()
    findNotFollowingBack()
    createNotFollowingBack()

flow()
