from fastapi_template.domain.users import user_queries, user_services


def get_user_services() -> user_services.Service:
    return user_services.Service(user_queries.Queries())
