using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.Metadata.Builders;

namespace Model 
{
  public class Organization 
  {
    public long Id { get; set; }
    public required string OrganizationName { get; set; }
    public required string CorporateEmail { get; set; }
    public string? PhoneNumber { get; set; }
    public string? Website { get; set;}
    public DateTime CreatedDate { get; set; }
    public DateTime? UpdatedDate { get; set; }
    public bool IsActive { get; set; }
  }

  public class OrganizationConfiguration : IEntityTypeConfiguration<Organization> 
  {
    public void Configure(EntityTypeBuilder<Organization> builder) 
    {
      builder.ToTable("tblOrganization");
      
      builder.HasKey(e => e.Id);
      builder.Property(e => e.OrganizationName).IsRequired().HasMaxLength(50);
      builder.Property(e => e.CorporateEmail).IsRequired().HasMaxLength(50);
      builder.Property(e => e.PhoneNumber).HasMaxLength(12);
      builder.Property(e => e.Website).HasMaxLength(20);
      builder.Property(e => e.CreatedDate).IsRequired().HasDefaultValueSql("GETUTCDATE()");
      builder.Property(e => e.UpdatedDate).HasDefaultValueSql("GETUTCDATE()");
      builder.Property(e => e.IsActive).IsRequired();
    }
  }
}