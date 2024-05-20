CREATE TABLE [dbo].[tblSuppliers] (
  [supIdpk] [int] IDENTITY,
  [supName] [nvarchar](100) NOT NULL,
  [supContactInfo] [nvarchar](255) NULL,
  [supAddressLine1] [nvarchar](255) NULL,
  [supAddressLine2] [nvarchar](255) NULL,
  [supCity] [nvarchar](100) NULL,
  [supState] [nvarchar](100) NULL,
  [supPostalCode] [nvarchar](20) NULL,
  [supCountry] [nvarchar](100) NULL,
  PRIMARY KEY CLUSTERED ([supIdpk])
)
ON [PRIMARY]
GO