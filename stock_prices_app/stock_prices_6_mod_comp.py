import streamlit as st


st.title("""
Feature Comparison
""")

st.write("""
For each feature for each ML model, I calculated what I'm calling Feature Quality Score (FQS). I calculated it thusly:

    0.5 * feature_importance (as determined by Scikit-Learn's built-in metric)

    +

    0.3 * inverted correlation to normalized absolute error

    +

    0.2 * inverted correlation to directional correctness

Once I had my FQS for each model, I then measured Mean Absolute Deviation of all FQS score from the average. This provided the basis of my metric Consistency. Finally, I then performed the following operation to arrive at my final scores:

    0.2 * (1 - MAD percentile) (AKA consistency)

    +

    0.8 * FQS percentile


""")

# st.write("""
# between all pairs of models. The smaller the number, the more similarly the feature performed across all models. The higher the number, the more 'controversial' the feature was. I am using Pairwise Disagreements because it goes farther than a simple Min-Max comparison. 

# Finally, for each feature, I balanced both metrics to find Consistency Adjusted FQS:

#     Avg_FQS
    
#     -
    
#     (Avg_Disagreement * 0.5)

# Features with a high CAFQS are both high-performing and consistent.

# """)

# from PIL import Image
# img = Image.open('FQS_Dataframe.png')
# st.image(img)


# st.write("""
# For a future attempt, I will try using only the features above a CAFQS threshold, and use this new feature set on all models again to see how much improvement takes place.

# I will add more models before that step.

# NOTE - Different types of models such as RNNs may not work for this comparison.
# """)




st.title("""
Stumped
""")

st.write("""
Using my Round 1 results and scoring each feature by my formula, I have tried using the top three, two, and one quartiles on a Random Forest. Results are not exactly linear - still without GridSearch, directional accuracy is 50.63% with three quartiles, 50.89% with two quartiles, and 50.00% with one quartile. Neither of these mark a notable improvement from the version that used all features.

I tried instead to test accuracy for every possible amount of features, sorting by adjusted score from high to low with each successive run cutting one from the bottom, and choose my number of features from a plot. However, I could not get this to run with a Random Forest after 6 hours.

In the absence of more precision, my next thought was to go ahead with using the top two quartiles for the other models, including ones not compatible with my original feature selection method. It is possible that by adding in more models, improvement will become noticable. 

The Linear Regression, which lacks GridSearch, under this feature set, had a directional accuracy of 49.87%.

With GridSearch, Random Forest reached ____

With GridSearch, XGBoost reached _____

With GridSearch, Gradient Booster reached _____
""")

# so I am instead running accuracy with every possible list of Features, sorted by my adjusted Score from high to low, with each successive run cutting one from the bottom. When I can visualize the exact optimal number of features, I will run the model again with that.

st.title("What next?")

st.write("""
Truthfully, I don't know what the next move is, and I don't know how confident I am in finding a truly predictive model. Directional accuracy has been barely better than 50% with anything I've tried so far.

I wonder if the better idea is something that originated as a side-analysis: measuring whether following the model's advice would produce a better long-term return than simply holding. I achieved surprisingly strong results with a rudimentary version of this principle which you can see in the next section.
""")