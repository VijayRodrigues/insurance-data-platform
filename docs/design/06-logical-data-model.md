# Logical Data Model

## 1. Model Overview
This section defines the logical schema only. It does not include SQL or physical database syntax.

The design follows 3NF principles:

- Each entity has a single business purpose
- Non-key attributes depend on the key, the whole key, and nothing but the key
- Repeating groups are extracted into child entities
- Reference values are isolated from transactional data

## 2. Entity Specifications

### customer
| Item | Details |
|---|---|
| Business Purpose | Anchor record for insured individuals or parties |
| Primary Key | customer_id |
| Foreign Keys | customer_type_code |
| Attributes | customer_number, customer_type_code, first_name, last_name, full_name, date_of_birth, national_identifier, email_address, phone_number, created_at, updated_at |
| Data Types | identifiers, text, date, timestamp |
| Nullability | customer_number and customer_type_code required; personal attributes depend on customer type |
| Constraints | customer_number unique; customer_type_code must exist in lookup table |
| Recommended Indexes | customer_number, national_identifier, customer_type_code |
| Relationships | one-to-many with customer_address, one-to-many with policy |

### customer_address
| Item | Details |
|---|---|
| Business Purpose | Stores customer mailing and risk location addresses |
| Primary Key | customer_address_id |
| Foreign Keys | customer_id, address_type_code |
| Attributes | address_line_1, address_line_2, city, state_province, postal_code, country_code, address_type_code, is_primary, effective_start_date, effective_end_date |
| Data Types | text, code, date, boolean |
| Nullability | address_line_1, city, country_code required |
| Constraints | date range must be valid; only one primary address per type per customer |
| Recommended Indexes | customer_id, address_type_code, postal_code |
| Relationships | many-to-one to customer |

### business_customer
| Item | Details |
|---|---|
| Business Purpose | Business-only customer details |
| Primary Key | business_customer_id |
| Foreign Keys | customer_id, industry_code |
| Attributes | customer_id, business_legal_name, trade_name, tax_identifier, incorporation_date, industry_code, employee_count, annual_revenue_band |
| Data Types | identifier, text, date, code, number |
| Nullability | customer_id and business_legal_name required |
| Constraints | customer_id unique; tax_identifier unique where present |
| Recommended Indexes | customer_id, tax_identifier, industry_code |
| Relationships | one-to-one with customer |

### agent
| Item | Details |
|---|---|
| Business Purpose | Authorized sales intermediary |
| Primary Key | agent_id |
| Foreign Keys | branch_id, agent_status_code |
| Attributes | agent_number, agent_name, branch_id, license_number, license_state_code, agent_status_code, appointed_date |
| Data Types | identifier, text, code, date |
| Nullability | agent_number and agent_name required |
| Constraints | agent_number unique; license_number unique where present |
| Recommended Indexes | agent_number, branch_id, agent_status_code |
| Relationships | one-to-many with policy |

### broker
| Item | Details |
|---|---|
| Business Purpose | External broker entity |
| Primary Key | broker_id |
| Foreign Keys | broker_status_code |
| Attributes | broker_number, broker_name, broker_status_code, license_number, license_state_code, appointment_date |
| Data Types | identifier, text, code, date |
| Nullability | broker_number and broker_name required |
| Constraints | broker_number unique |
| Recommended Indexes | broker_number, broker_status_code |
| Relationships | one-to-many with policy |

### branch
| Item | Details |
|---|---|
| Business Purpose | Operating unit for policy issuance and oversight |
| Primary Key | branch_id |
| Foreign Keys | branch_type_code, region_code |
| Attributes | branch_number, branch_name, branch_type_code, region_code, opened_date, closed_date |
| Data Types | identifier, text, code, date |
| Nullability | branch_number and branch_name required |
| Constraints | branch_number unique |
| Recommended Indexes | branch_number, region_code |
| Relationships | one-to-many with agent, policy, underwriter |

### underwriter
| Item | Details |
|---|---|
| Business Purpose | Risk authority for policy approval |
| Primary Key | underwriter_id |
| Foreign Keys | branch_id, underwriting_level_code |
| Attributes | underwriter_number, underwriter_name, branch_id, underwriting_level_code, active_flag |
| Data Types | identifier, text, code, boolean |
| Nullability | underwriter_number and underwriter_name required |
| Constraints | underwriter_number unique |
| Recommended Indexes | underwriter_number, branch_id |
| Relationships | one-to-many with policy |

