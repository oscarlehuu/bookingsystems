using Microsoft.EntityFrameworkCore.Migrations;

#nullable disable

namespace Booking_Systems.Migrations
{
    /// <inheritdoc />
    public partial class CreatetblApplicationMessage : Migration
    {
        /// <inheritdoc />
        protected override void Up(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.CreateTable(
                name: "tblApplicationMessages",
                columns: table => new
                {
                    Id = table.Column<int>(type: "int", nullable: false)
                        .Annotation("SqlServer:Identity", "1, 1"),
                    MessageTag = table.Column<string>(type: "nvarchar(max)", nullable: false),
                    MessageValue = table.Column<string>(type: "nvarchar(max)", nullable: false),
                    LanguageCode = table.Column<string>(type: "nvarchar(max)", nullable: false)
                },
                constraints: table =>
                {
                    table.PrimaryKey("PK_tblApplicationMessages", x => x.Id);
                });

            migrationBuilder.Sql(@"INSERT INTO tblApplicationMessages (MessageTag, MessageValue, LanguageCode) 
                                VALUES ('UsernameEmpty', 'Your username can not be empty.', 'en-AU')");
            migrationBuilder.Sql(@"INSERT INTO tblApplicationMessages (MessageTag, MessageValue, LanguageCode) 
                                VALUES ('UsernameExisted', 'Your username is not available.', 'en-AU')");
            migrationBuilder.Sql(@"INSERT INTO tblApplicationMessages (MessageTag, MessageValue, LanguageCode) 
                                VALUES ('UsernameMoreThanMaxLength', 'Your username can only have 50 characters maximum.', 'en-AU')");
            
            migrationBuilder.Sql(@"INSERT INTO tblApplicationMessages (MessageTag, MessageValue, LanguageCode) 
                                VALUES ('EmailEmpty', 'Your email can not be empty.', 'en-AU')");
            migrationBuilder.Sql(@"INSERT INTO tblApplicationMessages (MessageTag, MessageValue, LanguageCode) 
                                VALUES ('EmailInvalid', 'Your email is invalid.', 'en-AU')");
            migrationBuilder.Sql(@"INSERT INTO tblApplicationMessages (MessageTag, MessageValue, LanguageCode) 
                                VALUES ('EmailExisted', 'Your email is not available.', 'en-AU')");

            migrationBuilder.Sql(@"INSERT INTO tblApplicationMessages (MessageTag, MessageValue, LanguageCode) 
                                VALUES ('PasswordEmpty', 'Your password needs to have at least 8 charecters, 1 capital character, 1 number and 1 special character.', 'en-AU')");
            migrationBuilder.Sql(@"INSERT INTO tblApplicationMessages (MessageTag, MessageValue, LanguageCode) 
                                VALUES ('PasswordLessThanMinLength', 'Your password needs to have at least 8 characters.', 'en-AU')");
            migrationBuilder.Sql(@"INSERT INTO tblApplicationMessages (MessageTag, MessageValue, LanguageCode) 
                                VALUES ('PasswordMoreThanMaxLength', 'Your password can only have 100 characters maximum.', 'en-AU')");
            migrationBuilder.Sql(@"INSERT INTO tblApplicationMessages (MessageTag, MessageValue, LanguageCode) 
                                VALUES ('PasswordMissOneUpperCharacter', 'Your password needs to have at least 1 capital character.', 'en-AU')");
            migrationBuilder.Sql(@"INSERT INTO tblApplicationMessages (MessageTag, MessageValue, LanguageCode) 
                                VALUES ('PasswordMissOneNumber', 'Your password needs to have at least 1 number.', 'en-AU')");
            migrationBuilder.Sql(@"INSERT INTO tblApplicationMessages (MessageTag, MessageValue, LanguageCode) 
                                VALUES ('PasswordMissOneSpecialCharecter', 'Your password needs to have at least 1 special character.', 'en-AU')");
            migrationBuilder.Sql(@"INSERT INTO tblApplicationMessages (MessageTag, MessageValue, LanguageCode) 
                                VALUES ('ConfirmPasswordNotMatched', 'Passwords are not matched.', 'en-AU')");
            
            migrationBuilder.Sql(@"INSERT INTO tblApplicationMessages (MessageTag, MessageValue, LanguageCode) 
                                VALUES ('UserCreateFailed', 'User could not be created.', 'en-AU')");
            migrationBuilder.Sql(@"INSERT INTO tblApplicationMessages (MessageTag, MessageValue, LanguageCode) 
                                VALUES ('UserCreatedSuccessfully', 'User is created successfully.', 'en-AU')");
        }

        /// <inheritdoc />
        protected override void Down(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DropTable(
                name: "tblApplicationMessages");
        }
    }
}
