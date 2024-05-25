CREATE TABLE [dbo].[tblReviews] (
  [revIdpk] [int] IDENTITY,
  [revPrdIdfk] [int] NULL,
  [revCustIdfk] [int] NULL,
  [revRating] [int] NULL,
  [revComments] [text] NULL,
  PRIMARY KEY CLUSTERED ([revIdpk])
)
ON [PRIMARY]
TEXTIMAGE_ON [PRIMARY]
GO

ALTER TABLE [dbo].[tblReviews]
  ADD FOREIGN KEY ([revCustIdfk]) REFERENCES [dbo].[tblCustomers] ([custIdpk])
GO

ALTER TABLE [dbo].[tblReviews]
  ADD FOREIGN KEY ([revPrdIdfk]) REFERENCES [dbo].[tblProducts] ([prdIdpk])
GO