import json
import os

from src.data_tables.CSVDataTable import CSVDataTable


def t1():
    c_info = {
        "directory": "/Users/donaldferguson/OneDrive - ANSYS, Inc/Columbia/IntroToDBHWs/W4111HW2/Data/csv",
        "file_name": "scenes.csv"
    }
    c_tbl = CSVDataTable("scenes", connect_info=c_info,
                         columns=['seasonNum', "episodeNum", "sceneNo",
                                  "sceneStart", "sceneEnd", "location", "subLocation", "flashback"])
    print("\n************* t1 *************")
    print("CSV Table:\n", c_tbl)


def t2():
    c_info = {
        "directory": "/Users/donaldferguson/OneDrive - ANSYS, Inc/Columbia/IntroToDBHWs/W4111HW2/Data/csv",
        "file_name": "scenes.csv"
    }
    c_tbl = CSVDataTable("scenes", connect_info=c_info,
                         columns=['seasonNum', "episodeNum", "sceneNo",
                                  "sceneStart", "sceneEnd", "location", "subLocation", "flashback"])
    template = {"seasonNum": 1, "sceneNo": 12}
    result = c_tbl.find_by_template(template=template, field_list=['seasonNum', 'episodeNum', 'flashback'])
    print("Template", json.dumps(template))
    print("Fields list: ", str(['seasonNum', 'episodeNum', 'flashback']))
    print("result: \n", result)

    result2 = result.find_by_template({"episodeNum": 8})
    print("\nresult2:", result2)
    print("\n************* t1 *************")


#t1()
t2()