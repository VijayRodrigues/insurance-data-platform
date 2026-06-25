from generators.master.customer_generator import CustomerGenerator
from generators.master.customer_address_generator import CustomerAddressGenerator
from generators.master.business_customer_generator import BusinessCustomerGenerator
from generators.master.branch_generator import BranchGenerator
from generators.master.agent_generator import AgentGenerator
from generators.master.broker_generator import BrokerGenerator
from generators.master.underwriter_generator import UnderwriterGenerator
from generators.master.insurance_product_generator import InsuranceProductGenerator
from generators.master.coverage_type_generator import CoverageTypeGenerator

from generators.sales.quote_generator import QuoteGenerator
from generators.sales.quote_version_generator import QuoteVersionGenerator

from generators.policy.policy_generator import PolicyGenerator
from generators.policy.policy_version_generator import PolicyVersionGenerator
from generators.policy.policy_transaction_generator import PolicyTransactionGenerator
from generators.policy.policy_coverage_generator import PolicyCoverageGenerator
from generators.policy.vehicle_generator import VehicleGenerator
from generators.policy.property_generator import PropertyGenerator

from generators.finance.premium_generator import PremiumGenerator
from generators.finance.premium_payment_generator import PremiumPaymentGenerator

from generators.claims.fnol_generator import FNOLGenerator
from generators.claims.claim_generator import ClaimGenerator
from generators.claims.claim_note_generator import ClaimNoteGenerator
from generators.claims.claim_reserve_generator import ClaimReserveGenerator
from generators.claims.claim_reserve_transaction_generator import ClaimReserveTransactionGenerator
from generators.claims.claim_payment_generator import ClaimPaymentGenerator

from loaders.loader_manager import LoaderManager


# =============================================================================
# MASTER DATA
# =============================================================================

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


# =============================================================================
# SALES
# =============================================================================

quote_generator = QuoteGenerator()

quotes = quote_generator.generate(
    customer_df=customers,
    product_df=products,
    agent_df=agents,
    broker_df=brokers,
    branch_df=branches
)

quote_version_generator = QuoteVersionGenerator()
quote_versions = quote_version_generator.generate(quotes)


# =============================================================================
# POLICY
# =============================================================================

policy_generator = PolicyGenerator()

policies = policy_generator.generate(
    quote_df=quotes,
    quote_version_df=quote_versions,
    underwriter_df=underwriters
)

policy_version_generator = PolicyVersionGenerator()
policy_versions = policy_version_generator.generate(
    policies
)

policy_transaction_generator = PolicyTransactionGenerator()

policy_transactions = policy_transaction_generator.generate(
    policy_df=policies,
    policy_version_df=policy_versions
)

policy_coverage_generator = PolicyCoverageGenerator()

policy_coverages = policy_coverage_generator.generate(
    policy_version_df=policy_versions,
    coverage_type_df=coverages
)

vehicle_generator = VehicleGenerator()
vehicles = vehicle_generator.generate(
    policies
)

property_generator = PropertyGenerator()
properties = property_generator.generate(
    policies
)


# =============================================================================
# FINANCE
# =============================================================================

premium_generator = PremiumGenerator()

premiums = premium_generator.generate(
    policy_df=policies,
    policy_version_df=policy_versions
)

premium_payment_generator = PremiumPaymentGenerator()

premium_payments = premium_payment_generator.generate(
    premiums
)


# =============================================================================
# CLAIMS
# =============================================================================

fnol_generator = FNOLGenerator()
fnols = fnol_generator.generate(
    policies
)

claim_generator = ClaimGenerator()
claims = claim_generator.generate(
    fnols
)

claim_note_generator = ClaimNoteGenerator()
claim_notes = claim_note_generator.generate(
    claims
)

claim_reserve_generator = ClaimReserveGenerator()
claim_reserves = claim_reserve_generator.generate(
    claims
)

claim_reserve_transaction_generator = ClaimReserveTransactionGenerator()

claim_reserve_transactions = (
    claim_reserve_transaction_generator.generate(
        claim_reserves
    )
)

claim_payment_generator = ClaimPaymentGenerator()

claim_payments = claim_payment_generator.generate(
    claims
)


# =============================================================================
# LOAD TO POSTGRESQL
# =============================================================================

datasets = [

    ("master", "branch", branches),
    ("master", "agent", agents),
    ("master", "broker", brokers),
    ("master", "underwriter", underwriters),
    ("master", "insurance_product", products),
    ("master", "coverage_type", coverages),
    ("master", "customer", customers),
    ("master", "customer_address", addresses),
    ("master", "business_customer", business_customers),

    ("sales", "quote", quotes),
    ("sales", "quote_version", quote_versions),

    ("policy", "policy", policies),
    ("policy", "policy_version", policy_versions),
    ("policy", "policy_transaction", policy_transactions),
    ("policy", "policy_coverage", policy_coverages),
    ("policy", "vehicle", vehicles),
    ("policy", "property", properties),

    ("finance", "premium", premiums),
    ("finance", "premium_payment", premium_payments),

    ("claims", "fnol", fnols),
    ("claims", "claim", claims),
    ("claims", "claim_note", claim_notes),
    ("claims", "claim_reserve", claim_reserves),
    ("claims", "claim_reserve_transaction", claim_reserve_transactions),
    ("claims", "claim_payment", claim_payments)

]

loader = LoaderManager()
loader.load_all(datasets)


# =============================================================================
# SUMMARY
# =============================================================================

print("\n==============================================")
print("Insurance Data Platform Pipeline Completed")
print("==============================================")

print(f"Customers               : {len(customers)}")
print(f"Customer Addresses      : {len(addresses)}")
print(f"Business Customers      : {len(business_customers)}")
print(f"Branches                : {len(branches)}")
print(f"Agents                  : {len(agents)}")
print(f"Brokers                 : {len(brokers)}")
print(f"Underwriters            : {len(underwriters)}")
print(f"Insurance Products      : {len(products)}")
print(f"Coverage Types          : {len(coverages)}")
print(f"Quotes                  : {len(quotes)}")
print(f"Quote Versions          : {len(quote_versions)}")
print(f"Policies                : {len(policies)}")
print(f"Policy Versions         : {len(policy_versions)}")
print(f"Policy Transactions     : {len(policy_transactions)}")
print(f"Policy Coverages        : {len(policy_coverages)}")
print(f"Vehicles                : {len(vehicles)}")
print(f"Properties              : {len(properties)}")
print(f"Premiums                : {len(premiums)}")
print(f"Premium Payments        : {len(premium_payments)}")
print(f"FNOLs                   : {len(fnols)}")
print(f"Claims                  : {len(claims)}")
print(f"Claim Notes             : {len(claim_notes)}")
print(f"Claim Reserves          : {len(claim_reserves)}")
print(f"Reserve Transactions    : {len(claim_reserve_transactions)}")
print(f"Claim Payments          : {len(claim_payments)}")

print("\nPipeline completed successfully.")