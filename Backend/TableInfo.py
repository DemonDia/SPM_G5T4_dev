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
    "role": [
        ("Role_ID", "int"),
        ("Role_Name", "str"),
        ("Role_Description","str"),
        ("Active","bool")
    ],
    "skill":[
        ("Skill_ID","int"),
        ("Skill_Name","str"),
        ("Skill_Description","str"),
        ("Active","bool")

    ]

}
