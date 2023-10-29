#ライブラリーのインポート
import requests
import pandas as pd
import streamlit as st
import numpy as np
#- 楽天トラベルのデータ
#- 取得したデータをPandasで読み込む
# ページのタイトル
st.title("Miyako Hotel Search")
st.title('楽天トラベル_分析')
df = pd.read_csv("Miyako_hotel.csv")
#- グラフ化
import streamlit as st
import matplotlib.pyplot as plt
#- Plotlyで読む

# 数字に変換したホテル料金を追加するための空配列
x = []
y = []

# ホテル料金を数字の型に変換
# ホテル評価を数字の型に変換
# xに数字に変換したホテル料金を追加
# yに数字に変換したホテル評価を追加
for i in range(0, len(df)):
    a1 = int(df["hotelMinCharge"][i])
    a2 = float(df["reviewAverage"][i])
    
    if (a1 > 0):
        x.append(a1)
        y.append(a2)

# Streamlitアプリの設定
st.title("Scatter Plot of Hotel Data")

# グラフを表示
st.write("Scatter Plot of x and y")
st.write(x)  # xの値を表示
st.write(y)  # yの値を表示

# 散布図の作成
fig, ax = plt.subplots()
ax.scatter(x, y)

# タイトルと軸ラベルを追加
ax.set_title("Hotel Data Scatter Plot")
ax.set_xlabel("Hotel Min Charge")
ax.set_ylabel("Review Average")

# 散布図をStreamlitアプリに表示
st.pyplot(fig)

#---------------------------
import streamlit as st
import pandas as pd
import plotly.express as px

#データ読み込み
df = pd.read_csv("Miyako_hotel.csv")

#ダッシュボードのタイトル
st.title("楽天トラベルデータ可視化")

#データ表示
st.write(df)

#グラフ化
fig = px.scatter(df, x="hotelMinCharge", y="reviewAverage", color="hotelName")
st.plotly_chart(fig,use_container_width=True )
#-------------------------------------------