### insurance_product
| Item | Details |
|---|---|
| Business Purpose | Product catalog for P&C offerings |
| Primary Key | insurance_product_id |
| Foreign Keys | product_line_code, product_status_code |
| Attributes | product_code, product_name, product_line_code, product_status_code, effective_start_date, effective_end_date |
| Data Types | identifier, text, code, date |
| Nullability | product_code and product_name required |
| Constraints | product_code unique |
| Recommended Indexes | product_code, product_line_code, product_status_code |
| Relationships | one-to-many with policy |

### coverage_type
| Item | Details |
|---|---|
| Business Purpose | Standard catalog of available coverages |
| Primary Key | coverage_type_id |
| Foreign Keys | product_line_code, coverage_category_code |
| Attributes | coverage_code, coverage_name, product_line_code, coverage_category_code, default_limit_amount, default_deductible_amount, active_flag |
| Data Types | identifier, text, code, numeric, boolean |
| Nullability | coverage_code and coverage_name required |
| Constraints | coverage_code unique |
| Recommended Indexes | coverage_code, product_line_code, coverage_category_code |
| Relationships | one-to-many with policy_coverage |

### policy
| Item | Details |
|---|---|
| Business Purpose | Primary insurance contract record |
| Primary Key | policy_id |
| Foreign Keys | customer_id, insurance_product_id, branch_id, agent_id, broker_id, underwriter_id, policy_status_code |
| Attributes | policy_number, customer_id, insurance_product_id, branch_id, agent_id, broker_id, underwriter_id, policy_status_code, policy_effective_date, policy_expiry_date, cancellation_date, renewal_policy_id, issued_date |
| Data Types | identifier, text, code, date, timestamp |
| Nullability | policy_number, customer_id, insurance_product_id, branch_id, underwriter_id, policy_status_code, policy_effective_date required |
| Constraints | policy_number unique; expiry must be after effective date |
| Recommended Indexes | policy_number, customer_id, branch_id, policy_status_code, policy_effective_date |
| Relationships | many-to-one to customer, insurance_product, branch, agent/broker, underwriter; one-to-many with policy_version, premium, claim |

### policy_version
| Item | Details |
|---|---|
| Business Purpose | Versioned snapshot of policy state |
| Primary Key | policy_version_id |
| Foreign Keys | policy_id, version_status_code |
| Attributes | policy_version_number, policy_id, version_status_code, version_effective_date, version_expiry_date, change_reason_code, created_at |
| Data Types | identifier, integer, date, code, timestamp |
| Nullability | policy_id, policy_version_number, version_effective_date required |
| Constraints | policy_id and policy_version_number unique together |
| Recommended Indexes | policy_id, policy_version_number, version_effective_date |
| Relationships | many-to-one to policy; one-to-many with policy_coverage and premium |

### policy_coverage
| Item | Details |
|---|---|
| Business Purpose | Coverage selection and limits on a policy version |
| Primary Key | policy_coverage_id |
| Foreign Keys | policy_version_id, coverage_type_id, vehicle_id, property_id |
| Attributes | coverage_limit, deductible_amount, premium_amount, coverage_status_code |
| Data Types | numeric, code |
| Nullability | policy_version_id, coverage_type_id, coverage_limit required |
| Constraints | limit must be positive; deductible cannot be negative |
| Recommended Indexes | policy_version_id, coverage_type_id, vehicle_id, property_id |
| Relationships | many-to-one to policy_version and coverage_type; optional many-to-one to vehicle/property |

### vehicle
| Item | Details |
|---|---|
| Business Purpose | Insured auto risk asset |
| Primary Key | vehicle_id |
| Foreign Keys | customer_id, vehicle_type_code |
| Attributes | vin, registration_number, vehicle_type_code, make, model, model_year, garaging_zip_code |
| Data Types | identifier, text, code, integer |
| Nullability | vin, make, model, model_year required for auto risks |
| Constraints | vin unique |
| Recommended Indexes | vin, customer_id, registration_number |
| Relationships | one-to-many with policy_coverage |

### property
| Item | Details |
|---|---|
| Business Purpose | Insured physical property asset |
| Primary Key | property_id |
| Foreign Keys | customer_id, property_type_code |
| Attributes | property_number, property_type_code, street_address, city, state_province, postal_code, occupancy_type_code, market_value_amount, construction_year |
| Data Types | identifier, text, code, numeric, date |
| Nullability | property_number, property_type_code, street_address, market_value_amount required |
| Constraints | property_number unique |
| Recommended Indexes | property_number, customer_id, postal_code |
| Relationships | one-to-many with policy_coverage |

