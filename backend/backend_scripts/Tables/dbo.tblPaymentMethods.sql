CREATE TABLE [dbo].[tblPaymentMethods] (
  [pmtIdpk] [int] IDENTITY,
  [pmtName] [nvarchar](100) NULL,
  [pmtDescription] [nvarchar](255) NULL,
  [pmtCreatedDate] [datetime] NULL DEFAULT (getdate()),
  [pmtLastUpdateDate] [datetime] NULL DEFAULT (getdate()),
  PRIMARY KEY CLUSTERED ([pmtIdpk])
)
ON [PRIMARY]
GO