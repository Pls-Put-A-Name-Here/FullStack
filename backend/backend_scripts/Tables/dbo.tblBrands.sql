CREATE TABLE [dbo].[tblBrands] (
  [brdIdpk] [int] IDENTITY,
  [brdName] [nvarchar](100) NOT NULL,
  [brdCountryOfOrigin] [nvarchar](100) NULL,
  [brdYearEstablished] [int] NULL,
  [brdDescription] [text] NULL,
  [brdCreatedDate] [datetime] NULL DEFAULT (getdate()),
  [brdLastEditDate] [datetime] NULL DEFAULT (getdate()),
  PRIMARY KEY CLUSTERED ([brdIdpk])
)
ON [PRIMARY]
TEXTIMAGE_ON [PRIMARY]
GO