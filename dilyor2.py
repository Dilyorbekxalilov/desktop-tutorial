import numpy as np 

# 1. massiv yaratish
olma = np.array([1,2,3,4,5])
nok =np.array([[1,2,3],[4,5,6]])

# 2. matematik yaratish
qoshish=np.sum(olma)
ortacha=np.mean(olma)
kop=np.prod(olma)
qoshish1 =np.sum(nok)
ortacha1 =np.mean(nok)
kop1 =np.prod(nok)
print("olma masivi ", olma )
print("nok:\2",nok )

print("massivlar yegindisi",qoshish)
print("massivlar ortachasi",ortacha)
print("massivlar kopaytmasi",kop)

print("massivlar yegindisi",qoshish1)
print("massivlar ortacha ",ortacha1)
print("massivlar kopaytma ",kop1)