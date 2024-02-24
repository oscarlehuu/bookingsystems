using Microsoft.EntityFrameworkCore.Migrations;

#nullable disable

namespace Booking_Systems.Migrations
{
    /// <inheritdoc />
    public partial class CreateFirstOrganization : Migration
    {
        /// <inheritdoc />
        protected override void Up(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.Sql(@"INSERT INTO tblOrganization (OrganizationName, CorporateEmail, PhoneNumber, Website, CreatedDate, IsActive) 
                                    VALUES ('Koyo Pty Ltd', 'oscar.lehuu@gmail.com', '0414603198', 'koyoadl.au', GETUTCDATE(), '1')");
        }

        /// <inheritdoc />
        protected override void Down(MigrationBuilder migrationBuilder)
        {

        }
    }
}
