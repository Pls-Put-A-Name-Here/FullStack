CREATE TABLE [dbo].[tblInventory] (
  [invIdpk] [int] IDENTITY,
  [invPrdIdfk] [int] NULL,
  [invQuantityAvailable] [int] NULL,
  [invUnitPrice] [decimal](10, 2) NULL,
  [invUnitCost] [decimal](10, 2) NULL,
  [invSupIdfk] [int] NULL,
  [invDateAdded] [datetime] NULL,
  [invExpirationDate] [datetime] NULL,
  [invLastUpdateDate] [datetime] NULL DEFAULT (getdate()),
  PRIMARY KEY CLUSTERED ([invIdpk])
)
ON [PRIMARY]
GO

ALTER TABLE [dbo].[tblInventory]
  ADD FOREIGN KEY ([invPrdIdfk]) REFERENCES [dbo].[tblProducts] ([prdIdpk])
GO

ALTER TABLE [dbo].[tblInventory]
  ADD FOREIGN KEY ([invSupIdfk]) REFERENCES [dbo].[tblSuppliers] ([supIdpk])
GO