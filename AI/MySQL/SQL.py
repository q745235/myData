
import pandas as pd
import requests
import mysql.connector

def nearby_search(pos, radius='1500', type='doctor'):
    url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json'
    payloads = {
        'location': pos,
        'radius': radius,
        'type': type,
        'language': 'zh-TW',
        "keyword" : '皮膚科',
        'key': key
    }
    res = requests.get(url, params=payloads)
    # print(res)
    return [i['place_id'] for i in res.json().get('results')]

def place_detal(place_id):
    place_url = 'https://maps.googleapis.com/maps/api/place/details/json'
    place_payloads = {
        'place_id': place_id,
        'language': 'zh-TW',
        'key': key
    }
    place_res = requests.get(place_url, params=place_payloads)
#     print(place_res)
    result = place_res.json().get('result')
    reviews = result.get('reviews')
#     print(result, "\n\n\n")
#     if "皮膚" in result['name']:
    columns = ["name", 'address', 'comment', 'rating']
    data = pd.DataFrame(columns = columns)

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="hos"
        )
    mycursor = mydb.cursor()
    sql = 'INSERT INTO hos (name, address, comment, rating) VALUES (%s, %s, %s, %s)'
    # sql = 'INSERT INTO hos (name, address, comment, rating) VALUES (?, ?, ?, ?)'
    if reviews:
        for data in reviews:
            val = (result['name'], result['formatted_address'], data['text'], data['rating'])
            mycursor.execute(sql, val)
            mydb.commit()
    mydb.close()
    
    


#     print('醫院名稱: %s' % result['name'])
#     print('地址: %s' % result['formatted_address'])

#     reviews = result.get('reviews')
#     if reviews:
#         for data in reviews:
# #             print(data)
#             print(data['text'])
#             print(data['rating'])
#             print('next')

if __name__ == '__main__':

    key = 'AIzaSyC4CLjCqzMwkD9Guyr4d6-plU9H1yLjo1k'
    near_result = nearby_search(
        pos='24.150840, 120.651124',
        radius='4500'
    )

    for place_id in near_result:
        place_detal(place_id)





#         print(reviews[1])
#     if opening_hours := result.get('opening_hours'):
#         for i in opening_hours.get('weekday_text'):
#             print(i)
#     print('營業時間: %s' % result['opening_hours']['weekday_text'])
    
#     if international_phone_number:=result.get('international_phone_number'):
#         for i in international_phone_number:    
#             print('電話: %s' % result['international_phone_number'])
        
#     print('---------------------------------------')
    
#     if reviews:=result.get('reviews'):
#         for i in reviews:
#             print('評論人: %s\n星等: %s\n評論內容: %s' % (i['author_name'], i['rating'], i['text']))
#     print('======================================================================')
    





