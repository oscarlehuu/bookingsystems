public interface IRegisterService {
  Task<UserRegisterResponse> RegisterUserAsync (UserRegisterRequest request);
}