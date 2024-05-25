CREATE TABLE [dbo].[tblRoles] (
  [rolIdpk] [int] IDENTITY,
  [rolName] [varchar](50) NOT NULL,
  [rolDescription] [varchar](255) NULL,
  PRIMARY KEY CLUSTERED ([rolIdpk])
)
ON [PRIMARY]
GO