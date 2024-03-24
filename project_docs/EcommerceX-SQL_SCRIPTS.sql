--Bright Start
-- User Table
CREATE TABLE tblUsers (
    usrIdpk INT PRIMARY KEY IDENTITY(1,1),
    usrName NVARCHAR(50),
    usrPassword NVARCHAR(50),
	usrEmail NVARCHAR(50),
	usrDoB Date,
	usrPhoneNumber NVARCHAR(50)
);
-- Address Table
CREATE TABLE tblAddresses (
    adrIdpk INT PRIMARY KEY IDENTITY(1,1),
    adrLocation NVARCHAR(255),
    adrDigitalAddress NVARCHAR(255),
    adrHouseAddress NVARCHAR(255)
);
-- Customer Table
CREATE TABLE tblCustomers (
    custIdpk INT PRIMARY KEY IDENTITY(1,1),
    custUsrIdfk INT FOREIGN KEY REFERENCES tblUsers(usrIdpk),
    custAdrIdfk INT FOREIGN KEY REFERENCES tblAddresses(adrIdpk)
);

-- Brand Table
CREATE TABLE tblBrands (
    brdIdpk INT PRIMARY KEY IDENTITY(1,1),
    brdName NVARCHAR(100) NOT NULL,
    brdCountryOfOrigin NVARCHAR(100),
    brdYearEstablished INT,
    brdDescription TEXT,
    brdCreatedDate DATETIME DEFAULT GETDATE(),
    brdLastEditDate DATETIME DEFAULT GETDATE()
);

-- Product Category Table
CREATE TABLE tblProductCategories (
    ctgIdpk INT PRIMARY KEY IDENTITY(1,1),
    ctgName NVARCHAR(100) NOT NULL,
    ctgCreatedDate DATETIME DEFAULT GETDATE(),
    ctgLastEditDate DATETIME DEFAULT GETDATE(),
);
-- Bright Ends
-- Kirk Starts 
-- ProductSubCategories Table
CREATE TABLE tblProductSubCategories(
	sctgIdpk INT PRIMARY KEY IDENTITY(1,1),
    sctgName NVARCHAR(100) NOT NULL,
    sctgCreatedDate DATETIME DEFAULT GETDATE(),
    sctgLastEditDate DATETIME DEFAULT GETDATE(),
 
);
-- Product Table
CREATE TABLE tblProducts (
    prdIdpk INT PRIMARY KEY IDENTITY(1,1),
    prdBrdIdfk INT FOREIGN KEY REFERENCES tblBrands(brdIdpk),
	prdCtgIdfk INT FOREIGN KEY REFERENCES tblProductCategories(ctgIdpk),
    prdSctgIdfk INT FOREIGN KEY REFERENCES tblProductSubCategories(sctgIdpk),
    prdName NVARCHAR(255) NOT NULL,
    prdDescription TEXT,
    prdUnitPrice DECIMAL(10, 2),
    prdStockQuantity INT,
    prdCreatedDate DATETIME DEFAULT GETDATE(),
    prdLastEditDate DATETIME DEFAULT GETDATE()
);

-- Product Images Table
CREATE TABLE tblProductImages (
    imgIdpk INT PRIMARY KEY IDENTITY(1,1),
    imgPrdIdfk INT FOREIGN KEY REFERENCES tblProducts(prdIdpk),
    imgURL NVARCHAR(255),
    imgDescription TEXT,
    imgUploadDate DATETIME DEFAULT GETDATE(),
    imgLastEditDate DATETIME DEFAULT GETDATE()
);
-- 9 Product Details Table
CREATE TABLE tblProductDetails (
    prdDetailsIdpk INT PRIMARY KEY,
    prdDetailsPrdIdfk INT FOREIGN KEY REFERENCES tblProducts(prdIdpk),
    prdWeight NVARCHAR(100),
    prdHeight NVARCHAR(255),
	prdDimensions NVARCHAR(100),
	prdTechnicalSpecification NVARCHAR(100),
	prdDetailsCreatedDate DATETIME DEFAULT GETDATE(),
    prdDetailsLastEditDate DATETIME DEFAULT GETDATE()
);

-- Product Variants Tablew
CREATE TABLE tblProductVariants (
    prvIdpk INT PRIMARY KEY IDENTITY(1,1),
    prvPrdIdfk INT FOREIGN KEY REFERENCES tblProducts(prdIdpk),
    prvColor NVARCHAR(50),
    prvSize NVARCHAR(50),
    prvMaterial NVARCHAR(50),
    prvPriceModifier DECIMAL(10, 2),
    prvQuantityAvailable INT,
    prvSKU NVARCHAR(100),
    prvCreatedDate DATETIME DEFAULT GETDATE(),
    prvLastEditDate DATETIME DEFAULT GETDATE()
);
-- Kirk Ends

