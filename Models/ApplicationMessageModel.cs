using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.Metadata.Builders;

namespace Booking_Systems.Models
{
    public class ApplicationMessageModel
    {
        public int Id { get; set; }
        public required string MessageTag { get; set; }
        public required string MessageValue { get; set; }
        public required string LanguageCode { get; set; }
    }

    public class ApplicationMessageModelConfiguration : IEntityTypeConfiguration<ApplicationMessageModel>
    {
        public void Configure(EntityTypeBuilder<ApplicationMessageModel> builder)
        {
            builder.ToTable("tblApplicationMessages");

            builder.HasKey(e => e.Id);
            builder.Property(e => e.MessageTag).IsRequired();
            builder.Property(e => e.MessageValue).IsRequired();
            builder.Property(e => e.LanguageCode).IsRequired();
        }
    }
}