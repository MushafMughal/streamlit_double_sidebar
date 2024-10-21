import streamlit as st


sidebar_style = '''
    <style>

    #root > div:nth-child(1) > div.withScreencast > div > div > div > section.stAppViewMain.main > div.stAppViewBlockContainer.block-container > div > div > div > div > div:first-child {
	font-size: 16px;
    	font-family: "Source Sans Pro", sans-serif;
    	font-weight: 400;
    	line-height: 1.6;
    	text-size-adjust: 100%;
    	-webkit-tap-highlight-color: rgba(0, 0, 0, 0);
    	-webkit-font-smoothing: auto;
    	color: rgb(49, 51, 63);
    	color-scheme: light;
    	box-sizing: border-box;
    	width: 550px !important;
    	margin-right: 20px !important;
        flex: none !important;
    }
    
    #root > div:nth-child(1) > div.withScreencast > div > div > div > section.stAppViewMain.main > div.stAppViewBlockContainer.block-container {
        max-width: 55rem;
    }

    #right-sidebar-filters {
	    text-size-adjust: 100%;
    	-webkit-tap-highlight-color: rgba(0, 0, 0, 0);
    	-webkit-font-smoothing: auto;
    	color-scheme: light;
    	word-break: break-word;
    	text-wrap: pretty;
    	box-sizing: border-box;
    	font-family: "Source Sans Pro", sans-serif;
    	font-weight: 600;
    	color: rgb(49, 51, 63);
    	padding: 1.25rem 0px 1rem;
    	margin: 0px;
    	line-height: 1.2;
    	font-size: 1.5rem;
    	scroll-margin-top: 3.75rem;
    }

    #root > div:nth-child(1) > div.withScreencast > div > div > div > section.stAppViewMain.main > div.stAppViewBlockContainer.block-container > div {
        margin-top: -40px;
    }
    </style> 
    '''
st.markdown(sidebar_style, unsafe_allow_html=True)


# Left Sidebar - Filters
st.sidebar.title("Left Sidebar - Filters")
left_filter1 = st.sidebar.selectbox("Select Category", ["Category 1", "Category 2", "Category 3"])
left_filter2 = st.sidebar.slider("Select Range", 0, 100, (25, 75))

st.sidebar.write("Selected Category:", left_filter1)
st.sidebar.write("Selected Range:", left_filter2)

# Main Content Layout - with columns
col2, col3 = st.columns([3, 1])

# Main Content Area
with col2:
    st.title("Main Content Area")
    user_input = st.text_input("Enter some input:")
    st.write("You entered:", user_input)

# Right Sidebar - Filters
with col3:
    st.title("Right Sidebar - Filters")
    right_filter1 = st.selectbox("Select Option", ["Option 1", "Option 2", "Option 3"])
    right_filter2 = st.multiselect("Select Multiple Options", ["Option A", "Option B", "Option C"])

    st.write("Selected Option:", right_filter1)
    st.write("Selected Multiple Options:", right_filter2)