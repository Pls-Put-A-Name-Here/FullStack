CREATE TABLE [dbo].[tblProductDetails] (
  [prdDetailsIdpk] [int] IDENTITY,
  [prdDetailsPrdIdfk] [int] NULL,
  [prdWeight] [nvarchar](100) NULL,
  [prdHeight] [nvarchar](255) NULL,
  [prdDimensions] [nvarchar](100) NULL,
  [prdTechnicalSpecification] [nvarchar](255) NULL,
  [prdDetailsCreatedDate] [datetime] NULL DEFAULT (getdate()),
  [prdDetailsLastEditDate] [datetime] NULL DEFAULT (getdate()),
  PRIMARY KEY CLUSTERED ([prdDetailsIdpk])
)
ON [PRIMARY]
GO

ALTER TABLE [dbo].[tblProductDetails]
  ADD FOREIGN KEY ([prdDetailsPrdIdfk]) REFERENCES [dbo].[tblProducts] ([prdIdpk])
GO