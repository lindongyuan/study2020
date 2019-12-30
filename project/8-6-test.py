#编写一个city_country()函数，它接受城市的名称及其所属的国家
def city_country(city,country):
    territo = city + "," + country
    return territo.title()

terr = city_country('meizhou','china')
print(terr)

terr = city_country('alaska','usa')
print(terr)

terr =  city_country('santiago','chile')
print(terr)
'''
#编写一个名为make_album()的函数，这个函数应接受歌手的名字和专辑名，并返回一个包含这两项信息的字典
#创建并打印3个返回的值，给函数make_album()添加一个可选形参，以便能够存储专辑包含的歌曲数。
def make_album(singer,album,num=''):
    music = {'singer':singer,'album':album}
    if num:
        music['num'] = num
    return music

albums = make_album('Gwen Stefani','The Sweet Escape')
print(albums)

albums = make_album('Sarah.Brightmen','harem',num=12)
print(albums)

albums = make_album('Beyonce Knowles','Listen')
print(albums)
'''
#编写一个名为make_album()的函数，这个函数应接受歌手的名字和专辑名，并返回一个包含这两项信息的字典
#创建并打印3个返回的值，给函数make_album()添加一个可选形参，以便能够存储专辑包含的歌曲数。
#编写一个while循环，让用户输入一个专辑的歌手和名称，获取这些信息后，使用它们来调用函数
#并将创建的字典打印出来，循环需要提供退出途径
def make_album(singer,album,num=''):
    music = {'singer':singer,'album':album}
    return music

while True:
    print("\nPlease enter your favorite singers and albums.")
    print("(enter 'q' at any time to qiut)")
    s_singer = input("Singer:")
    if s_singer == 'q':
        break
    a_album = input("Album:")
    if a_album == 'q':
        break
    albums = make_album(s_singer,a_album)
    print(albums)
