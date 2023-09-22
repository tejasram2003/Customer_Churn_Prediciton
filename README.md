
<body>

<h1>Customer Churn Prediction</h1>

<h2>Introduction</h2>
<p>This project aims to predict customer churn based on historical customer data. The goal is to develop a machine learning model that can identify customers who are likely to churn so that appropriate retention strategies can be implemented.</p>

<h2>Data Preprocessing</h2>
<p>In this project, several data preprocessing steps were performed:</p>
<ul>
<li><strong>Handling Missing Data:</strong> There wasn't much significant Data found to be missing in the provided dataset, most of the rows were full.</li>
<li><strong>Outlier Detection:</strong> Outliers in numeric features were identified and treated to ensure the quality of the data.</li>
<li><strong>Scaling:</strong> Features were scaled to bring them to a similar scale. Robust Standardization (z-score scaling) and Min-Max scaling was applied, depending on the algorithm used.</li>
<li><strong>One-Hot Encoding:</strong> Categorical variables, such as "Location", "Gender" and "Age_Group," were one-hot encoded to convert them into a numerical format suitable for machine learning.</li>
<li><strong>Feature Engineering:</strong> Additional features were generated to capture relevant information. For example, "Cost_per_GB" was calculated by dividing "Monthly_Bill" by "Total_Usage_GB."</li>
<li><strong>Age Categories:</strong> The "Age" variable was transformed into age categories (bins) to capture different customer age groups. This was achieved using the pd.cut function in pandas.</li>
<li><strong>Correlation Matrix (Before preprocessing):</strong></li>
<img src="https://ik.imagekit.io/tejasram/churn_screenshots/correlation_before.png?updatedAt=1695374661161" width="500">
<li><strong>Correlation Matrix (After preprocessing):</strong></li>
<img src="https://ik.imagekit.io/tejasram/churn_screenshots/correlation_after.png?updatedAt=1695374651456" width="500">
<li><strong>User count from each city:</strong></li>
<img src="https://ik.imagekit.io/tejasram/churn_screenshots/location_headcount.png?updatedAt=1695374650217" width="500">
<li><strong>BoxPlot Before MinMaxScaling:</strong></li>
<img src="https://ik.imagekit.io/tejasram/churn_screenshots/boxplot_before.png?updatedAt=1695374650390" width="500">
<li><strong>BoxPlot After MinMaxScaling:</strong></li>
<img src="https://ik.imagekit.io/tejasram/churn_screenshots/boxplot_after.png?updatedAt=1695374650271" width="500">

</ul>

<h2>Model Building</h2>
<p>For customer churn prediction, various machine learning algorithms were considered, including decision trees, random forests, k-nearest neighbors (KNN), and artificial neural networks (ANN). Model selection and evaluation were performed using appropriate metrics such as accuracy, precision, recall, and F1-score.</p>

<h2>Model Deployment</h2>
<p>Once a satisfactory model was trained and validated, it was deployed in a production-like environment. The deployed model is capable of accepting new customer data as input and providing churn predictions.</p>
<img src="https://ik.imagekit.io/tejasram/churn_screenshots/output.png?updatedAt=1695374651046" width="500">

<h2>Additional Information</h2>
<p>Python and relevant machine learning and data analytics libraries, such as scikit-learn, numpy, pandas, matplotlib and PyTorch, were used to implement the project. The code and details of the project can be found in the provided Jupyter Notebook <code>churn_predction.ipynb</code>.</p>

<h2>Evaluation Criteria</h2>
<p>The project was evaluated based on various criteria, including data preprocessing and cleaning, feature engineering, model selection and optimization, model deployment and integration, code clarity and organization, and documentation and reporting of the work.</p>
<p>Decision Tree:</p>
<img src="https://ik.imagekit.io/tejasram/churn_screenshots/Decision_tree_metrics.png?updatedAt=1695374661155" width="500">
<p>Random Forest:</p>
<img src="https://ik.imagekit.io/tejasram/churn_screenshots/random_forest_metrics.png?updatedAt=1695374651398" width="500">
<p>ANN:</p>
<img src="https://ik.imagekit.io/tejasram/churn_screenshots/ann_metrics.png?updatedAt=1695374650767" width="500">
<p>Grid Search (Decision Tree):</p>
<img src="https://ik.imagekit.io/tejasram/churn_screenshots/grid_search_metrics.png?updatedAt=1695374651393" width="500">


</body>
