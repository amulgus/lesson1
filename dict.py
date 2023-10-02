meme_dict = {
            "CRINGE": "something very strange or very embarassing",
            "LOL": "common respond to something funny",
            "ROFL": "a response to a joke",
            "SHEESH": "slight disapproval",
            "CREEPY": "scary, unpleasant",
            "AGGRO": "to be aggressive/angry"
            }
            
            
            
word = input("imput the word that you dont understand (all must be capital!): ")


if word in meme_dict.keys():
    # Apa yang harus kita lakukan jika kata itu ditemukan?
    print(meme_dict[word])
else:
    # Apa yang harus kita lakukan jika kata itu tidak ditemukan?
    print("no such word in dictionary")
