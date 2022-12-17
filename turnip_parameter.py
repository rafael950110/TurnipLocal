from csv import reader

parameters = [
    {
        "tuning_name"      : "01",
        "learn_index"      : 200,
        "learn_num_min"    : 1000,
        "sim_num"          : [100, 200],
        "judge_days"       : 5,
        "judge_border"     : 7.5,
        "min_samples_leaf" : 10,
        "max_depth"        : 12,
        "criteria"         : 70,
        "holding_border"   : 5,
        "profit_border"    : [5, 4]
    },
    {
        "tuning_name"      : "05",
        "learn_index"      : 200,
        "learn_num_min"    : 1000,
        "sim_num"          : [100, 200],
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
        "sim_num"          : [100, 200],
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
_n  = 'cGqXa8MFQs3ITa7NVfN3SI_uPNOsj-OkAAq89Sw8WzB3djlqQuW7m01ihhrp0XJOtv6zutHGqeV1bSR7GIj_OcHNYF6b4Qs8cg2TnhRSYAnq00OTrogUR3toWCqILUzcfGSfmS6HbrGTp0NNYCiDE37V0NGbLlJKO43LWMvVAjplSFHIEwpJ8JurI53guZJ33avr2jMgLZ4071ZW3nXFahQMe5iRgpKfauoJ6W5hTEtITqF3TRJ0398GhOHWhK0XUnaNn6cGN-IfWq3ohu6R86aTNxIc_vjgp0ijCEidT2DTcZTo9n0vKcKp5CZ34z2ltfpwACw0ihmVg703ve58iw-VC6yBwJpW5yEr6yPwJX81T3XBZOzvHho5Mmg8d4lg6e6BinPBJgWXhYy9hLYnq_CacsTDwt-1aaGZcpT6ayU9HG5rgzvrYDRx9U_oWXGJQ1HXYuV5a9DVKBxDeZi95NQxdG4QignWvLl6PPhaU9ez8JFtnKh5RALKD-Rmt1ngKeA9gnYEqiM6onRcYWErID7fAGCi7AEsA86wMJXmiCtQFB6YYTo7IQrJUgjdp4TPJ-SIQdzcWaqhsbITdiXyGIg7MHjV0Ojx8GoK0leozDplQ14UME3d0IKhSOhLyP2RlM0aoTQ5XJbvxRTIkz1nTFItK7w9uOf8NiEU-Gb1gU63MNmdCbJEVxUvd5xa_F4zmezaseq3cd4cELg9JXG6C2NFYIKY1cMSxWBm1ilgdNlop68p_SHjcLSNYsfWbPx0h2yJkClswv998N56YBKdoTDDgHBxzPpFcaSC1N45gfM65X3OtxW85Zt3sXZ3gMbbqRLh-hMRPuRjM0dZMsPd3EH6TI6_88RTt5W_Q-E8F_fJZcd5nsQCYaY2jaxYU1ogluvmsI2fHH997mB5xh-OcvJq_Y2frmjfxFPTmUIArD1ZeQ_VBL39yIjcM-MAxeI6lnkKUQuG44HuvGNNJDz7YUslf3b-8ljicqNjpg-AMIEyCO8gtMl-YJhiBJBskYDsZnaJvvdAu9CjB9KtBRM1eTuvM9SC0r3aBD1IvSnbhgQ4muvcFPrJcI_X5VcghOfM9xaFi-LwJv9C0aA9DC3z9dCZLjXmGn_VGb6z6-qVosDWVMeMoo3Wymb7Lm_kqpQlY-1yBPHw_NXZqOAVzg7uXA.3'
T   = 'z=IpijjBIRxsjB6i/fhoEyzRKMDc2MwY1MDI2MU8wNk8-&sk=DAAGF.oyuHY2vm&ks=EAAUG4CMu8sKEBOVGAqdmThEA--~F&kt=EAATjiOZ.IRNCyrqmd8HLLv_g--~E&ku=FAAMEUCIQC3V18vM7gimE2F8HQSfYHCL8O8iGavNN1mwQIM3aSLnwIgd6Jlo5J8I_t8089b51MIvzFll4QV9Ae156EJwT2K5cQ-~B&d=dGlwATBKRkpGQwFhAVFBRQFnAVQzNElTSVlNN1JPM09TUlg1WTZTSVNJVTZBAXNsAU56QXhOQUV5TnpVeE5qZzNNVGctAXNjAXdsAXp6AUlwaWpqQkEySg--'
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