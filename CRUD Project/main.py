from flask import Flask, render_template, request, redirect
import db_operations

app = Flask(__name__)

# Route untuk halaman utama
@app.route('/')
def index():
    items = db_operations.get_all_items()
    return render_template('index.html', items=items)

# Route untuk menambah item
@app.route('/add', methods=['GET', 'POST'])
def add_item():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        db_operations.add_item(name, description)
        return redirect('/')
    return render_template('add.html')

# Route untuk mengedit item
@app.route('/edit/<int:item_id>', methods=['GET', 'POST'])
def edit_item(item_id):
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        db_operations.update_item(item_id, name, description)
        return redirect('/')
    item = db_operations.get_item(item_id)
    return render_template('edit.html', item=item)

# Route untuk menghapus item
@app.route('/delete/<int:item_id>')
def delete_item(item_id):
    db_operations.delete_item(item_id)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
