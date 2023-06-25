# Bike Sharing Study Case: GIRA, Lisbon

## Introduction
GIRA is the sharing bike project from Lisbon city. Created in 2019, it's part of Lison goverment iniciative to became the green capital of Europe. The main goal of this project is to enhance the usability of the shared bicicles by understanding demand patterns.

## The dataset
Information about GIRA station position and the amount of bicicles per station are publically available on [Lisboa Aberta](https://lisboaaberta.cm-lisboa.pt/index.php/pt/mobilidade). Information include:
- Station position
- Number of docs on the station
- Number of bicicles
- Timestamp of update

## EDA
Starting with an exploratory data analysis, I realized that the time stamp is not evenly distributed and range from 20 minutes to 7 hours. I resampled the data in an hourly frequency and filled up the remain blanck spaces with an interpolation on the number of bicicles available. 
