import streamlit as st
import time

st.title('Streamlit 超入門')

st.write('プログレスバーの表示')
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)
for i in range(100):
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i+1)
  time.sleep(0.1)

'Done!!'

left_colum, right_colum = st.columns(2)
button = left_colum.button('右コラムに文字を表示')
if button:
  right_colum.write('ここは右コラム')

expander = st.expander('問い合わせ')
expander.write('問い合わせ内容を書く')
