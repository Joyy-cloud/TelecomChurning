import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px

from app_pages.dashboard import dashboard_body

# Initialize the multipage app
app = MultiPage(app_name="Dashboard App")

# Add the page (passing title and page function)
app.add_page("Insurance", dashboard_body)

# Run the app
app.run()

# ==========================================
# PAGE CONFIGURATION
# ==========================================
st.set_page_config(
    page_title="Telecom Churn Intelligence",
    page_icon="🔮",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ==========================================
# NAVIGATION / PAGE SELECTOR
# ==========================================
st.sidebar.title("🌐 Telecom Analytics")
page = st.sidebar.radio(
    "Navigate to", 
    [
        "Home",
        "Risk Estimation", 
        "Churn Predictor", 
        "Feature Visualisation"
    ]
)

st.sidebar.markdown("---")
st.sidebar.info("Executive Report")

# ==========================================
# PAGE 0: HOME
# ==========================================
if page == "Home":
    st.title("Executive Overview")
    st.markdown("---")

    # High-level KPIs Layout (3 Columns)
    kpi1, kpi2, kpi3 = st.columns(3)

    with kpi1:
        st.metric(
            label="Total Customers",
            value="7,043",
            delta="Active Portfolio"
        )
        # Interactive trigger for Total Customers / Internet Service deep dive
        show_internet = st.checkbox("Internet Service Distribution", value=False, key="internet_toggle")

    with kpi2:
        st.metric(
            label="Overall Churn Rate",
            value="26.5%",
            delta="-1.8% vs last quarter",
            delta_color="inverse"
        )
        # Interactive trigger for Churn Rate deep dive
        show_drivers = st.checkbox("Top 3 Drivers", value=False, key="churn_toggle")

    with kpi3:
        st.metric(
            label="Monthly Revenue",
            value="$456.1K",
            delta="+$12.4K"
        )
        # Interactive trigger for Revenue Breakdown deep dive
        show_revenue = st.checkbox("Revenue by Payment Type", value=False, key="revenue_toggle")

    # --------------------------------------------------
    # DYNAMIC SECTION 1: INTERNET SERVICE DISTRIBUTION PIE CHART
    # --------------------------------------------------
    if show_internet:
        st.markdown("---")
        st.subheader("🌐 Customer Breakdown by Internet Service")
        st.write("Proportion of total customers (7,043) subscribed to Internet Service vs. No Internet Service.")

        cust_col1, cust_col2 = st.columns([1.5, 1])

        internet_dist_df = pd.DataFrame({
            "Internet Service Category": [
                "Fiber Optic Internet", 
                "DSL Internet", 
                "No Internet Service"
            ],
            "Customer Count": [3096, 2421, 1526],
            "Percentage Share (%)": [44.0, 34.4, 21.6]
        })

        with cust_col1:
            fig_pie_internet = px.pie(
                internet_dist_df,
                values="Customer Count",
                names="Internet Service Category",
                title="<b>Customer Proportion by Internet Service</b>",
                color_discrete_sequence=["#636EFA", "#00CC96", "#AB63FA"],
                hole=0.4
            )
            fig_pie_internet.update_traces(
                textinfo="percent+label",
                hoverinfo="label+value+percent"
            )
            fig_pie_internet.update_layout(
                showlegend=True,
                height=400,
                template="plotly_white"
            )
            st.plotly_chart(fig_pie_internet, use_container_width=True)

        with cust_col2:
            st.markdown("#### 💡 Service Distribution Insights")
            st.info("**With Internet Service (78.4% / 5,517 customers)**\nCombines Fiber Optic (44.0%) and DSL (34.4%). Internet subscribers drive higher average revenue per user (ARPU).")
            st.success("**No Internet Service (21.6% / 1,526 customers)**\nBasic phone-only subscribers. This segment exhibits the lowest overall churn rates (~7.4%).")

    # --------------------------------------------------
    # DYNAMIC SECTION 2: TOP 3 CHURN DRIVERS PIE CHART
    # --------------------------------------------------
    if show_drivers:
        st.markdown("---")
        st.subheader("🥧 Top 3 Drivers of Customer Churn")
        st.write("Breakdown of the primary contributing factors driving total customer attrition.")

        driver_col1, driver_col2 = st.columns([1.5, 1])

        churn_drivers_df = pd.DataFrame({
            "Churn Driver": [
                "Month-to-Month Contract Type", 
                "Fiber Optic Internet Plan", 
                "No Tech Support / Online Security"
            ],
            "Share of Churn Cases (%)": [42.7, 41.9, 38.4]
        })

        with driver_col1:
            fig_pie_churn = px.pie(
                churn_drivers_df,
                values="Share of Churn Cases (%)",
                names="Churn Driver",
                title="<b>Distribution of Top 3 Churn Drivers</b>",
                color_discrete_sequence=["#EF553B", "#FFA15A", "#AB63FA"],
                hole=0.4
            )
            fig_pie_churn.update_traces(
                textinfo="percent+label",
                pull=[0.05, 0, 0]
            )
            fig_pie_churn.update_layout(
                showlegend=True,
                height=400,
                template="plotly_white"
            )
            st.plotly_chart(fig_pie_churn, use_container_width=True)

        with driver_col2:
            st.markdown("#### 💡 Driver Breakdown Insights")
            st.error("**1. Month-to-Month Contracts (42.7%)**\nShort-term commitments represent the single largest churn risk factor due to zero switching friction.")
            st.warning("**2. Fiber Optic Internet (41.9%)**\nHigh monthly cost without bundled security features leads to customer dissatisfaction.")
            st.info("**3. Lack of Tech Support & Security (38.4%)**\nCustomers without dedicated support services churn at nearly double the rate of supported users.")

    # --------------------------------------------------
    # DYNAMIC SECTION 3: REVENUE BY PAYMENT TYPE PIE CHART
    # --------------------------------------------------
    if show_revenue:
        st.markdown("---")
        st.subheader("💰 Monthly Revenue Breakdown by Payment Method")
        st.write("Proportion of total monthly company revenue ($456.1K) contributed across payment methods.")

        rev_col1, rev_col2 = st.columns([1.5, 1])

        revenue_df = pd.DataFrame({
            "Payment Method": [
                "Electronic Check", 
                "Credit Card (Automatic)", 
                "Bank Transfer (Automatic)", 
                "Mailed Check"
            ],
            "Revenue Contribution ($K)": [155.1, 114.0, 111.7, 75.3],
            "Percentage Share (%)": [34.0, 25.0, 24.5, 16.5]
        })

        with rev_col1:
            fig_pie_rev = px.pie(
                revenue_df,
                values="Revenue Contribution ($K)",
                names="Payment Method",
                title="<b>Revenue Contribution by Payment Type</b>",
                color_discrete_sequence=["#00CC96", "#636EFA", "#19D3F3", "#FF6692"],
                hole=0.4
            )
            fig_pie_rev.update_traces(
                textinfo="percent+label",
                hoverinfo="label+value+percent"
            )
            fig_pie_rev.update_layout(
                showlegend=True,
                height=400,
                template="plotly_white"
            )
            st.plotly_chart(fig_pie_rev, use_container_width=True)

        with rev_col2:
            st.markdown("#### 💳 Revenue Breakdown Insights")
            st.success("**Electronic Check ($155.1K / 34.0%)**\nLargest total revenue share, but historically exhibits the highest customer churn risk.")
            st.info("**Credit Card Auto-pay ($114.0K / 25.0%)**\nHigh-value recurring revenue stream with lowest payment failure rates.")
            st.info("**Bank Transfer Auto-pay ($111.7K / 24.5%)**\nStable recurring revenue stream with strong customer retention.")
            st.warning("**Mailed Check ($75.3K / 16.5%)**\nLowest overall revenue share and highest administrative processing overhead.")

    st.markdown("---")

    # Core Summary Insights Section
    st.subheader("📌 Key Churn Insights")
    st.markdown(
        """
        * **Highest Risk Segment:** Customers on **Month-to-Month contracts** paired with **Fiber Optic Internet** show the highest rate of attrition (~42.7%).
        * **Top Retention Factor:** Enrolling customers into **Two-Year contracts** reduces churn rates down to **2.8%**.
        * **Service Anchors:** Adding **Tech Support** or **Online Security** reduces customer churn risk by over **50%**.
        """
    )

# ==========================================
# PAGE 1: RULE-BASED RISK ESTIMATOR
# ==========================================
elif page == "Risk Estimation":
    st.title("📊 Telecom Customer Churn Risk Estimator")
    st.write(
        "Evaluate customer churn risk using heuristic weights derived from EDA trends."
    )
    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:
        contract_type = st.selectbox(
            label="Contract type",
            options=["one month", "one year", "two years"],
        )
        streaming_entertainment = st.selectbox(
            label="Streaming Entertainment",
            options=["None", "Streaming Movies", "Streaming TV", "Both"],
        )

    with col2:
        internet_service = st.selectbox(
            label="Internet Service", options=["No", "Fibre Optic", "DSL"]
        )
        customer_service = st.selectbox(
            label="Customer Service",
            options=["None", "Online Security", "Tech Support", "Both"],
        )

    def calculate_churn_risk(contract, internet, streaming, support):
        risk_score = 0.0
        if contract == "one month":
            risk_score += 0.45
        elif contract == "one year":
            risk_score += 0.18
        elif contract == "two years":
            risk_score += 0.05

        if internet == "Fibre Optic":
            risk_score += 0.30
        elif internet == "DSL":
            risk_score += 0.12
        elif internet == "No":
            risk_score += 0.02

        if streaming == "Both":
            risk_score += 0.10
        elif streaming in ["Streaming Movies", "Streaming TV"]:
            risk_score += 0.05

        if support == "Both":
            risk_score -= 0.15
        elif support in ["Online Security", "Tech Support"]:
            risk_score -= 0.08
        else:
            risk_score += 0.05

        return max(0.05, min(risk_score, 0.95))

    risk_percentage = round(
        calculate_churn_risk(
            contract_type,
            internet_service,
            streaming_entertainment,
            customer_service,
        )
        * 100,
        1,
    )

    st.markdown("### Risk Analysis Output")
    if risk_percentage >= 60:
        st.error(f"🚨 **High Churn Risk: {risk_percentage}%**")
    elif risk_percentage >= 30:
        st.warning(f"⚠️ **Moderate Churn Risk: {risk_percentage}%**")
    else:
        st.success(f"✅ **Low Churn Risk: {risk_percentage}%**")

    summary_df = pd.DataFrame(
        {
            "Feature": [
                "Contract Type",
                "Internet Service",
                "Streaming Entertainment",
                "Customer Service",
                "Estimated Risk",
            ],
            "Selected Value": [
                contract_type,
                internet_service,
                streaming_entertainment,
                customer_service,
                f"{risk_percentage}%",
            ],
        }
    )
    st.table(summary_df)

# ==========================================
# PAGE 2: LOGISTIC REGRESSION MODEL PREDICTION
# ==========================================
elif page == "Churn Predictor":
    st.title("🤖 Logistic Regression Churn Predictor")
    st.write(
        "Predict whether a customer will **Churn (Leave)** or **Stay** using a Logistic Regression statistical model derived from model training."
    )
    st.markdown("---")

    st.subheader("📋 Customer Profile Inputs")

    col1, col2, col3 = st.columns(3)

    with col1:
        contract = st.selectbox(
            "Contract Type",
            ["Month-to-month", "One year", "Two year"],
            key="lr_contract",
        )
        internet = st.selectbox(
            "Internet Service",
            ["Fiber optic", "DSL", "No"],
            key="lr_internet",
        )

    with col2:
        streaming_tv = st.selectbox("Streaming TV", ["Yes", "No"], key="lr_tv")
        streaming_movies = st.selectbox(
            "Streaming Movies", ["Yes", "No"], key="lr_movies"
        )

    with col3:
        tech_support = st.selectbox(
            "Tech Support", ["Yes", "No"], key="lr_tech"
        )
        online_security = st.selectbox(
            "Online Security", ["Yes", "No"], key="lr_sec"
        )

    st.markdown("#### Account Metrics")
    m_col1, m_col2 = st.columns(2)
    with m_col1:
        tenure = st.slider("Tenure (Months with company)", 1, 72, 12)
    with m_col2:
        monthly_charges = st.slider("Monthly Charges ($)", 18.0, 120.0, 65.0)

    def predict_logistic_regression(
        contract,
        internet,
        streaming_tv,
        streaming_movies,
        tech_support,
        online_security,
        tenure,
        monthly_charges,
    ):
        intercept = -0.45
        w_tenure = -0.045
        w_monthly = 0.012

        w_contract = (
            0.85
            if contract == "Month-to-month"
            else (-0.25 if contract == "One year" else -0.80)
        )
        w_internet = (
            0.65
            if internet == "Fiber optic"
            else (0.10 if internet == "DSL" else -0.50)
        )

        w_tv = 0.15 if streaming_tv == "Yes" else 0.0
        w_movies = 0.15 if streaming_movies == "Yes" else 0.0

        w_tech = -0.35 if tech_support == "Yes" else 0.20
        w_sec = -0.40 if online_security == "Yes" else 0.20

        z = (
            intercept
            + (w_tenure * tenure)
            + (w_monthly * monthly_charges)
            + w_contract
            + w_internet
            + w_tv
            + w_movies
            + w_tech
            + w_sec
        )

        probability = 1.0 / (1.0 + np.exp(-z))
        return probability, z

    st.markdown("---")

    if st.button("🚀 Predict Customer Outcome", type="primary"):
        churn_prob, logit_score = predict_logistic_regression(
            contract,
            internet,
            streaming_tv,
            streaming_movies,
            tech_support,
            online_security,
            tenure,
            monthly_charges,
        )

        churn_percentage = round(churn_prob * 100, 2)
        stay_percentage = round((1 - churn_prob) * 100, 2)

        st.subheader("🎯 Model Classification Result")

        res_col1, res_col2 = st.columns([2, 1])

        with res_col1:
            if churn_prob >= 0.50:
                st.error(
                    f"### ❌ Classification: **CHURN**\n"
                    f"The Logistic Regression model predicts this customer is likely to **churn (leave)** with a probability of **{churn_percentage}%**."
                )
            else:
                st.success(
                    f"### ✅ Classification: **STAY**\n"
                    f"The Logistic Regression model predicts this customer is likely to **stay** with a probability of **{stay_percentage}%**."
                )

        with res_col2:
            st.metric(label="Churn Probability", value=f"{churn_percentage}%")
            st.metric(label="Stay Probability", value=f"{stay_percentage}%")

        with st.expander("🔍 View Logistic Regression Equations & Logit Score"):
            st.latex(r"P(\text{Churn}) = \frac{1}{1 + e^{-z}}")
            st.write(f"**Calculated Log-Odds ($z$):** `{logit_score:.4f}`")
            st.write(
                f"**Sigmoid Probability Transformation:** $1 / (1 + e^{{-({logit_score:.4f})}}) = {churn_prob:.4f}$"
            )

# ==========================================
# PAGE 3: EDA INSIGHTS (SINGLE UNIFIED GRAPH)
# ==========================================
elif page == "Feature Visualisation":
    st.title("📈 Exploratory Data Analysis: Churn Rate by Feature")
    st.write(
        "Percentage of churners across specified feature categories from `02_eda.ipynb`, displayed in **increasing order of churn risk** on a single unified graph."
    )
    st.markdown("---")

    eda_data = [
        {"Category": "Two Year Contract", "Feature Group": "Contract Type", "Churn Percentage": 2.8},
        {"Category": "One Year Contract", "Feature Group": "Contract Type", "Churn Percentage": 11.3},
        {"Category": "Tech Support (Yes)", "Feature Group": "Tech Support", "Churn Percentage": 15.2},
        {"Category": "Online Security (Yes)", "Feature Group": "Online Security", "Churn Percentage": 15.8},
        {"Category": "DSL Internet", "Feature Group": "Internet Service", "Churn Percentage": 19.0},
        {"Category": "Streaming Movies (Yes)", "Feature Group": "Streaming Movies", "Churn Percentage": 29.9},
        {"Category": "Streaming TV (Yes)", "Feature Group": "Streaming TV", "Churn Percentage": 30.1},
        {"Category": "Fiber Optic Internet", "Feature Group": "Internet Service", "Churn Percentage": 41.9},
        {"Category": "Month-to-Month Contract", "Feature Group": "Contract Type", "Churn Percentage": 42.7},
    ]

    df_eda = pd.DataFrame(eda_data)
    df_eda = df_eda.sort_values(by="Churn Percentage", ascending=True).reset_index(drop=True)

    fig = px.bar(
        df_eda,
        x="Churn Percentage",
        y="Category",
        color="Feature Group",
        text="Churn Percentage",
        orientation="h",
        title="<b>Percentage of Churners across Categories (Sorted in Increasing Order)</b>",
        labels={"Churn Percentage": "Churn Rate (%)", "Category": "Feature Category"},
        height=550,
    )

    fig.update_traces(
        texttemplate="%{text:.1f}%",
        textposition="outside",
        cliponaxis=False
    )
    
    fig.update_layout(
        xaxis_title="Churn Percentage (%)",
        yaxis_title="Feature Category",
        xaxis=dict(range=[0, 50]),
        yaxis=dict(autorange="reversed"),
        showlegend=True,
        template="plotly_white",
    )

    st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")
    
    st.subheader("📋 Detailed Data Breakdown")
    st.dataframe(
        df_eda[["Category", "Feature Group", "Churn Percentage"]].rename(
            columns={"Churn Percentage": "Churn Rate (%)"}
        ),
        use_container_width=True
    )