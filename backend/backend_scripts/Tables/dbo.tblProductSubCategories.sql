CREATE TABLE [dbo].[tblProductSubCategories] (
  [sctgIdpk] [int] IDENTITY,
  [sctgName] [nvarchar](100) NOT NULL,
  [sctgCreatedDate] [datetime] NULL DEFAULT (getdate()),
  [sctgLastEditDate] [datetime] NULL DEFAULT (getdate()),
  PRIMARY KEY CLUSTERED ([sctgIdpk])
)
ON [PRIMARY]
GO