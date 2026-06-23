from generators.base_generator import BaseGenerator


class BranchGenerator(BaseGenerator):

    def generate(self):

        branches = [

            {
                "branch_id": 1,
                "branch_code": "BLR001",
                "branch_name": "Bangalore Branch",
                "address_line_1": "Prestige Tech Park",
                "address_line_2": "Outer Ring Road",
                "city": "Bengaluru",
                "state": "Karnataka",
                "postal_code": "560103",
                "country": "India",
                "phone_number": "+91-80-40000001",
                "email_address": "blr.branch@insuranceplatform.com",
                "branch_status": "ACTIVE",
                **self.audit_columns()
            },

            {
                "branch_id": 2,
                "branch_code": "MUM001",
                "branch_name": "Mumbai Branch",
                "address_line_1": "BKC Business Park",
                "address_line_2": "Bandra Kurla Complex",
                "city": "Mumbai",
                "state": "Maharashtra",
                "postal_code": "400051",
                "country": "India",
                "phone_number": "+91-22-40000002",
                "email_address": "mum.branch@insuranceplatform.com",
                "branch_status": "ACTIVE",
                **self.audit_columns()
            },

            {
                "branch_id": 3,
                "branch_code": "DEL001",
                "branch_name": "New Delhi Branch",
                "address_line_1": "Connaught Place",
                "address_line_2": "Block A",
                "city": "New Delhi",
                "state": "Delhi",
                "postal_code": "110001",
                "country": "India",
                "phone_number": "+91-11-40000003",
                "email_address": "del.branch@insuranceplatform.com",
                "branch_status": "ACTIVE",
                **self.audit_columns()
            },

            {
                "branch_id": 4,
                "branch_code": "CHE001",
                "branch_name": "Chennai Branch",
                "address_line_1": "OMR IT Corridor",
                "address_line_2": "Sholinganallur",
                "city": "Chennai",
                "state": "Tamil Nadu",
                "postal_code": "600119",
                "country": "India",
                "phone_number": "+91-44-40000004",
                "email_address": "che.branch@insuranceplatform.com",
                "branch_status": "ACTIVE",
                **self.audit_columns()
            },

            {
                "branch_id": 5,
                "branch_code": "HYD001",
                "branch_name": "Hyderabad Branch",
                "address_line_1": "HITEC City",
                "address_line_2": "Madhapur",
                "city": "Hyderabad",
                "state": "Telangana",
                "postal_code": "500081",
                "country": "India",
                "phone_number": "+91-40-40000005",
                "email_address": "hyd.branch@insuranceplatform.com",
                "branch_status": "ACTIVE",
                **self.audit_columns()
            }

        ]

        return self.dataframe(branches)