# Sokoyetu  

**Sokoyetu** is an online fresh produce application designed to connect farmers directly with consumers, retailers, and businesses. The system empowers smallholder farmers by giving them access to digital markets, reducing dependency on middlemen, and ensuring fair prices for their produce.  


## Features  

- User Accounts – farmers and customers can register, log in, and manage their profiles.  
- Produce Listings – farmers can upload their products with details (name, category, price, etc.).  
- Shopping Cart – customers can browse listings, add items to their cart, and proceed to checkout.  
- Orders Management – seamless order processing between farmers and customers.  
- Analytics (future scope) – insights on sales trends and customer demand.  
- Sustainability Focus – promotes local sourcing and reduces post-harvest losses.  


## Getting Started  

### Prerequisites  
- Python 3.9+  
- Django 4.x  
- Virtual environment (recommended)  

### Installation  

```bash
# Clone the repository
git clone https://github.com/Chaser-254/sokoyetu.git
cd sokoyetu

# Create virtual environment
python -m venv venv
source venv/bin/activate   # On Windows use: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Start development server
python manage.py runserver
