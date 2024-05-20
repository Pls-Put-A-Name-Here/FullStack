CREATE TABLE [dbo].[tblOrderItems] (
  [ordtIdpk] [int] IDENTITY,
  [ordtOrdIdfk] [int] NULL,
  [ordtPrdIdfk] [int] NULL,
  [ordtQuantity] [int] NULL,
  [ordtUnitPrice] [decimal](10, 2) NULL,
  [ordtSubtotal] [decimal](10, 2) NULL,
  [ordtCreatedDate] [datetime] NULL DEFAULT (getdate()),
  [ordtLastUpdateDate] [datetime] NULL DEFAULT (getdate()),
  PRIMARY KEY CLUSTERED ([ordtIdpk])
)
ON [PRIMARY]
GO

ALTER TABLE [dbo].[tblOrderItems]
  ADD FOREIGN KEY ([ordtOrdIdfk]) REFERENCES [dbo].[tblOrders] ([ordIdpk])
GO

ALTER TABLE [dbo].[tblOrderItems]
  ADD FOREIGN KEY ([ordtPrdIdfk]) REFERENCES [dbo].[tblProducts] ([prdIdpk])
GO