"""# প্যারেন্ট ক্লাস (Parent Class)
class Animal:
    def make_sound(self):
        # এই মেথডটি চাইল্ড ক্লাসগুলো নিজেদের মতো করে পরিবর্তন (Override) করবে
        pass

# প্রথম চাইল্ড ক্লাস (Child Class 1)
class Dog(Animal):
    def make_sound(self):
        return "Gau Gau! (Barking)"

# দ্বিতীয় চাইল্ড ক্লাস (Child Class 2)
class Cat(Animal):
    def make_sound(self):
        return "Mue Mue! (Meowing)"

# ---- পলিমরফিজম পরীক্ষা করার ফাংশন ----
def introduce_animal(animal_object):
    # ফাংশনটি জানে না কোন পশু আসছে, কিন্তু সে সবার ক্ষেত্রে একই নামের মেথড কল করবে
    print(animal_object.make_sound())

# ---- অবজেক্ট তৈরি এবং রান করা ----

# কুকুরের অবজেক্ট এবং বিড়ালের অবজেক্ট তৈরি করা হলো
tomy = Dog()
mini = Cat()

# একই ফাংশনে ভিন্ন ভিন্ন অবজেক্ট পাঠানো হচ্ছে
print("Dog Barking: ")
introduce_animal(tomy)  # আউটপুট: ঘেউ ঘেউ!

print("\nCat Meowing: ")
introduce_animal(mini)  # আউটপুট: Mue Mue!"""

class Animal:
    def __init__(self, name):
        self.name = name
        print(self.name+"was adopted")
    def run(self):
        print(self.name+"running")

class Turtle(Animal):
    def run(self):
        print(self.name+"is running very slow")

tim=Turtle("Tim")
tim.run()