from csv import reader

parameters = [
    {
        "tuning_name"      : "01",
        "learn_index"      : 200,
        "learn_num_min"    : 1000,
        "sim_num"          : [50, 100, 200],
        "judge_days"       : 5,
        "judge_border"     : 7.5,
        "min_samples_leaf" : 10,
        "max_depth"        : 12,
        "criteria"         : 70,
        "holding_border"   : 5,
        "profit_border"    : [5, 4]
    },
#     {
#         "tuning_name"      : "02",
#         "learn_index"      : 200,
#         "learn_num_min"    : 1000,
#         "sim_num"          : [50, 100, 200],
#         "judge_days"       : 5,
#         "judge_border"     : 7.5,
#         "min_samples_leaf" : 10,
#         "max_depth"        : 12,
#         "criteria"         : 70,
#         "holding_border"   : 5,
#         "profit_border"    : [4, 3]
#     },
#     {
#         "tuning_name"      : "03",
#         "learn_index"      : 200,
#         "learn_num_min"    : 1000,
#         "sim_num"          : [50, 100, 200],
#         "judge_days"       : 5,
#         "judge_border"     : 5,
#         "min_samples_leaf" : 10,
#         "max_depth"        : 15,
#         "criteria"         : 70,
#         "holding_border"   : 5,
#         "profit_border"    : [4, 3]
#     },
    {
        "tuning_name"      : "05",
        "learn_index"      : 200,
        "learn_num_min"    : 1000,
        "sim_num"          : [50, 100, 200],
        "judge_days"       : 3,
        "judge_border"     : 4,
        "min_samples_leaf" : 10,
        "max_depth"        : 12,
        "criteria"         : 70,
        "holding_border"   : 3,
        "profit_border"    : [4, 3]
    },
    {
        "tuning_name"      : "07",
        "learn_index"      : 200,
        "learn_num_min"    : 1000,
        "sim_num"          : [50, 100, 200],
        "judge_days"       : 4,
        "judge_border"     : 5,
        "min_samples_leaf" : 10,
        "max_depth"        : 12,
        "criteria"         : 70,
        "holding_border"   : 4,
        "profit_border"    : [5, 4]
    }
]

lists = {
    "judgeColList"  : ["上昇判定結果", "下落判定結果"],
    "removeColList" : ["Date", "Close_origin"],
    "renameColList" : { "Close_origin" : ["Adj Close"] }
}

paths = {
    "NODES_PATH"  : "./nodes",
    "CSV_PATH"    : "./csvs",
    "RESULT_PATH" : "./result"
}

step01_path_names = ["NODES_PATH", "CSV_PATH"]
step02_path_names = ["NODES_PATH", "CSV_PATH", "RESULT_PATH"]
step03_path_names = ["NODES_PATH", "CSV_PATH"]

step01_parameter_names = ["tuning_name", "learn_index", "learn_num_min", "judge_days", "judge_border", "min_samples_leaf", "max_depth", "criteria"]
step02_parameter_names = ["tuning_name", "learn_index", "sim_num", "judge_days", "judge_border", "holding_border", "profit_border"]
step03_parameter_names = ["tuning_name", "data_num"]

step01Paths = { key: value for key, value in paths.items() if key in step01_path_names }
step02Paths = { key: value for key, value in paths.items() if key in step02_path_names }
step03Paths = { key: value for key, value in paths.items() if key in step03_path_names }

step01Parameters = [{ key: value for key, value in dic.items() if key in step01_parameter_names } for dic in parameters]
step02Parameters = [{ key: value for key, value in dic.items() if key in step02_parameter_names } for dic in parameters]
step03Parameters = [{ key: value for key, value in dic.items() if key in step03_parameter_names } for dic in parameters]