--Joseph Starts
-- Order Status Table
CREATE TABLE tblOrderStatuses (
    ordStatusIdpk INT PRIMARY KEY,
    ordStatusName NVARCHAR(50),
    ordStatusDescription TEXT,
    ordStatusCreatedDate DATETIME DEFAULT GETDATE(),
    ordStatusLastEditDate DATETIME DEFAULT GETDATE()
);

-- Payment Status Table
CREATE TABLE tblPaymentStatuses (
    pstIdpk INT PRIMARY KEY,
    pstStatusName NVARCHAR(50),
    pstDescription TEXT,
    pstCreatedDate DATETIME DEFAULT GETDATE(),
    pstLastUpdateDate DATETIME DEFAULT GETDATE()
);

-- Order Table
CREATE TABLE tblOrders (
    ordIdpk INT PRIMARY KEY IDENTITY(1,1),
    ordCustIdpk INT FOREIGN KEY REFERENCES tblCustomers(custIdpk),
    ordDate DATETIME,
    ordDeliveryAddress NVARCHAR(255),
    ordTotalCost DECIMAL(10, 2),
    ordStatusIdfk INT FOREIGN KEY REFERENCES tblOrderStatuses(ordStatusIdpk),
    ordStatusCreatedDate DATETIME DEFAULT GETDATE(),
    LastUpdateDate DATETIME DEFAULT GETDATE()
);

-- Order Item Table
CREATE TABLE tblOrderItem (
    ordtIdpk INT PRIMARY KEY IDENTITY(1,1),
    ordtOrdIdfk INT FOREIGN KEY REFERENCES tblOrders(ordIdpk),
    ordtPrdIdfk INT FOREIGN KEY REFERENCES tblProducts(prdIdpk),
    ordtQuantity INT,
    ordtUnitPrice DECIMAL(10, 2),
    ordtSubtotal DECIMAL(10, 2),
    ordtCreatedDate DATETIME DEFAULT GETDATE(),
    ordtLastUpdateDate DATETIME DEFAULT GETDATE()
);

-- Supplier Table
CREATE TABLE tblSuppliers (
    supIdpk INT PRIMARY KEY IDENTITY(1,1),
    supName NVARCHAR(100) NOT NULL,
    supContactInfo NVARCHAR(255),
    supAddressLine1 NVARCHAR(255),
    supAddressLine2 NVARCHAR(255),
    supCity NVARCHAR(100),
    supState NVARCHAR(100),
    supPostalCode NVARCHAR(20),
    supCountry NVARCHAR(100)
);
--Joseph Ends

-- Jonathan Starts
-- Inventory Table
CREATE TABLE tblInventory (
    invIdpk INT PRIMARY KEY IDENTITY(1,1),
    invPrdIdfk INT FOREIGN KEY REFERENCES tblProducts(prdIdpk),
    invQuantityAvailable INT,
    invUnitPrice DECIMAL(10, 2),
    invUnitCost DECIMAL(10, 2),
    invSupIdfk INT FOREIGN KEY REFERENCES tblSuppliers(supIdpk),
    invDateAdded DATETIME,
    invExpirationDate DATETIME,
    invLastUpdateDate DATETIME DEFAULT GETDATE()
);
-- 17 Payment Methods Table
CREATE TABLE tblPaymentMethods(
	pmtIdpk INT PRIMARY KEY IDENTITY(1,1),
	pmtName NVARCHAR(100),
	pmtDescription NVARCHAR(255),
	pmtCreatedDate DATETIME DEFAULT GETDATE(),
	pmtLastUpdateDate DATETIME DEFAULT GETDATE()
);

-- Purchase Table
CREATE TABLE tblPurchase (
    pchIdpk INT PRIMARY KEY IDENTITY(1,1),
    pchCustIdfk INT FOREIGN KEY REFERENCES tblCustomers(custIdpk),
    pchPurchaseDate DATETIME,
    pchTotalAmount DECIMAL(10, 2),
    pchPmtIdfk INT FOREIGN KEY REFERENCES tblPaymentMethods(pmtIdpk),
    pchPstIdfk INT FOREIGN KEY REFERENCES tblPaymentStatuses(pstIdpk),
    pchCreatedDate DATETIME DEFAULT GETDATE(),
    pchLastUpdateDate DATETIME DEFAULT GETDATE()
);



-- Cart Table
CREATE TABLE tblCarts (
    crtIdpk INT PRIMARY KEY IDENTITY(1,1),
    crtCustomerIdfk INT FOREIGN KEY REFERENCES tblCustomers(custIdpk),
    crtCreatedAt DATETIME DEFAULT GETDATE(),
    crtStatus NVARCHAR(50) DEFAULT 'Active'
);

-- Cart Items Table
CREATE TABLE tblCartItems (
    crtItemIdpk INT PRIMARY KEY IDENTITY(1,1),
    crtItemCrtIdfk INT FOREIGN KEY REFERENCES tblCarts(crtIdpk),
    crtItemPrdIdfk INT FOREIGN KEY REFERENCES tblProducts(prdIdpk),
    crtItemQuantity INT,
    crtItemUnitPrice DECIMAL(10, 2)
);
-- Jonathan Ends

