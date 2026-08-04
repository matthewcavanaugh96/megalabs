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

Once I had my FQS for each model, I then measured Average Pairwise Disagreement between all pairs of models. The smaller the number, the more similarly the feature performed across all models. The higher the number, the more 'controversial' the feature was. I am using Pairwise Disagreements because it goes farther than a simple Min-Max comparison. 

Finally, for each feature, I balanced both metrics to find Consistency Adjusted FQS:

    Avg_FQS
    
    -
    
    (Avg_Disagreement * 0.5)

Features with a high CAFQS are both high-performing and consistent.

""")

from PIL import Image
img = Image.open('FQS_Dataframe.png')
st.image(img)


st.write("""
For a future attempt, I will try using only the features above a CAFQS threshold, and use this new feature set on all models again to see how much improvement takes place.

I will add more models before that step.

NOTE - Differetn types of models such as RNNs may not work for this comparison.
""")

