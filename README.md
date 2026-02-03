📊 **SME Financial Health Assessment Platform 🏆 GUVI / HCL Hackathon Project**

An AI-driven financial health assessment platform designed for Small and Medium Enterprises (SMEs) to evaluate creditworthiness, identify financial risks, and provide actionable insights for business owners, banks, and NBFCs.

🚀 **Problem Statement**

SMEs often lack access to structured financial analysis and expert guidance. Traditional credit assessment is manual, time-consuming, and difficult for non-finance users to understand.

This platform simplifies financial evaluation by:

i) Analyzing SME financial data ii) Assessing credit risk and business stability iii) Providing real-time, actionable recommendations iv) Enabling scalable integration with financial systems

💡 **Solution Overview**

This project implements a production-aligned MVP that performs real-time SME financial risk analysis using structured financial datasets and AI-style analytics.

Key Capabilities

i) Creditworthiness evaluation ii) Financial risk classification iii) Actionable business recommendations iv) API-driven backend architecture v) Interactive React frontend vi) Scalable, modular design

🏗️ **System Architecture**

The platform follows a three-layer architecture:

**1️⃣ Frontend Layer - React.js**

i) User-friendly interface ii) Business ID selection and analysis trigger iii) Displays financial risk and recommendations

**2️⃣ Backend Layer - FastAPI**

i) RESTful API endpoints ii) Secure frontend–backend communication iii) Swagger API documentation

**3️⃣ Data & Intelligence Layer - Python, Pandas, NumPy**

i) Dynamic financial feature extraction ii) Deterministic, explainable risk scoring logic iii) Designed for future ML / LLM integration

⚙️ **Technology Stack**

Frontend React.js Backend FastAPI Data Processing Python, Pandas, NumPy API Documentation Swagger UI Security CORS, Encryption-ready architecture Data Source CSV-based financial datasets

🔐 **Security Considerations**

i) CORS middleware to control cross-origin access ii) Stateless REST APIs iii) Encryption-ready backend design iv) Production-ready HTTPS compatibility

📡 **API Endpoints**

🔹 Get Business IDs http://127.0.0.1:8000/business_ids

Returns unique SME identifiers dynamically from the dataset.

🔹 Analyze SME Financial Health http://127.0.0.1:8000/analyze/22

Performs financial risk analysis and returns:

i) Credit metric used ii) Credit value iii) Risk classification iv) Actionable recommendation

🧠 **AI & Financial Intelligence**

The current system uses deterministic and explainable scoring logic, ensuring:

i) Transparency ii) Auditability iii) Regulatory compatibility iv) The architecture is LLM-ready, allowing seamless future integration of: v) Machine Learning models vi) Advanced forecasting vii) Natural language financial explanations

🖥️ Demo Backend (Swagger UI) http://127.0.0.1:8000/docs

Frontend (React) http://localhost:3000

🚀 **Future Enhancements**

i) Planned extensions include: ii) GST data integration iii) Banking & payment APIs (up to 2) iv) Financial forecasting & cash-flow prediction v) Working capital optimization vi) Industry-specific benchmarking vii) Multilingual support (Hindi & regional languages) viii) PostgreSQL database integration ix) Investor-ready financial reports

🎯 **Hackathon Readiness**

✔ End-to-end working prototype ✔ Real-time analysis ✔ Scalable architecture ✔ AI-driven financial insights ✔ Clean UI + API integration

This project demonstrates a real-world, production-aligned approach to SME financial intelligence.

👩‍💻 **Author**

Subiya

📌 **Note to Evaluators**

This solution is designed as a production-ready MVP. Advanced enterprise features are intentionally modularized for future deployment without architectural changes.
