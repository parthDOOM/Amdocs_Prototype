from ChatbotWebsite import db,create_app

# Create the app
app = create_app()

with app.app_context():
    db.create_all()

# Run the app
if __name__ == '__main__':
    app.run()
