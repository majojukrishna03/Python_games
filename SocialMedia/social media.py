def initializePlatform():
    platform = []
    return platform

def createPost(platform,content):
    post = {}
    post['content'] = content
    post['likes'] = 0
    post['comments'] = []
    platform.append(post)
    return platform

def viewTimeline(platform):
    for i in range(len(platform)):
        print(f"Post {i} : {platform[i]}")

def likePost(platform,postIndex):
    if postIndex in range(len(platform)):
        for i in range(len(platform)):
            platform[postIndex]['likes'] += 1
    else: 
        print("Invalid index.")
    return platform


def commentOnPost(platform,postIndex,comment):
    if postIndex in range(len(platform)):
        for i in range(len(platform)):
            platform[postIndex]['comments'].append(comment)
    else: 
        print("Invalid index.")
    return platform

def startPlatform():
    print()
    print("Welcome to the social media platform. ")
    platform = initializePlatform()
    while True: 
        print()
        print("1. Create a post.")
        print("2. View the timeline.")
        print("3. Like a post.")
        print("4. Comment on a post.")
        print("5. Exit the platform.")
        print("-----------------------------------------------------------------------------")
        option = int(input("Enter the serial number of the operation you want to perform : "))

        if option == 1:
            content = input("Enter the content of the post : ")
            platform = createPost(platform,content)
            print("Post created.")
            print()
            print("-----------------------------------------------------------------------------")
        elif option == 2:
            if platform:
                print("Displaying the available posts in the platform :")
                viewTimeline(platform)
            else: 
                print("No posts available in the platform.")
            print()
            print("-----------------------------------------------------------------------------")
        elif option == 3:
            print("Displaying the available posts in the platform :")
            viewTimeline(platform)
            postIndex = int(input("Enter the index position of the post to like : "))
            platform = likePost(platform,postIndex)
            print("Liked the post.")
            print()
            print("-----------------------------------------------------------------------------")
        elif option == 4:
            print("Displaying the available posts in the platform :")
            viewTimeline(platform)
            postIndex = int(input("Enter the index position of the post to make a comment : "))
            comment = input("Enter the comment to add to the post : ")
            platform = commentOnPost(platform,postIndex,comment)
            print("Commented on the post.")
            print()
            print("-----------------------------------------------------------------------------")
        elif option == 5:
            print("Thank you for using the social media platform. Bye!!")
            print("-----------------------------------------------------------------------------")
            break
        else: 
            print("Invalid. Please choose valid serial number.")
        
startPlatform()