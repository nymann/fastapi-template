from fastapi_template.domain.users import user_services, user_queries


def get_user_services() -> user_services.Service:
    return user_services.Service(user_queries.Queries())
