from flask import Flask, render_template

app = Flask(__name__)

# Пример структур пользователей
users_data = {
    'user1': {'name': 'John Doe', 'age': 30, 'city': 'New York'},
    'user2': {'name': 'Jane Doe', 'age': 25, 'city': 'San Francisco'},
    # Добавьте других пользователей по необходимости
}

@app.route('/user/<username>')
def user_profile(username):
    # Получаем данные пользователя из словаря
    user_data = users_data.get(username)

    # Проверяем, существует ли пользователь
    if user_data:
        return render_template('user_profile.html', user=user_data)
    else:
        return 'Пользователь не найден', 404

if __name__ == '__main__':
    app.run(debug=True)