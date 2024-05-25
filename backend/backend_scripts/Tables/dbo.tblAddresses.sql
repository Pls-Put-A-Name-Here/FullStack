CREATE TABLE [dbo].[tblAddresses] (
  [adrIdpk] [int] IDENTITY,
  [adrLocation] [nvarchar](255) NULL,
  [adrDigitalAddress] [nvarchar](255) NULL,
  [adrHouseAddress] [nvarchar](255) NULL,
  PRIMARY KEY CLUSTERED ([adrIdpk])
)
ON [PRIMARY]
GO