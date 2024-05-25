CREATE TABLE [dbo].[tblProducts] (
  [prdIdpk] [int] IDENTITY,
  [prdBrdIdfk] [int] NULL,
  [prdCtgIdfk] [int] NULL,
  [prdSctgIdfk] [int] NULL,
  [prdName] [nvarchar](255) NOT NULL,
  [prdDescription] [text] NULL,
  [prdUnitPrice] [decimal](10, 2) NULL,
  [prdStockQuantity] [int] NULL,
  [prdCreatedDate] [datetime] NULL DEFAULT (getdate()),
  [prdLastEditDate] [datetime] NULL DEFAULT (getdate()),
  PRIMARY KEY CLUSTERED ([prdIdpk])
)
ON [PRIMARY]
TEXTIMAGE_ON [PRIMARY]
GO

ALTER TABLE [dbo].[tblProducts]
  ADD FOREIGN KEY ([prdBrdIdfk]) REFERENCES [dbo].[tblBrands] ([brdIdpk])
GO

ALTER TABLE [dbo].[tblProducts]
  ADD FOREIGN KEY ([prdCtgIdfk]) REFERENCES [dbo].[tblProductCategories] ([ctgIdpk])
GO

ALTER TABLE [dbo].[tblProducts]
  ADD FOREIGN KEY ([prdSctgIdfk]) REFERENCES [dbo].[tblProductSubCategories] ([sctgIdpk])
GO