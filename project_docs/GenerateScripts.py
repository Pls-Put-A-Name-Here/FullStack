from faker import Faker
import random
import datetime

fake = Faker()

# Define lists to store generated IDs
product_ids = []
customer_ids = []
order_ids = []


# Function to generate a random date of birth
def generate_dob():
    return fake.date_of_birth(minimum_age=18, maximum_age=90)


# Function to generate SQL statements for creating user records
def generate_user_records(num_records):
    with open("ecommerce_data.sql", "a") as f:
        f.write("-- User Table\n")
        f.write(
            "INSERT INTO tblUsers (usrName, usrPassword, usrEmail, usrDoB, usrPhoneNumber) VALUES\n"
        )
        for _ in range(num_records):
            usrName = fake.user_name()
            usrPassword = fake.password()
            usrEmail = fake.email()
            usrDoB = generate_dob()
            usrPhoneNumber = fake.phone_number()
            f.write(
                f"('{usrName}', '{usrPassword}', '{usrEmail}', '{usrDoB}', '{usrPhoneNumber}'),\n"
            )
        f.write(";\n\n")


# Function to generate SQL statements for creating address records
def generate_address_records(num_records):
    with open("ecommerce_data.sql", "a") as f:
        f.write("-- Address Table\n")
        f.write(
            "INSERT INTO tblAddresses (adrLocation, adrDigitalAddress, adrHouseAddress) VALUES\n"
        )
        for _ in range(num_records):
            adrLocation = fake.city()
            adrDigitalAddress = fake.street_address()
            adrHouseAddress = fake.address()
            f.write(f"('{adrLocation}', '{adrDigitalAddress}', '{adrHouseAddress}'),\n")
        f.write(";\n\n")


# Function to generate SQL statements for creating customer records
def generate_customer_records(num_records):
    with open("ecommerce_data.sql", "a") as f:
        f.write("-- Customer Table\n")
        f.write("INSERT INTO tblCustomers (custUsrIdfk, custAdrIdfk) VALUES\n")
        for _ in range(num_records):
            custUsrIdfk = fake.random_int(
                min=1, max=num_records
            )  # Assuming user IDs start from 1
            custAdrIdfk = fake.random_int(
                min=1, max=num_records
            )  # Assuming address IDs start from 1
            f.write(f"({custUsrIdfk}, {custAdrIdfk}),\n")
            customer_ids.append(_ + 1)
        f.write(";\n\n")


# Function to generate SQL statements for creating Brand records
def generate_brand_records(num_records):
    with open("ecommerce_data.sql", "a") as f:
        f.write("-- Brand Table\n")
        f.write(
            "INSERT INTO tblBrands (brdName, brdCountryOfOrigin, brdYearEstablished, brdDescription, brdCreatedDate, brdLastEditDate) VALUES\n"
        )
        for _ in range(num_records):
            brdName = fake.company()
            brdCountryOfOrigin = fake.country()
            brdYearEstablished = fake.random_int(
                min=1800, max=2023
            )  # Assuming brands could be established from 1800 to 2023
            brdDescription = fake.text()
            brdCreatedDate = fake.date_time_between(start_date="-1y", end_date="now")
            brdLastEditDate = brdCreatedDate
            f.write(
                f"('{brdName}', '{brdCountryOfOrigin}', {brdYearEstablished}, '{brdDescription}', '{brdCreatedDate}', '{brdLastEditDate}'),\n"
            )
        f.write(";\n\n")


# Function to generate SQL statements for creating Product Category records
def generate_product_category_records(num_records):
    with open("ecommerce_data.sql", "a") as f:
        f.write("-- Product Category Table\n")
        f.write(
            "INSERT INTO tblProductCategories (ctgName, ctgCreatedDate, ctgLastEditDate) VALUES\n"
        )
        for _ in range(num_records):
            ctgName = fake.word()
            ctgCreatedDate = fake.date_time_between(start_date="-1y", end_date="now")
            ctgLastEditDate = ctgCreatedDate
            f.write(f"('{ctgName}', '{ctgCreatedDate}', '{ctgLastEditDate}'),\n")
        f.write(";\n\n")


