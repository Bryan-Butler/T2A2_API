from flask import Blueprint


# Import your blueprint modules
from . import developer_controller
from . import game_controller
from . import genre_controller
from . import publisher_controller
from . import review_controller
from . import transaction_controller
from . import user_controller
from . import user_library_controller
from . import user_management_controller

# Define your blueprints
developers = Blueprint("developers", __name__, url_prefix="/developer")
game = Blueprint("game", __name__, url_prefix="/games")
genre = Blueprint("genre", __name__, url_prefix='/genres')
publisher = Blueprint('publisher_bp', __name__, url_prefix="/publisher")
review = Blueprint("review", __name__, url_prefix="/review")
transaction = Blueprint('transaction', __name__, url_prefix="/transaction")
home = Blueprint("home", __name__, url_prefix="/")
library = Blueprint("library", __name__, url_prefix="/library")
user_management = Blueprint("user_management", __name__, url_prefix="/management")




# Import other blueprint modules as needed

all_controllers = [developers, game, genre, publisher, review, transaction, home, library, user_management]