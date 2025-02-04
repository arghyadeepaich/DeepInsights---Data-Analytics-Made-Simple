# import pandas as pd
# import plotly.express as px
# import streamlit as st

# # Configure the Streamlit page
# st.set_page_config(
#     page_title="DeepInsights",
#     page_icon="📊",
#     layout="wide",
# )
# st.markdown(
#     """
#     <style>
#     .stApp {
#         background-color: #5C166F; 
#     }
#     h1, h2, h3, h4, h5, h6 {
#         color: #FFFFFF;  /* White for headers */
#     }
#     .stMarkdown p {
#         color: #ffffff;  /* Light gray for general text */
#     }
#     .stCaption {
#         color: #FFD700;  /* Gold for captions */
#     }
#     .stTabs [data-baseweb="tab"] {
#         color: #ffffff;  /* Light gray for tab labels */
#     }
#     .stButton>button {
#         background-color: #ffffff; /* Gold background for buttons */
#         color: #FFFFFF; /* Black text on buttons */
        
#     .streamlit-expanderHeader {
#         color:  #FFFFFF !important
   
#     }
#     .st-expander-content {
#         background-color: #000000;  /* Match background with page color or use any other color */
#         color: #ffffff;  /* Set text color inside the expander */
#     }
#     </style>
#     """,
#     unsafe_allow_html=True,
# )

# # Application title and description
# st.title("Data Analytics Web Application")
# st.write(" Developed by Arghyadeep Aich")

# st.subheader("Data Analysis Made Simple: Upload your Excel or CSV files to effortlessly generate powerful insights—No coding skills needed!")

# # File uploader for user to upload data
# uploaded_file = st.file_uploader("Upload CSV or Excel file", type=['csv', 'xlsx'])

# # Initialize data as None
# data = None

# if uploaded_file is not None:
#     try:
#         # Read the uploaded file based on its format
#         if uploaded_file.name.endswith('csv'):
#             data = pd.read_csv(uploaded_file)
#         else:
#             data = pd.read_excel(uploaded_file)

#         st.success("Your file has been successfully uploaded! 🔥")
#         st.dataframe(data)
#     except Exception as e:
#         st.error(f"An error occurred while reading the file: {e}")

# # Basic information about the dataset
# st.subheader("Dataset Overview")
# summary_tab, top_bottom_tab, data_types_tab, columns_tab = st.tabs(['Summary', 'Top and Bottom Rows', 'Data Types', 'Columns'])

# if data is not None:
#     with summary_tab:
#         st.write(f'The dataset contains {data.shape[0]} rows and {data.shape[1]} columns.')
#         st.subheader('Descriptive Statistics')
#         st.dataframe(data.describe())

#     with top_bottom_tab:
#         st.subheader('Top Rows')
#         num_top_rows = st.slider("Select number of top rows to display", 1, min(100, data.shape[0]), key='topslider')
#         st.dataframe(data.head(num_top_rows))

#         st.subheader('Bottom Rows')
#         num_bottom_rows = st.slider("Select number of bottom rows to display", 1, min(100, data.shape[0]), key='bottomslider')
#         st.dataframe(data.tail(num_bottom_rows))

#     with data_types_tab:
#         st.subheader("Data Types of Each Column")
#         st.dataframe(data.dtypes)

#     with columns_tab:
#         st.subheader("Column Names in the Dataset")
#         st.write(list(data.columns))
# else:
#     st.warning("Please upload a file to view dataset information.")


# st.subheader(':grey[Column Values To Count]',divider='rainbow')
# with st.expander('Value Count'):
#     if data is not None:
#         col1, col2 = st.columns(2)
#         with col1:
#             column = st.selectbox('Choose Column name', options=list(data.columns))
#         with col2:
#             toprows = st.number_input('Top rows', min_value=1, step=1)
        
#         count = st.button('Count')
#         if count:
#             result = data[column].value_counts().reset_index().head(toprows)
#             st.dataframe(result)
#             # Visualization
#             st.subheader('Visualization', divider='gray')
#             fig = px.bar(data_frame=result, x=column, y='count', text='count', template='plotly_white')
#             st.plotly_chart(fig)
#             fig = px.line(data_frame=result, x=column, y='count', text='count', template='plotly_white')
#             st.plotly_chart(fig)
#             fig = px.pie(data_frame=result, names=column, values='count')
#             st.plotly_chart(fig)
#     else:
#         st.warning("Please upload a file to perform value counting operations.")

# # Groupby functionality for data summarization
# st.subheader("Group By: Simplifying Data Analysis")
# st.write('Use the groupby feature to summarize data based on specific categories.')

# with st.expander('Group By Columns'):
#     if data is not None:
#         col1, col2, col3 = st.columns(3)
#         with col1:
#             groupby_columns = st.multiselect('Select Columns for Grouping', options=list(data.columns))
#         with col2:
#             operation_column = st.selectbox('Select Column for Operation', options=list(data.columns))
#         with col3:
#             aggregation_operation = st.selectbox('Select Aggregation Operation', options=['sum', 'max', 'min', 'mean', 'median', 'count'])

