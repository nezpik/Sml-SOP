# Pistologistics: S&OP Dataset for AI-Driven Supply Chain Optimization

A comprehensive Sales and Operations Planning (S&OP) dataset with synthetic data generation capabilities for supply chain AI modeling and optimization.

## Overview

Pistologistics provides a rich, synthetic dataset that simulates a complete supply chain ecosystem with realistic patterns and relationships. It is designed specifically for training and evaluating AI models for supply chain optimization, demand forecasting, inventory management, and production planning.

## Key Features

- **Comprehensive Supply Chain Data Model**: Complete schema covering master data, transaction data, and planning tables
- **Realistic Data Generation**: Sophisticated algorithms to create realistic patterns with trends, seasonality, external factors, and anomalies
- **Advanced Supply Chain Metrics**: Includes inventory optimization metrics (EOQ, safety stock), production planning, and KPIs
- **Multi-horizon Forecasting Support**: Historical and future data for training time-series models
- **Configurable Generation Parameters**: Customize data size, complexity, and characteristics
- **Supply Chain Disruption Simulation**: Model the impact of disruptions on the supply chain
- **Promotion Impact Modeling**: Simulate marketing activities and their effect on demand

## Dataset Components

### Master Data
- Products with categories, costs, and attributes
- Locations (DCs, stores, plants, suppliers)
- Customers with segments and regions
- Suppliers with reliability metrics
- Resources with capacity and efficiency

### Transaction Data
- Demand forecasts with confidence levels
- Inventory levels with optimization metrics
- Production plans with resource requirements
- Transport lanes with costs and transit times

### External Factors
- Economic indicators (GDP, inflation)
- Seasonal patterns
- Market events
- Weather impacts
- Promotional activities
- Supply disruptions

### Performance Metrics
- Inventory KPIs (turns, days of supply)
- Production KPIs (efficiency, utilization)
- Supply chain KPIs (forecast accuracy, on-time delivery)

## AI Model Compatibility

The dataset is designed to support various AI/ML model types:

### Time Series Forecasting Models
- ARIMA/SARIMA
- Prophet
- LSTM Networks
- Transformer-based Models

### Gradient Boosting Models
- XGBoost
- LightGBM
- CatBoost

### Neural Network Models
- Feed-forward Neural Networks
- Recurrent Neural Networks
- Graph Neural Networks

### Optimization Models
- Linear Programming
- Mixed Integer Programming
- Constraint Programming
- Reinforcement Learning

## Example Use Case: Multi-horizon Demand Forecasting

```python
import pandas as pd
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor

# Load the data
demand_df = pd.read_csv('sample_data/DemandForecast.csv')
external_factors = pd.read_csv('sample_data/ExternalFactors.csv')
promotions = pd.read_csv('sample_data/PromotionCalendar.csv')

# Merge datasets
merged_data = demand_df.merge(external_factors, on='date', how='left')

# Feature engineering
merged_data['day_of_week'] = pd.to_datetime(merged_data['date']).dt.dayofweek
merged_data['month'] = pd.to_datetime(merged_data['date']).dt.month
merged_data['is_promoted'] = merged_data['product_id'].isin(promotions['product_id'])

# Prepare features and target
features = ['day_of_week', 'month', 'gdp_factor', 'inflation_factor', 
            'seasonal_factor', 'market_event_factor', 'weather_impact_factor', 
            'is_promoted']
X = merged_data[features]
y = merged_data['forecast_quantity']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = XGBRegressor(n_estimators=100, learning_rate=0.1, max_depth=5)
model.fit(X_train, y_train)

# Evaluate
predictions = model.predict(X_test)
rmse = ((predictions - y_test) ** 2).mean() ** 0.5
print(f"RMSE: {rmse}")
```

## Installation and Usage

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/pistologistics.git
   cd pistologistics
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Generate sample data:
   ```
   python data_generator.py
   ```

4. Explore the generated data in the `sample_data` directory

## Scaling Recommendations

For different use cases, adjust the data generation parameters:

- **Small-scale testing**: 100 products, 10 locations, 1,000 forecast records
- **Medium-scale development**: 500 products, 50 locations, 10,000 forecast records
- **Large-scale production**: 1,000+ products, 100+ locations, 50,000+ forecast records

## Advanced Supply Chain Engineering Features

The dataset includes specialized features for supply chain engineers:

### Inventory Optimization
- Economic Order Quantity (EOQ) calculation
- Safety stock determination based on service levels
- Reorder point calculation
- Inventory turns and days of supply metrics

### Production Planning
- Resource capacity planning
- Setup time optimization
- Material requirements planning
- Production cost analysis

### Supply Chain Risk Management
- Disruption impact modeling
- Supplier reliability analysis
- Risk mitigation strategies
- Resilience assessment

### Performance Management
- KPI tracking and analysis
- Target setting methodology
- Variance analysis
- Performance improvement planning

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Inspired by real-world S&OP processes and supply chain management practices
- Designed for educational and research purposes in supply chain analytics
