from app import db


class character(db.Model):
	# ID and character name
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    name = db.Column(db.String(25), unique=True, nullable=False)
    
    # First set of Objects from objects from service-2
    race = db.Column(db.String(25), nullable=False)
    stature = db.Column(db.String(25), nullable=False)
    location = db.Column(db.String(25), nullable=False)
    rank = db.Column(db.String(25), nullable=False)
    profession = db.Column(db.String(25), nullable=False)
    
    # second set of objects from service-3
    grade = db.Column(db.String(25), nullable=False)
    weapon = db.Column(db.String(25), nullable=False)
    stance = db.Column(db.String(25), nullable=False)
    trait_1 = db.Column(db.String(25), nullable=False)
    trait_2 = db.Column(db.String(25), nullable=False)
    trait_3 = db.Column(db.String(25), nullable=False)

    # Thrid set of objects from service-5 
    melee_prowess = db.Column(db.Integer, nullable=False)
    archery_prowess = db.Column(db.Integer, nullable=False)
    strength = db.Column(db.Integer, nullable=False)
    endurance = db.Column(db.Integer, nullable=False)
    intelligence = db.Column(db.Integer, nullable=False)
    awareness = db.Column(db.Integer, nullable=False)
    dexterity = db.Column(db.Integer, nullable=False)
    dodge = db.Column(db.Integer, nullable=False)

    