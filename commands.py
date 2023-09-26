from flask import Blueprint
from datetime import datetime
from random import randint
import time

from main import db, bcrypt
from models.user import User
from models.review import Review
from models.transaction import Transactions
from models.userlibrary import User_Library
from models.game import Game
from models.genre import Genre
from models.developer import Developer
from models.publisher import Publisher


db_commands = Blueprint("db", __name__)

@db_commands.cli.command("create")
def create_db():
    db.create_all()
    print("Tables are created")

@db_commands.cli.command("drop")
def drop_db():
    db.drop_all()
    print("Tables are dropped")

@db_commands.cli.command("seed")
def seed_db():
    try:
        seed_users()
        seed_games()
        seed_genres()
        seed_developers()
        seed_publishers()
        seed_reviews()
        seed_transactions()
        seed_user_libraries()
        print("Database has been seeded")
    except Exception as e:
        print(f"Error seeding database: {str(e)}")


@db_commands.cli.command("seed_users")
def seed_users():
    # create User objects
    user1 = User(
        Username = "Bryan",
        Email = "Bryan@fakeemail.com",
        Password = bcrypt.generate_password_hash("password").decode("utf-8"),
        Registration_Date = datetime.now()
    )
    user2 = User(
        Username = "Fake",
        Email = "fake@fakeemail.com",
        Password = bcrypt.generate_password_hash("password").decode("utf-8"),
        Registration_date = datetime.now()
    )

    # add all users object to db
    db.session.add_all([
        user1, user2,
    ])
    # commit db for users
    db.session.commit()
   


@db_commands.cli.command("seed_games")
def seed_games():
    # Create Game objects
    game1 = Game(
        Genre_ID=1, 
        Developer_ID=1, 
        Publisher_ID=1, 
        Title="World of Warcraft",
        Release_Date=datetime(2004, 11, 23), 
        Avg_User_Rating=4.5,  
        Num_User_Rating=100  
    )

    game2 = Game(
        Genre_ID=2,  
        Developer_ID=2,  
        Publisher_ID=2,  
        Title="League of Legends",
        Release_Date=datetime(2009, 10, 27),  
        Avg_User_Rating=4.0,  
        Num_User_Rating=50  
    )

    game3 = Game(
        Genre_ID=3,
        Developer_ID=3,
        Publisher_ID=3,
        Title="Counter-Strike go",
        Release_Date=datetime(2012, 8, 21),
        Avg_User_Rating=4.0,
        Num_User_Rating=34
    )

    # Add all Game objects to the database session
    db.session.add_all([game1, game2, game3])

    # Commit the games to the database
    db.session.commit()



@db_commands.cli.command("seed_genres")
def seed_genres():
    # Create Genre objects
    genre1 = Genre(
        Genre_Name="Massive Multiplayer Online Role Playing Game"
    )
    genre2 = Genre(
        Genre_Name="Massive Online Battle Arena"
    )
    genre3 = Genre(
        Genre_Name="First Person Shooter"
    )

    # Add all Genre objects to the database session
    db.session.add_all([genre1, genre2, genre3])

    # Commit the genres to the database
    db.session.commit()



@db_commands.cli.command("seed_developers")
def seed_developers():
    # Create Developer objects
    developer1 = Developer(
        Name="Activision Blizzard",
        Website="https://www.blizzard.com",
        Contact_Info="contact@blizzard.com"
    )
    developer2 = Developer(
        Name="Riot Games",
        Website="https://www.riot.com",
        Contact_Info="contact@riot.com"
    )
    developer3 = Developer(
        Name="Valve",
        Website="https://www.valve.com",
        Contact_Info="contact@valve.com"
    )

    # Add all Developer objects to the database session
    db.session.add_all([developer1, developer2, developer3])

    # Commit the changes to the database
    db.session.commit()



@db_commands.cli.command("seed_publishers")
def seed_publishers():
    # Create Publisher objects
    publisher1 = Publisher(
        Name="Blizzard",
        Website="https://www.blizzard.com",
        Contact_info="contact@blizzard.com"
    )
    publisher2 = Publisher(
        Name="Riot Games",
        Website="https://www.Riot.com",
        Contact_info="contact@riot.com"
    )
    publisher3 = Publisher(
        Name="Valve Corporation",
        Website="https://www.valve.com",
        Contact_info="contact@valve.com"
    )

    # Add all Publisher objects to the database session
    db.session.add_all([publisher1, publisher2, publisher3])

    # Commit the changes to the database
    db.session.commit()



@db_commands.cli.command("seed_reviews")
def seed_reviews():
    reviews = [
        Review(
            User_ID=1,  
            Game_ID=1,  
            Rating=randint(1, 5), 
            Review_Description="Review goes here",
            Review_Date=datetime.now(),
        ),
        Review(
            User_ID=2,  
            Game_ID=2,  
            Rating=randint(1, 5),  
            Review_Description="Type review here.",
            Review_Date=datetime.now(),
        ),
        Review(
            User_ID=3,
            Game_ID=3,
            Rating=randint(1, 5),
            Review_description="Another review",
            Review_Date=datetime.now(),
        )
    ]

    # Add all Review objects to the database session
    db.session.add_all(reviews)

    # Commit the changes to the database
    db.session.commit()



@db_commands.cli.command("seed_transactions")
def seed_transactions():
    # Create Transactions objects
    transactions = [
        Transactions(
            User_ID=1,  
            Game_ID=1,  
            Purchase_Date=datetime.now(),
            Transaction_Amount=1999,  
            Payment_Method="Credit Card",
            Transaction_Status="Completed",
        ),
        Transactions(
            User_ID=2,  
            Game_ID=2,  
            Purchase_Date=datetime.now(),
            Transaction_Amount=2499,  
            Payment_Method="PayPal",
            Transaction_Status="Completed",
        ),
        Transactions(
            User_ID=3,
            Game_ID=3,
            Purchase_Date=datetime.now(),
            Transaction_Amount=1632,
            Payment_Method="gift card",
            Transaction_Status="Processing"
        )
    ]

    # Add all Transactions objects to the database session
    db.session.add_all(transactions)

    # Commit the transactions to the database
    db.session.commit()

@db_commands.cli.command("seed_user_libraries")
def seed_user_libraries():
    # Create UserLibrary objects
    user_libraries = [
        User_Library(
            User_ID=1,  
            Game_ID=1, 
            Purchase_Date=datetime.now(),
            Play_Time=10, 
            Status="Owned",
        ),
        User_Library(
            User_ID=2,  
            Game_ID=2,  
            Purchase_Date=datetime.now(),
            Play_Time=5,  
            Status="Owned",
        ),
        User_Library(
            User_ID=3,
            Game_ID=3,
            Purchase_Date=datetime.now(),
            Play_Time=0,
            Status="Not Owned"
        )
        # Add more user libraries as needed
    ]

    # Add all UserLibrary objects to the database session
    db.session.add_all(user_libraries)

    # Commit the changes to the database
    db.session.commit()

    # log if seed is succeeded
    print("Database has been seeded")