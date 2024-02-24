using System.Runtime.InteropServices;
using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.Metadata.Builders;
using Model;

public class User {
  public int Id { get; set; }
  public required string Username { get; set; }
  public required string Password { get; set;}
  public required string Email { get; set; }
  public string? PhoneNumber { get; set; }
  public long OrganizationId { get; set; }
  public Organization Organization { get; set; }
  public int RoleId { get; set; }
  public Role Role { get; set; }
  public DateTime CreatedDate { get; set; }
  public DateTime UpdatedDate { get; set; }
  public bool IsActive { get; set; }
  public bool IsAdmin { get; set; }
}

public class UserConfiguration : IEntityTypeConfiguration<User> {
  public void Configure(EntityTypeBuilder<User> builder) { 
    builder.ToTable("tblUsers");

    builder.HasKey(x => x.Id);
    builder.Property(x => x.Username).IsRequired().HasMaxLength(50);
    builder.Property(x => x.Password).IsRequired().HasMaxLength(100);
    builder.Property(x => x.Email).IsRequired().HasMaxLength(50);
    builder.Property(x => x.PhoneNumber).HasMaxLength(12);
    builder.HasOne(u => u.Organization)
           .WithMany()
           .HasForeignKey(u => u.OrganizationId);
    builder.HasOne(u => u.Role)
           .WithMany()
           .IsRequired()
           .HasForeignKey(u => u.RoleId);
    builder.Property(x => x.CreatedDate).IsRequired().HasDefaultValueSql("GETUTCDATE()");
    builder.Property(x => x.UpdatedDate).HasDefaultValueSql("GETUTCDATE()");
    builder.Property(x => x.IsActive).IsRequired();
    builder.Property(x => x.IsAdmin).IsRequired();
  }
}