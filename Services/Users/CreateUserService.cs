using Booking_Systems;
using Booking_Systems.Services.Common;
using Microsoft.AspNetCore.Identity;
using Microsoft.EntityFrameworkCore;
using Model;


namespace Services {
  public class CreateUserService : IRegisterService
  {
    private readonly UserManager<User> _userManager;
    private readonly DatabaseChangelog _dbContext;
    private MessageService _messageSerivce;
    public CreateUserService (UserManager<User> userManager, DatabaseChangelog dbContext, MessageService messageService ) {
      _userManager = userManager;
      _dbContext = dbContext;
      _messageSerivce = messageService
    }
    public Task<UserRegisterResponse> RegisterUserAsync(UserRegisterRequest request)
    {
      if(request.Password.Length < 8) {
        return Task.FromResult(new UserRegisterResponse {
          IsSuccess = false,
          Message = new[] { _messageSerivce.GetMessage("PasswordLessThanMinLength") }
        });
      }
    }
  }
}
