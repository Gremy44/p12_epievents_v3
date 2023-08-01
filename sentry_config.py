import sentry_sdk
from sentry_sdk.integrations.sqlalchemy import SqlalchemyIntegration
import sys
import os
from dotenv import load_dotenv


def call_centry():
    load_dotenv()

    sentry_sdk.init(
        dsn=os.getenv("SENTRY_DSN"),
        integrations=[
            SqlalchemyIntegration(),
        ],
    )
