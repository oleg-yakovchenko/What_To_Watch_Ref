from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('settings.Config')

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Импорты из модулей пакета размещены в конце файла,
# чтобы избежать циклических зависимостей:
# views/models/cli_commands/error_handlers импортируют db,
# а db должен быть создан раньше.
from .views import blueprint                                     # noqa: E402
from .cli_commands import load_opinions_command                  # noqa: E402
from .error_handlers import internal_error, page_not_found       # noqa: E402

app.register_blueprint(blueprint)
app.cli.add_command(load_opinions_command)
app.register_error_handler(404, page_not_found)
app.register_error_handler(500, internal_error)