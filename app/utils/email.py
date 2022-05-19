import json

# from app.external_apis import account_api, transactions_api
import os
import shutil
import time

import pandas as pd
from flask import render_template, url_for
from itsdangerous import URLSafeTimedSerializer

from app import app, redisConn
from app.core.celery_app import celery_app
from app.core.logger import log

ts = URLSafeTimedSerializer(
    "7vjr7UZb6WEhJY9Hme5mJSBXmhLKmXSb3KY79Ju2FLEmWjMB9utnnRPhCz9HjdJH"
)
CELERY_BACKOFF_TIME = 300


def send_email(to, subject, message):
    celery_app.send_task(
        "email.send_email",
        kwargs={"to": [to], "subject": subject, "message": message},
        queue="email",
    )


def user_password_reset(id, email, name):
    # Now we'll send the email confirmation link
    subject = "Reset password request"

    token = ts.dumps(id, salt="password-reset-key")

    reset_url = url_for("base.reset_password_token", token=token, _external=True)

    html = render_template("email/reset.djhtml", reset_url=reset_url, name=name)

    with app.app_context():
        token = redisConn.set(token, json.dumps({"email": email, "id": str(id)}))

    send_email([email], subject, html)


def user_activate(id, email, name, password):
    # Now we'll send the email confirmation link
    subject = "Please confirm your email"

    token = ts.dumps(id, salt="email-confirm-key")

    confirm_url = url_for("base.confirm_email", token=token, _external=True)

    html = render_template(
        "email/activate.djhtml",
        confirm_url=confirm_url,
        name=name,
        email=email,
        password=password,
    )

    send_email([email], subject, html)


def email_report(BASE_URL, title, data, email, columns=None):
    recipient_email = os.environ.get("OVERRIDE_EMAIL", email)
    df = pd.DataFrame.from_dict(data)
    if columns:
        df = df[columns]
    timestamp = int(time.time())

    filename = f"{title}-{timestamp}"

    try:
        df["Date"] = df["Date"].dt.tz_localize(None)
    except Exception:
        log.debug("Not a datetime value. Ignored")

    try:
        df["Last Used"] = df["Last Used"].dt.tz_localize(None)
    except Exception:
        log.debug("Not a time value. Ignored")

    try:
        df = pd.to_timedelta(df["Last Used"].str.strip())
    except Exception as e:
        log.debug("Not a time value. Ignored: ")
        log.debug(e)

    df.to_excel(f"/project/reports/{filename}.xlsx", index=False)

    zipf = shutil.make_archive(
        f"/project/reports/{filename}",
        "zip",
        root_dir="/project/reports",
        base_dir=f"{filename}.xlsx",
    )

    _url = f"{BASE_URL}reports/files/{filename}.zip"

    html = f"""
<html>
<head></head>
<body>
    <p>Please use the following link to download your report as requested from the 50MAWSP SMS Gateway</p>
    <p><a href='{_url}'>{_url}</a></p>
</body>
</html>
"""

    send_email([recipient_email], title, html)
