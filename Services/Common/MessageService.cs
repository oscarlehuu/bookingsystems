using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.EntityFrameworkCore;
using Model;

namespace Booking_Systems.Services.Common
{
    public class MessageService
    {
        private readonly DatabaseChangelog _dbContext;
        public MessageService (DatabaseChangelog dbContext) 
        {
            _dbContext = dbContext;
        }

        public string GetMessage (string messageTag, string languageCode = "en-AU") {
            var message =  _dbContext.ApplicationMessageModel
                             .Where(m => m.MessageTag == messageTag && m.LanguageCode == languageCode)
                             .Select(m => m.MessageValue)
                             .FirstOrDefault();
            return message ?? "Please try again later.";
        }
    }
}