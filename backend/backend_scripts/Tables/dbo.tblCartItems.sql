CREATE TABLE [dbo].[tblCartItems] (
  [crtItemIdpk] [int] IDENTITY,
  [crtItemCrtIdfk] [int] NULL,
  [crtItemPrdIdfk] [int] NULL,
  [crtItemQuantity] [int] NULL,
  [crtItemUnitPrice] [decimal](10, 2) NULL,
  PRIMARY KEY CLUSTERED ([crtItemIdpk])
)
ON [PRIMARY]
GO

ALTER TABLE [dbo].[tblCartItems]
  ADD FOREIGN KEY ([crtItemCrtIdfk]) REFERENCES [dbo].[tblCarts] ([crtIdpk])
GO

ALTER TABLE [dbo].[tblCartItems]
  ADD FOREIGN KEY ([crtItemPrdIdfk]) REFERENCES [dbo].[tblProducts] ([prdIdpk])
GO