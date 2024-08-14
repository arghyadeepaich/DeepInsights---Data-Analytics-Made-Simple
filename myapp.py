import pandas as pd
import plotly.express as px
import streamlit as st

# Configure the Streamlit page
st.set_page_config(
    page_title="DeepInsights",
    page_icon="📊",
    layout="wide",
)
st.markdown(
    """
    <style>
    .stApp {
        background-color: #5C166F; 
   
    }
    </style>
    """,
    unsafe_allow_html=True,
)
# Application title and description
st.title(":white[Data Analytics Web Application]")
st.caption("### Developed by Arghyadeep Aich")

st.subheader("Data Analysis Made Simple: Upload your Excel or CSV files to effortlessly generate powerful insights—No coding skills needed!")

# File uploader for user to upload data
uploaded_file = st.file_uploader("Upload CSV or Excel file", type=['csv', 'xlsx'])

# Initialize data as None
data = None

if uploaded_file is not None:
    try:
        # Read the uploaded file based on its format
        if uploaded_file.name.endswith('csv'):
            data = pd.read_csv(uploaded_file)
        else:
            data = pd.read_excel(uploaded_file)

        st.success("Your file has been successfully uploaded! 🔥")
        st.dataframe(data)
    except Exception as e:
        st.error(f"An error occurred while reading the file: {e}")

# Basic information about the dataset
st.subheader("Dataset Overview")
summary_tab, top_bottom_tab, data_types_tab, columns_tab = st.tabs(['Summary', 'Top and Bottom Rows', 'Data Types', 'Columns'])

if data is not None:
    with summary_tab:
        st.write(f'The dataset contains {data.shape[0]} rows and {data.shape[1]} columns.')
        st.subheader('Descriptive Statistics')
        st.dataframe(data.describe())

    with top_bottom_tab:
        st.subheader('Top Rows')
        num_top_rows = st.slider("Select number of top rows to display", 1, min(100, data.shape[0]), key='topslider')
        st.dataframe(data.head(num_top_rows))

        st.subheader('Bottom Rows')
        num_bottom_rows = st.slider("Select number of bottom rows to display", 1, min(100, data.shape[0]), key='bottomslider')
        st.dataframe(data.tail(num_bottom_rows))

    with data_types_tab:
        st.subheader("Data Types of Each Column")
        st.dataframe(data.dtypes)

    with columns_tab:
        st.subheader("Column Names in the Dataset")
        st.write(list(data.columns))
else:
    st.warning("Please upload a file to view dataset information.")

st.subheader("Column Values To Count")
with st.expander('Value Count'):
    if data is not None:
        col1, col2 = st.columns(2)
        with col1:
            column = st.selectbox('Choose Column name', options=list(data.columns))
        with col2:
            toprows = st.number_input('Top rows', min_value=1, max_value=100, step=1)

        count = st.button('Count')
        if count:
            result = data[column].value_counts().reset_index().head(toprows)
            st.dataframe(result)

            st.subheader('Visualization')
            fig = px.bar(result, x='index', y=column, text=column, template='plotly_white')
            st.plotly_chart(fig)
            fig = px.line(result, x='index', y=column, text=column, template='plotly_white')
            st.plotly_chart(fig)
            fig = px.pie(result, names='index', values=column)
            st.plotly_chart(fig)
    else:
        st.warning("Please upload a file to perform value counts.")

# Groupby functionality for data summarization
st.subheader("Group By: Simplifying Data Analysis")
st.write('Use the groupby feature to summarize data based on specific categories.')

with st.expander('Group By Columns'):
    if data is not None:
        col1, col2, col3 = st.columns(3)
        with col1:
            groupby_columns = st.multiselect('Select Columns for Grouping', options=list(data.columns))
        with col2:
            operation_column = st.selectbox('Select Column for Operation', options=list(data.columns))
        with col3:
            aggregation_operation = st.selectbox('Select Aggregation Operation', options=['sum', 'max', 'min', 'mean', 'median', 'count'])

        if groupby_columns:
            grouped_result = data.groupby(groupby_columns).agg(
                new_column=(operation_column, aggregation_operation)
            ).reset_index()

            st.dataframe(grouped_result)

            st.subheader('Data Visualization')
            graph_type = st.selectbox('Select Graph Type', options=['line', 'bar', 'scatter', 'pie'])

            if graph_type == 'line':
                x_axis = st.selectbox('Select X Axis', options=list(grouped_result.columns))
                y_axis = st.selectbox('Select Y Axis', options=list(grouped_result.columns))
                color_option = st.selectbox('Color By', options=[None] + list(grouped_result.columns))
                line_fig = px.line(grouped_result, x=x_axis, y=y_axis, color=color_option, markers='o')
                st.plotly_chart(line_fig)

            elif graph_type == 'bar':
                x_axis = st.selectbox('Select X Axis', options=list(grouped_result.columns))
                y_axis = st.selectbox('Select Y Axis', options=list(grouped_result.columns))
                color_option = st.selectbox('Color By', options=[None] + list(grouped_result.columns))
                facet_column = st.selectbox('Facet By', options=[None] + list(grouped_result.columns))
                bar_fig = px.bar(grouped_result, x=x_axis, y=y_axis, color=color_option, facet_col=facet_column, barmode='group')
                st.plotly_chart(bar_fig)

            elif graph_type == 'scatter':
                x_axis = st.selectbox('Select X Axis', options=list(grouped_result.columns))
                y_axis = st.selectbox('Select Y Axis', options=list(grouped_result.columns))
                color_option = st.selectbox('Color By', options=[None] + list(grouped_result.columns))
                size_option = st.selectbox('Size By', options=[None] + list(grouped_result.columns))
                scatter_fig = px.scatter(grouped_result, x=x_axis, y=y_axis, color=color_option, size=size_option)
                st.plotly_chart(scatter_fig)

            elif graph_type == 'pie':
                values_column = st.selectbox('Select Values Column', options=list(grouped_result.columns))
                names_column = st.selectbox('Select Labels Column', options=list(grouped_result.columns))
                pie_fig = px.pie(grouped_result, values=values_column, names=names_column)
                st.plotly_chart(pie_fig)

            # Option to download grouped data
            st.download_button(
                label="Download Grouped Data as CSV",
                data=grouped_result.to_csv(index=False).encode('utf-8'),
                file_name='grouped_data.csv',
                mime='text/csv',
            )
    else:
        st.warning("Please upload a file to perform groupby operations.")
