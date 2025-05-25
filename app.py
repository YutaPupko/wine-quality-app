import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("winequality-red.csv")

st.title("Red Wine Quality Explorer 🍷")
st.write("Explore the relationships between different wine properties and their quality.")

# Histogram selection
feature = st.selectbox("Choose a feature to visualize:", df.columns[:-1])

st.subheader(f"Distribution of {feature}")
fig1, ax1 = plt.subplots()
sns.histplot(df[feature], kde=True, ax=ax1)
st.pyplot(fig1)

# Boxplot for feature vs. quality
st.subheader(f"{feature} vs. Quality")
fig2, ax2 = plt.subplots()
sns.boxplot(x='quality', y=feature, data=df, ax=ax2)
st.pyplot(fig2)

# Insights
st.subheader("📌 Key Insights")
st.markdown("""
- Higher alcohol and sulphates are associated with better wine quality.
- Wines with high volatile acidity tend to have lower quality.
- Density tends to decrease as quality increases.
""")
