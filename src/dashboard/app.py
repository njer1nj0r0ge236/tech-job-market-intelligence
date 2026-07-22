# import streamlit as st

# import plotly.express as px

# from src.services.dashboard_service import DashboardService


# dashboard = DashboardService()

# overview = dashboard.get_overview().iloc[0]

# st.set_page_config(
#     page_title="TJMI Dashboard",
#     page_icon="📊",
#     layout="wide",
# )

# st.title("📊 Tech Job Market Intelligence")

# st.write(
#     "An analytics dashboard built from live technology job postings."
# )

# # Add the overview metrics

# col1, col2, col3, col4, col5 = st.columns(5)

# col1.metric("Jobs", overview["total_jobs"])

# col2.metric("Companies", overview["total_companies"])

# col3.metric("ATS", overview["total_ats"])

# col4.metric("Kenya Jobs", overview["kenya_jobs"])

# col5.metric("Remote Jobs", overview["remote_jobs"])

# # Add the first chart
# st.subheader("Jobs by Company")

# company_df = dashboard.get_company_summary()

# st.bar_chart(
#     company_df.set_index("company")
# )


# # ATS distribution- pia chart
# st.subheader("Jobs by ATS")

# ats_df = dashboard.get_ats_summary()

# fig = px.pie(
#     ats_df,
#     names="ats",
#     values="total_jobs",
#     hole=0.4,
# )

# st.plotly_chart(fig, use_container_width=True)

# # jobs by location
# st.subheader("Jobs by Location")

# location_df = dashboard.get_location_summary()

# fig = px.bar(
#     location_df.head(10),
#     x="location",
#     y="total_jobs",
#     title="Top 10 Job Locations",
# )

# st.plotly_chart(fig, use_container_width=True)

# # employment types
# st.subheader("Employment Types")

# employment_df = dashboard.get_employment_summary()

# fig = px.bar(
#     employment_df,
#     x="employment_type",
#     y="total_jobs",
#     title="Employment Types",
# )

# st.plotly_chart(fig, use_container_width=True)

# # Remote Hiring Companies
# st.subheader("Top Remote Hiring Companies")

# remote_df = dashboard.get_remote_summary()

# fig = px.bar(
#     remote_df.head(10),
#     x="company",
#     y="total_jobs",
#     title="Top Remote Hiring Companies",
# )

# st.plotly_chart(fig, use_container_width=True)

# # Kenya Hiring Companies
# st.subheader("Top Companies Hiring in Kenya")

# kenya_df = dashboard.get_kenya_summary()

# fig = px.bar(
#     kenya_df.head(10),
#     x="company",
#     y="total_jobs",
#     title="Top Kenya Hiring Companies",
# )

# st.plotly_chart(fig, use_container_width=True)

# # Data Roles
# st.subheader("Companies Hiring for Data Roles")

# data_df = dashboard.get_data_roles_summary()

# fig = px.bar(
#     data_df,
#     x="company",
#     y="total_jobs",
#     title="Data Roles",
# )

# st.plotly_chart(fig, use_container_width=True)

# # Software Engineering Roles
# st.subheader("Companies Hiring for Software Roles")

# software_df = dashboard.get_software_roles_summary()

# fig = px.bar(
#     software_df.head(10),
#     x="company",
#     y="total_jobs",
#     title="Software Engineering Roles",
# )

# st.plotly_chart(fig, use_container_width=True)

# 
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))


import streamlit as st
import plotly.express as px

from src.services.dashboard_service import DashboardService

from PIL import Image


# Page Configuration
logo = Image.open("assets/tjmi_logo.png")

st.set_page_config(
    page_title="TJMI Dashboard",
    page_icon=logo,
    layout="wide",
)

dashboard = DashboardService()
overview = dashboard.get_overview().iloc[0]


# Header
st.title("Tech Job Market Intelligence")

st.write(
    "Live insights from technology job postings collected across multiple applicant tracking systems."
)


