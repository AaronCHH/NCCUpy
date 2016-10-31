import random
import numpy as np

eyes = ["●","･","๑","o","◕","¯","ㅇ"]
mouth = ["д","ㅂ","₃","ω","∀","‿","◇"]
hands = ["ლ","Ψ","づ"]

e = np.random.choice(eyes)
m = np.random.choice(mouth)
h = np.random.choice(hands)

print("%s(%s%s%s)%s"%(h, e, m, e, h))