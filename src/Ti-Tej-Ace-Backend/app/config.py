config_json = {
    "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",
    "CELERY_BROKER_URL": "redis://localhost:6379/1",
    "CELERY_RESULT_BACKEND": "redis://localhost:6379/1"
}