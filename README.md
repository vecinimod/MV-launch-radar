A machine vision based low cost launch monitor radar project 

Typical launch monitors costs anywhere from $400 to $20K. The goal of this project is to show what can be done with very little hardware ($6 24 Ghz doppler radar module) and tensor flow.

Table of contents
=================
* [Example](#example)
* [Parts](#parts)
* [Setup](#setup)
* [Instructions](#instructions)

Example
=======
The data from a single doppler radar recorded from a macbook microphone audio card input shows how clear to interpret the data is:
![image](https://github.com/vecinimod/MV-launch-radar/assets/7244561/e72bbc06-25ef-406f-bc4e-2d2235a817fc)

Parts
=====
The parts needed to collect radar measurements include:
1. [24 Ghz doppler radar module](https://www.amazon.com/gp/product/B07WH67J9W/ref=ppx_yo_dt_b_asin_title_o05_s00?ie=UTF8&psc=1)
2. low noise 5v DC power source (e.g. a buck converter stepped down to 5v 2s lipo battery)
3. [TRRS headphone lead](https://www.amazon.com/gp/product/B07QQPG6BT/ref=ppx_yo_dt_b_asin_title_o06_s00?ie=UTF8&psc=1)
4. optional: [amplifier](https://www.amazon.com/gp/product/B07D1VXRDL/ref=ppx_yo_dt_b_asin_title_o05_s01?ie=UTF8&psc=1)

Setup
=====
apparatus and golf ball with foil tape added

<img width="404" alt="image" src="https://github.com/vecinimod/MV-launch-radar/assets/7244561/a9131b07-2398-41b9-bf07-732aef11c841">


Instructions
============
1. connect the radar to power and microphone jack of your macbook
2. record yourself throwing a ball 10+ times using quicktime, export as audio only m4a, and write down the result of that movement (e.g. how far you throw a ball in front of the radar)
    - save the recordings as a consistent prefix file in m4a format, e.g. throw1.m4a, throw2.m4a, ...
4. store the distances from step 1 in order of the file sequence in the python array on line 56 of train_test_model.py
5. run python3 train_test_model.py to train the model and receive the error on the automatically held-out portion of samples
