import os
import pandas as pd
import numpy as np
from faker import Faker
import datetime
import math
import random

# Initialize Faker
fake = Faker()

# Create output directory if it doesn't exist
os.makedirs('sample_data', exist_ok=True)

def generate_product_data(num_products=100):
    """Generate synthetic product data"""
    products = []
    categories = ['Electronics', 'Clothing', 'Food', 'Furniture', 'Automotive']
    lifecycle_stages = ['New', 'Growth', 'Mature', 'Decline']
    
    for i in range(num_products):
        products.append({
            'product_id': f'P{i:04d}',
            'product_name': fake.product_name(),
            'product_category': random.choice(categories),
            'product_lifecycle_stage': random.choice(lifecycle_stages),
            'unit_cost': round(random.uniform(10, 1000), 2),
            'lead_time_days': random.randint(1, 30),
            'min_order_quantity': random.randint(10, 100),
            'pack_size': random.choice([1, 6, 12, 24, 48])
        })
    
    df = pd.DataFrame(products)
    df.to_csv('sample_data/Product.csv', index=False)
    print(f"Generated {os.path.abspath('sample_data/Product.csv')}")
    return df

def generate_location_data(num_locations=20):
    """Generate synthetic location data"""
    locations = []
    location_types = ['DC', 'Store', 'Plant', 'Supplier']
    
    for i in range(num_locations):
        locations.append({
            'location_id': f'L{i:04d}',
            'location_name': fake.city(),
            'location_type': random.choice(location_types),
            'storage_capacity': random.randint(1000, 10000),
            'handling_capacity': random.randint(100, 1000),
            'operating_cost': round(random.uniform(1000, 5000), 2)
        })
    
    df = pd.DataFrame(locations)
    df.to_csv('sample_data/Location.csv', index=False)
    print(f"Generated {os.path.abspath('sample_data/Location.csv')}")
    return df

def generate_customer_data(num_customers=50):
    """Generate synthetic customer data"""
    customers = []
    segments = ['Retail', 'Wholesale', 'Online', 'Direct']
    regions = ['North', 'South', 'East', 'West', 'Central']
    
    for i in range(num_customers):
        customers.append({
            'customer_id': f'C{i:04d}',
            'customer_name': fake.company(),
            'segment': random.choice(segments),
            'region': random.choice(regions),
            'credit_score': round(random.uniform(300, 850), 2),
            'payment_terms': random.choice([30, 45, 60, 90])
        })
    
    df = pd.DataFrame(customers)
    df.to_csv('sample_data/Customer.csv', index=False)
    print(f"Generated {os.path.abspath('sample_data/Customer.csv')}")
    return df

def generate_supplier_data(num_suppliers=30):
    """Generate synthetic supplier data"""
    suppliers = []
    
    for i in range(num_suppliers):
        suppliers.append({
            'supplier_id': f'S{i:04d}',
            'supplier_name': fake.company(),
            'reliability_score': round(random.uniform(0.6, 1.0), 2),
            'capacity': random.randint(1000, 5000),
            'lead_time_variability': round(random.uniform(0.1, 0.5), 2)
        })
    
    df = pd.DataFrame(suppliers)
    df.to_csv('sample_data/Supplier.csv', index=False)
    print(f"Generated {os.path.abspath('sample_data/Supplier.csv')}")
    return df

def generate_resource_data(num_resources=40):
    """Generate synthetic resource data"""
    resources = []
    resource_types = ['Machine', 'Vehicle', 'Worker', 'Tool']
    
    for i in range(num_resources):
        resources.append({
            'resource_id': f'R{i:04d}',
            'resource_type': random.choice(resource_types),
            'capacity': random.randint(100, 1000),
            'efficiency': round(random.uniform(0.7, 1.0), 2),
            'cost_per_hour': round(random.uniform(50, 200), 2)
        })
    
    df = pd.DataFrame(resources)
    df.to_csv('sample_data/Resource.csv', index=False)
    print(f"Generated {os.path.abspath('sample_data/Resource.csv')}")
    return df

def generate_time_dimension(start_date='2023-01-01', periods=36):
    """Generate time dimension data"""
    dates = pd.date_range(start=start_date, periods=periods, freq='M')
    time_data = []
    
    for date in dates:
        time_data.append({
            'date_id': date.strftime('%Y-%m-%d'),
            'year': date.year,
            'quarter': date.quarter,
            'month': date.month,
            'week': date.weekofyear if hasattr(date, 'weekofyear') else date.isocalendar()[1],
            'day_of_week': date.dayofweek,
            'is_holiday': random.random() < 0.1,
            'is_business_day': date.dayofweek < 5
        })
    
    df = pd.DataFrame(time_data)
    df.to_csv('sample_data/TimeDimension.csv', index=False)
    print(f"Generated {os.path.abspath('sample_data/TimeDimension.csv')}")
    return df

