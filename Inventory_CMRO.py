import pandas as pd
import streamlit as st


# Function to filter stock data
def filter_stock_data(uploaded_file):
    # Check if the file is uploaded
    if uploaded_file is not None:
        # Read the uploaded file
        df_stock = pd.read_csv(uploaded_file, encoding="latin-1")
        df_stock["Value_USD"].fillna(0, inplace=True)
        return df_stock
    else:
        st.error("Please upload a file.")
        return pd.DataFrame()  # Return an empty DataFrame if no file is uploaded


# Function to calculate total value
def calculate_total_value(df_stock):
    total_value_USD = "{:,.2f}".format(df_stock["Value_USD"].sum())
    return f"Total Reporting Inventory Value: ${total_value_USD}"


# Function to calculate label value and plot
def calculate_label_value(df_stock):
    label_value_df = df_stock.groupby("LABEL")["Value_USD"].sum().reset_index()
    label_value_df["Value_USD"] = label_value_df["Value_USD"].apply(
        lambda x: "{:,.2f}".format(x)
    )

    label_value_str = "Label Value in USD:<br>"
    for index, row in label_value_df.iterrows():
        label_value_str += f"{row['LABEL']} {row['Value_USD']}<br>"

    # Convert formatted strings back to float for plotting
    label_value_df["Value_USD"] = (
        label_value_df["Value_USD"].str.replace(",", "").astype(float)
    )

    return label_value_str, label_value_df


# Function to calculate fleet value and plot
def calculate_fleet_value(df_stock):
    fleet_value_df = (
        df_stock.groupby("COMBINED_FLEET_SHORT")["Value_USD"].sum().reset_index()
    )
    fleet_value_df["Value_USD"] = fleet_value_df["Value_USD"].apply(
        lambda x: "{:,.2f}".format(x)
    )

    fleet_value_str = "Fleet Short Value:<br>"
    for index, row in fleet_value_df.iterrows():
        fleet_value_str += f"{row['COMBINED_FLEET_SHORT']} {row['Value_USD']}<br>"

    # Convert formatted strings back to float for plotting
    fleet_value_df["Value_USD"] = (
        fleet_value_df["Value_USD"].str.replace(",", "").astype(float)
    )

    return fleet_value_str, fleet_value_df


# Function to calculate purchased for value and plot
def calculate_purchased_for_value(df_stock):
    purchased_for_value_df = (
        df_stock.groupby("Purchased for")["Value_USD"].sum().reset_index()
    )
    purchased_for_value_df["Value_USD"] = purchased_for_value_df["Value_USD"].apply(
        lambda x: "{:,.2f}".format(x)
    )

    purchased_for_value_str = "Purchased For:<br>"
    for index, row in purchased_for_value_df.iterrows():
        purchased_for_value_str += f"{row['Purchased for']} {row['Value_USD']}<br>"

    # Convert formatted strings back to float for plotting
    purchased_for_value_df["Value_USD"] = (
        purchased_for_value_df["Value_USD"].str.replace(",", "").astype(float)
    )

    return purchased_for_value_str, purchased_for_value_df


def calculate_cons_cat_value(df_stock):
    cons_cat_value_df = (
        df_stock.groupby("cons_cat_new")["Value_USD"].sum().reset_index()
    )
    cons_cat_value_df["Value_USD"] = cons_cat_value_df["Value_USD"].apply(
        lambda x: "{:,.2f}".format(x)
    )

    cons_cat_value_str = "Consumption Category:<br>"
    for index, row in cons_cat_value_df.iterrows():
        cons_cat_value_str += f"{row['cons_cat_new']} {row['Value_USD']}<br>"

    # Convert formatted strings back to float for plotting
    cons_cat_value_df["Value_USD"] = (
        cons_cat_value_df["Value_USD"].str.replace(",", "").astype(float)
    )

    return cons_cat_value_str, cons_cat_value_df


def calculate_NEW_INV_LABEL_value(df_stock):
    NEW_INV_LABEL_value_df = (
        df_stock.groupby("NEW_INV_LABEL")["Value_USD"].sum().reset_index()
    )
    NEW_INV_LABEL_value_df["Value_USD"] = NEW_INV_LABEL_value_df["Value_USD"].apply(
        lambda x: "{:,.2f}".format(x)
    )

    NEW_INV_LABEL_value_str = "Consumption Category:<br>"
    for index, row in NEW_INV_LABEL_value_df.iterrows():
        NEW_INV_LABEL_value_str += f"{row['NEW_INV_LABEL']} {row['Value_USD']}<br>"

    # Convert formatted strings back to float for plotting
    NEW_INV_LABEL_value_df["Value_USD"] = (
        NEW_INV_LABEL_value_df["Value_USD"].str.replace(",", "").astype(float)
    )

    return NEW_INV_LABEL_value_str, NEW_INV_LABEL_value_df


def calculate_SUB_INV_DESC_value(df_stock):
    SUB_INV_DESC_value_df = (
        df_stock.groupby("SUB INV DESC")["Value_USD"].sum().reset_index()
    )
    SUB_INV_DESC_value_df["Value_USD"] = SUB_INV_DESC_value_df["Value_USD"].apply(
        lambda x: "{:,.2f}".format(x)
    )

    SUB_INV_DESC_value_str = "Sub Inventory Desc:<br>"
    for index, row in SUB_INV_DESC_value_df.iterrows():
        SUB_INV_DESC_value_str += f"{row['SUB INV DESC']} {row['Value_USD']}<br>"

    # Convert formatted strings back to float for plotting
    SUB_INV_DESC_value_df["Value_USD"] = (
        SUB_INV_DESC_value_df["Value_USD"].str.replace(",", "").astype(float)
    )

    return SUB_INV_DESC_value_str, SUB_INV_DESC_value_df