# スクレイピング用クッキー
_n  = 'cGqXa8MFQs3ITa7NVfN3SI_uPNOsj-OkAAq89Sw8WzB3djlqQuW7m01ihhrp0XJOtv6zutHGqeV1bSR7GIj_OaXoORHxVPh5uQMuHJ1SJyTbF9RuQTbiQ8qMuvmXUlUvzefPXQmW48Pcu0xErHTVlL3ZX8mImStXFz_6rQEecjmPI2yrlr0372eEpavSsitZjuTa_efduwG0FTjQAf7A17snunKMR4j6dGUygm6w-xqT296sLCAOw0naxt_uxdBiwWhuf1nW_AzrVSyzso1KSmi4XzJVBq0a_PswNXZOwW7ebepsnZXasUrp9qd1jRRJoMVUU_7Gdk1ajtUbpiBpk4cirot2ingyiiz64zijkudBFcdv9dwfRS7o34CyBGa6sqf3oQvTi31V4evUI6TBYHfb4u9_1ZvuqRLrBWY71RZewMk9dzz5DVF6YuLH8RShzx6GwVa3Yi31OStDObztpWs2qkJXoqyT02q8XZTnQgDNpmIQ2Vm1cZSKZ1xv4vy0zZ84rqCLjtSIvTiL-LBKzAHs8dfDtIUAk9Yp1hkg5Yn6douE1oCnVQPr_J5bZrhadahHooxDvkI8sqgaWvzZepjbugZVawXJ1-LcpxRkEW-4Zxt6-YH6JoY0smTuUQ9D5CWsNl1Buhd-qtZFdl7B17z-EbMh_XtDEJoiYOR3u_eSdEy7mZiM-SRBj3HnFQR4305E0EbxbGEyUFIjrAXWdf6ORG3-T38n7ITEs_DQJxTF5IvrFYnDHU3TgoyqOax3xf93A_GOt7RonWfeY0Lw6DiKFEV73T6M5ziumdKNgonovmC1yYTHeKaGdFL6G8oJeVgTgefMLLa5bIjln-4BFCK3rZrIKUMg_bpbkWKAlBXSLQD09MOHAF751X9nwJfeeK6DAM9IYoVa0QbRF63cG-qS_dOhiKXVVM5ez59wZ-THqiDjWC4CWNdSSbspkHTJ6O8qA2vafO23Wh7-3t8NAZdeMSV1y-wk4aOoVh1FqmHubpx3uXtE3w--ZMmwgoeuoruxMB7RZ-ffoiKLFJEhL3kwjH452HdujjE2Rh15_T8UP7J0D7-K4_sLlm_ZAYK-7WZwUk6r25WO0WuLi9n-yB5TUKTOBGZObeYoDGNBUyRUDLc7YBWu-Bly-0S0qo-MiCGOnulCpewTOVqYK3mgRQ.3'
T   = 'z=CqRWjBCSgfjBdL9fH9t9Wp5MDc2MwY1MDI2MU8wNk8-&sk=DAApC1HUTICL.C&ks=EAAis1FrDbBySFRfv.B0veT.A--~F&kt=EAAv8ARNTF.qqZVksCX8rhljg--~E&ku=FAAMEYCIQDx0H6YfJtGa36QEicXlvwhsK40pXDDsV9iTGpU_MgsuwIhAOgTxGm6ghs_gEkGpDr16_8mdzkpNUGtjkzD6LirfWZX~B&d=dGlwATBKRkpGQwFhAVFBRQFnAVQzNElTSVlNN1JPM09TUlg1WTZTSVNJVTZBAXNsAU56QXhOQUV5TnpVeE5qZzNNVGctAXNjAWZpbmFuY2UBenoBQ3FSV2pCQTJK'
Y   = 'v=1&n=7or81vjtjipcr&l=5kc8o0_c8o0d8i78/o&p=m2nvvjpa52000g00&ig=00mi2&r=i0&lg=ja-JP&intl=jp'

# カラム
COL_NAME_Open="Open"
COL_NAME_High="High"
COL_NAME_Low="Low"
COL_NAME_Close="Close"
COL_NAME_Volume="Volume"
COL_NAME_Close_origin="Close_origin"

with open('./code.csv') as csv_file: cdlst = sorted([x[0] for x in list(reader(csv_file))])
# cdlst=[ "3681", "3110", "6197", "3921", "6191", "1712" ]