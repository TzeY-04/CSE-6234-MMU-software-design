class Slide:
    def createSlide(self, Title):
        pass

    def removeSlide(self, Title):
        pass

    def searchSlide(self):
        pass

paperslide = ["Slide Title 3","Slide Title 4"]
# using factory pattern to modify paperslide
class paperSlide(Slide):
    def __init__(self):
        self.observers = []

    def createSlide(self, Title):
        print(f"Title is {Title}")
        paperslide.append(Title)
        
        #for i in paperslide:
        #    print(i)

    def removeSlide(self, Title):
        print(f"Removing...: {Title}")
        paperslide.remove(Title)

    def searchSlide(self):
        print(f"The slide about paper : ")
        for i in paperslide:
            print(i)

plasticslide = ["Slide Title 1","Slide Title 2"]
# using factory pattern to modify plasticslide
class plasticSlide(Slide):
    def __init__(self):
        self.observers = []

    def createSlide(self, Title):
        print(f"Title is {Title}")
        plasticslide.append(Title)
        
        #for i in plasticslide:
        #    print(i)

    def removeSlide(self, Title):
        print(f"Removing...: {Title}")
        plasticslide.remove(Title)

    def searchSlide(self):
        print(f"The slide about plastic : ")
        for i in self.plasticslide:
            print(i)

canslide = ["Slide Title 5","Slide Title 6"]
# using factory pattern to modify canslide
class canSlide(Slide):
    def __init__(self):
        self.observers = []

    def createSlide(self, Title):
        print(f"Title is {Title}")
        canslide.append(Title)
        
        #for i in canslide:
        #    print(i)

    def removeSlide(self, Title):
        print(f"Removing...: {Title}")
        canslide.remove(Title)

    def searchSlide(self):
        print(f"The slide about plastic : ")
        for i in self.canslide:
            print(i)

class SlideFactory:
    def get_Type(self, slide_type: str):
        if slide_type is None:
            return None
        
        slide_type = slide_type.lower()

        if slide_type == "paper":
            return paperSlide()
        elif slide_type == "plastic":
            return plasticSlide()
        elif slide_type == "can":
            return canSlide()
        else:
            print("Selected type does not exist")
            return None

class SlideManagement:
    def __init__(self, searchSlide):
        self.searchSlide = searchSlide

    def searchRelatedSlide(self):
        pass

class SlideFunctionality(SlideManagement):
    def __init__(self, searchSlide):
        super().__init__(searchSlide)

    def searchRelatedSlide(self):
        self.searchSlide.searchSlide()
        
# using factory pattern to create slide
# using facade pattern to run specific function (create slide)
class CreateSlide:
    def create_slide(self):
        print("Creating slide...")
        factory = SlideFactory()
        slideType = input("Enter a type (paper/plastic): ")
        slide = factory.get_Type(slideType)
        slideTitle = input("Enter a slide Title for the slide: ")
        slide.createSlide(slideTitle)
        print("Slide Created \n")

# using factory pattern to remove slide
# using facade pattern to run specific function (remove slide)
class RemoveSlide:
    def remove_slide(self):
        print("Removing slide...")
        factory = SlideFactory()
        slideType = input("Enter a type (paper/plastic): ")
        slide = factory.get_Type(slideType)
        slideTitle = input("Enter a slide Title to remove the slide: ")
        slide.removeSlide(slideTitle)
        print("Slide Removed \n")

# using bridge pattern to search slide
# using facade pattern to run specific function (searchslide)
class SearchSlide:
    def search_slide(self):
        print("Searching slide...")
        factory = SlideFactory()
        findType = input("Enter a type (paper/plastic): ")
        slide = factory.get_Type(findType)
        searchingSlide = SlideFunctionality(slide)
        searchingSlide.searchRelatedSlide()

class SlideFacade:
    def __init__(self):
        self.createslide = CreateSlide()
        self.searchslide = SearchSlide()
        self.removeslide = RemoveSlide()
    
    def creating_slide(self):
        self.createslide.create_slide()

    def removing_slide(self):
        self.removeslide.remove_slide()

    def searching_slide(self):
        self.searchslide.search_slide()

RC_dict = {
    "Ali Recycle Centre": "Taman Tasik Lolo",
    "Abu Recycle Centre": "Taman Putra Lili",
    "New Recycle Centre": "Taman Sauda Lala"
}
verified_RC_dict = {
    "Tui Recycle (verified)": "Puchong",
    "UOI Recycle (verified)": "Taman Putri Kajang"
}
members = {
    "Ken" , "John" , "Ren" , "Tim"
}

