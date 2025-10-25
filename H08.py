# Harjutus 08

# tooted = {
# 'piim': {'kogus': 20, 'hind': 1.19},
# 'küpsised': {'kogus': 20, 'hind': 4.99},
# 'või': {'kogus': 20, 'hind': 2.29},
# 'juust': {'kogus': 15, 'hind': 1.9},
# 'leib': {'kogus': 15, 'hind': 2.59},
# 'jogurt': {'kogus': 18, 'hind': 3.65},
# 'õunad': {'kogus': 35, 'hind': 3.15},
# 'apelsinid': {'kogus': 40, 'hind': 0.99},
# 'banaanid': {'kogus': 23, 'hind': 1.29}
# }

# # print(tooted["piim"]["kogus"])
# try:
#     toode = input("Lisa toode:").lower()
#     kogus = int(input("Vali kogus:"))
    
#     if toode in tooted.keys():
#         if kogus <= tooted[toode]["kogus"] and kogus > 0:
#             print("--- ARVE ----")
#             summa = kogus * tooted[toode]["hind"]
#             print(f"{summa:.2f}eur")
#             tooted[toode]["kogus"] -= kogus
#             print(tooted)
#         else:
#             print("Pole Piisavalt!")
#     else:
#         print(f"Toodet '{toode}' ei leitud!")

# except:
#     print("Ole nüüd normaalne!")





# telefonid={
# 'Mari': '5957503',
# 'Toomas': '5719979',
# 'Kertu': '5201750',
# 'Siim': '5580027',
# 'Piret': '5960799',
# 'Jaan': '5160415',
# 'Lea': '5760164',
# 'Mart': '5337951',
# 'Anni': '5004818',
# 'Tõnu': '5721873',
# 'Kai': '5811884',
# 'Rasmus': '5859489',
# 'Eva': '5039393',
# 'Oskar': '5635812',
# 'Liina': '5696114',
# 'Peeter': '5560756',
# 'Sandra': '5257415',
# 'Heiki': '5207248',
# 'Kristi': '5703338',
# 'Urmas': '5400549'
# }

# telefonid["Mario"] = "65465454654"
# eemalda = telefonid.pop("Kristi")
# telefonid["Eva"] = "555555555555"

# # print(telefonid["Rasmus"])
# # print(eemalda)
# # print(telefonid["Eva"])

# for i in telefonid:
#     print(telefonid[i])

# nimi = input("Sisesta nimi: ").capitalize()
# # try:
# #     print(telefonid[nimi])
# # except:
# #     print("Sellist nime pole")
# try:
#     print(telefonid[nimi])
# except:
#     print("Sellist nime pole")