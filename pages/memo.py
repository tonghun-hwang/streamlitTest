import streamlit as st
from datetime import datetime
import os

st.title("Memo")
st.write("this is memo.")

memo_list = ['newMemo'] + os.listdir('memo/')
fn = st.selectbox('select memo.', memo_list)
content = '' 

if fn != 'newMemo':
    with open(f'memo/{fn}', 'r', encoding='utf-8') as f:
        content = f.read()
else:
    fn = datetime.now().strftime('%Y_%m_%d__%H_%M_%S') + '.txt'

txt = st.text_area("put your memo.", value=content)

left, right = st.columns(2)
with left:
    button = st.button ("save", use_container_width=True)
with right:
    down_button = st.download_button(
        'download', data=txt, file_name=fn, use_container_width=True
    )

if button:
    try:
        st.write("button is clicked.")
        st.write(txt)

        with open(f'memo/{fn}', 'w', encoding='utf-8') as f:
            f.write(txt)
            st.success('memo is saved.')
    except Exception as e:
        st.error(e)
