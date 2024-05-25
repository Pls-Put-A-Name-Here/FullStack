CREATE TABLE [dbo].[tblOrderStatuses] (
  [ordStatusIdpk] [int] NOT NULL,
  [ordStatusName] [nvarchar](50) NULL,
  [ordStatusDescription] [text] NULL,
  [ordStatusCreatedDate] [datetime] NULL DEFAULT (getdate()),
  [ordStatusLastEditDate] [datetime] NULL DEFAULT (getdate()),
  PRIMARY KEY CLUSTERED ([ordStatusIdpk])
)
ON [PRIMARY]
TEXTIMAGE_ON [PRIMARY]
GO