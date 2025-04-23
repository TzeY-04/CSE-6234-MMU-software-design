class Slide:
    def createSlide(self, Title):
        pass

    def showSlide(self):
        pass

paperslide = ["Slide Title 3","Slide Title 4"]

class paperSlide(Slide):
    def __init__(self):
        self.observers = []

    def createSlide(self, Title):
        print(f"Title is {Title}")
        paperslide.append(Title)
        
        #for i in self.paperslide:
        #    print(i)

    def showSlide(self):
        print(f"The slide about paper : ")
        for i in paperslide:
            print(i)

plasticslide = ["Slide Title 1","Slide Title 2"]

class plasticSlide(Slide):
    def __init__(self):
        self.observers = []

    def createSlide(self, Title):
        print(f"Title is {Title}")
        plasticslide.append(Title)
        
        #for i in self.plasticslide:
        #    print(i)

    def showSlide(self):
        print(f"The slide about plastic : ")
        for i in self.plasticslide:
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
        else:
            return None

class SlideManagement:
    def __init__(self, searchSlide):
        self.searchSlide = searchSlide

    def showRelatedSlide(self):
        pass

class SlideFunctionality(SlideManagement):
    def __init__(self, searchSlide):
        super().__init__(searchSlide)

    def showRelatedSlide(self):
        self.searchSlide.showSlide()
        

# using factory pattern to create slide
class CreateSlide(Slide):
    def create_slide(self):
        print("Creating slide...")
        factory = SlideFactory()
        slideType = input("Enter a type (paper/plastic): ")
        slide = factory.get_Type(slideType)
        slideTitle = input("Enter your slide Title: ")
        slide.createSlide(slideTitle)
        print("Slide Created \n")


# using bridge pattern to search slide
class SearchSlide:
    def search_slide(self):
        print("Searching slide...")
        factory = SlideFactory()
        findType = input("Enter a type (paper/plastic): ")
        slide = factory.get_Type(findType)
        searchingSlide = SlideFunctionality(slide)
        searchingSlide.showRelatedSlide()

class RemoveSlide:
    def remove_slide(self):
       pass

class SlideFacade:
    def __init__(self):
        self.createslide = CreateSlide()
        self.searchslide = SearchSlide()
        self.removeslide = RemoveSlide()
    
    def creating_slide(self):
        self.createslide.create_slide()

    def searching_slide(self):
        self.searchslide.search_slide()

    def removing_slide(self):
        self.removeslide.remove_slide()

#client
facade = SlideFacade()
facade.creating_slide()
facade.searching_slide()