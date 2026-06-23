from generators.master.customer_generator import CustomerGenerator
from generators.master.customer_address_generator import CustomerAddressGenerator
from generators.master.business_customer_generator import BusinessCustomerGenerator
from generators.master.branch_generator import BranchGenerator
from generators.master.agent_generator import AgentGenerator
from generators.master.broker_generator import BrokerGenerator
from generators.master.underwriter_generator import UnderwriterGenerator
from generators.master.insurance_product_generator import InsuranceProductGenerator
from generators.master.coverage_type_generator import CoverageTypeGenerator

customer_generator = CustomerGenerator()
customers = customer_generator.generate(20)

address_generator = CustomerAddressGenerator()
addresses = address_generator.generate(customers)

business_generator = BusinessCustomerGenerator()
business_customers = business_generator.generate(customers)

branch_generator = BranchGenerator()
branches = branch_generator.generate()

agent_generator = AgentGenerator()
agents = agent_generator.generate(
    branch_df=branches,
    number_of_agents=50
)

broker_generator = BrokerGenerator()
brokers = broker_generator.generate(
    number_of_brokers=25
)

underwriter_generator = UnderwriterGenerator()
underwriters = underwriter_generator.generate(
    branch_df=branches,
    number_of_underwriters=20
)

product_generator = InsuranceProductGenerator()
products = product_generator.generate()

coverage_generator = CoverageTypeGenerator()
coverages = coverage_generator.generate()


print(customers.head())

print()

print(addresses.head())

print()

print(business_customers.head())

print()

print(branches.head())

print()

print(agents.head())

print()

print(brokers.head())

print()

print(underwriters.head())

print()

print(products.head())

print()

print(coverages.head())

print()



print(f"Customers           : {len(customers)}")
print(f"Customer Addresses  : {len(addresses)}")
print(f"Business Customers  : {len(business_customers)}")
print(f"Branches            : {len(branches)}")
print(f"Agents              : {len(agents)}")
print(f"Brokers             : {len(brokers)}")
print(f"Underwriters        : {len(underwriters)}")
print(f"Insurance Products  : {len(products)}")
print(f"Coverage Types      : {len(coverages)}")