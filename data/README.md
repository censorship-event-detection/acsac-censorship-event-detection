# Accessing the raw data
GFWatch data was downloaded from the ([GFWatch google drive](https://drive.google.com/drive/folders/1911y0-rLfTjrcoDdgKLhMj4c8rqd0Iyd)). We downloaded the `domain.rules.gz` for each day which are in the format `censored domain | blocking rules | base domain` and include all of the domains found to be censored that day. For the GFWatch data in our work, we first removed `http://`, `https://`, and `www.` from each url then counted the unique values in the `censored domain` column by day. 

Tor data was downloaded from ([Tor metrics](https://metrics.torproject.org/userstats-relay-country.html)). The Tor data in our work includes the `date` and `users` values directly from the downloaded Tor data. 

OONI data was downloaded using OONI's command line interface tool and processed using the source code and manual steps outlined in their online tutorial. The source code from the tutorial labels each measurement as `ok` if the measurement was valid and did not experience interference, `error` if the measurement was invalid, and `dns`, `tls`, or `http`, if the measurement was valid but experienced interference. The OONI data in our work includes counts of the measurements with each label per day. Instructions for the CLI tool and tutorial can be found ([here](https://ooni.org/notebooks/tutorial-russia-data-analysis-case-study.html)).

Censored Planet data was provided to us directly from the Censored Planet team. When we received the data, the Hyperquack HTTP and Hyperquack HTTPS measurements had already been labeled by the ([Censored Planet Data Analysis Pipeline](https://github.com/censoredplanet/censoredplanet-analysis/tree/master)), but the Satellite measurements still required processing. We labeled the Satellite measurements using ([source code](https://github.com/censoredplanet/censoredplanet-analysis/blob/master/table/queries/merged_reduced_scans.sql)) Censored Planet developed for the pipeline but had not yet implemented. Censored Planet's pipeline labels a measurement with `expected` if the measurement was valid and no interference was detected. If the measurement was invalid, its labeled as `error`, and the measurements that were valid but experienced interference (refered to as "anomalies" in our paper) were labeled based on what type of interference was present. The Censored Planet data in our work is the ratio of anomalies to total measurements per day. 

# data folder contents:
- ([gfwatch](/data/gfwatch))
    - gfwatch-data-cn.csv: All GFWatch data
    > columns:
        - date: day measurements were collected
        - count: number of censored domains
- ([censoredplanet](/data/censoredplanet))
    - http: Hyperquack HTTP data for each country
        - http-data-\<country code>.csv
    - https: Hyperquack HTTPS data for each country
        - https-data-\<country code>.csv
    - satellite: Satellite data for each country
        - satellite-data-\<country code>.csv
    > columns:
        - date: day measurements were collected
        - measurements: Count of all valid measurements
        - ok (in the http/https files): Count of valid measurements that did not experience any interference
        - error (in the satellite files): Count of invalid measurements
        - anomalies: Count of valid measurements that experienced interference
        - ratio: anomalies/measurements
- ([ooni](/data/ooni)): OONI data for each country
    - ooni-data-\<country code>.csv
    > columns:
        - ok: Count of valid measurements that did not experience any interference
        - dns: Count of measurements that experienced interference at the DNS level
        - http: Count of measurements that experienced interference at the HTTP level
        - tls: Count of measurements that experienced interference at the TLS level
        - error: Count of invalid measurements
        - date: day measurements were collected
        - total: Count of all valid measurements

Country Codes: CN = China, IR = Iran, MM = Myanmar, PK = Pakistan, TR = Türkiye, RU = Russia
