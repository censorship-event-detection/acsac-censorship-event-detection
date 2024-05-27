import pandas as pd
import numpy as np
import statistics as sta
import math
import pymannkendall as mk

def non_overlapping_average(k, points):
    average = []
    for i in range(0,len(points) + 1, k):
        start = i
        end = i + k
        if(len(points[start:end]) > 0):
            average.append(sta.mean(points[start:end]))
    return average

def non_overlapping_stddev(k, points):
    stddev = []
    for i in range(0,len(points) + 1, k):
        start = i
        end = i + k
        if(len(points[start:end]) > 1):
            stddev.append(sta.stdev(points[start:end]))
    return stddev

def get_dates(k, d):
    final_dates = []
    for i in range(0,len(d), k):
        final_dates.append(d[i])
    return final_dates

def mr_average(points):
    mr = []
    for i in range(1, len(points)):
        mr.append(abs(points[i] - points[i-1]))
    return sta.mean(mr)

def calculate_limits(data_points, data_set):
    if data_set == 'averages':
        stdev = non_overlapping_stddev(5, data_points)
        stddev_average = sta.mean(stdev)
        Mean = sta.mean(data_points)
        UCL = Mean + (3*stddev_average)/(0.9727*math.sqrt(5))
        LCL = Mean - (3*stddev_average)/(0.9727*math.sqrt(5))
    elif data_set == 'ratio':
        Mean = sta.mean(data_points)
        mr = mr_average(data_points)
        UCL = Mean + (3*mr/1.128)
        LCL = Mean - (3*mr/1.128)
    return Mean, UCL, LCL

def calculate_mk(v, data_points):
    mk_df = pd.DataFrame(columns=['start_date', 'end_date', v, 'trend', 'p-value'])
    window_size = 10
    start = 0
    for i in range(window_size,len(data_points) + 1):
        end = i-1
        trend, h, p, z, Tau, s, var_s, slope, intercept = mk.original_test(data_points[start:end])
        df_new_line = pd.DataFrame([[dates[start], dates[end], data_points[start], trend, p]], columns=['start_date', 'end_date', v, 'trend', 'p-value'])
        mk_df = pd.concat([mk_df, df_new_line], ignore_index=True)
        start += 1
    return mk_df

def calculate_cc(mk_df, data_type, c, dataset):
    ucl = 0
    lcl = 0
    mean = 0
    df_control_limit_points = []
    no_trend_count = 0
    calculate_new_limits = True
    above_limit_count = 0
    below_limit_count = 0
    cc_df = pd.DataFrame(columns=['Start Date', 'End Date', 'MK Signal', 'Control Limit Signal', 'Current Mean', 'Current UCL', 'Current LCL'])
    for index, row in mk_df.iterrows():
        date = row['start_date']
        end_date = row['end_date']
        m = row['trend']
        #If new limits are needed
        if calculate_new_limits:
            cc = 'Waiting'
            #Count no trend points
            if row['trend'] == 'no trend':
                no_trend_count += 1
                df_control_limit_points.append(row[version])
            else:
                #If a window has a trend reset the control limit count
                no_trend_count = 0
                df_control_limit_points = []
            #If there are 20 points in a row, new limits can be calculated
            if no_trend_count == 20:
                mean, ucl, lcl = calculate_limits(df_control_limit_points, data_type)
                #print(mean)
                #print(ucl)
                #print(lcl)
                cc = 'New limits'
                calculate_new_limits = False
                no_trend_count = 0
                df_control_limit_points = []

        #If new limits are not currently needed
        if not calculate_new_limits:
            if row[version] > ucl:
                cc = 'above limits'
                above_limit_count += 1
                below_limit_count = 0
            elif row[version] < lcl:
                cc = 'below limits'
                below_limit_count += 1
                above_limit_count = 0
            else:
                cc = 'within limits'
                above_limit_count = 0
                below_limit_count = 0
            if above_limit_count == 5 or below_limit_count == 5:
                calculate_new_limits = True
                above_limit_count = 0
                below_limit_count = 0

        df_new_line = pd.DataFrame([[date, end_date, m, cc, mean, ucl, lcl]], columns=['Start Date', 'End Date', 'MK Signal', 'Control Limit Signal', 'Current Mean', 'Current UCL', 'Current LCL'])
        cc_df = pd.concat([cc_df, df_new_line], ignore_index=True)
    
    cc_df.to_csv('../results/' + c + '-' + dataset + '.csv')

    return cc_df

def calculate_signal_dates(df_sig, c, dataset):
    df_sig_dates = pd.DataFrame(columns=['Signal Start', 'Signal End', 'Type', 'Country', 'Dataset'])
    types = ["increasing", "decreasing", "above limits", "below limits"]
    type_labels = ["MK Increasing", "MK Decreasing", "CC Above", "CC Below"]
    column_number = [2,2,3,3]

    for j in range(len(types)):
        start = False
        start_date = ""
        current_end_date = ""

        for i in range(len(df_sig)):
            signal = df_sig.iloc[i, column_number[j]]
            date = df_sig.iloc[i, 0]
            if signal == types[j] and not start:
                start = True
                start_date = date
                current_end_date = date

            if signal != types[j] and start:
                if df_sig.iloc[i-1, column_number[j]] != types[j]:
                    start = False
                    if start_date != current_end_date:
                            df_new_line = pd.DataFrame([[start_date, current_end_date, type_labels[j], c, dataset]], columns=['Signal Start', 'Signal End', 'Type', 'Country', 'Dataset'])
                            df_sig_dates = pd.concat([df_sig_dates, df_new_line], ignore_index=True)

            if signal == types[j] and start:
                current_end_date = date

        if start:
            if start_date != current_end_date:
                df_new_line = pd.DataFrame([[start_date, current_end_date, type_labels[j], c, dataset]], columns=['Signal Start', 'Signal End', 'Type', 'Country', 'Dataset'])
                df_sig_dates = pd.concat([df_sig_dates, df_new_line], ignore_index=True)
    return df_sig_dates

datasets = ['http', 'https','satellite', 'ooni', 'tor', 'gfwatch']
index = 'date'

df_final = pd.DataFrame(columns=['Signal Start', 'Signal End', 'Type', 'Country', 'Dataset'])

for d in datasets:

    countries = ['cn', 'ir', 'mm', 'pk', 'ru', 'tr']
    if d == 'ooni':
        typ = 'averages'
        version = 'total'
    elif d == 'tor':
        typ = 'averages'
        version = 'users'
        countries = ['cn', 'ir', 'pk', 'ru', 'tr']
    elif d == 'gfwatch':
        typ = 'averages'
        version = 'count'
        countries = ['cn']
    else:
        typ = 'ratio'
        version = 'ratio'

    for country in countries:
        path_to_dataset = '../data/' + d + '/' + d + '-data-' + country + '.csv'
        df = pd.read_csv(path_to_dataset, index_col=0)
        df = df.set_index(df[index])
        df = df.sort_index()

        if typ == 'averages':
            n = 5
            measure_smoothed = non_overlapping_average(n, df[version].tolist())
            dates = get_dates(n, df[index])
        if typ == 'ratio':
            measure_smoothed = df[version]
            dates = df[index]
            
        mann_kendall_df = calculate_mk(version,measure_smoothed)

        df_signals = calculate_cc(mann_kendall_df, typ, country, d)

        df_signal_dates = calculate_signal_dates(df_signals, country, d)

        print(c + " " + d)
        df_final = pd.concat([df_final, df_signal_dates], ignore_index=True)
df_final.to_csv('../results/all_signal_dates.csv')
