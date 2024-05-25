CREATE TABLE [dbo].[tblUserRoles] (
  [urlIdpk] [int] IDENTITY,
  [urlAccIdfk] [int] NULL,
  [urlRolIdfk] [int] NULL,
  PRIMARY KEY CLUSTERED ([urlIdpk])
)
ON [PRIMARY]
GO

ALTER TABLE [dbo].[tblUserRoles]
  ADD FOREIGN KEY ([urlAccIdfk]) REFERENCES [dbo].[tblAccounts] ([accIdpk])
GO

ALTER TABLE [dbo].[tblUserRoles]
  ADD FOREIGN KEY ([urlRolIdfk]) REFERENCES [dbo].[tblRoles] ([rolIdpk])
GO