def generate_external_factors(start_date, periods):
    """Generate external factors that influence demand"""
    dates = pd.date_range(start=start_date, periods=periods, freq='D')
    
    # Economic indicators
    gdp_trend = np.linspace(1, 1.2, periods) + np.random.normal(0, 0.02, periods)
    inflation = np.random.normal(0.02, 0.005, periods).cumsum()
    
    # Seasonal factors
    season_effect = np.sin(np.linspace(0, 4*np.pi, periods)) * 0.15
    
    # Market events
    market_events = np.zeros(periods)
    event_points = np.random.choice(periods, size=int(periods*0.05), replace=False)
    market_events[event_points] = np.random.uniform(0.1, 0.3, size=len(event_points))
    
    # Weather impact
    weather_impact = np.random.normal(0, 0.1, periods)
    weather_impact = pd.Series(weather_impact).rolling(window=7).mean()
    
    factors_df = pd.DataFrame({
        'date': dates,
        'gdp_factor': gdp_trend,
        'inflation_factor': 1 + inflation,
        'seasonal_factor': 1 + season_effect,
        'market_event_factor': 1 + market_events,
        'weather_impact_factor': 1 + weather_impact
    })
    
    factors_df.to_csv('sample_data/ExternalFactors.csv', index=False)
    return factors_df

def generate_promotion_calendar(start_date, periods, num_products):
    """Generate promotional events calendar"""
    dates = pd.date_range(start=start_date, periods=periods, freq='D')
    promotions = []
    
    promotion_types = ['Price Discount', 'BOGO', 'Bundle Deal', 'Flash Sale']
    
    # Generate promotions for random products and dates
    for _ in range(int(periods * 0.2)):  # 20% of days have promotions
        promo_date = np.random.choice(dates)
        product_id = f'P{random.randint(0, num_products-1):04d}'
        promo_type = random.choice(promotion_types)
        discount = random.uniform(0.1, 0.5)
        duration = random.randint(1, 14)
        
        promotions.append({
            'date': promo_date,
            'product_id': product_id,
            'promotion_type': promo_type,
            'discount_factor': discount,
            'duration_days': duration
        })
    
    promo_df = pd.DataFrame(promotions)
    promo_df.to_csv('sample_data/PromotionCalendar.csv', index=False)
    return promo_df

def generate_supply_disruptions(start_date, periods, num_suppliers):
    """Generate supply chain disruption events"""
    dates = pd.date_range(start=start_date, periods=periods, freq='D')
    disruptions = []
    
    disruption_types = ['Port Delay', 'Production Issue', 'Natural Disaster', 'Labor Strike']
    
    # Generate random disruption events
    for _ in range(int(periods * 0.05)):  # 5% of days have disruptions
        disruption_date = np.random.choice(dates)
        supplier_id = f'S{random.randint(0, num_suppliers-1):04d}'
        disruption_type = random.choice(disruption_types)
        severity = random.uniform(0.3, 1.0)
        duration = random.randint(1, 30)
        
        disruptions.append({
            'date': disruption_date,
            'supplier_id': supplier_id,
            'disruption_type': disruption_type,
            'severity_factor': severity,
            'duration_days': duration
        })
    
    disruption_df = pd.DataFrame(disruptions)
    disruption_df.to_csv('sample_data/SupplyDisruptions.csv', index=False)
    return disruption_df

