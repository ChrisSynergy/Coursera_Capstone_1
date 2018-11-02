{
    "nbformat_minor": 1, 
    "cells": [
        {
            "source": "This notebook will be mainly used for the capstone project.", 
            "cell_type": "markdown", 
            "metadata": {
                "collapsed": true
            }
        }, 
        {
            "execution_count": 1, 
            "cell_type": "code", 
            "metadata": {}, 
            "outputs": [], 
            "source": "import pandas as pd"
        }, 
        {
            "execution_count": 2, 
            "cell_type": "code", 
            "metadata": {}, 
            "outputs": [], 
            "source": "import numpy as np"
        }, 
        {
            "execution_count": 3, 
            "cell_type": "code", 
            "metadata": {}, 
            "outputs": [
                {
                    "output_type": "stream", 
                    "name": "stdout", 
                    "text": "Hello Capstone Project Course!\n"
                }
            ], 
            "source": "print('Hello Capstone Project Course!')"
        }, 
        {
            "execution_count": null, 
            "cell_type": "code", 
            "metadata": {}, 
            "outputs": [], 
            "source": ""
        }, 
        {
            "source": "<html>\n<head>\n  <title>Capstone Project Report</title>\n  <style>\n    body {\n      background-color: #f7f7f7;\n    }\n  </style>\n</head>\n\n<body>\n  <h1>Project Report</h1>\n  <h2>Introduction/Business Problem </h2>\n    \n  \n    A client wants to oepn a coffee shop but they don't know where to locate the coffee shop.\n    The client is struggling to find the exact spot or location where to open the coffee shop.\n    The client is targeting middle class to high class customers in between New York and Torono.\n    The client wants their coffee shop to be the best but also have reasonable prices.\n    \n    This project aims to make it easy for the client to find a perfect spot to open their coffee shop,\n    by providing all nearby locations or spots around New York and Toronto.\n    \n    This project will try to build and make recommendations which will be a guiding line to the client.\n    \n    Data:\n    \n    The data will be collected from Foursquare. The data will be about the municipalities in New York and Toronto\n    which includes all the locations within New York and Toronto.\n    \n    The data will allow us to inspect and find a suitable location or spot for the client to open their coffee shop.\n    \n    Methodology:\n    \n    K-Means was used to cluster or segment the neighborhoods based on their similarities.\n    \n    This method will make it easy for the client to make an informed decision about the location\n    to open their coffee shop.\n    \n    Results:\n    \n    K-Means produced the results which were looked into. Based on the feautures around the areas,\n    5 clusters were found. Each cluster has it's unique features.\n    It is hard to find the perfect spot but the client will make an informed decition based on the\n    characteristics in each cluster.\n    \n    Conclusion:\n    \n    After careful assessment, the spots which seems to be the perfect spots are the ones situated\n    around shopping centres.\n \n</body>\n\n</html>\n", 
            "cell_type": "markdown", 
            "metadata": {}
        }, 
        {
            "execution_count": null, 
            "cell_type": "code", 
            "metadata": {}, 
            "outputs": [], 
            "source": "\n\n"
        }, 
        {
            "source": "<html>\n<head>\n  <title>Capstone Project Report</title>\n  <style>\n    body {\n      background-color: #f7f7f7;\n    }\n  </style>\n</head>\n\n<body>\n  <h1>Project Presentation</h1>\n  <h2>Introduction/Business Problem </h2>\n    \n  \n    A client wants to oepn a coffee shop but they don't know where to locate the coffee shop.\n    The client is struggling to find the exact spot or location where to open the coffee shop.\n    The client is targeting middle class to high class customers in between New York and Torono.\n    The client wants their coffee shop to be the best but also have reasonable prices.\n    \n    This project aims to make it easy for the client to find a perfect spot to open their coffee shop,\n    by providing all nearby locations or spots around New York and Toronto.\n    \n    This project will try to build and make recommendations which will be a guiding line to the client.\n    \n \n \n</body>\n\n</html>\n", 
            "cell_type": "markdown", 
            "metadata": {}
        }, 
        {
            "source": "<html>\n<head>\n  <title>Capstone Project Report</title>\n  <style>\n    body {\n      background-color: #f7f7f7;\n    }\n  </style>\n</head>\n\n<body>\n  <h1>Project Presentation</h1>\n  <h2>Data </h2>\n    \n  \n    The data will be collected from Foursquare. The data will be about the municipalities in New York and Toronto\n    which includes all the locations within New York and Toronto.\n    \n    The data will allow us to inspect and find a suitable location or spot for the client to open their coffee shop.\n    \n \n</body>\n\n</html>", 
            "cell_type": "markdown", 
            "metadata": {}
        }, 
        {
            "source": "<html>\n<head>\n  <title>Capstone Project Report</title>\n  <style>\n    body {\n      background-color: #f7f7f7;\n    }\n  </style>\n</head>\n\n<body>\n  <h1>Project Presentation</h1>\n  <h2>Methodology </h2>\n    \n    \n    K-Means was used to cluster or segment the neighborhoods based on their similarities.\n    \n    This method will make it easy for the client to make an informed decision about the location\n    to open their coffee shop.\n    \n \n \n</body>\n\n</html>", 
            "cell_type": "markdown", 
            "metadata": {}
        }, 
        {
            "source": "<html>\n<head>\n  <title>Capstone Project Report</title>\n  <style>\n    body {\n      background-color: #f7f7f7;\n    }\n  </style>\n</head>\n\n<body>\n  <h1>Project Presentation</h1>\n  <h2>Results </h2>\n    \n  \n    K-Means produced the results which were looked into. Based on the feautures around the areas,\n    5 clusters were found. Each cluster has it's unique features.\n    It is hard to find the perfect spot but the client will make an informed decition based on the\n    characteristics in each cluster.\n    \n \n</body>\n\n</html>", 
            "cell_type": "markdown", 
            "metadata": {}
        }, 
        {
            "source": "<html>\n<head>\n  <title>Capstone Project Report</title>\n  <style>\n    body {\n      background-color: #f7f7f7;\n    }\n  </style>\n</head>\n\n<body>\n  <h1>Project Presentation</h1>\n  <h2>Conclusion </h2>\n    \n  \n    After careful assessment, the spots which seems to be the perfect spots are the ones situated\n    around shopping centres.\n    \n \n</body>\n\n</html>", 
            "cell_type": "markdown", 
            "metadata": {}
        }, 
        {
            "execution_count": 36, 
            "cell_type": "code", 
            "metadata": {}, 
            "outputs": [], 
            "source": ""
        }, 
        {
            "execution_count": 12, 
            "cell_type": "code", 
            "metadata": {}, 
            "outputs": [], 
            "source": ""
        }, 
        {
            "execution_count": null, 
            "cell_type": "code", 
            "metadata": {}, 
            "outputs": [], 
            "source": ""
        }, 
        {
            "execution_count": null, 
            "cell_type": "code", 
            "metadata": {}, 
            "outputs": [], 
            "source": ""
        }, 
        {
            "execution_count": null, 
            "cell_type": "code", 
            "metadata": {}, 
            "outputs": [], 
            "source": ""
        }, 
        {
            "execution_count": null, 
            "cell_type": "code", 
            "metadata": {}, 
            "outputs": [], 
            "source": "\n"
        }, 
        {
            "execution_count": null, 
            "cell_type": "code", 
            "metadata": {}, 
            "outputs": [], 
            "source": ""
        }
    ], 
    "metadata": {
        "kernelspec": {
            "display_name": "Python 3.5", 
            "name": "python3", 
            "language": "python"
        }, 
        "language_info": {
            "mimetype": "text/x-python", 
            "nbconvert_exporter": "python", 
            "version": "3.5.5", 
            "name": "python", 
            "file_extension": ".py", 
            "pygments_lexer": "ipython3", 
            "codemirror_mode": {
                "version": 3, 
                "name": "ipython"
            }
        }
    }, 
    "nbformat": 4
}