# Function to generate SQL statements for creating Product Subcategory records
def generate_product_subcategory_records(num_records):
    with open("ecommerce_data.sql", "a") as f:
        f.write("-- Product Subcategory Table\n")
        f.write(
            "INSERT INTO tblProductSubCategories (sctgName, sctgCreatedDate, sctgLastEditDate) VALUES\n"
        )
        for _ in range(num_records):
            sctgName = fake.word()
            sctgCreatedDate = fake.date_time_between(start_date="-1y", end_date="now")
            sctgLastEditDate = sctgCreatedDate
            f.write(f"('{sctgName}', '{sctgCreatedDate}', '{sctgLastEditDate}'),\n")
        f.write(";\n\n")


# Function to generate SQL statements for creating Product records
def generate_product_records(num_records):
    with open("ecommerce_data.sql", "a") as f:
        f.write("-- Product Table\n")
        f.write(
            "INSERT INTO tblProducts (prdBrdIdfk, prdCtgIdfk, prdSctgIdfk, prdName, prdDescription, prdUnitPrice, prdStockQuantity, prdCreatedDate, prdLastEditDate) VALUES\n"
        )
        for _ in range(num_records):
            prdBrdIdfk = fake.random_int(
                min=1, max=num_records
            )  # Assuming Brand IDs start from 1
            prdCtgIdfk = fake.random_int(
                min=1, max=num_records
            )  # Assuming Product Category IDs start from 1
            prdSctgIdfk = fake.random_int(
                min=1, max=num_records
            )  # Assuming Product Subcategory IDs start from 1
            prdName = fake.catch_phrase()
            prdDescription = fake.text()
            prdUnitPrice = round(
                random.uniform(10, 1000), 2
            )  # Random price between 10 and 1000
            prdStockQuantity = fake.random_int(min=0, max=1000)
            prdCreatedDate = fake.date_time_between(start_date="-1y", end_date="now")
            prdLastEditDate = prdCreatedDate
            f.write(
                f"({prdBrdIdfk}, {prdCtgIdfk}, {prdSctgIdfk}, '{prdName}', '{prdDescription}', {prdUnitPrice}, {prdStockQuantity}, '{prdCreatedDate}', '{prdLastEditDate}'),\n"
            )
            product_ids.append(_ + 1)
        f.write(";\n\n")


# Function to generate SQL statements for creating Product Images records
def generate_product_images_records(num_records, product_ids):
    with open("ecommerce_data.sql", "a") as f:
        f.write("-- Product Images Table\n")
        f.write(
            "INSERT INTO tblProductImages (imgPrdIdfk, imgURL, imgDescription, imgUploadDate, imgLastEditDate) VALUES\n"
        )
        for _ in range(num_records):
            imgPrdIdfk = random.choice(product_ids)
            imgURL = fake.image_url()
            imgDescription = fake.text()
            imgUploadDate = fake.date_time_between(start_date="-1y", end_date="now")
            imgLastEditDate = imgUploadDate
            f.write(
                f"({imgPrdIdfk}, '{imgURL}', '{imgDescription}', '{imgUploadDate}', '{imgLastEditDate}'),\n"
            )
        f.write(";\n\n")


# Function to generate SQL statements for creating Product Details records
def generate_product_details_records(num_records, product_ids):
    with open("ecommerce_data.sql", "a") as f:
        f.write("-- Product Details Table\n")
        f.write(
            "INSERT INTO tblProductDetails (prdDetailsPrdIdfk, prdWeight, prdHeight, prdDimensions, prdTechnicalSpecification, prdDetailsCreatedDate, prdDetailsLastEditDate) VALUES\n"
        )
        for _ in range(num_records):
            prdDetailsPrdIdfk = random.choice(product_ids)
            prdWeight = fake.random_element(
                elements=("100g", "200g", "300g", "500g", "1kg")
            )
            prdHeight = fake.random_element(
                elements=("10cm", "20cm", "30cm", "40cm", "50cm")
            )
            prdDimensions = fake.random_element(
                elements=("5x5x5cm", "10x10x10cm", "15x15x15cm")
            )
            prdTechnicalSpecification = fake.text()
            prdDetailsCreatedDate = fake.date_time_between(
                start_date="-1y", end_date="now"
            )
            prdDetailsLastEditDate = prdDetailsCreatedDate
            f.write(
                f"({prdDetailsPrdIdfk}, '{prdWeight}', '{prdHeight}', '{prdDimensions}', '{prdTechnicalSpecification}', '{prdDetailsCreatedDate}', '{prdDetailsLastEditDate}'),\n"
            )
        f.write(";\n\n")