def generate_demand_forecast(products_df, locations_df, time_df, num_forecasts=1000):
    """Generate synthetic demand forecast data with realistic patterns"""
    forecasts = []
    
    # Get external factors
    external_factors = generate_external_factors(time_df['date'].min(), len(time_df))
    promotions = generate_promotion_calendar(time_df['date'].min(), len(time_df), len(products_df))
    
    for _ in range(num_forecasts):
        product = products_df.sample(n=1).iloc[0]
        location = locations_df.sample(n=1).iloc[0]
        
        # Base demand parameters
        base_demand = random.uniform(100, 1000)
        trend = random.uniform(-0.2, 0.3)
        seasonality = random.uniform(0.1, 0.4)
        noise_level = random.uniform(0.05, 0.15)
        
        for _, time_row in time_df.iterrows():
            date = time_row['date']
            
            # Calculate trend component
            time_factor = (date - time_df['date'].min()).days / 365
            trend_component = (1 + trend * time_factor)
            
            # Calculate seasonal component
            day_of_year = date.dayofyear
            seasonal_component = 1 + seasonality * np.sin(2 * np.pi * day_of_year / 365)
            
            # Get external factors for this date
            date_factors = external_factors[external_factors['date'] == date].iloc[0]
            external_impact = (
                date_factors['gdp_factor'] *
                date_factors['inflation_factor'] *
                date_factors['seasonal_factor'] *
                date_factors['market_event_factor'] *
                date_factors['weather_impact_factor']
            )
            
            # Check for promotions
            promo_impact = 1.0
            active_promos = promotions[
                (promotions['product_id'] == product['product_id']) &
                (promotions['date'] <= date) &
                (promotions['date'] + pd.Timedelta(days=promotions['duration_days']) >= date)
            ]
            if not active_promos.empty:
                promo_impact = 1 + active_promos['discount_factor'].mean()
            
            # Calculate final demand
            demand = base_demand * trend_component * seasonal_component * external_impact * promo_impact
            
            # Add noise
            noise = np.random.normal(0, noise_level * demand)
            demand = max(0, demand + noise)
            
            forecasts.append({
                'date': date,
                'product_id': product['product_id'],
                'location_id': location['location_id'],
                'forecast_quantity': round(demand, 2),
                'confidence_level': random.uniform(0.6, 0.95)
            })
    
    df = pd.DataFrame(forecasts)
    df.to_csv('sample_data/DemandForecast.csv', index=False)
    print(f"Generated {os.path.abspath('sample_data/DemandForecast.csv')}")
    return df

def generate_transport_lanes(locations_df, num_lanes=50):
    """Generate synthetic transport lane data"""
    lanes = []
    transport_modes = ['Road', 'Rail', 'Air', 'Sea']
    
    for i in range(num_lanes):
        # Select random origin and destination
        origin, destination = locations_df.sample(n=2).iloc
        
        lanes.append({
            'lane_id': f'TL{i:04d}',
            'origin_id': origin['location_id'],
            'destination_id': destination['location_id'],
            'transport_mode': random.choice(transport_modes),
            'transit_time': random.randint(1, 10),
            'cost_per_unit': round(random.uniform(5, 50), 2),
            'capacity': random.randint(1000, 5000),
            'reliability': round(random.uniform(0.8, 1.0), 2)
        })
    
    df = pd.DataFrame(lanes)
    df.to_csv('sample_data/TransportLane.csv', index=False)
    print(f"Generated {os.path.abspath('sample_data/TransportLane.csv')}")
    return df

def generate_inventory_data(products_df, locations_df, time_df):
    """Generate inventory data with optimization metrics"""
    inventory_records = []
    
    for _, product in products_df.iterrows():
        for _, location in locations_df.iterrows():
            # Base inventory parameters
            base_stock = random.randint(50, 500)
            demand_variability = random.uniform(0.1, 0.4)
            lead_time = product['lead_time_days']
            service_level = random.uniform(0.9, 0.99)
            
            # Calculate safety stock using statistical method
            z_score = np.abs(np.random.normal(2, 0.5))  # Approximation for service levels
            safety_stock = int(z_score * np.sqrt(lead_time) * demand_variability * base_stock)
            
            # Calculate reorder point
            avg_daily_demand = base_stock / 30  # Approximation
            reorder_point = int(avg_daily_demand * lead_time + safety_stock)
            
            # Calculate EOQ (Economic Order Quantity)
            annual_demand = avg_daily_demand * 365
            ordering_cost = random.uniform(50, 200)
            holding_cost_rate = random.uniform(0.1, 0.3)
            holding_cost = product['unit_cost'] * holding_cost_rate
            eoq = int(np.sqrt((2 * annual_demand * ordering_cost) / holding_cost))
            
            for _, time_row in time_df.iterrows():
                date = time_row['date']
                
                # Generate inventory levels with realistic patterns
                days_passed = (date - time_df['date'].min()).days
                cycle_position = days_passed % (eoq / avg_daily_demand)
                cycle_ratio = cycle_position / (eoq / avg_daily_demand)
                
                # Inventory follows a sawtooth pattern with some noise
                inventory_level = int(max(0, eoq * (1 - cycle_ratio) + np.random.normal(0, safety_stock * 0.1)))
                
                # Calculate inventory metrics
                turns = annual_demand / max(1, inventory_level)
                days_of_supply = max(1, inventory_level) / avg_daily_demand
                carrying_cost = inventory_level * product['unit_cost'] * (holding_cost_rate / 365) * 30  # Monthly
                
                inventory_records.append({
                    'date': date,
                    'product_id': product['product_id'],
                    'location_id': location['location_id'],
                    'quantity_on_hand': inventory_level,
                    'safety_stock_level': safety_stock,
                    'reorder_point': reorder_point,
                    'economic_order_quantity': eoq,
                    'inventory_turns': round(turns, 2),
                    'days_of_supply': round(days_of_supply, 2),
                    'carrying_cost': round(carrying_cost, 2),
                    'stockout_probability': round(1 - service_level, 4),
                    'fill_rate': round(random.uniform(service_level - 0.05, service_level), 4)
                })
    
    df = pd.DataFrame(inventory_records)
    df.to_csv('sample_data/Inventory.csv', index=False)
    print(f"Generated {os.path.abspath('sample_data/Inventory.csv')}")
    return df

