from flask import Blueprint
from datetime import datetime
from main import db, bcrypt

from models import (User, Review, Transactions, User_Library,
                    Game, Genre, Developer, Publisher)



db_commands = Blueprint("db", __name__)

@db_commands.cli.command("create")
def create_db():
    db.create_all()
    print("Tables are created")

@db_commands.cli.command("drop")
def drop_db():
    db.drop_all()
    print("Tables are dropped")


#seed data for ALL tables
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



#seed data for users table
@db_commands.cli.command("seed_users")
def seed_users():
    # create User objects
    user1 = User(
        username = "Bryan",
        email = "Bryan@fakeemail.com",
        password = bcrypt.generate_password_hash("password").decode("utf-8"),
        registration_date = datetime.now(),
        is_admin = True
    )
    user2 = User(
        username = "Fake",
        email = "fake@fakeemail.com",
        password = bcrypt.generate_password_hash("password").decode("utf-8"),
        registration_date = datetime.now(),
        is_admin = False
    )

    # add all users object to db
    db.session.add_all([
        user1, user2,
    ])
    # commit db for users
    db.session.commit()
   


#seed data for games table
@db_commands.cli.command("seed_games")
def seed_games():
    # Create Game objects
    game1 = Game(
        genre_id=1, 
        developer_id=1, 
        publisher_id=1, 
        title="World of Warcraft",
        release_date=datetime(2004, 11, 23), 
        avg_user_rating=4.5,  
        num_user_rating=100  
    )

    game2 = Game(
        genre_id=2,  
        developer_id=2,  
        publisher_id=2,  
        title="League of Legends",
        release_date=datetime(2009, 10, 27),  
        avg_user_rating=4.0,  
        num_user_rating=50  
    )

    game3 = Game(
        genre_id=3,
        developer_id=3,
        publisher_id=3,
        title="Counter-Strike go",
        release_date=datetime(2012, 8, 21),
        avg_user_rating=4.0,
        num_user_rating=34
    )

    # Add all Game objects to the database session
    db.session.add_all([game1, game2, game3])

    # Commit the games to the database
    db.session.commit()



# seed data for genres table
@db_commands.cli.command("seed_genres")
def seed_genres():
    # Create Genre objects
    genre1 = Genre(
        genre_name="Massive Multiplayer Online Role Playing Game"
    )
    genre2 = Genre(
        genre_name="Massive Online Battle Arena"
    )
    genre3 = Genre(
        genre_name="First Person Shooter"
    )

    # Add all Genre objects to the database session
    db.session.add_all([genre1, genre2, genre3])

    # Commit the genres to the database
    db.session.commit()



# seed data for developers table
@db_commands.cli.command("seed_developers")
def seed_developers():
    # Create Developer objects
    developer1 = Developer(
        name="Activision Blizzard",
        website="https://www.blizzard.com",
        contact_info="contact@blizzard.com"
    )
    developer2 = Developer(
        name="Riot Games",
        website="https://www.riot.com",
        contact_info="contact@riot.com"
    )
    developer3 = Developer(
        name="Valve",
        website="https://www.valve.com",
        contact_info="contact@valve.com"
    )

    # Add all Developer objects to the database session
    db.session.add_all([developer1, developer2, developer3])

    # Commit the changes to the database
    db.session.commit()



#seed data for publishers table
@db_commands.cli.command("seed_publishers")
def seed_publishers():
    # Create Publisher objects
    publisher1 = Publisher(
        name="Blizzard",
        website="https://www.blizzard.com",
        contact_info="contact@blizzard.com"
    )
    publisher2 = Publisher(
        name="Riot Games",
        website="https://www.Riot.com",
        contact_info="contact@riot.com"
    )
    publisher3 = Publisher(
        name="Valve Corporation",
        website="https://www.valve.com",
        contact_info="contact@valve.com"
    )

    # Add all Publisher objects to the database session
    db.session.add_all([publisher1, publisher2, publisher3])

    # Commit the changes to the database
    db.session.commit()



# seed data for reviews table
@db_commands.cli.command("seed_reviews")
def seed_reviews():
    reviews = [
        Review(
            user_id=1,  
            game_id=1,  
            rating=4, 
            review_description="Review goes here",
            revie_date=datetime.now(),
        ),
        Review(
            user_id=2,  
            game_id=2,  
            rating=3,  
            review_description="Type review here.",
            revie_date=datetime.now(),
        ),
        Review(
            user_id=3,
            game_id=3,
            rating=5,
            review_description="Another review",
            revie_date=datetime.now(),
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
            user_id=1,  
            game_id=1,  
            purchase_date=datetime.now(),
            transaction_amount=1999,  
            payment_method="Credit Card",
            transaction_status="Completed",
        ),
        Transactions(
            user_id=2,  
            game_id=2,  
            purchase_date=datetime.now(),
            transaction_amount=2499,  
            payment_method="PayPal",
            transaction_status="Completed",
        ),
        Transactions(
            user_id=3,
            game_id=3,
            purchase_date=datetime.now(),
            transaction_amount=1632,
            payment_method="gift card",
            transaction_status="Processing"
        )
    ]

    # Add all Transactions objects to the database session
    db.session.add_all(transactions)

    # Commit the transactions to the database
    db.session.commit()



#seed data for User_librarys table
@db_commands.cli.command("seed_user_libraries")
def seed_user_libraries():
    # Create UserLibrary objects
    user_libraries = [
        User_Library(
            user_id=1,  
            game_id=1, 
            purchase_date=datetime.now(),
            play_time=10, 
            status="Owned",
        ),
        User_Library(
            user_id=2,  
            game_id=2,  
            purchase_date=datetime.now(),
            play_time=5,  
            status="Owned",
        ),
        User_Library(
            user_id=3,
            game_id=3,
            purchase_date=datetime.now(),
            play_time=0,
            status="Not Owned"
        )
        # Add more user libraries as needed
    ]

    # Add all UserLibrary objects to the database session
    db.session.add_all(user_libraries)

    # Commit the changes to the database
    db.session.commit()

    # log if seed is succeeded
    print("Database has been seeded")