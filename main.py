# #1-masala
# ball = float(input("Ballni kiriting: "))

# if ball < 0 or ball > 100:
#     print("Xato: Ball 0 dan 100 gacha bo‘lishi kerak.")

# else:
#     if ball >= 90:
#         print("A")
#     elif ball >= 80:
#         print("B")
#     elif ball >= 70:
#         print("C")
#     elif ball >= 60:
#         print("D")
#     else:
#         print("F")


# #2-masala
# yosh = int(input("Yoshingizni kiriting: "))
# daromad = float(input("Daromadingizni kiriting (so'mda): "))

# if yosh < 0 or yosh > 120 or daromad < 0:
#     print("Xato: Yosh 0-120 oralig‘ida, daromad musbat bo‘lishi kerak.")

# else:
#     if yosh < 18:
#         print("Soliq: 0%")
#     elif yosh <= 60:
#         if daromad > 5000:
#             print("Soliq: 20%")
#         else:
#             print("Soliq: 10%")
#     else:
#         print("Soliq: 5%")


# #3-masala
# kun = int(input("Hafta kunini kiriting (1-7):  "))
# soat = int(input("Soatni kiriting (0-23): "))



# #4-masala
# harorat = float(input("Havo haroratini kiriting (℃): "))
# y_h = input("Yomg'ir holatini kiriting (True/Faalse):").lower()

# if harorat < -50 or harorat > 60:
#     print("Xato: Harorat -50 ℃ dan 60 ℃ gacha bo'lishi kerak.")

# else:
#     if harorat < 0:
#         print("Qor yog‘ishi mumkin.")
#     elif harorat <= 20:
#         if y_h == 'true':
#             print("Yomg'irli va sovuq")
#         else:
#             print("Sovuq, lekin quruq")
#     else:
#         print("Issiq")


# #5-masala
# masofa = float(input("Masofani kiriting (km): "))
# vaqt = float(input("Vaqtni kiriting (soat): "))

# if masofa < 0 or vaqt < 0:
#     print("Xato: Masofa va vaqt manfiy bo‘lmasligi kerak.")
# else:
#     if masofa < 5:
#         print("Piyoda")
#     elif masofa <= 50:
#         if vaqt > 1:
#             print("Avtobus")
#         else:
#             print("Velosiped")
#     else:
#         print("Samolyot")


# #6-masala
# yosh2 = int(input("Yoshingizni kiriting: "))
# daromad2 = float(input("Daromadingizni kiriting (so'mda): "))
# kredit = float(input("Kredit summasini kiriting (so'mda): "))

# if yosh2 < 18 or yosh2 > 100 or daromad2 < 0 or kredit <= 0:
#     print("Xato: Yosh 18-100 oralig'ida, daromad va kredit summasi musbat bolishi kerak.")
# else:
#     if yosh2 < 21:
#         print("Kredit berilmaydi")
#     elif yosh2 <= 60:
#         if daromad2 > kredit * 0.2:
#             print("Kredit tasdiqlanadi")
#         else:
#             print("Kredit rad etildi")
#     else:
#         print("Kredit faqat maxsus shartlarda")


# #7-masala
