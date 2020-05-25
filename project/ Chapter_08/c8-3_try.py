"""
#Test#8-7
def describe_city(city = "Reykjavik",country = "iceland"):
    print(city.title() + "is in " + country.title())

describe_city()
describe_city("shanghai","china")
describe_city("vancouver","australia")

def city_country(city,country):
    city_category = city + "," + country
    return city_category
full_city_name_1 = city_country("shanghai","china")
full_city_name_2 = city_country("beijing","china")
full_city_name_3 = city_country("Vancouver","Australia")

#Test#8-7专辑
#判断专辑数量，定义专辑数量为可选形参
def make_album(album,singer,number=""):
    if number:
        music_album = "music name:" + album + ", " + "singer:" + singer + ", " + "music number:" + number
    else:
        music_album = "music name:" + album + ", " + "singer:" + singer
    return music_album

output = make_album("bad","Michael Jackson")
print(output)
output = make_album("bad","Michael Jackson","14")
print(output)
"""
def make_album(singer,album):
    music_album = {"singer's name":singer,"album name":album}
    return music_album
while True:
    print("please tell me the singer and the album.")
    print("enter 'q' anytime to qiuit.")
    singer_name = input("Singer's name:")
    if singer_name == "q":
        break
    album_name = input("Album's name:")
    if album_name == "q":
        break
output = make_album(singer_name,album_name)
print(output)