# Function to generate SQL statements for creating Product Variants records
def generate_product_variants_records(num_records, product_ids):
    with open("ecommerce_data.sql", "a") as f:
        f.write("-- Product Variants Table\n")
        f.write(
            "INSERT INTO tblProductVariants (prvPrdIdfk, prvColor, prvSize, prvMaterial, prvPriceModifier, prvQuantityAvailable, prvSKU) VALUES\n"
        )
        for _ in range(num_records):
            prvPrdIdfk = random.choice(product_ids)
            prvColor = fake.color_name()
            prvSize = fake.random_element(elements=("Small", "Medium", "Large", "XL"))
            prvMaterial = fake.random_element(
                elements=("Cotton", "Polyester", "Wool", "Silk")
            )
            prvPriceModifier = round(random.uniform(-50, 50), 2)
            prvQuantityAvailable = fake.random_int(min=0, max=100)
            prvSKU = fake.uuid4()
            f.write(
                f"({prvPrdIdfk}, '{prvColor}', '{prvSize}', '{prvMaterial}', {prvPriceModifier}, {prvQuantityAvailable}, '{prvSKU}'),\n"
            )
        f.write(";\n\n")


# Function to generate SQL statements for creating Order Status records
def generate_order_status_records():
    with open("ecommerce_data.sql", "a") as f:
        f.write("-- Order Status Table\n")
        f.write(
            "INSERT INTO tblOrderStatuses (ordStatusIdpk, ordStatusName, ordStatusDescription, ordStatusCreatedDate, ordStatusLastEditDate) VALUES\n"
        )
        f.write(
            "(1, 'Pending', 'Order is pending processing', GETDATE(), GETDATE()),\n"
        )
        f.write(
            "(2, 'Processing', 'Order is being processed', GETDATE(), GETDATE()),\n"
        )
        f.write("(3, 'Shipped', 'Order has been shipped', GETDATE(), GETDATE()),\n")
        f.write(
            "(4, 'Delivered', 'Order has been delivered', GETDATE(), GETDATE());\n\n"
        )


# Function to generate SQL statements for creating Payment Status records
def generate_payment_status_records():
    with open("ecommerce_data.sql", "a") as f:
        f.write("-- Payment Status Table\n")
        f.write(
            "INSERT INTO tblPaymentStatuses (pstIdpk, pstStatusName, pstDescription, pstCreatedDate, pstLastUpdateDate) VALUES\n"
        )
        f.write("(1, 'Pending', 'Payment is pending', GETDATE(), GETDATE()),\n")
        f.write(
            "(2, 'Completed', 'Payment has been completed', GETDATE(), GETDATE()),\n"
        )
        f.write("(3, 'Failed', 'Payment has failed', GETDATE(), GETDATE());\n\n")


# Function to generate SQL statements for creating Order records
def generate_order_records(num_records, customer_ids):
    with open("ecommerce_data.sql", "a") as f:
        f.write("-- Order Table\n")
        f.write(
            "INSERT INTO tblOrders (ordCustIdpk, ordDate, ordDeliveryAddress, ordTotalCost, ordStatusIdfk, ordStatusCreatedDate, LastUpdateDate) VALUES\n"
        )
        for _ in range(num_records):
            ordCustIdpk = random.choice(customer_ids)
            ordDate = fake.date_time_between(start_date="-1y", end_date="now")
            ordDeliveryAddress = fake.address()
            ordTotalCost = round(
                random.uniform(10, 1000), 2
            )  # Random total cost between 10 and 1000
            ordStatusIdfk = random.randint(
                1, 4
            )  # Assuming there are 4 order status types
            ordStatusCreatedDate = fake.date_time_between(
                start_date="-1y", end_date="now"
            )
            LastUpdateDate = ordStatusCreatedDate
            f.write(
                f"({ordCustIdpk}, '{ordDate}', '{ordDeliveryAddress}', {ordTotalCost}, {ordStatusIdfk}, '{ordStatusCreatedDate}', '{LastUpdateDate}'),\n"
            )
            order_ids.append(_ + 1)
        f.write(";\n\n")


