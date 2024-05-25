CREATE TABLE [dbo].[tblPaymentStatuses] (
  [pstIdpk] [int] NOT NULL,
  [pstStatusName] [nvarchar](50) NULL,
  [pstDescription] [text] NULL,
  [pstCreatedDate] [datetime] NULL DEFAULT (getdate()),
  [pstLastUpdateDate] [datetime] NULL DEFAULT (getdate()),
  PRIMARY KEY CLUSTERED ([pstIdpk])
)
ON [PRIMARY]
TEXTIMAGE_ON [PRIMARY]
GO