def calculate_Age_Yrs_value(df_stock):
    Age_Yrs_value_df = df_stock.groupby("Age Yrs")["Value_USD"].sum().reset_index()
    Age_Yrs_value_df["Value_USD"] = Age_Yrs_value_df["Value_USD"].apply(
        lambda x: "{:,.2f}".format(x)
    )

    Age_Yrs_value_str = "Age in Years:<br>"
    for index, row in Age_Yrs_value_df.iterrows():
        Age_Yrs_value_str += f"{row['Age Yrs']} {row['Value_USD']}<br>"

    # Convert formatted strings back to float for plotting
    Age_Yrs_value_df["Value_USD"] = (
        Age_Yrs_value_df["Value_USD"].str.replace(",", "").astype(float)
    )

    return Age_Yrs_value_str, Age_Yrs_value_df


# Streamlit app
def main():
    st.title("Inventory Calculator")

    # Initialize session state
    if "selected_option" not in st.session_state:
        st.session_state.selected_option = "Inventory Latest Value"

    # File uploader widget
    uploaded_file = st.file_uploader("Choose the CMRO Stock file.", type="csv")

    # Check if a file is uploaded
    df_stock = filter_stock_data(uploaded_file)

    st.sidebar.header("Options")

    if st.sidebar.button("Inventory Latest Value"):
        st.session_state.selected_option = "Inventory Latest Value"

    if st.sidebar.button("Label Value"):
        st.session_state.selected_option = "Label Value"

    if st.sidebar.button("Fleet Short Value"):
        st.session_state.selected_option = "Fleet Short Value"

    if st.sidebar.button("Purchased For Value"):
        st.session_state.selected_option = "Purchased For Value"

    if st.sidebar.button("Consumption Category Value"):
        st.session_state.selected_option = "Consumption Category Value"

    if st.sidebar.button("InvLabel Safety Stock Value"):
        st.session_state.selected_option = "InvLabel Safety Stock Value"

    if st.sidebar.button("Sub Inv Desc Value"):
        st.session_state.selected_option = "Sub Inv Desc Value"

    if st.sidebar.button("Age In Years Value"):
        st.session_state.selected_option = "Age In Years Value"

    if st.session_state.selected_option == "Inventory Latest Value":
        if not df_stock.empty:
            st.write(calculate_total_value(df_stock))

    elif st.session_state.selected_option == "Label Value":
        if not df_stock.empty:
            label_value_str, label_value_df = calculate_label_value(df_stock)
            st.markdown(label_value_str, unsafe_allow_html=True)
            st.bar_chart(label_value_df.set_index("LABEL")["Value_USD"])

    elif st.session_state.selected_option == "Fleet Short Value":
        if not df_stock.empty:
            fleet_value_str, fleet_value_df = calculate_fleet_value(df_stock)
            st.markdown(fleet_value_str, unsafe_allow_html=True)
            st.bar_chart(fleet_value_df.set_index("COMBINED_FLEET_SHORT")["Value_USD"])

    elif st.session_state.selected_option == "Purchased For Value":
        if not df_stock.empty:
            (
                purchased_for_value_str,
                purchased_for_value_df,
            ) = calculate_purchased_for_value(df_stock)
            st.markdown(purchased_for_value_str, unsafe_allow_html=True)
            st.bar_chart(purchased_for_value_df.set_index("Purchased for")["Value_USD"])

    elif st.session_state.selected_option == "Consumption Category Value":
        if not df_stock.empty:
            cons_cat_value_str, cons_cat_value_df = calculate_cons_cat_value(df_stock)
            st.markdown(cons_cat_value_str, unsafe_allow_html=True)
            st.bar_chart(cons_cat_value_df.set_index("cons_cat_new")["Value_USD"])

    elif st.session_state.selected_option == "InvLabel Safety Stock Value":
        if not df_stock.empty:
            (
                NEW_INV_LABEL_value_str,
                NEW_INV_LABEL_value_df,
            ) = calculate_NEW_INV_LABEL_value(df_stock)
            st.markdown(NEW_INV_LABEL_value_str, unsafe_allow_html=True)
            st.bar_chart(NEW_INV_LABEL_value_df.set_index("NEW_INV_LABEL")["Value_USD"])

    elif st.session_state.selected_option == "Sub Inv Desc Value":
        if not df_stock.empty:
            (
                SUB_INV_DESC_value_str,
                SUB_INV_DESC_value_df,
            ) = calculate_SUB_INV_DESC_value(df_stock)
            st.markdown(SUB_INV_DESC_value_str, unsafe_allow_html=True)
            st.bar_chart(SUB_INV_DESC_value_df.set_index("SUB INV DESC")["Value_USD"])

    elif st.session_state.selected_option == "Age In Years Value":
        if not df_stock.empty:
            (
                Age_Yrs_value_str,
                Age_Yrs_value_df,
            ) = calculate_Age_Yrs_value(df_stock)
            st.markdown(Age_Yrs_value_str, unsafe_allow_html=True)
            st.bar_chart(Age_Yrs_value_df.set_index("Age Yrs")["Value_USD"])


if __name__ == "__main__":
    main()
