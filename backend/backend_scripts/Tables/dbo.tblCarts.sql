CREATE TABLE [dbo].[tblCarts] (
  [crtIdpk] [int] IDENTITY,
  [crtCustomerIdfk] [int] NULL,
  [crtCreatedAt] [datetime] NULL DEFAULT (getdate()),
  [crtStatus] [nvarchar](50) NULL DEFAULT ('Active'),
  PRIMARY KEY CLUSTERED ([crtIdpk])
)
ON [PRIMARY]
GO

ALTER TABLE [dbo].[tblCarts]
  ADD FOREIGN KEY ([crtCustomerIdfk]) REFERENCES [dbo].[tblCustomers] ([custIdpk])
GO