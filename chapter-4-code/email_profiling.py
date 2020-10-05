import re
import tld
import time

import pandas as pd
import numpy as np
import cffi_re2

import time

def extract_emails(html_list, url_list, reg):
    
    email_list = []
    for i, html_res in enumerate(html_list):
        email_match = reg.findall(html_res)
        for email in email_match:
            potential_tld = "http://"+email.split('@')[1]

            try:
                res = tld.get_tld(potential_tld)
            except:
                continue

            temp_dict = {}
            temp_dict["email"] = email
            temp_dict["url"] = url_list.iloc[i]
            email_list.append(temp_dict)
    
    return email_list
    
def profile_email_regex(reg, iterations, df_html):
    
    python_engine_list = []
    for iteration in iterations:
        start_time = time.time()
        for i in range(iteration):
            email_list = extract_emails(df_html["html"], df_html["url"], reg)
        
        end_time = time.time()
        total_time = end_time-start_time
        python_engine_list.append(total_time)
        print("total time (in seconds) for " + str(iteration) + " is ", end_time-start_time)
    return email_list, python_engine_list


if __name__ == "__main__":  # confirms that the code is under main function

    df_html = pd.read_csv("/home/ubuntu/server_files/us_fda_raw_html.csv")

    iteration_list = [10,20,40,80,160,320,640]
    reg = re.compile("([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)")
    print("profiling Python 3 regex engine\n")
    email_list_py, python_engine_list = profile_email_regex(reg, iteration_list, df_html)
    
    print("profiling re2 regex engine\n")
    reg = cffi_re2.compile("([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)")
    email_list_re2, re2_engine_list = profile_email_regex(reg, iteration_list, df_html)
    
    df_emails_re2 = pd.DataFrame(email_list_re2)
    df_emails_re2.to_csv("/home/ubuntu/server_files/emails_re2.csv")
    
    df_emails_py = pd.DataFrame(email_list_py)
    df_emails_py.to_csv("/home/ubuntu/server_files/emails_py.csv")
    
    df_profile = pd.DataFrame({"iteration_no":iteration_list, "python_engine_time": python_engine_list, "re2_engine_time": re2_engine_list})
    df_profile.to_csv("/home/ubuntu/server_files/profile.csv")