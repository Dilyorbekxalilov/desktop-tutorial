import pandas as pd

#1 . DataFream yaratish 
data={
    'ism ': ['ali','vali','gani','ayubxon','bunyod','farrux','hakim','anvarjon','eldor','dilyor'],
    'yosh': [19,25,16,19,19,24,95,16,15,40],
    'shahar': ['Toshkent','fargona','samarqand','fargona','fargona','Toshkent','fargona','samarqand','fargona','fargona'], 
}
df=pd.DataFrame(data)
# 2. malumotlarni korish 
print(df)
# 3,filtirlash
young_people=df[df['yosh']<40]
print("40 yoshdan kichiklarni :\n",young_people)
#4 ozgartirish
df['yosh']+=1 #har  bir shahsni 1ga qosh
print("yangilanga data fream:\n",df)

#5 fargonaliklar chiqsin
city=df[df['shahar']=='fargona']
print("fargona shahrdegilar chiqarilar",city)

