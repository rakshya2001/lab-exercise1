# wtite a python program to convert seconds to day, hour, minutes and seconds.

second=int(input('Enter the value in seconds:'))

day= (((second//60//24)))
print(f"total day for given seconds:{day}")

hour= ((second//60//60))
print(f"total hour for given seconds:{hour}")

minutes= (second//60)
print(f"total minutes for given second:{minutes}")
