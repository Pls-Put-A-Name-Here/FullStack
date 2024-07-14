CREATE TABLE [dbo].[tblProductCategories] (
  [ctgIdpk] [int] IDENTITY,
  [ctgName] [nvarchar](100) NOT NULL,
  [ctgCreatedDate] [datetime] NULL DEFAULT (getdate()),
  [ctgLastEditDate] [datetime] NULL DEFAULT (getdate()),
  PRIMARY KEY CLUSTERED ([ctgIdpk])
)
ON [PRIMARY]
GO