
# E-Auctify - Online Auction Platform


Welcome to E-Auctify, an exciting online auction platform where you can discover, bid, and win unique items. This repository provides a Django-based web application designed to create and manage online auction events.


## Features

1. User-Friendly Interface:

- Seamless and intuitive design for a user-friendly experience.

2. Authentication System:

- Secure user authentication to ensure only authorized users can participate in auctions.

3. Auction Creation:

- Easily create new auction events with details such as title, description, starting bid, and end time.
4. Bid Management:

- Users can place bids on items.
- The system automatically handles bid tracking and winner determination.
5. Real-Time Updates:

- Utilizes WebSocket technology for real-time updates on bid activities, ensuring a dynamic and engaging auction experience.
6. Admin Dashboard:

- An intuitive admin interface for managing users, auctions, and monitoring bidding activities.
7. Responsive Design:

- Mobile-friendly interface providing a seamless experience across various devices.




## Deployment

Follow these steps to set up the E-Auctify platform locally:


1. Clone the repository:
```bash
  git clone https://github.com/amandange2001/E-Auctify.git
  cd e_auctify
```

2. Configure the database:
```bash
python manage.py makemigrations
python manage.py migrate
```

3. Create a superuser for admin access:
```bash
python manage.py createsuperuser
```

4. Run the development server:
```bash
python manage.py runserver
```
Access the application at http://localhost:8000/
## Usage

1.Admin Dashboard:

- Log in as an admin at http://localhost:8000/admin/ to create auctions and manage users.

2. User Registration:
- Create a user account to participate in auctions.

3. Browse and Bid:
- Visit the auction platform, explore, and bid on available items.

4. Create Auctions:
- Authenticated users can create new auctions easily.

## Contributing

We welcome contributions to enhance the E-Auctify platform. Please follow our contribution guidelines for more details.
