using System;
using Microsoft.EntityFrameworkCore.Migrations;

#nullable disable

namespace Booking_Systems.Migrations
{
    /// <inheritdoc />
    public partial class CreateTableRole : Migration
    {
        /// <inheritdoc />
        protected override void Up(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.AddColumn<DateTime>(
                name: "CreatedDate",
                table: "tblOrganization",
                type: "datetime2",
                nullable: false,
                defaultValueSql: "GETUTCDATE()");

            migrationBuilder.AddColumn<bool>(
                name: "IsActive",
                table: "tblOrganization",
                type: "bit",
                nullable: false,
                defaultValue: false);

            migrationBuilder.AddColumn<DateTime>(
                name: "UpdatedDate",
                table: "tblOrganization",
                type: "datetime2",
                nullable: true,
                defaultValueSql: "GETUTCDATE()");
        }

        /// <inheritdoc />
        protected override void Down(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DropColumn(
                name: "CreatedDate",
                table: "tblOrganization");

            migrationBuilder.DropColumn(
                name: "IsActive",
                table: "tblOrganization");

            migrationBuilder.DropColumn(
                name: "UpdatedDate",
                table: "tblOrganization");
        }
    }
}
