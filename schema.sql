-- Schema for Pistologistics S&OP Dataset
-- Comprehensive database schema for supply chain and logistics data

-- Product dimension table
CREATE TABLE Product (
    product_id VARCHAR(10) PRIMARY KEY,
    product_name VARCHAR(100) NOT NULL,
    product_category VARCHAR(50) NOT NULL,
    product_lifecycle_stage VARCHAR(20) NOT NULL,
    unit_cost DECIMAL(10,2) NOT NULL,
    lead_time_days INTEGER NOT NULL,
    min_order_quantity INTEGER NOT NULL,
    pack_size INTEGER NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Location dimension table
CREATE TABLE Location (
    location_id VARCHAR(10) PRIMARY KEY,
    location_name VARCHAR(100) NOT NULL,
    location_type VARCHAR(20) NOT NULL,
    storage_capacity INTEGER NOT NULL,
    handling_capacity INTEGER NOT NULL,
    operating_cost DECIMAL(10,2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Customer dimension table
CREATE TABLE Customer (
    customer_id VARCHAR(10) PRIMARY KEY,
    customer_name VARCHAR(100) NOT NULL,
    segment VARCHAR(50) NOT NULL,
    region VARCHAR(50) NOT NULL,
    credit_score DECIMAL(5,2) NOT NULL,
    payment_terms INTEGER NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Supplier dimension table
CREATE TABLE Supplier (
    supplier_id VARCHAR(10) PRIMARY KEY,
    supplier_name VARCHAR(100) NOT NULL,
    reliability_score DECIMAL(3,2) NOT NULL,
    capacity INTEGER NOT NULL,
    lead_time_variability DECIMAL(3,2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Time dimension table
CREATE TABLE TimeDimension (
    date_id DATE PRIMARY KEY,
    year INTEGER NOT NULL,
    quarter INTEGER NOT NULL,
    month INTEGER NOT NULL,
    week INTEGER NOT NULL,
    day_of_week INTEGER NOT NULL,
    is_weekend BOOLEAN NOT NULL,
    is_holiday BOOLEAN NOT NULL,
    season VARCHAR(20) NOT NULL
);

-- External factors table
CREATE TABLE ExternalFactors (
    date_id DATE REFERENCES TimeDimension(date_id),
    gdp_factor DECIMAL(5,3) NOT NULL,
    inflation_factor DECIMAL(5,3) NOT NULL,
    seasonal_factor DECIMAL(5,3) NOT NULL,
    market_event_factor DECIMAL(5,3) NOT NULL,
    weather_impact_factor DECIMAL(5,3) NOT NULL,
    PRIMARY KEY (date_id)
);

-- Promotion calendar table
CREATE TABLE PromotionCalendar (
    promotion_id SERIAL PRIMARY KEY,
    product_id VARCHAR(10) REFERENCES Product(product_id),
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    promotion_type VARCHAR(50) NOT NULL,
    discount_factor DECIMAL(3,2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Supply disruptions table
CREATE TABLE SupplyDisruptions (
    disruption_id SERIAL PRIMARY KEY,
    supplier_id VARCHAR(10) REFERENCES Supplier(supplier_id),
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    disruption_type VARCHAR(50) NOT NULL,
    severity_factor DECIMAL(3,2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Transport lanes table
CREATE TABLE TransportLane (
    lane_id SERIAL PRIMARY KEY,
    origin_location_id VARCHAR(10) REFERENCES Location(location_id),
    destination_location_id VARCHAR(10) REFERENCES Location(location_id),
    transport_mode VARCHAR(20) NOT NULL,
    distance_km DECIMAL(10,2) NOT NULL,
    transit_time_days INTEGER NOT NULL,
    cost_per_km DECIMAL(5,2) NOT NULL,
    capacity_weight_kg INTEGER NOT NULL,
    capacity_volume_m3 INTEGER NOT NULL,
    reliability_score DECIMAL(3,2) NOT NULL,
    CONSTRAINT unique_lane UNIQUE (origin_location_id, destination_location_id, transport_mode)
);

-- Demand forecast table
CREATE TABLE DemandForecast (
    forecast_id SERIAL PRIMARY KEY,
    date_id DATE REFERENCES TimeDimension(date_id),
    product_id VARCHAR(10) REFERENCES Product(product_id),
    location_id VARCHAR(10) REFERENCES Location(location_id),
    forecast_quantity DECIMAL(10,2) NOT NULL,
    confidence_level DECIMAL(3,2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Inventory table
CREATE TABLE Inventory (
    inventory_id SERIAL PRIMARY KEY,
    date_id DATE REFERENCES TimeDimension(date_id),
    product_id VARCHAR(10) REFERENCES Product(product_id),
    location_id VARCHAR(10) REFERENCES Location(location_id),
    quantity_on_hand INTEGER NOT NULL,
    quantity_on_order INTEGER NOT NULL,
    safety_stock_level INTEGER NOT NULL,
    reorder_point INTEGER NOT NULL,
    carrying_cost DECIMAL(10,2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Production plan table
CREATE TABLE ProductionPlan (
    plan_id SERIAL PRIMARY KEY,
    date_id DATE REFERENCES TimeDimension(date_id),
    product_id VARCHAR(10) REFERENCES Product(product_id),
    location_id VARCHAR(10) REFERENCES Location(location_id),
    planned_quantity INTEGER NOT NULL,
    resource_requirements JSON NOT NULL,
    production_cost DECIMAL(10,2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- S&OP Scenario table
CREATE TABLE SOP_Scenario (
    scenario_id SERIAL PRIMARY KEY,
    scenario_name VARCHAR(100) NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    description TEXT,
    assumptions JSON NOT NULL,
    created_by VARCHAR(50) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- KPI Dashboard table
CREATE TABLE KPI_Dashboard (
    kpi_id SERIAL PRIMARY KEY,
    date_id DATE REFERENCES TimeDimension(date_id),
    metric_name VARCHAR(50) NOT NULL,
    metric_value DECIMAL(10,2) NOT NULL,
    target_value DECIMAL(10,2) NOT NULL,
    variance_percentage DECIMAL(5,2) NOT NULL,
    dimension_type VARCHAR(20) NOT NULL,
    dimension_id VARCHAR(10) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create indexes for better query performance
CREATE INDEX idx_product_category ON Product(product_category);
CREATE INDEX idx_location_type ON Location(location_type);
CREATE INDEX idx_customer_segment ON Customer(segment);
CREATE INDEX idx_supplier_reliability ON Supplier(reliability_score);
CREATE INDEX idx_time_date ON TimeDimension(date_id);
CREATE INDEX idx_forecast_date_product ON DemandForecast(date_id, product_id);
CREATE INDEX idx_inventory_date_product ON Inventory(date_id, product_id);
CREATE INDEX idx_production_date_product ON ProductionPlan(date_id, product_id);
CREATE INDEX idx_kpi_date_metric ON KPI_Dashboard(date_id, metric_name);
