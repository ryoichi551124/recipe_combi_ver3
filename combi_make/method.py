import numpy as np
import pandas as pd
import random
import csv
import fcntl


with open('rakuten_main.csv') as f:
    reader = csv.DictReader(f)
    main = [row for row in reader]

with open('rakuten_sub.csv') as f:
    reader = csv.DictReader(f)
    sub = [row for row in reader]

with open('rakuten_soup.csv') as f:
    reader = csv.DictReader(f)
    soup = [row for row in reader]


#OKかNOを判定してtrain.csvに組み合わせデータを追加する処理              
def choice(main_num, sub_num, soup_num, judge):

    main_num = int(main_num)
    sub_num = int(sub_num)
    soup_num = int(soup_num)

    with open('combi.csv') as f:
        fcntl.flock(f.fileno(), fcntl.LOCK_EX)

        reader = csv.DictReader(f)
        combi = [row for row in reader]

        all_list = list(combi[0].keys())[7:]

        combi[0]['主菜'] = main[main_num]['recipeTitle']
        combi[0]['副菜'] = main[sub_num]['recipeTitle']
        combi[0]['汁物'] = main[soup_num]['recipeTitle']

        for material in all_list:
            if material in main[main_num]['recipeMaterial']:
                combi[0][material] = int(combi[0][material]) + 1
            if material in main[sub_num]['recipeMaterial']:
                combi[0][material] = int(combi[0][material]) + 1
            if material in main[soup_num]['recipeMaterial']:
                combi[0][material] = int(combi[0][material]) + 1
        if judge:
            combi[0]['採用/不採用'] = 1.0  

        fcntl.flock(f.fileno(), fcntl.LOCK_UN)


    with open('train.csv', 'r+') as f:
        fcntl.flock(f.fileno(), fcntl.LOCK_EX)

        reader = csv.reader(f)
        train = [row for row in reader]
        combi[0]['ID'] = float(train[-1][1]) + 1
        writer = csv.writer(f, lineterminator='\n')
        writer.writerow(combi[0].values()) 
        f.flush()
        
        fcntl.flock(f.fileno(), fcntl.LOCK_UN)



#主菜、副菜、汁物のランダムなデータを取得
def random_get():
    main_num = random.randint(0, len(main))
    sub_num = random.randint(0, len(sub))
    soup_num = random.randint(0, len(soup))

    recipe = {
        'main_image': main[main_num]['mediumImageUrl'],
        'sub_image': sub[sub_num]['mediumImageUrl'],
        'soup_image': soup[soup_num]['mediumImageUrl'],
        'main_name': main[main_num]['recipeTitle'],
        'sub_name': sub[sub_num]['recipeTitle'],
        'soup_name': soup[soup_num]['recipeTitle'],
        'main_num': main_num,
        'sub_num': sub_num,
        'soup_num': soup_num,
    }
    return recipe

