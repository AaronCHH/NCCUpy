import random
eyes = ["●","･","๑","o","◕","¯","ㅇ"]
mouths = ["д","ㅂ","₃","ω","∀","‿","◇"]
hands = ["ლ","Ψ","づ"]

face = []

hand = hands[random.randrange(0,len(hands) )]
eye = eyes[random.randrange(0,len(eyes) )]
mouth = mouths[random.randrange(0,len(mouths) )]

face.append(hand)
face.append("(")
face.append(eye)
face.append(mouth)
face.append(eye)
face.append(")")
face.append(hand)

print(''.join(face))