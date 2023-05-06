<!DOCTYPE html>
<html>
<head>
  <title>E-Commerce Bookstore</title>
</head>
<body>
  <h1>E-Commerce Bookstore</h1>
  <p>This is an e-commerce website for selling books. It is built using Django, a Python web framework. The website allows users to browse through a collection of books, add them to a shopping cart, and make purchases using their credit card.</p>
  <h2>Features</h2>
  <ul>
    <li>Browse books by category or search for books by title or author</li>
    <li>View book details such as description, price, and availability</li>
    <li>Add books to a shopping cart and proceed to checkout</li>
    <li>Create an account to save billing and shipping information for future purchases</li>
    <li>Make purchases using a credit card</li>
    <li>View order history and order details</li>
  </ul>
  <h2>Installation</h2>
  <ol>
    <li>Clone the repository to your local machine:</li>
    <pre><code>git clone https://github.com/yourusername/ecommerce-bookstore.git</code></pre>
    <li>Install the required dependencies:</li>
    <pre><code>pip install -r requirements.txt</code></pre>
    <li>Create a new database and run migrations:</li>
    <pre><code>python manage.py migrate</code></pre>
    <li>Load initial data into the database:</li>
    <pre><code>python manage.py loaddata books.json</code></pre>
    <li>Start the development server:</li>
    <pre><code>python manage.py runserver</code></pre>
    <li>Open your web browser and go to <a href="http://localhost:8000/">http://localhost:8000/</a> to view the website.</li>
  </ol>
  <h2>Configuration</h2>
  <p>The website uses environment variables for configuration. You can set these variables in a <code>.env</code> file in the root directory of the project. Here are the required variables:</p>
  <ul>
    <li><code>SECRET_KEY</code>: Django secret key used for security purposes</li>
    <li><code>DEBUG</code>: Set to <code>True</code> for development mode, <code>False</code> for production mode</li>
    <li><code>ALLOWED_HOSTS</code>: A comma-separated list of allowed hosts for the website</li>
    <li><code>STRIPE_PUBLIC_KEY</code>: Stripe public key for processing credit card payments</li>
    <li><code>STRIPE_SECRET_KEY</code>: Stripe secret key for processing credit card payments</li>
  </ul>
</body>
</html>
