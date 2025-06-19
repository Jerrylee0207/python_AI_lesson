import numpy as np
import pandas as pd
import os

def rank(filepath:str):
    print(filepath);
    score_pd = pd.read_excel(filepath,index_col='ID');
    sum = np.sum(score_pd, axis=1);
    avg = np.mean(score_pd, axis=1);
    score_pd["SUM"] = sum;
    score_pd["AVG"] = avg;

    score_sort = score_pd.sort_values(by="SUM", ascending=False);
    ranking = score_sort["SUM"].rank(ascending=False, method="min");
    score_sort["rank"] = ranking;
    
    curr_dir = os.path.realpath(__name__);
    root_dir = os.path.dirname(curr_dir);
    dest_folder = os.path.join(root_dir, "excel_finish");
    filename = os.path.basename(filepath);
    save_dir = os.path.join(dest_folder, filename);
    score_pd.to_excel(save_dir, index=True);

script_path = os.path.realpath(__name__);
script_root = os.path.dirname(script_path);
excel_folder = os.path.join(script_root,"excel");

for excel_name in os.listdir(excel_folder):
    excel_path = os.path.join(excel_folder,excel_name)
    rank(excel_path);