import streamlit as st
import pandas as pd
import plotly.express as px

def main():
    # 스트림릿에서 제공해주는 차트
    # line_chart, area_chart

    df1 = pd.read_csv('data2/lang_data.csv')

    st.dataframe(df1)
    
    lang_list = df1.columns[1:]
    choice_list = st.multiselect('언어를 선택하시오', lang_list)

    if len(choice_list) != 0:
        df_choice = df1[choice_list]
        st.dataframe(df_choice)

        #스트림릿이 제공하는 line_chart
        st.line_chart(df_choice)

        # 스트림릿이 제고하는 area_chart
        st.area_chart(df_choice)
    
    df2 = pd.read_csv('data2/iris.csv')
    st.dataframe(df2)

    #스트림릿이 제공하는 bar_chart
    st.bar_chart(df2.iloc[:, : -2 +1 ])

   

if __name__=='__main__':
    main()