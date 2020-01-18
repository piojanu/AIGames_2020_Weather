This directory contains dataset which will be used for training purposes.
Core dataset from all weather stations is contained inside 3 .zip files -
one for each month. Inside of those .zip files you will find several .csv
files with various weather parameters. They are explained in kody_parametr.csv
file. Their meaning and units are as follow:

B00300S	Temperatura powietrza (oficjalna)
        Air temperature
        Unit - C
B00305A	Temperatura gruntu (czujnik)
        Soil temperature
        Unit - C
B00202A	Kierunek wiatru (czujnik)
        Wind direction
        Unit - degrees
B00702A	Srednia predkosc wiatru czujnik 10 minut
        Avg wind speed for the past 10 minutes
        Unit - m/s
B00703A	Predkosc maksymalna (czujnik)
        Max speed
        Unit - m/s
B00608S	Suma opadu 10 minutowego
        Precipitation sum for past 10 minutes
        Unit - mm
B00604S	Suma opadu dobowego
        Precipitation sum for past 24 hours
        Unit - mm
B00606S	Suma opadu godzinowego
        Precipitation sum for past 1 hour
        Unit - mm
B00802A	Wilgotnosc wzgledna powietrza (czujnik)
        Relative humidity
        Unit - %
B00714A	Najwiekszy poryw w okresie 10min ze stacji Synoptycznej
        Max wind gust in past 10 minutes
        Unit - m/s
B00910A	Zapas wody w sniegu (obserwator)
        Water in snow
        Unit - mm

Station coordinates (lat, long) are contained inside of ats.txt file.
This is an old database, so some of stations mentioned there are not used.
Some of stations visible in the core data will also not be present in
ats.txt.

Stations located in territory mentioned in challenge description are listed
in chosen_stations.txt. There may be more of them, but if they didn't have
coordinates in ats.txt file we skipped them for sake of this challenge.

Labels are located in train_labels.csv file. For each hour in time frame
01 Jun - 31 Aug there is an associated label 0/1. 1 means that in the next
24 hours precipitation of over 15mm in total was recorded. 0 means otherwise.

Happy hacking!