def generate_production_plan(products_df, locations_df, time_df, demand_forecast_df):
    """Generate production plans based on demand forecasts"""
    production_records = []
    
    # Filter locations that are manufacturing plants
    plant_locations = locations_df[locations_df['location_type'] == 'Plant']
    
    if len(plant_locations) == 0:
        # If no plants exist, use a subset of locations as plants
        plant_locations = locations_df.sample(min(3, len(locations_df)))
    
    # Group demand forecasts by product, location, and date
    grouped_demand = demand_forecast_df.groupby(['product_id', 'date']).agg({
        'forecast_quantity': 'sum',
        'confidence_level': 'mean'
    }).reset_index()
    
    for _, product in products_df.iterrows():
        # Assign this product to a random plant
        plant = plant_locations.sample(1).iloc[0]
        
        # Production parameters
        setup_time_hours = random.uniform(1, 8)
        production_rate_per_hour = random.uniform(5, 50)
        resource_efficiency = random.uniform(0.7, 0.95)
        
        # Get demand for this product
        product_demand = grouped_demand[grouped_demand['product_id'] == product['product_id']]
        
        for _, demand_row in product_demand.iterrows():
            date = demand_row['date']
            forecast_qty = demand_row['forecast_quantity']
            
            # Calculate production quantities with some buffering
            confidence = demand_row['confidence_level']
            buffer_factor = 1 + (1 - confidence) * 0.5
            planned_qty = int(forecast_qty * buffer_factor)
            
            # Calculate production metrics
            production_hours = (planned_qty / production_rate_per_hour) / resource_efficiency
            total_hours = production_hours + setup_time_hours
            production_cost = total_hours * random.uniform(50, 200)  # Cost per hour
            material_cost = planned_qty * product['unit_cost'] * random.uniform(0.6, 0.8)  # Material is % of unit cost
            
            # Resource requirements as JSON
            resources = {
                'labor_hours': round(total_hours * random.uniform(0.3, 0.5), 2),
                'machine_hours': round(total_hours * random.uniform(0.5, 0.8), 2),
                'setup_hours': round(setup_time_hours, 2),
                'materials_required': [
                    {
                        'material_id': f"M{random.randint(1000, 9999)}",
                        'quantity': round(planned_qty * random.uniform(0.5, 2.0), 2)
                    }
                    for _ in range(random.randint(1, 3))
                ]
            }
            
            production_records.append({
                'date': date,
                'product_id': product['product_id'],
                'location_id': plant['location_id'],
                'planned_quantity': planned_qty,
                'production_hours': round(production_hours, 2),
                'setup_hours': round(setup_time_hours, 2),
                'resource_efficiency': round(resource_efficiency, 2),
                'production_cost': round(production_cost, 2),
                'material_cost': round(material_cost, 2),
                'total_cost': round(production_cost + material_cost, 2),
                'resource_requirements': str(resources)  # Convert to string for CSV
            })
    
    df = pd.DataFrame(production_records)
    df.to_csv('sample_data/ProductionPlan.csv', index=False)
    print(f"Generated {os.path.abspath('sample_data/ProductionPlan.csv')}")
    return df

