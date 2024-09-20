# Accessing the raw data
GFWatch data was downloaded from their ([Google Drive](https://drive.google.com/drive/folders/1911y0-rLfTjrcoDdgKLhMj4c8rqd0Iyd)). From the google drive we collected the `domain.rules.gz` files for each day. The files are in the format `censored domain | blocking rules | base domain` and include all of the domains found to be censored that day. For the GFWatch data in this repository, we first removed `http://`, `https://`, and `www.` from each url then counted the unique values in the censored domain column by day. 

The Tor data was downloaded from ([Tor metrics](https://metrics.torproject.org/userstats-relay-country.html)). The Tor data in this repository is the `date` and `users` values directly from the downloaded Tor data. 

The raw OONI data was downloaded using OONI's command line interface tool and processed using the source code and manual steps outlined in their online tutorial. The source code from the tutuorial labels each measurement as `ok` if the measurement was successful and no censorship was detected, `error` if the measurement was unsuccesful, and `dns`, `tls`, or `http`, if the measurement was successful but exhibited signs of censorship. The OONI data in this repository contains counts of the total successful measurements per day (i.e., all measurements minus measurements labeled `error`). Instructions for the CLI tool and tutorial can be found ([here](https://ooni.org/notebooks/tutorial-russia-data-analysis-case-study.html)).

The Censored Planet data was provided to us directly from the Censored Planet team. When we received the data, the Hyperquack HTTP and Hyperquack HTTPS measurements had already been labeled by the ([Censored Planet Data Analysis Pipeline](https://github.com/censoredplanet/censoredplanet-analysis/tree/master)). The Satellite measurements still needed to be labeled which we completed by running ([source code](https://github.com/censoredplanet/censoredplanet-analysis/blob/master/table/queries/merged_reduced_scans.sql)) also created by Censored Planet but not yet fully implemented in their pipeline. If a measurement was successful and no censorship was detected, it's label started with `expected`. If the measurement was unsuccessful, it was labeled as `error`, and the measurements that were successful but exhibited signs of censorship (refered to as "anomalies" in our paper) were labeled based on what type of censorship was present. The Censored Planet data in this repository is the ratio of anomalies to total measurements each day. 

# data folder contents:
- ([gfwatch](/data/gfwatch))
    - gfwatch-data-cn.csv: All GFWatch data
    - columns:
        - date: day measurements were collected
        - count: number of censored domains
- ([censoredplanet](/data/censoredplanet))
    - http: Hyperquack HTTP data for each country
        - http-data-\<country code>.csv
    - https: Hyperquack HTTPS data for each country
        - https-data-\<country code>.csv
    - satellite: Satellite data for each country
        - satellite-data-\<country code>.csv
    - columns:
        - date: day measurements were collected
        - measurements: Count of all valid measurements
        - ok (in the http/https files): Count of valid measurements that did not experience any interference
        - error (in the satellite files): Count of invalid measurements
        - anomalies: Count of valid measurements that experienced interference
        - ratio: anomalies/measurements
- ([ooni](/data/ooni)): OONI data for each country
    - ooni-data-\<country code>.csv
    - columns:
        - ok: Count of valid measurements that did not experience any interference
        - dns: Count of measurements that experienced interference at the DNS level
        - http: Count of measurements that experienced interference at the HTTP level
        - tls: Count of measurements that experienced interference at the TLS level
        - error: Count of invalid measurements
        - date: day measurements were collected
        - total: Count of all valid measurements