--Vine Starts
-- Reviews Table
CREATE TABLE tblReviews (
    revIdpk INT PRIMARY KEY IDENTITY(1,1),
    revPrdIdfk INT FOREIGN KEY REFERENCES tblProducts(prdIdpk),
    revCustIdfk INT FOREIGN KEY REFERENCES tblCustomers(custIdpk),
    revRating INT,
    revComments TEXT
);

-- Ratings Table
CREATE TABLE tblRatings (
    ratIdpk INT PRIMARY KEY IDENTITY(1,1),
    ratPrdIdfk INT FOREIGN KEY REFERENCES tblProducts(prdIdpk),
    ratCustIdfk INT FOREIGN KEY REFERENCES tblCustomers(custIdpk),
    ratRating INT,
    ratComments TEXT,
    ratTimestamp DATETIME DEFAULT GETDATE()
);

-- Accounts Table
CREATE TABLE tblAccounts (
    accIdpk INT PRIMARY KEY IDENTITY(1,1),
	accUsrIdfk INT FOREIGN KEY REFERENCES tblUsers(usrIDpk),
    accUsername VARCHAR(50) NOT NULL,
    accPasswordHash VARCHAR(100) NOT NULL,
    accEmail VARCHAR(100) NOT NULL,
    accCreatedAt DATETIME DEFAULT GETDATE(),
	accLastUpdateDate DATETIME DEFAULT GETDATE(),
    accLastLogin DATETIME,
    accIsActive BIT DEFAULT 1
);

-- Roles Table
CREATE TABLE tblRoles (
    rolIdpk INT PRIMARY KEY IDENTITY(1,1),
    rolName VARCHAR(50) NOT NULL,
    rolDescription VARCHAR(255)
);

-- UserRoles Table
CREATE TABLE tblUserRoles (
    urlIdpk INT PRIMARY KEY IDENTITY(1,1),
    urlAccIdfk INT FOREIGN KEY REFERENCES tblAccounts(accIdpk),
    urlRolIdfk INT FOREIGN KEY REFERENCES tblRoles(rolIdpk)
);
-- vine Ends

-- Pick one of the below tables in this order and write models on them.
-- Comment them afterwards
--Bright
--Kirk
--Joseph
-- Jonathan
--Vine


---- Payment Details Table
--CREATE TABLE tblPaymentDetails (
--    pydIdpk INT PRIMARY KEY IDENTITY(1,1),
--    ProductID INT FOREIGN KEY REFERENCES tblProducts(ProductID),
--    AddID INT FOREIGN KEY REFERENCES Address(AddID)
--);

---- Store Table
--CREATE TABLE tblStore (
--    StoreID INT PRIMARY KEY IDENTITY(1,1),
--    UserID INT FOREIGN KEY REFERENCES [User](UserID),
--    StoreName NVARCHAR(100) NOT NULL,
--    Description TEXT,
--    CreatedDate DATETIME DEFAULT GETDATE(),
--    LastEditDate DATETIME DEFAULT GETDATE()
--);

---- Store Product Table
--CREATE TABLE tblStoreProduct (
--    StoreProductID INT PRIMARY KEY IDENTITY(1,1),
--    StoreID INT FOREIGN KEY REFERENCES Store(StoreID),
--    ProductID INT FOREIGN KEY REFERENCES Product(ProductID),
--    Price DECIMAL(10, 2),
--    QuantityAvailable INT,
--    CreatedDate DATETIME DEFAULT GETDATE(),
--    LastEditDate DATETIME DEFAULT GETDATE()
--);

---- Store Review Table
--CREATE TABLE tblStoreReview (
--    ReviewID INT PRIMARY KEY,
--    StoreID INT FOREIGN KEY REFERENCES Store(StoreID),
--    CustomerID INT FOREIGN KEY REFERENCES Customer(CustID),
--    Rating INT,
--    ReviewText TEXT,
--    CreatedDate DATETIME DEFAULT GETDATE()
--);

---- Store Order Table
--CREATE TABLE tblStoreOrder (
--    StoreOrderID INT PRIMARY KEY IDENTITY(1,1),
--    StoreID INT FOREIGN KEY REFERENCES Store(StoreID),
--    CustomerID INT FOREIGN KEY REFERENCES Customer(CustID),
--    OrderDate DATETIME,
--    DeliveryAddress NVARCHAR(255),
--    TotalCost DECIMAL(10, 2),
--    OrderStatusID INT FOREIGN KEY REFERENCES OrderStatus(OrderStatusID),
--    CreatedDate DATETIME DEFAULT GETDATE(),
--    LastUpdateDate DATETIME DEFAULT GETDATE()
--);

