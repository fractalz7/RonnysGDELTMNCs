
# coding: utf-8

# In[11]:

# Quick prototype to demonstrate a concept, by Ronny Ashar
# April 28, 2018
# I have extracted GDELT MNC(Multinational Corporations) data for a particular date and plot WordCloulds
# to get a quick indication of Positive and Negative sentiments in media coverage related to the MNCs
# Reference: http://data.gdeltproject.org
# Reference: wordCloud courtesy of Andreas Miller, https://amueller.github.io/word_cloud/index.html

import wordcloud
import matplotlib.pyplot as plt
import random
from os import path
from wordcloud import WordCloud

#d = path.dirname(__file__)
def gray_color_func(word, font_size, position, orientation, random_state=None,
                    **kwargs):
    return "hsl(0, 0%%, %d%%)" % random.randint(60, 100)

def plotCloud(date, filePositive, fileNegative):
    # Read the whole text.
    textPositive = open(filePositive).read()
    textNegative = open(fileNegative).read()
    
    #wc = WordCloud(max_words=1000, mask=mask, stopwords=stopwords, margin=10,
     #          random_state=1).generate(text)
    wcPos = WordCloud(margin=1, random_state=1).generate(textPositive)
    wcNeg = WordCloud(margin=1, random_state=1).generate(textNegative)
    # store default colored image
    default_colors = wcPos.to_array()
    
    plt.subplots(1,2,figsize=(15, 15))
        
    plt.subplot(1, 2, 1)
    plt.title(date + " - Positive Sentiment")
    plt.imshow(default_colors, interpolation="bilinear")
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.title(date + " - Negative Sentiment")
    plt.imshow(wcNeg.recolor(color_func=gray_color_func, random_state=3),
            interpolation="bilinear")
    plt.axis("off")
        #wc.to_file("a_new_hope.png")
        
    
    #plt.figure()
    plt.show()

    return

plotCloud("April 20, 2018", "C:\DataIncubator\Project\TonePositiveNeutralApril202018.txt", "C:\DataIncubator\Project\ToneNegativeApril202018.txt")


# In[ ]:



