CREATE TABLE [dbo].[tblOrders] (
  [ordIdpk] [int] IDENTITY,
  [ordCustIdpk] [int] NULL,
  [ordDate] [datetime] NULL,
  [ordDeliveryAddress] [nvarchar](255) NULL,
  [ordTotalCost] [decimal](10, 2) NULL,
  [ordStatusIdfk] [int] NULL,
  [ordStatusCreatedDate] [datetime] NULL DEFAULT (getdate()),
  [LastUpdateDate] [datetime] NULL DEFAULT (getdate()),
  PRIMARY KEY CLUSTERED ([ordIdpk])
)
ON [PRIMARY]
GO

ALTER TABLE [dbo].[tblOrders]
  ADD FOREIGN KEY ([ordCustIdpk]) REFERENCES [dbo].[tblCustomers] ([custIdpk])
GO

ALTER TABLE [dbo].[tblOrders]
  ADD FOREIGN KEY ([ordStatusIdfk]) REFERENCES [dbo].[tblOrderStatuses] ([ordStatusIdpk])
GO