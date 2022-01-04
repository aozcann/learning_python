# # key - value

# # 41 => kocaeli 34 => istanbul

# sehirler = ["kocaeli","istanbul"]
# plakalar = [41,34]

# print(plakalar[sehirler.index("kocaeli")])

# plakalar = { "kocaeli" : 41 , "istanbul" : 34}

# print(plakalar["kocaeli"])
# print(plakalar["istanbul"])

# plakalar["ankara"] = 6
# plakalar["kocaeli"] = "new value"

# print(plakalar)

users = {
    "sadıkturan" : {
        "age" : 36,
        "roles" : ["admin","user"],
        "email" : "sadıkturan@gmail.com",
        "address" : "kocaeli",
        "phone" : "123456"
    },
    "cınarturan" : {
        "age" : 2,
        "roles" : ["users"],
        "email" : "sadıkturan@gmail.com",
        "address" : "kocaeli",
        "phone" : "123456"
    }
}

print(users["cınarturan"])
print(users["sadıkturan"])
print(users["sadıkturan"]["age"])
print(users["sadıkturan"]["address"])
print(users["sadıkturan"]["email"])
print(users["sadıkturan"]["roles"])
print(users["cınarturan"]["roles"])





