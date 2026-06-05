# функція для ініціалізації бази даних та додавання даних
def create_db():
    from app import app
    from models import db,Shirts,Print,Other

    with app.app_context():
        # db.drop_all() # видаляє всі таблиці (для навчання)
        db.create_all()  # створює заново

        if not Shirts.query.first():
            Shirt1 = Shirts(name="Футболка", description="удобно носити літом", price=5.0,
                           image="images/shirt.png")
            Shirt2 = Shirts(name="Худі", description="удобно носити коли холодно", price=5.0,
                           image="images/hoodie.png")
            Shirt3 = Shirts(name="Світер", description="удобно носити коли холодно", price=5.0,
                           image="images/sweeter.png")
            db.session.add_all([Shirt1,Shirt2,Shirt3])
        if not Print.query.first():
            Print1=Print(name="гоблін", description="монстр з гри", price=1.0,
                           image="images/goblin.png")
            Print2=Print(name="Скелет", description="монстр з гри", price=1.0,
                           image="images/skeleton.png")
            Print3=Print(name="Слайм", description="монстр з гри", price=1.0,
                           image="images/slime.png")
            db.session.add_all([Print1,Print2,Print3])
        if not Other.query.first():
            Other1=Other(name="Бейсболка", description="", price=1.0,
                           image="images/Cap.png")
            Other2=Other(name="Панамка", description="", price=1.0,
                           image="images/panama.png")
            Other3=Other(name="socks", description="", price=1.0,
                           image="images/socks.png")
            db.session.add_all([Other1,Other2,Other3])
        db.session.commit()

if __name__ == '__main__':
    create_db()
    print("Базу даних успішно ініціалізовано!")