#         if groupby_columns:
#             grouped_result = data.groupby(groupby_columns).agg(
#                 new_column=(operation_column, aggregation_operation)
#             ).reset_index()

#             st.dataframe(grouped_result)

#             st.subheader('Data Visualization')
#             graph_type = st.selectbox('Select Graph Type', options=['line', 'bar', 'scatter', 'pie'])

#             if graph_type == 'line':
#                 x_axis = st.selectbox('Select X Axis', options=list(grouped_result.columns))
#                 y_axis = st.selectbox('Select Y Axis', options=list(grouped_result.columns))
#                 color_option = st.selectbox('Color By', options=[None] + list(grouped_result.columns))
#                 line_fig = px.line(grouped_result, x=x_axis, y=y_axis, color=color_option, markers='o')
#                 st.plotly_chart(line_fig)

#             elif graph_type == 'bar':
#                 x_axis = st.selectbox('Select X Axis', options=list(grouped_result.columns))
#                 y_axis = st.selectbox('Select Y Axis', options=list(grouped_result.columns))
#                 color_option = st.selectbox('Color By', options=[None] + list(grouped_result.columns))
#                 facet_column = st.selectbox('Facet By', options=[None] + list(grouped_result.columns))
#                 bar_fig = px.bar(grouped_result, x=x_axis, y=y_axis, color=color_option, facet_col=facet_column, barmode='group')
#                 st.plotly_chart(bar_fig)

#             elif graph_type == 'scatter':
#                 x_axis = st.selectbox('Select X Axis', options=list(grouped_result.columns))
#                 y_axis = st.selectbox('Select Y Axis', options=list(grouped_result.columns))
#                 color_option = st.selectbox('Color By', options=[None] + list(grouped_result.columns))
#                 size_option = st.selectbox('Size By', options=[None] + list(grouped_result.columns))
#                 scatter_fig = px.scatter(grouped_result, x=x_axis, y=y_axis, color=color_option, size=size_option)
#                 st.plotly_chart(scatter_fig)

#             elif graph_type == 'pie':
#                 values_column = st.selectbox('Select Values Column', options=list(grouped_result.columns))
#                 names_column = st.selectbox('Select Labels Column', options=list(grouped_result.columns))
#                 pie_fig = px.pie(grouped_result, values=values_column, names=names_column)
#                 st.plotly_chart(pie_fig)

#             # Option to download grouped data
#             st.download_button(
#                 label="Download Grouped Data as CSV",
#                 data=grouped_result.to_csv(index=False).encode('utf-8'),
#                 file_name='grouped_data.csv',
#                 mime='text/csv',
#             )
#     else:
#         st.warning("Please upload a file to perform groupby operations.")






import pandas as pd
import plotly.express as px
import streamlit as st
from io import BytesIO

# Configure the Streamlit page
st.set_page_config(
    page_title="DeepInsights Pro",
    page_icon="📊",
    layout="wide",
)

# Custom CSS styling
st.markdown("""
    <style>
    .stApp {
        background-color: #2E0240;
    }
    h1, h2, h3, h4, h5, h6 {
        color: #FFFFFF;
    }
    .stMarkdown p {
        color: #F0E6F6;
    }
    .stCaption {
        color: #FFD700;
    }
    .stTabs [data-baseweb="tab"] {
        color: #FFFFFF;
    }
    .stButton>button {
        background-color: #4CAF50 !important;
        color: white !important;
    }
    .streamlit-expanderHeader {
        color: #FFFFFF !important;
    }
    .st-expander-content {
        background-color: #3A1E4D;
        color: #FFFFFF;
    }
    </style>
""", unsafe_allow_html=True)

# Application title and description
st.title("📈 DeepInsights Pro - Advanced Data Analytics")
st.markdown("""
    **Developed by Arghyadeep Aich**  
    *Transform your data into actionable insights with zero coding required!*
""")

# File uploader section
with st.expander("📤 Upload Your Data", expanded=True):
    uploaded_file = st.file_uploader(
        "Drag & Drop CSV or Excel file here",
        type=['csv', 'xlsx'],
        help="Supported formats: CSV, Excel (XLSX)"
    )

# Initialize session state for data
if 'data' not in st.session_state:
    st.session_state.data = None

# Load data with caching
@st.cache_data(show_spinner="Processing your data...")
def load_data(file):
    try:
        if file.name.endswith('csv'):
            return pd.read_csv(file)
        return pd.read_excel(file)
    except Exception as e:
        st.error(f"Error reading file: {str(e)}")
        return None

if uploaded_file:
    st.session_state.data = load_data(uploaded_file)
    if st.session_state.data is not None:
        st.success("✅ File successfully loaded!")
        with st.expander("🔍 Preview First 10 Rows"):
            st.dataframe(st.session_state.data.head(10))

