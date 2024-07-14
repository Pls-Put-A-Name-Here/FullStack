CREATE TABLE [dbo].[tblPurchase] (
  [pchIdpk] [int] IDENTITY,
  [pchCustIdfk] [int] NULL,
  [pchPurchaseDate] [datetime] NULL,
  [pchTotalAmount] [decimal](10, 2) NULL,
  [pchPmtIdfk] [int] NULL,
  [pchPstIdfk] [int] NULL,
  [pchCreatedDate] [datetime] NULL DEFAULT (getdate()),
  [pchLastUpdateDate] [datetime] NULL DEFAULT (getdate()),
  PRIMARY KEY CLUSTERED ([pchIdpk])
)
ON [PRIMARY]
GO

ALTER TABLE [dbo].[tblPurchase]
  ADD FOREIGN KEY ([pchCustIdfk]) REFERENCES [dbo].[tblCustomers] ([custIdpk])
GO

ALTER TABLE [dbo].[tblPurchase]
  ADD FOREIGN KEY ([pchPmtIdfk]) REFERENCES [dbo].[tblPaymentMethods] ([pmtIdpk])
GO

ALTER TABLE [dbo].[tblPurchase]
  ADD FOREIGN KEY ([pchPstIdfk]) REFERENCES [dbo].[tblPaymentStatuses] ([pstIdpk])
GO