def generate_kpi_dashboard(inventory_df, production_df, demand_forecast_df, time_df):
    """Generate KPI dashboard metrics for supply chain performance"""
    kpi_records = []
    
    # Calculate inventory KPIs
    inventory_by_date = inventory_df.groupby('date').agg({
        'quantity_on_hand': 'sum',
        'carrying_cost': 'sum'
    }).reset_index()
    
    # Calculate production KPIs
    production_by_date = production_df.groupby('date').agg({
        'planned_quantity': 'sum',
        'total_cost': 'sum',
        'production_hours': 'sum',
        'setup_hours': 'sum'
    }).reset_index()
    
    # Calculate demand KPIs
    demand_by_date = demand_forecast_df.groupby('date').agg({
        'forecast_quantity': 'sum'
    }).reset_index()
    
    # Generate KPIs for each date
    for _, time_row in time_df.iterrows():
        date = time_row['date']
        
        # Get metrics for this date
        try:
            inv_metrics = inventory_by_date[inventory_by_date['date'] == date].iloc[0]
            prod_metrics = production_by_date[production_by_date['date'] == date].iloc[0]
            demand_metrics = demand_by_date[demand_by_date['date'] == date].iloc[0]
            
            # Inventory KPIs
            kpi_records.append({
                'date': date,
                'metric_name': 'Inventory Value',
                'metric_value': round(inv_metrics['quantity_on_hand'] * random.uniform(10, 50), 2),
                'target_value': round(inv_metrics['quantity_on_hand'] * random.uniform(8, 45), 2),
                'dimension_type': 'Overall'
            })
            
            kpi_records.append({
                'date': date,
                'metric_name': 'Inventory Carrying Cost',
                'metric_value': round(inv_metrics['carrying_cost'], 2),
                'target_value': round(inv_metrics['carrying_cost'] * 0.9, 2),
                'dimension_type': 'Overall'
            })
            
            # Production KPIs
            kpi_records.append({
                'date': date,
                'metric_name': 'Production Cost',
                'metric_value': round(prod_metrics['total_cost'], 2),
                'target_value': round(prod_metrics['total_cost'] * 0.95, 2),
                'dimension_type': 'Overall'
            })
            
            kpi_records.append({
                'date': date,
                'metric_name': 'Resource Utilization',
                'metric_value': round(prod_metrics['production_hours'] / (prod_metrics['production_hours'] + prod_metrics['setup_hours']) * 100, 2),
                'target_value': 85.0,
                'dimension_type': 'Overall'
            })
            
            # Supply Chain KPIs
            forecast_accuracy = random.uniform(0.8, 0.98)
            kpi_records.append({
                'date': date,
                'metric_name': 'Forecast Accuracy',
                'metric_value': round(forecast_accuracy * 100, 2),
                'target_value': 95.0,
                'dimension_type': 'Overall'
            })
            
            on_time_delivery = random.uniform(0.85, 0.99)
            kpi_records.append({
                'date': date,
                'metric_name': 'On-Time Delivery',
                'metric_value': round(on_time_delivery * 100, 2),
                'target_value': 98.0,
                'dimension_type': 'Overall'
            })
            
            perfect_order = random.uniform(0.8, 0.95)
            kpi_records.append({
                'date': date,
                'metric_name': 'Perfect Order Rate',
                'metric_value': round(perfect_order * 100, 2),
                'target_value': 95.0,
                'dimension_type': 'Overall'
            })
            
            # Calculate variance
            for record in kpi_records[-7:]:
                record['variance_percentage'] = round((record['metric_value'] - record['target_value']) / record['target_value'] * 100, 2)
                record['dimension_id'] = 'ALL'
                
        except (IndexError, KeyError):
            # Skip dates with missing data
            pass
    
    df = pd.DataFrame(kpi_records)
    df.to_csv('sample_data/KPI_Dashboard.csv', index=False)
    print(f"Generated {os.path.abspath('sample_data/KPI_Dashboard.csv')}")
    return df

def main():
    """Main function to generate all sample data"""
    print("Generating S&OP dataset...")
    
    # Generate master data
    products_df = generate_product_data(num_products=100)
    locations_df = generate_location_data(num_locations=20)
    customers_df = generate_customer_data(num_customers=50)
    suppliers_df = generate_supplier_data(num_suppliers=30)
    resources_df = generate_resource_data(num_resources=40)
    
    # Generate time dimension
    time_df = generate_time_dimension(start_date='2023-01-01', periods=36)
    
    # Generate supply chain disruptions
    disruptions_df = generate_supply_disruptions(time_df['date'].min(), len(time_df), len(suppliers_df))
    
    # Generate demand forecast with external factors
    demand_forecast_df = generate_demand_forecast(products_df, locations_df, time_df, num_forecasts=1000)
    
    # Generate transport lanes
    transport_lanes_df = generate_transport_lanes(locations_df, num_lanes=50)
    
    # Generate inventory data with optimization metrics
    inventory_df = generate_inventory_data(products_df, locations_df, time_df)
    
    # Generate production plans
    production_df = generate_production_plan(products_df, locations_df, time_df, demand_forecast_df)
    
    # Generate KPI dashboard
    kpi_df = generate_kpi_dashboard(inventory_df, production_df, demand_forecast_df, time_df)
    
    print("Dataset generation complete!")
    print(f"Files saved to: {os.path.abspath('sample_data')}")

if __name__ == "__main__":
    main()
