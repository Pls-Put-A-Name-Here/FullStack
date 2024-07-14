CREATE TABLE [dbo].[tblUsers] (
  [usrIdpk] [int] IDENTITY,
  [usrName] [nvarchar](50) NULL,
  [usrPassword] [nvarchar](50) NULL,
  [usrEmail] [nvarchar](50) NULL,
  [usrDoB] [date] NULL,
  [usrPhoneNumber] [nvarchar](50) NULL,
  PRIMARY KEY CLUSTERED ([usrIdpk])
)
ON [PRIMARY]
GO