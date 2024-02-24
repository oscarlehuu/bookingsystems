using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.Metadata.Builders;

public class Role {
  public int Id { get; set; }
  public required string Name { get;  set; }
  public string? Description { get; set; }
  public DateTime CreatedDate { get; set; }
  public DateTime UpdatedDate { get; set; }
  
}

public class RoleConfiguration : IEntityTypeConfiguration<Role> {
  public void Configure(EntityTypeBuilder<Role> builder) { 
    builder.ToTable("tblRoles");

    builder.HasKey(x => x.Id);
    builder.Property(x => x.Name).IsRequired().HasMaxLength(50);
    builder.Property(x => x.Description).IsRequired();
    builder.Property(x => x.CreatedDate).IsRequired().HasDefaultValueSql("GETUTCDATE()");
    builder.Property(x => x.UpdatedDate).HasDefaultValueSql("GETUTCDATE()");
  }
}