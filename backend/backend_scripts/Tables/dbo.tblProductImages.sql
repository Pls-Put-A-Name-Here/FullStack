CREATE TABLE [dbo].[tblProductImages] (
  [imgIdpk] [int] IDENTITY,
  [imgPrdIdfk] [int] NULL,
  [imgURL] [nvarchar](255) NULL,
  [imgDescription] [text] NULL,
  [imgUploadDate] [datetime] NULL DEFAULT (getdate()),
  [imgLastEditDate] [datetime] NULL DEFAULT (getdate()),
  PRIMARY KEY CLUSTERED ([imgIdpk])
)
ON [PRIMARY]
TEXTIMAGE_ON [PRIMARY]
GO

ALTER TABLE [dbo].[tblProductImages]
  ADD FOREIGN KEY ([imgPrdIdfk]) REFERENCES [dbo].[tblProducts] ([prdIdpk])
GO