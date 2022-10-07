# ==================== names of columns for each entity ====================
# data types:
# float --> corresponding number (.0)
# int --> corresponding number
# bool --> True/False
# string -->  col_name #number
# datetime --> datetime.today()  (import datetime)

from datetime import datetime
# the key of the dictionary is  name of the model
#format:
'''
Format:
model_name:[
    (column_name,column_datatype)
]
'''
#please refer to the model inside the Models folder
modelColumnInfo = {
    "track": [
        ("id", "int"),
        ("title", "str"),
        ("artist", "str"),
        ("duration", "float"),
        ("last_play", "datetime")
    ],

    "role": [
        ("id", "int"),
        ("role_name", "str"),
        ("role_description","str"),
        ("active","bool")
    ],
    "skill":[
        ("id","int"),
        ("skill_name","str"),
        ("skill_description","str"),
        ("active","bool")

    ]

}