admin = "Ali"

class RC_ManageAddressStrategy:
    def modify(self, RC_name ,address):
        pass

class RC_ModifyAddressStrategy(RC_ManageAddressStrategy):
    def modify(self, RC_name ,address):
        RC_dict[RC_name] = address

class RC_RemoveAddressStrategy(RC_ManageAddressStrategy):
    def modify(self, RC_name, address):
        if RC_name in RC_dict:
            RC_dict.pop(RC_name)
            print(f"{RC_name} has been removed from the platform.")
        else:
            print("Not found.")
        
class RC_ManageAddresses:
    def __init__(self, strategy):
        self.strategy = strategy

    def setStrategy(self, strategy):    
        self.strategy = strategy

    def startStrategy(self, RC_name, address):
        self.strategy.modify(RC_name,address)

class Observer():# Observer
    def notify(self , recycle_centre , address):

class Subject(): #Subject
    def add_observer(self,observer):
        pass
    def remove_observer(self,observer):
        pass
    def notify_observer(self , recycle_centre_name, address):
        pass

class RecycleCentreNotifier(Subject): # concrete subject
    def __init__(self):
        self.observers = []

    def add_observer(self,observer):
        self.observers.append(observer)

    def remove_observer(self,observer):
        self.observers.remove(observer)

    def notify_observer(self, recycle_centre_name, address):
        for observer in self.observers:
            observer.notify(recycle_centre_name, address)

class memberObserver(Observer): # concrete observer
    def __init__(self , member_name):
        self.member_name = member_name

    def notify(self, recycle_centre_name , address):
        print(f"[{self.member_name}] Notification: New Recycle Centre Submitted - {recycle_centre_name} at {address} verified by {admin}")


#facade client code

"""
slidefacade = SlideFacade()
action_slide = input("Choose an action to modify slides: ")
action_slide.lower()
if action_slide == "create":
    slidefacade.creating_slide()
elif action_slide == "search":
    slidefacade.searching_slide()
elif action_slide == "remove":
    slidefacade.removing_slide()
else:
    print("Selected action does not exist")


"""



#Observer client code
notifier = RecycleCentreNotifier()

for member in members:
    add_member=memberObserver(member)
    notifier.add_observer(add_member)


RC_name = "abc" #那个是在verify function里面的时候叫observer(RC_name,RC_address) pass过去之后你再set RC_name跟address
address = "Kajang"

notifier.notify_observer(RC_name,address) 


=======





#facade client code 
slidefacade = SlideFacade()
action_slide = input("Choose an action to modify slides: ")
action_slide.lower()
if action_slide == "create":
    slidefacade.creating_slide()
elif action_slide == "search":
    slidefacade.searching_slide()
elif action_slide == "remove":
    slidefacade.removing_slide()
else:
    print("Selected action does not exist")


"""
#Observer client code
notifier = RecycleCentreNotifier()
while True:
    admin = input("Enter a name for admin:(press Q to quit) ").lower()
    if (admin and admin != "q"):
        add_admin = adminObserver(admin)
        notifier.add_observer(add_admin)
    else:
        break
        
rc_name = input("Enter new Recycle Centre name: ")
rc_address = input("Enter address: ")

notifier.notify_observer(rc_name,rc_address)
"""

"""
choice = input("Remove or modify address: ")
choice = choice.lower()
#Strategy client code
if choice == "remove":
    manageRC = RC_ManageAddresses(RC_RemoveAddressStrategy())
    RC_name = input("Enter your Recycle Centre name: ")
    address = "None"
    manageRC.startStrategy(RC_name, address)
    for RC_names,RC_addresses in RC_dict.items():
        print(f"RC Name: {RC_names} , RC Address: {RC_addresses}")

elif choice == "modify":
    manageRC = RC_ManageAddresses(RC_ModifyAddressStrategy())
    RC_name = input("Enter your Recycle Centre name: ")
    address = input("Modifying address: ")
    manageRC.startStrategy(RC_name, address)
    for RC_names,RC_addresses in RC_dict.items():
        print(f"RC Name: {RC_names} , RC Address: {RC_addresses}")

else:
    print("you didnt choose one of it")
    pass
"""
