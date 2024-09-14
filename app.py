import streamlit as st
import postgres

def main():
    st.set_page_config(page_title='IPL Trivia', layout = 'wide', initial_sidebar_state = 'auto')
    st.title("IPL Trivia - Powered by AlloyDB AI - NL2SQL(Preview°)")

    with st.form(key='my_form'):
        user_input = st.text_area("Enter your IPL Query here:")
        submit_button = st.form_submit_button(label='Submit')

    if submit_button:
        print(user_input)
        st.subheader("Output SQL Query : ", divider="gray")
        sql_text = postgres.fetch_query_output(user_input,False)
        st.text(sql_text)
        table_df = postgres.fetch_query_output(sql_text,True)
        st.subheader("IPL Data Trivia: ", divider="gray")
        st.write("Query data")
        st.dataframe(table_df)
        st.subheader("Visual representation : ", divider="gray")
        first_col = table_df.columns[0]  
        second_col = table_df.columns[1]  

        table_df.set_index(first_col, inplace=True)

        st.write(f"Bar Chart of {second_col} by {first_col}")
        st.bar_chart(table_df[second_col], x_label=first_col, y_label=second_col)

main()