CREATE TABLE [dbo].[tblRatings] (
  [ratIdpk] [int] IDENTITY,
  [ratPrdIdfk] [int] NULL,
  [ratCustIdfk] [int] NULL,
  [ratRating] [int] NULL,
  [ratComments] [text] NULL,
  [ratTimestamp] [datetime] NULL DEFAULT (getdate()),
  PRIMARY KEY CLUSTERED ([ratIdpk])
)
ON [PRIMARY]
TEXTIMAGE_ON [PRIMARY]
GO

ALTER TABLE [dbo].[tblRatings]
  ADD FOREIGN KEY ([ratCustIdfk]) REFERENCES [dbo].[tblCustomers] ([custIdpk])
GO

ALTER TABLE [dbo].[tblRatings]
  ADD FOREIGN KEY ([ratPrdIdfk]) REFERENCES [dbo].[tblProducts] ([prdIdpk])
GO