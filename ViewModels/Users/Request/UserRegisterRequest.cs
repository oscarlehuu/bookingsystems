using System.ComponentModel.DataAnnotations;

public class UserRegisterRequest {
  [Required]
  public required string Username { get; set;}
  [Required]
  [EmailAddress]
  public required string Email { get; set; }
  [Required]
  [DataType(DataType.Password)]
  [MinLength(8)]
  [RegularExpression(@"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$")]
  public required string Password { get; set; }
  [Required]
  [DataType(DataType.Password)]
  [Compare("Password")]
  public required string ConfirmPassword { get; set; }

}