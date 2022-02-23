from ninja import Ninja
from pet import Pet


yuki = Pet("Yuki", "dog", ["sit", "fetch", "come", "dance"])
nick = Ninja("Nick", "Smart", ["Cranberry Nut", "Natural Banana"], "Royal Canin Maltese Food", yuki)

nick.walk().feed().bathe()