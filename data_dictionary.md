# Data Dictionary for S&OP Dataset

## Master Data Tables

### Product
| Field | Type | Description |
|-------|------|-------------|
| product_id | string | Unique identifier for the product |
| product_name | string | Name of the product |
| product_category | string | Category classification |
| product_lifecycle_stage | string | Current lifecycle stage (New, Growth, Mature, Decline) |
| unit_cost | float | Standard cost per unit |
| lead_time_days | integer | Standard lead time for procurement/production |
| min_order_quantity | integer | Minimum order quantity |
| pack_size | integer | Units per standard pack |

### Location
| Field | Type | Description |
|-------|------|-------------|
| location_id | string | Unique identifier for the location |
| location_name | string | Name of the location |
| location_type | string | Type (DC, Store, Plant, Supplier) |
| storage_capacity | integer | Maximum storage capacity in units |
| handling_capacity | integer | Daily handling capacity in units |
| operating_cost | float | Daily operating cost |

### Customer
| Field | Type | Description |
|-------|------|-------------|
| customer_id | string | Unique identifier for the customer |
| customer_name | string | Name of the customer |
| segment | string | Customer segment |
| region | string | Geographical region |
| credit_score | float | Credit rating score |
| payment_terms | integer | Standard payment terms in days |

### Supplier
| Field | Type | Description |
|-------|------|-------------|
| supplier_id | string | Unique identifier for the supplier |
| supplier_name | string | Name of the supplier |
| reliability_score | float | Supplier reliability rating |
| capacity | integer | Daily production capacity |
| lead_time_variability | float | Standard deviation of lead time |

### Resource
| Field | Type | Description |
|-------|------|-------------|
| resource_id | string | Unique identifier for the resource |
| resource_type | string | Type of resource |
| capacity | integer | Daily capacity in units |
| efficiency | float | Resource efficiency rating |
| cost_per_hour | float | Operating cost per hour |

## Transaction Data Tables

### DemandForecast
| Field | Type | Description |
|-------|------|-------------|
| forecast_id | string | Unique identifier for the forecast |
| product_id | string | Reference to Product |
| location_id | string | Reference to Location |
| forecast_date | date | Date of the forecast |
| forecast_quantity | integer | Forecasted quantity |
| actual_quantity | integer | Actual quantity (if available) |
| confidence_level | float | Forecast confidence score |
| external_demand_index | float | External market demand indicator |
| promotion_impact_factor | float | Impact multiplier for promotions |
| seasonality_factor | float | Seasonal adjustment factor |
| market_trend_factor | float | Market trend indicator |
| ml_forecast_quantity | integer | Machine learning model forecast |

### TransportLane
| Field | Type | Description |
|-------|------|-------------|
| lane_id | string | Unique identifier for the transport lane |
| origin_id | string | Reference to origin Location |
| destination_id | string | Reference to destination Location |
| transport_mode | string | Mode of transportation |
| transit_time | integer | Standard transit time in days |
| cost_per_unit | float | Transportation cost per unit |
| capacity | integer | Daily transportation capacity |
| reliability | float | Lane reliability score |

## Time Dimension
| Field | Type | Description |
|-------|------|-------------|
| date_id | date | Date identifier |
| year | integer | Year |
| quarter | integer | Quarter (1-4) |
| month | integer | Month (1-12) |
| week | integer | Week number |
| day_of_week | integer | Day of week (1-7) |
| is_holiday | boolean | Holiday indicator |
| is_business_day | boolean | Business day indicator |

## External Factors Tables

### ExternalFactors
| Field | Type | Description |
|-------|------|-------------|
| date | date | Date of the factor measurement |
| gdp_factor | float | GDP growth impact factor |
| inflation_factor | float | Inflation impact factor |
| seasonal_factor | float | Seasonal impact factor |
| market_event_factor | float | Market events impact factor |
| weather_impact_factor | float | Weather impact factor |

### PromotionCalendar
| Field | Type | Description |
|-------|------|-------------|
| date | date | Date of the promotion |
| product_id | string | Reference to Product |
| promotion_type | string | Type of promotion (Price Discount, BOGO, Bundle Deal, Flash Sale) |
| discount_factor | float | Discount percentage (0.1-0.5) |
| duration_days | integer | Duration of promotion in days |

### SupplyDisruptions
| Field | Type | Description |
|-------|------|-------------|
| date | date | Date of the disruption |
| supplier_id | string | Reference to Supplier |
| disruption_type | string | Type of disruption (Port Delay, Production Issue, Natural Disaster, Labor Strike) |
| severity_factor | float | Severity of disruption (0.3-1.0) |
| duration_days | integer | Duration of disruption in days |

