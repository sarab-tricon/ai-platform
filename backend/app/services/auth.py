import logging
from app.schemas.auth import TokenResponse

logger = logging.getLogger(__name__)


class AuthService:

    def login(self, email: str, password: str) -> TokenResponse:
        logger.info(f"Login attempt for user: {email}")

        # TODO: replace with DB validation
        if email != "test@example.com" or password != "password":
            logger.warning("Invalid login credentials")
            raise ValueError("Invalid credentials")

        # TODO: replace with JWT generation
        token = "dummy_jwt_token"

        logger.info("Login successful")

        return TokenResponse(
            access_token=token,
            token_type="bearer"
        )


auth_service = AuthService()