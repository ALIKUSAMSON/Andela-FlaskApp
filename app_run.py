from flask import Flask, render_template, redirect, url_for, request, sessions, flash
import models
import yummymodel

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        if email in models.users:
            loginuser = models.YummyRecipeApp(email, password)
            if loginuser.login() == 'Logged in':
                # models.logged_in[0] is the identifier of the logged in user
                user_DB = yummymodel.User(models.logged_in[0]).view_user_DB(models.logged_in[0])
                # user_DB returns the DB of the logged in user
                return render_template("dashboard.html", user_DB=user_DB)
            else:
                flash('Password Incorrect')
                return render_template("login.html")
        else:
            flash('Unknown user')
            return render_template("signup.html")
    return render_template("login.html")


@app.route("/signup", methods=['GET', "POST"])
def signup():
    """method implementing signup"""
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        createuser = models.YummyRecipeApp(email, password, name, )
        createuser.signup()  # creates users with above credentials
        return render_template('login.html')
    else:
        return render_template("signup.html")

@app.route('/logout')
def logout():

    models.logged_in[0] = None  # replaces logged in user with None
    return redirect(url_for('login'))

@app.route("/dashboard",methods=["GET",'POST'])
def dashboard():

    if models.logged_in[0]:
        user_DB = yummymodel.User(models.logged_in[0]).view_user_DB(models.logged_in[0])
        # user_bucketlists returns the bucketlist of the logged in user
        return render_template("dashboard.html", user_DB=user_DB)
    else:
        return redirect(url_for('login'))

@app.route("/create")
def create_page():
    return render_template("create.html")

@app.route("/createrecipe",methods=['POST','GET'])
def createRecipe():
    if models.logged_in[0]:
        if request.method == 'POST':
            recipe = request.form['recipe']
            create_DB = yummymodel.User(models.logged_in[0])
            create_DB.create_user_DB(recipe)
            return redirect(url_for('dashboard'))
    else:
        return redirect(url_for('login'))
    return render_template('create.html') 

@app.route('/yummylists/<int:RecipeID>/delete', methods=['POST', 'GET'])
def deleteRecipe(RecipeID):
    if models.logged_in[0]:
        if request.method == 'POST':
            recipe = request.form['recipe']
            user_DB = yummymodel.User(models.logged_in[0]).delete_DB(yummymodel.current_user_DB[RecipeID])
            return redirect(url_for('dashboard'))
    else:
        return redirect(url_for('login'))


@app.route('/yummylists/<int:RecipeID>/update', methods=['POST', 'GET'])
def update_DB(RecipeID):
    if models.logged_in[0]:
        if request.method == 'POST':
            new_recipe = request.form['new_recipe']
            user_DB = yummymodel.User(models.logged_in[0]).update_DB(yummymodel.current_user_DB[RecipeID], new_recipe)
            return redirect(url_for('dashboard'))
        elif request.method == 'GET':
            return render_template('update.html')
    else:
        return redirect(url_for('login'))

@app.route("/update")
def update():
    return render_template("update.html")

@app.route('/yummylists/<int:RecipeID>', methods=['GET', 'POST'])
def view_items_in_yummylist(RecipeID):
    if models.logged_in[0]:
        if request.method =='GET':
            user_DB = yummymodel.User(models.logged_in[0]).view_user_DB(models.logged_in[0])
            yummylist = yummymodel.current_user_DB[RecipeID]
        else:
            return render_template("dashboard.html",user_DB=user_DB)
    else:
        return render_template('login')



if __name__ == '__main__':
    app.run(debug=True)