## Inventory Management Tables

### Inventory
| Field | Type | Description |
|-------|------|-------------|
| date | date | Date of inventory record |
| product_id | string | Reference to Product |
| location_id | string | Reference to Location |
| quantity_on_hand | integer | Current inventory level |
| safety_stock_level | integer | Calculated safety stock level |
| reorder_point | integer | Calculated reorder point |
| economic_order_quantity | integer | Calculated EOQ |
| inventory_turns | float | Inventory turnover ratio |
| days_of_supply | float | Days of inventory coverage |
| carrying_cost | float | Monthly inventory carrying cost |
| stockout_probability | float | Calculated probability of stockout |
| fill_rate | float | Expected customer order fill rate |

## Production Planning Tables

### ProductionPlan
| Field | Type | Description |
|-------|------|-------------|
| date | date | Production date |
| product_id | string | Reference to Product |
| location_id | string | Reference to Location (Plant) |
| planned_quantity | integer | Planned production quantity |
| production_hours | float | Required production hours |
| setup_hours | float | Required setup hours |
| resource_efficiency | float | Resource efficiency factor |
| production_cost | float | Direct production cost |
| material_cost | float | Material cost |
| total_cost | float | Total production cost |
| resource_requirements | json | Detailed resource requirements |

## Performance Monitoring Tables

### KPI_Dashboard
| Field | Type | Description |
|-------|------|-------------|
| date | date | Date of KPI measurement |
| metric_name | string | Name of the KPI metric |
| metric_value | float | Actual value of the metric |
| target_value | float | Target value for the metric |
| variance_percentage | float | Variance from target (%) |
| dimension_type | string | Dimension type (Overall, Product, Location) |
| dimension_id | string | Dimension identifier |

## Data Generation Parameters

### Demand Forecast Generation
- Base demand range: 100-1000 units
- Trend component: -20% to +30% annual
- Seasonality component: 10-40% amplitude
- External factors impact: Combined multiplicative effect
- Promotion impact: 10-50% lift during active promotions
- Noise level: 5-15% of demand

### Inventory Optimization Parameters
- Service level range: 90-99%
- Demand variability: 10-40%
- Holding cost rate: 10-30% of unit cost annually
- Ordering cost range: $50-$200 per order
- Safety stock calculation: Statistical method using service level z-score

### Production Planning Parameters
- Setup time: 1-8 hours
- Production rate: 5-50 units per hour
- Resource efficiency: 70-95%
- Production cost: $50-$200 per hour
- Material cost: 60-80% of unit cost

### Supply Chain KPIs
- Inventory Value
- Inventory Carrying Cost
- Production Cost
- Resource Utilization
- Forecast Accuracy
- On-Time Delivery
- Perfect Order Rate

## Data Patterns and Anomalies

### Inventory Patterns
- Sawtooth pattern following EOQ cycle
- Random variations around safety stock levels
- Occasional stockouts based on service level

### Production Patterns
- Production quantities buffered based on forecast confidence
- Resource requirements vary by product complexity
- Setup times independent of production quantity

### Supply Chain Disruptions
- Random disruption events affecting 5% of days
- Variable severity and duration
- Impact on supply availability and lead times

## Advanced Analytics Use Cases

### Inventory Optimization
- Safety stock optimization
- EOQ calculation
- Reorder point determination
- Inventory cost analysis

### Production Planning
- Resource capacity planning
- Production scheduling
- Cost optimization
- Make vs. buy analysis

### Supply Chain Risk Management
- Disruption impact analysis
- Supplier reliability assessment
- Risk mitigation planning
- Resilience modeling

### Performance Management
- KPI tracking and analysis
- Target setting
- Variance analysis
- Performance improvement planning

## Data Quality Notes
- All monetary values are in USD
- Quantities are in base units
- Dates follow ISO 8601 format (YYYY-MM-DD)
- Scores and factors are normalized to 0-1 range
- Missing values are represented as NULL

## Data Generation Parameters
- Time span: 24 months historical + 12 months projection
- Product count: 100-1000
- Location count: 10-100
- Customer count: 50-500
- Supplier count: 10-100
- Resource count: 20-200
- Forecast records: 1000-50000

## Anomaly Patterns
The dataset includes the following types of anomalies:
1. Demand spikes (5% probability)
2. Supply disruptions (3% probability)
3. Seasonal pattern shifts (2% probability)
4. Trend breaks (1% probability)
5. Random noise (constant 2% standard deviation)