# KPI Cards
col1, col2, col3, col4, col5 = st.columns(5)

col1.metric("Jobs", overview["total_jobs"])
col2.metric("Companies", overview["total_companies"])
col3.metric("ATS", overview["total_ats"])
col4.metric("Kenya Jobs", overview["kenya_jobs"])
col5.metric("Remote Jobs", overview["remote_jobs"])



# Row 1
left, right = st.columns(2)

with left:

    st.subheader("Top Hiring Companies")

    company_df = dashboard.get_company_summary()

    # fig = px.bar(
    #     company_df.head(10),
    #     x="company",
    #     y="total_jobs",
    # )

    fig = px.bar(
        company_df.head(10),
        x="total_jobs",
        y="company",
        orientation="h",
        color_discrete_sequence=["#2563EB"],
    )

    fig.update_layout(
        yaxis={"categoryorder": "total ascending"},
        height=420,
    )
    st.plotly_chart(fig, use_container_width=True)

with right:

    st.subheader("ATS Distribution")

    ats_df = dashboard.get_ats_summary()

    fig = px.pie(
        ats_df,
        names="ats",
        values="total_jobs",
        hole=0.4,
    )

    st.plotly_chart(fig, use_container_width=True)



# Row 2
left, right = st.columns(2)

with left:

    st.subheader("Top Job Locations")

    location_df = dashboard.get_location_summary()

    # fig = px.bar(
    #     location_df.head(10),
    #     x="location",
    #     y="total_jobs",
    # )

    fig = px.bar(
        location_df.head(10),
        x="total_jobs",
        y="location",
        orientation="h",
        color_discrete_sequence=["#2563EB"],
    )

    fig.update_layout(
        yaxis={"categoryorder": "total ascending"},
        height=420,
    )

    st.plotly_chart(fig, use_container_width=True)

with right:

    st.subheader("Employment Types")

    employment_df = dashboard.get_employment_summary()

    fig = px.bar(
        employment_df,
        x="employment_type",
        y="total_jobs",
    )

    st.plotly_chart(fig, use_container_width=True)



# Row 3
left, right = st.columns(2)

with left:

    st.subheader("Top Remote Employers")

    remote_df = dashboard.get_remote_summary()

    fig = px.bar(
        remote_df.head(10),
        x="total_jobs",
        y="company",
        orientation="h",
        color_discrete_sequence=["#2563EB"],
    )

    fig.update_layout(
        yaxis={"categoryorder": "total ascending"},
        height=420,
    )

    st.plotly_chart(fig, use_container_width=True)

with right:

    st.subheader("Top Kenya Employers")

    kenya_df = dashboard.get_kenya_summary()

    fig = px.bar(
        kenya_df.head(10),
        x="total_jobs",
        y="company",
        orientation="h",
        color_discrete_sequence=["#2563EB"],
    )

    fig.update_layout(
        yaxis={"categoryorder": "total ascending"},
        height=420,
    )

    st.plotly_chart(fig, use_container_width=True)



# Row 4
left, right = st.columns(2)

with left:

    st.subheader("Data Roles")

    data_df = dashboard.get_data_roles_summary()

    # fig = px.bar(
    #     data_df,
    #     x="company",
    #     y="total_jobs",
    # )

    fig = px.bar(
        data_df,
        x="total_jobs",
        y="company",
        orientation="h",
        color_discrete_sequence=["#2563EB"],
    )

    fig.update_layout(
        yaxis={"categoryorder": "total ascending"},
        height=420,
    )

    st.plotly_chart(fig, use_container_width=True)

with right:

    st.subheader("Software Roles")

    software_df = dashboard.get_software_roles_summary()

    fig = px.bar(
        software_df.head(10),
        x="total_jobs",
        y="company",
        orientation="h",
        color_discrete_sequence=["#2563EB"],
    )

    fig.update_layout(
        yaxis={"categoryorder": "total ascending"},
        height=420,
    )

    st.plotly_chart(fig, use_container_width=True)