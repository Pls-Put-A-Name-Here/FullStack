CREATE TABLE [dbo].[tblCustomers] (
  [custIdpk] [int] IDENTITY,
  [custUsrIdfk] [int] NULL,
  [custAdrIdfk] [int] NULL,
  PRIMARY KEY CLUSTERED ([custIdpk])
)
ON [PRIMARY]
GO

ALTER TABLE [dbo].[tblCustomers]
  ADD FOREIGN KEY ([custAdrIdfk]) REFERENCES [dbo].[tblAddresses] ([adrIdpk])
GO

ALTER TABLE [dbo].[tblCustomers]
  ADD FOREIGN KEY ([custUsrIdfk]) REFERENCES [dbo].[tblUsers] ([usrIdpk])
GO