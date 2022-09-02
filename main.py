import streamlit as st
import time

st.title('Streamlit 入門')

st.write('プログレスバーの表示')

'Start!!'
latest_iteration = st.empty()
bar = st.progress(0)
for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.1)
left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字表示')
if button:
    right_column.write('ここは右カラム')

expander = st.expander('問い合わせ')
# expander.write('問い合わせ内容を書く')
text = expander.text_input('問い合わせ内容を書く')
expander.write(text)
# text = st.text_input('あなたの趣味を教えてください。')
# cond = st.slider('あなたの今の調子は？', 0, 100, 50)


# 'あなたの趣味:', text
# 'コンディション', cond
# if st.checkbox('Show Image'):
#     img = Image.open('porker.png')
#     st.image(img, caption='Porker')