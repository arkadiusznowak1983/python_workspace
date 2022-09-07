import streamlit as st
from datetime import datetime
from time import sleep

from token_api import token_api


def main():
    value = token_api(key='token_api')
    if value is not None:
        print(value)
        sleep(10)
    st.button(label='aaa')
    sleep(10)


if __name__ == '__main__':
    main()
