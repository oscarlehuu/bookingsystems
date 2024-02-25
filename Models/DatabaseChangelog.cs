using System.Net;
using Booking_Systems.Models;
using Microsoft.EntityFrameworkCore;
using Model;

namespace Booking_Systems;

public class DatabaseChangelog : DbContext
{
  public DatabaseChangelog(DbContextOptions<DatabaseChangelog> options) : base(options) {}

  public DbSet<Organization> Organization { get; set; }
  public DbSet<Role> Role {get; set; }
  public DbSet<User> User { get; set; }
  public DbSet<ApplicationMessageModel> ApplicationMessageModel { get; set; }

    protected override void OnModelCreating(ModelBuilder modelBuilder)
    {
        modelBuilder.ApplyConfiguration(new OrganizationConfiguration());
        modelBuilder.ApplyConfiguration(new RoleConfiguration());
        modelBuilder.ApplyConfiguration(new UserConfiguration());
        modelBuilder.ApplyConfiguration(new ApplicationMessageModelConfiguration());
    }
}