# Function to generate SQL statements for creating Order Item records
def generate_order_item_records(num_records, order_ids, product_ids):
    with open("ecommerce_data.sql", "a") as f:
        f.write("-- Order Item Table\n")
        f.write(
            "INSERT INTO tblOrderItem (ordtOrdIdfk, ordtPrdIdfk, ordtQuantity, ordtUnitPrice, ordtSubtotal, ordtCreatedDate, ordtLastUpdateDate) VALUES\n"
        )
        for _ in range(num_records):
            ordtOrdIdfk = random.choice(order_ids)
            ordtPrdIdfk = random.choice(product_ids)
            ordtQuantity = fake.random_int(min=1, max=10)
            ordtUnitPrice = round(
                random.uniform(10, 1000), 2
            )  # Random unit price between 10 and 1000
            ordtSubtotal = ordtQuantity * ordtUnitPrice
            ordtCreatedDate = fake.date_time_between(start_date="-1y", end_date="now")
            ordtLastUpdateDate = ordtCreatedDate
            f.write(
                f"({ordtOrdIdfk}, {ordtPrdIdfk}, {ordtQuantity}, {ordtUnitPrice}, {ordtSubtotal}, '{ordtCreatedDate}', '{ordtLastUpdateDate}'),\n"
            )
        f.write(";\n\n")


# Function to generate SQL statements for creating Supplier records
def generate_supplier_records(num_records):
    with open("ecommerce_data.sql", "a") as f:
        f.write("-- Supplier Table\n")
        f.write(
            "INSERT INTO tblSuppliers (supName, supContactInfo, supAddressLine1, supAddressLine2, supCity, supState, supPostalCode, supCountry) VALUES\n"
        )
        for _ in range(num_records):
            supName = fake.company()
            supContactInfo = fake.phone_number()
            supAddressLine1 = fake.street_address()
            supAddressLine2 = fake.secondary_address()
            supCity = fake.city()
            supState = fake.state()
            supPostalCode = fake.postcode()
            supCountry = fake.country()
            f.write(
                f"('{supName}', '{supContactInfo}', '{supAddressLine1}', '{supAddressLine2}', '{supCity}', '{supState}', '{supPostalCode}', '{supCountry}'),\n"
            )
        f.write(";\n\n")


# Set the number of records to generate
num_product_images = 1000
num_product_details = 1000
num_product_variants = 1000
num_order_statuses = 4
num_payment_statuses = 3
num_orders = 1000
num_order_items = 1000
num_suppliers = 1000
num_brands = 1000
num_categories = 1000
num_subcategories = 1000
num_products = 1000
num_users = 1000
num_addresses = 1000
num_customers = 1000


# Generate SQL statements for the  tables

# Generate SQL statements for brand, product category, product subcategory, and product records
generate_brand_records(num_brands)
generate_product_category_records(num_categories)
generate_product_subcategory_records(num_subcategories)
generate_product_records(num_products)


# Generate SQL statements for user, address, and customer records
generate_user_records(num_users)
generate_address_records(num_addresses)
generate_customer_records(num_customers)

# Assuming product_ids and customer_ids are available from previous data generation
generate_product_images_records(num_product_images, product_ids)
generate_product_details_records(num_product_details, product_ids)
generate_product_variants_records(num_product_variants, product_ids)
generate_order_status_records()
generate_payment_status_records()
generate_order_records(num_orders, customer_ids)
generate_order_item_records(num_order_items, order_ids, product_ids)
generate_supplier_records(num_suppliers)
