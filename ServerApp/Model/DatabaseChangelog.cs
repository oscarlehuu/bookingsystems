using Microsoft.EntityFrameworkCore;
using Model;

namespace Booking_Systems;

public class DatabaseChangelog : DbContext
{
  public DatabaseChangelog(DbContextOptions<DatabaseChangelog> options) : base(options) {

  }
  public DbSet<Organization> Organizations { get; set; }

    protected override void OnModelCreating(ModelBuilder modelBuilder)
    {
        modelBuilder.ApplyConfiguration(new OrganizationConfiguration());
    }
}
