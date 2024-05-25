CREATE TABLE [dbo].[tblAccounts] (
  [accIdpk] [int] IDENTITY,
  [accUsrIdfk] [int] NULL,
  [accUsername] [varchar](50) NOT NULL,
  [accPasswordHash] [varchar](100) NOT NULL,
  [accEmail] [varchar](100) NOT NULL,
  [accCreatedAt] [datetime] NULL DEFAULT (getdate()),
  [accLastUpdateDate] [datetime] NULL DEFAULT (getdate()),
  [accLastLogin] [datetime] NULL,
  [accIsActive] [bit] NULL DEFAULT (1),
  PRIMARY KEY CLUSTERED ([accIdpk])
)
ON [PRIMARY]
GO

ALTER TABLE [dbo].[tblAccounts]
  ADD FOREIGN KEY ([accUsrIdfk]) REFERENCES [dbo].[tblUsers] ([usrIdpk])
GO