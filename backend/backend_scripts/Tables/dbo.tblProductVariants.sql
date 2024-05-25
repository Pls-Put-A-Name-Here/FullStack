CREATE TABLE [dbo].[tblProductVariants] (
  [prvIdpk] [int] IDENTITY,
  [prvPrdIdfk] [int] NULL,
  [prvColor] [nvarchar](50) NULL,
  [prvSize] [nvarchar](50) NULL,
  [prvMaterial] [nvarchar](50) NULL,
  [prvPriceModifier] [decimal](10, 2) NULL,
  [prvQuantityAvailable] [int] NULL,
  [prvSKU] [nvarchar](100) NULL,
  PRIMARY KEY CLUSTERED ([prvIdpk])
)
ON [PRIMARY]
GO

ALTER TABLE [dbo].[tblProductVariants]
  ADD FOREIGN KEY ([prvPrdIdfk]) REFERENCES [dbo].[tblProducts] ([prdIdpk])
GO