### premium
| Item | Details |
|---|---|
| Business Purpose | Billed premium obligation for a policy |
| Primary Key | premium_id |
| Foreign Keys | policy_id, policy_version_id, premium_frequency_code, premium_status_code |
| Attributes | premium_number, premium_amount, billing_start_date, billing_end_date, due_date, premium_frequency_code, premium_status_code |
| Data Types | identifier, numeric, date, code |
| Nullability | premium_number, policy_id, premium_amount, due_date required |
| Constraints | premium_number unique; premium_amount positive |
| Recommended Indexes | policy_id, policy_version_id, due_date, premium_status_code |
| Relationships | many-to-one to policy and policy_version; one-to-many with premium_payment |

### premium_payment
| Item | Details |
|---|---|
| Business Purpose | Cash receipt against premium |
| Primary Key | premium_payment_id |
| Foreign Keys | premium_id, payment_method_code, payment_status_code |
| Attributes | payment_reference, payment_date, payment_amount, payment_method_code, payment_status_code |
| Data Types | identifier, date, numeric, code |
| Nullability | premium_id, payment_date, payment_amount required |
| Constraints | payment_amount positive |
| Recommended Indexes | premium_id, payment_date, payment_reference |
| Relationships | many-to-one to premium |

### claim
| Item | Details |
|---|---|
| Business Purpose | Loss event and claim case record |
| Primary Key | claim_id |
| Foreign Keys | policy_id, policy_coverage_id, claim_status_code, loss_cause_code |
| Attributes | claim_reference, policy_id, policy_coverage_id, loss_date, reported_date, claim_status_code, loss_cause_code, claim_description, claim_open_date, claim_close_date, claim_amount |
| Data Types | identifier, text, date, code, numeric |
| Nullability | claim_reference, policy_id, loss_date, reported_date required |
| Constraints | claim_reference unique; reported_date must be on or after loss_date |
| Recommended Indexes | claim_reference, policy_id, loss_date, claim_status_code |
| Relationships | many-to-one to policy and policy_coverage; one-to-many with claim_reserve and claim_payment |

### claim_reserve
| Item | Details |
|---|---|
| Business Purpose | Expected claim liability |
| Primary Key | claim_reserve_id |
| Foreign Keys | claim_id, reserve_type_code, reserve_status_code |
| Attributes | reserve_amount, reserve_as_of_date, reserve_type_code, reserve_status_code, created_at |
| Data Types | numeric, date, code, timestamp |
| Nullability | claim_id, reserve_amount, reserve_as_of_date required |
| Constraints | reserve_amount cannot be negative |
| Recommended Indexes | claim_id, reserve_as_of_date, reserve_type_code |
| Relationships | many-to-one to claim |

### claim_payment
| Item | Details |
|---|---|
| Business Purpose | Monetary settlement on a claim |
| Primary Key | claim_payment_id |
| Foreign Keys | claim_id, claim_payment_type_code, claim_payment_status_code |
| Attributes | payment_reference, payment_date, payment_amount, payment_type_code, payment_status_code |
| Data Types | identifier, date, numeric, code |
| Nullability | claim_id, payment_date, payment_amount required |
| Constraints | payment_amount positive |
| Recommended Indexes | claim_id, payment_date, payment_reference |
| Relationships | many-to-one to claim |

### lookup tables
| Item | Details |
|---|---|
| Business Purpose | Controlled code sets |
| Primary Key | lookup_value_id |
| Foreign Keys | lookup_type_id |
| Attributes | lookup_code, lookup_name, lookup_description, active_flag, effective_start_date, effective_end_date |
| Data Types | identifier, text, boolean, date |
| Nullability | lookup_code and lookup_name required |
| Constraints | unique by lookup_type and lookup_code |
| Recommended Indexes | lookup_type_id, lookup_code |
| Relationships | referenced by many operational entities |

### reference tables
| Item | Details |
|---|---|
| Business Purpose | Stable reference descriptors and business classifications |
| Primary Key | reference_id |
| Foreign Keys | reference_type_code |
| Attributes | reference_code, reference_name, reference_description, active_flag |
| Data Types | identifier, text, boolean |
| Nullability | reference_code and reference_name required |
| Constraints | unique by reference_type and reference_code |
| Recommended Indexes | reference_type_code, reference_code |
| Relationships | referenced by operational entities |

### audit tables
| Item | Details |
|---|---|
| Business Purpose | Track changes, source, and lineage |
| Primary Key | audit_id |
| Foreign Keys | source_entity_id, source_system_code, change_type_code |
| Attributes | source_table_name, source_record_key, change_timestamp, changed_by, change_type_code, before_value, after_value |
| Data Types | identifier, text, timestamp, json-like document field conceptually |
| Nullability | source_table_name, source_record_key, change_timestamp required |
| Constraints | audit event must be immutable |
| Recommended Indexes | source_table_name, source_record_key, change_timestamp |
| Relationships | associated with all mutable entities |