# Main analysis sections
if st.session_state.data is not None:
    df = st.session_state.data
    st.markdown("---")
    
    # Dataset Overview Section
    st.header("📋 Dataset Overview")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Rows", df.shape[0])
    with col2:
        st.metric("Total Columns", df.shape[1])
    with col3:
        st.metric("Missing Values", df.isnull().sum().sum())

    # Advanced Tabs
    tab1, tab2, tab3, tab4 = st.tabs([
        "📊 Descriptive Stats", 
        "🔝 Top/Bottom Records", 
        "📑 Data Structure", 
        "🛠 Data Tools"
    ])

    with tab1:
        st.subheader("Descriptive Statistics")
        st.dataframe(df.describe(include='all').T.style.background_gradient(cmap='Blues'))

    with tab2:
        cols = st.columns(2)
        with cols[0]:
            st.subheader("Top Records")
            top_n = st.number_input("Number of top records:", 1, 100, 5, key="top_n")
            st.dataframe(df.head(top_n))
        with cols[1]:
            st.subheader("Bottom Records")
            bottom_n = st.number_input("Number of bottom records:", 1, 100, 5, key="bottom_n")
            st.dataframe(df.tail(bottom_n))

    with tab3:
        cols = st.columns(2)
        with cols[0]:
            st.subheader("Data Types")
            dtype_df = df.dtypes.reset_index()
            dtype_df.columns = ['Column', 'Data Type']
            st.dataframe(dtype_df)
        with cols[1]:
            st.subheader("Column Details")
            selected_col = st.selectbox("Select column:", df.columns)
            st.write(f"**Unique Values:** {df[selected_col].nunique()}")
            st.write(f"**Missing Values:** {df[selected_col].isnull().sum()}")

    with tab4:
        st.subheader("Advanced Data Tools")
        tool_choice = st.radio("Select Tool:", [
            "Value Distribution", 
            "Smart Grouping", 
            "Quick Visualizations"
        ], horizontal=True)

        if tool_choice == "Value Distribution":
            col = st.selectbox("Select Column:", df.columns)
            top_n = st.slider("Show Top:", 1, df[col].nunique(), 10)
            counts = df[col].value_counts().nlargest(top_n)
            
            fig_col1, fig_col2 = st.columns(2)
            with fig_col1:
                st.plotly_chart(px.bar(counts, title=f"Top {top_n} {col} Values"))
            with fig_col2:
                st.plotly_chart(px.pie(counts, names=counts.index, title="Distribution"))

        elif tool_choice == "Smart Grouping":
            with st.form("grouping_form"):
                cols = st.columns(3)
                with cols[0]:
                    group_cols = st.multiselect("Group By:", df.columns)
                with cols[1]:
                    agg_col = st.selectbox("Analyze Column:", df.select_dtypes(include='number').columns)
                with cols[2]:
                    agg_func = st.selectbox("Aggregation:", ['sum', 'mean', 'median', 'min', 'max', 'count'])
                
                if st.form_submit_button("Analyze"):
                    grouped = df.groupby(group_cols)[agg_col].agg(agg_func).reset_index()
                    st.subheader("Grouped Results")
                    st.dataframe(grouped.sort_values(agg_col, ascending=False))
                    st.plotly_chart(px.line(grouped, x=group_cols[0], y=agg_col, 
                                          title=f"{agg_func.title()} of {agg_col} by {group_cols[0]}"))

        elif tool_choice == "Quick Visualizations":
            viz_type = st.selectbox("Chart Type:", [
                "Line Chart", 
                "Bar Chart", 
                "Scatter Plot", 
                "Histogram"
            ])
            x_axis = st.selectbox("X Axis:", df.columns)
            y_axis = st.selectbox("Y Axis:", df.select_dtypes(include='number').columns if viz_type != "Histogram" else [None])
            
            if viz_type == "Line Chart":
                st.plotly_chart(px.line(df, x=x_axis, y=y_axis))
            elif viz_type == "Bar Chart":
                st.plotly_chart(px.bar(df, x=x_axis, y=y_axis))
            elif viz_type == "Scatter Plot":
                st.plotly_chart(px.scatter(df, x=x_axis, y=y_axis))
            elif viz_type == "Histogram":
                st.plotly_chart(px.histogram(df, x=x_axis))

    # Data Export Section
    st.markdown("---")
    with st.expander("💾 Export Options"):
        export_format = st.radio("Choose Export Format:", ["CSV", "Excel"])
        export_name = st.text_input("File Name:", "analyzed_data")
        
        if export_format == "CSV":
            buffer = BytesIO()
            df.to_csv(buffer, index=False)
            st.download_button(
                label="Download CSV",
                data=buffer.getvalue(),
                file_name=f"{export_name}.csv",
                mime="text/csv"
            )
        else:
            buffer = BytesIO()
            with pd.ExcelWriter(buffer, engine='xlsxwriter') as writer:
                df.to_excel(writer, index=False)
            st.download_button(
                label="Download Excel",
                data=buffer.getvalue(),
                file_name=f"{export_name}.xlsx",
                mime="application/vnd.ms-excel"
            )

else:
    st.info("ℹ️ Please upload a file to begin analysis")
    st.markdown("""
        ### Getting Started Guide:
        1. Upload your CSV or Excel file using the uploader above
        2. Explore dataset overview in the tabs
        3. Use advanced tools for in-depth analysis
        4. Export your results or visualizations
    """)
