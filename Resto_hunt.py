from flask import Flask, render_template, request

app = Flask(__name__)

# Sample hotel data specific to Wai city
hotels = [
    {
        'id': 1,
        'name': 'Jay Ambika Farms',
        'description': 'A 5-star hotel offering the best comfort in Wai.',
        'image': '/static/images/jay_ambika_farms.jpg',
        'rate': '₹1754',
        'amenities': ['Free WiFi', 'Pool', 'Spa', 'Food and drinks', 'Parking'],
        'maps_link': 'https://maps.app.goo.gl/yE4LCX1j85zMtqiq6',
        "gallery_images": [
        "images/jay_ambika_farms.jpg",
        "images/jay_ambika_farms1.jpg",
        "images/jay_ambika_farms2.jpg",
        "images/jay_ambika_farms3.jpg"
        ]
    },
    {
        'id': 2,
        'name': 'Gulmohar Resort',
        'description': 'A hotel with stunning views of the hills.',
        'image': '/static/images/gulmohar_resort.jpg',
        'rate': '₹2165',
        'amenities': ['Mountain view', 'Parking', 'Restaurant', 'pool'],
        'maps_link': 'https://maps.app.goo.gl/yQce9zKim4brFD9j6',
        "gallery_images": [
        "images/gulmohar_resort1.jpg",
        "images/gulmohar_resort2.jpg",
        "images/gulmohar_resort3.jpg",
        "images/gulmohar_resort4.jpg",
        "images/g.jpg",
        "images/gulmohar_resort6.jpg"
        ]
    },
    {
        'id': 3,
        'name': 'Hotel Anand Lodge',
        'description': 'A hotel with clean rooms and other amenities.',
        'image': '/static/images/hotel_anand_lodge.jpg',
        'rate': '₹1477',
        'amenities': ['Free WiFi', 'Parking', 'Restaurant',],
        'maps_link': 'https://maps.app.goo.gl/XMt1nuYnJapEziQdA',
        "gallery_images": [
        "images/hotel_anand_lodge1.jpg",
        "images/hotel_anand_lodge2.jpg",
        "images/hotel_anand_lodge3.jpg",
        "images/hotel_anand_lodge4.jpg",
        "images/hotel_anand_lodge5.jpg",
        "images/hotel_anand_lodge6.jpg"
        ]
    },
    {
        'id': 4,
        'name': 'Hotel Srushti Regency',
        'description': 'A place to stay near the nature.',
        'image': '/static/images/hotel_srushti_regency.jpg',
        'rate': '₹2582',
        'amenities': ['Free WiFi', 'Parking', 'Free Breakfast', 'Pet Friendly', 'Restaurant'],
        'maps_link': 'https://maps.app.goo.gl/unPTzV5aW6vEwDMt9',
    },
    {
        'id': 5,
        'name': 'Siddhagiri Hotel And Resort',
        'description': 'A hotel with clean rooms and other amenities.',
        'image': '/static/images/siddhigiri_resort.png',
        'rate': '₹3523',
        'amenities': ['Free WiFi', 'Paid Parking', 'Restaurant', 'Free Breakfast'],
        'maps_link': 'https://maps.app.goo.gl/vHCLpYcqBKnTeyGt8',
    },
    {
        'id': 6,
        'name': 'Anandvan Holiday Homes',
        'description': 'A hotel with clean rooms and other amenities.',
        'image': '/static/images/anandvan_holiday_home.jpeg',
        'rate': '₹2688',
        'amenities': ['Free WiFi', 'Parking', 'Restaurant', 'Outdoor Pool', 'Pet-friendly', 'Breakfast'],
        'maps_link': 'https://maps.app.goo.gl/tZQ4VzpWhKuTeZeA9',
    },
    {
        'id': 7,
        'name': 'Magnus Caverns Resort',
        'description': 'A hotel with Lakeside view and many fun activities.',
        'image': '/static/images/magnus_caverns_resort.jpg',
        'rate': '₹3808',
        'amenities': ['Free WiFi', 'Parking', 'Restaurant', 'Outdoor Pool', 'Hot tub', 'Free Breakfast', 'Airport Shuttle'],
        'maps_link': 'https://maps.app.goo.gl/5g6nB6bzUsi8eH2v9',
    },
    {
        'id': 8,
        'name': 'Nakshatra Resort',
        'description': 'A Luxury Dam View ( 40 kms from Mahabaleshwar )',
        'image': '/static/images/nakshatra_resort.jpg',
        'rate': '₹4857',
        'amenities': ['Free WiFi', 'Free Parking', 'Restaurant', 'Fitness Center', 'Paid Breakfast', 'Outdoor Pool'],
        'maps_link': 'https://maps.app.goo.gl/XMt1nuYnJapEziQdA',
    },
    {
        'id': 9,
        'name': 'Sandesh Resort',
        'description': 'A hotel with clean rooms and other amenities.',
        'image': '/static/images/sandesh_resort.jpg',
        'rate': '₹2127',
        'amenities': ['Free WiFi', 'Parking', 'Restaurant', 'Pool', 'Spa'],
        'maps_link': 'https://maps.app.goo.gl/TSW4nRng6FicdxvY6',
    },
    {
        'id': 10,
        'name': 'Gandharv Resorts',
        'description': 'A hotel with clean rooms and other amenities.',
        'image': '/static/images/gandharv_resorts.jpg',
        'rate': '₹5102',
        'amenities': ['Free WiFi', 'Parking', 'Restaurant', 'Free Breakfast', 'Pool', 'Kitchens in room'],
        'maps_link': 'https://maps.app.goo.gl/Np1aTR6wLgUzSo5X7',
    },
    {
        'id': 11,
        'name': 'Rutugandh River View Resort',
        'description': 'A hotel with stunning river and hills view.',
        'image': '/static/images/rutugandh.jpg',
        'rate': '₹5656',
        'amenities': ['Free WiFi', 'Free Parking', 'Restaurant', 'Airport Shuttle', 'Laundry Service'],
        'maps_link': 'https://maps.app.goo.gl/vxQoN3AWxJTY5MX76',
    },
    {
        'id': 12,
        'name': 'Hotel Sanai Residency',
        'description': 'A hotel with clean rooms and other amenities.',
        'image': '/static/images/sanai_residency.jpg',
        'rate': '₹3462',
        'amenities': ['Free WiFi', 'Free Parking', 'Restaurant', 'Free Breakfast', 'Outdoor Pool', 'Bar', 'Airport Shuttle'],
        'maps_link': 'https://maps.app.goo.gl/H4nUnVBAtXVsqTbz7',
    },
    {
        'id': 13,
        'name': 'Srushti Agri Tourism Resort',
        'description': 'A hotel with clean rooms and other amenities.',
        'image': '/static/images/srushti_agri.jpg',
        'rate': '₹3246',
        'amenities': ['Free WiFi', 'Parking', 'Restaurant', 'Kitchens in rooms', 'Pet Friendly', 'Laundry service'],
        'maps_link': 'https://maps.app.goo.gl/HYYu792H2zNZJcHZ6',
    },
]

# Sample restaurant data specific to Wai city
restaurants = [
    {
        'id': 1,
        'name': 'Shivshahi Family Restaurant',
        'image': '/static/images/shivshahi.jpg',
        'city': 'Wai',
        'cuisine_type': 'South Indian, North Indian, Snacks, Beverages, Non-Veg',
        'dishes': {
            'South Indian': [
                {'name': 'Vada Sambar', 'price': '50₹'},
                {'name': 'Idli Chutney Sambar', 'price': '30₹'},
                {'name': 'Plain Uttapam', 'price': '90₹'},
                {'name': 'Plain Dosa', 'price': '60₹'},
                {'name': 'Masala Dosa', 'price': '80₹'},
                {'name': 'Onion Uttapam', 'price': '70₹'},
                {'name': 'Medu Vada', 'price': '40₹'},
                {'name': 'Set Dosa', 'price': '85₹'},
                {'name': 'Rava Masala Dosa', 'price': '95₹'},
                {'name': 'Pongal Vada', 'price': '75₹'}
            ],
            'North Indian Veg': [
                {'name': 'Punjabi Thali', 'price': '295₹'},
                {'name': 'Paneer Handi', 'price': '290₹'},
                {'name': 'Kaju Curry', 'price': '300₹'},
                {'name': 'Veg Kofta', 'price': '250₹'},
                {'name': 'Palak Paneer', 'price': '280₹'},
                {'name': 'Chole Bhature', 'price': '150₹'},
                {'name': 'Mix Veg', 'price': '230₹'},
                {'name': 'Dal Makhani', 'price': '220₹'},
                {'name': 'Paneer Tikka Masala', 'price': '270₹'},
                {'name': 'Veg Pulao', 'price': '200₹'}
            ],
            'North Indian Non-Veg': [
                {'name': 'Chicken Tandoori', 'price': '280₹'},
                {'name': 'Butter Chicken', 'price': '320₹'},
                {'name': 'Chicken Biryani', 'price': '240₹'},
                {'name': 'Mutton Rogan Josh', 'price': '350₹'},
                {'name': 'Fish Curry', 'price': '310₹'},
                {'name': 'Prawn Masala', 'price': '300₹'},
                {'name': 'Mutton Biryani', 'price': '350₹'},
                {'name': 'Chicken Handi', 'price': '280₹'},
                {'name': 'Fish Fry', 'price': '220₹'},
                {'name': 'Egg Curry', 'price': '180₹'}
            ],
            'Snacks': [
                {'name': 'Misal Pav', 'price': '50₹'},
                {'name': 'Pav Bhaji', 'price': '60₹'},
                {'name': 'Samosa', 'price': '20₹'},
                {'name': 'Vada Pav', 'price': '15₹'},
                {'name': 'Puri Bhaji', 'price': '40₹'},
                {'name': 'Bhel Puri', 'price': '30₹'},
                {'name': 'Sev Puri', 'price': '30₹'},
                {'name': 'Dahi Puri', 'price': '35₹'},
                {'name': 'Onion Bhaji', 'price': '25₹'},
                {'name': 'Kurma Puri', 'price': '50₹'}
            ],
            'Starters': [
                {'name': 'Paneer Tikka', 'price': '180₹'},
                {'name': 'Chicken Tikka', 'price': '220₹'},
                {'name': 'Hara Bhara Kebab', 'price': '150₹'},
                {'name': 'Chicken Lollipop', 'price': '250₹'},
                {'name': 'Veg Manchurian', 'price': '180₹'},
                {'name': 'Fish Tikka', 'price': '260₹'},
                {'name': 'Chicken Malai Tikka', 'price': '270₹'},
                {'name': 'Tandoori Prawns', 'price': '320₹'},
                {'name': 'Paneer Pakoda', 'price': '160₹'},
                {'name': 'Veg Spring Roll', 'price': '140₹'}
            ],
            'Bread': [
                {'name': 'Roti', 'price': '10₹'},
                {'name': 'Chapati', 'price': '10₹'},
                {'name': 'Tandoori Roti', 'price': '20₹'},
                {'name': 'Naan', 'price': '40₹'},
                {'name': 'Butter Naan', 'price': '50₹'},
                {'name': 'Garlic Naan', 'price': '60₹'},
                {'name': 'Lachha Paratha', 'price': '60₹'},
                {'name': 'Stuffed Kulcha', 'price': '70₹'},
                {'name': 'Aloo Paratha', 'price': '50₹'},
                {'name': 'Paneer Paratha', 'price': '80₹'}
            ],
            'Rice': [
                {'name': 'Jeera Rice', 'price': '70₹'},
                {'name': 'Plain Rice', 'price': '50₹'},
                {'name': 'Veg Pulao', 'price': '120₹'},
                {'name': 'Chicken Biryani', 'price': '240₹'},
                {'name': 'Mutton Biryani', 'price': '350₹'},
                {'name': 'Egg Fried Rice', 'price': '140₹'},
                {'name': 'Paneer Biryani', 'price': '220₹'},
                {'name': 'Prawn Biryani', 'price': '320₹'},
                {'name': 'Schezwan Rice', 'price': '150₹'},
                {'name': 'Veg Fried Rice', 'price': '120₹'}
            ],
            'Beverages': [
                {'name': 'Tea', 'price': '20₹'},
                {'name': 'Coffee', 'price': '40₹'},
                {'name': 'Butter Milk', 'price': '25₹'},
                {'name': 'Mango Juice', 'price': '45₹'},
                {'name': 'Solkadhi', 'price': '35₹'},
                {'name': 'Lime Water', 'price': '30₹'},
                {'name': 'Lassi', 'price': '40₹'},
                {'name': 'Cold Coffee', 'price': '60₹'},
                {'name': 'Masala Chai', 'price': '30₹'},
                {'name': 'Milkshake', 'price': '70₹'}
            ]
        },
        'maps_link': 'https://maps.app.goo.gl/oh1jgZKxB2XdRK8p8'
    },
    {
        'id': 2,
        'name': 'Abhiruchi Resort',
        'city': 'Wai',
        'image': '/static/images/abhiruchi.jpg',
        'cuisine_type': 'South Indian, North Indian, Snacks, Beverages, Non-Veg',
        'dishes': {
            'South Indian': [
                {'name': 'Idli Sambar', 'price': '50₹'},
                {'name': 'Medu Vada Sambar', 'price': '40₹'},
                {'name': 'Masala Dosa', 'price': '60₹'},
                {'name': 'Onion Uttapam', 'price': '50₹'},
                {'name': 'Rava Dosa', 'price': '65₹'},
                {'name': 'Set Dosa', 'price': '80₹'},
                {'name': 'Pongal', 'price': '75₹'},
                {'name': 'Plain Uttapam', 'price': '90₹'},
                {'name': 'Plain Dosa', 'price': '60₹'},
                {'name': 'Pesarattu', 'price': '85₹'}
            ],
            'North Indian Veg': [
                {'name': 'North Indian Thali', 'price': '150₹'},
                {'name': 'Dal Tadka', 'price': '120₹'},
                {'name': 'Paneer Butter Masala', 'price': '250₹'},
                {'name': 'Kadai Paneer', 'price': '240₹'},
                {'name': 'Veg Jalfrezi', 'price': '220₹'},
                {'name': 'Paneer Lababdar', 'price': '260₹'},
                {'name': 'Mix Veg Curry', 'price': '210₹'},
                {'name': 'Baingan Bharta', 'price': '200₹'},
                {'name': 'Methi Malai Mutter', 'price': '240₹'},
                {'name': 'Aloo Gobi', 'price': '180₹'}
            ],
            'North Indian Non-Veg': [
                {'name': 'Chicken Tikka Masala', 'price': '300₹'},
                {'name': 'Mutton Korma', 'price': '360₹'},
                {'name': 'Butter Chicken', 'price': '320₹'},
                {'name': 'Tandoori Chicken', 'price': '280₹'},
                {'name': 'Fish Curry', 'price': '300₹'},
                {'name': 'Prawn Curry', 'price': '320₹'},
                {'name': 'Chicken Biryani', 'price': '240₹'},
                {'name': 'Mutton Biryani', 'price': '350₹'},
                {'name': 'Egg Curry', 'price': '180₹'},
                {'name': 'Chicken Rogan Josh', 'price': '310₹'}
            ],
            'Snacks': [
                {'name': 'Puri Bhaji', 'price': '40₹'},
                {'name': 'Chole Bhature', 'price': '50₹'},
                {'name': 'Onion Bhaji', 'price': '25₹'},
                {'name': 'Kurma Puri', 'price': '50₹'},
                {'name': 'Samosa', 'price': '20₹'},
                {'name': 'Vada Pav', 'price': '15₹'},
                {'name': 'Misal Pav', 'price': '50₹'},
                {'name': 'Pav Bhaji', 'price': '60₹'},
                {'name': 'Bhel Puri', 'price': '30₹'},
                {'name': 'Dahi Puri', 'price': '35₹'}
            ],
            'Starters': [
                {'name': 'Veg Manchurian', 'price': '180₹'},
                {'name': 'Paneer Tikka', 'price': '190₹'},
                {'name': 'Chicken Lollipop', 'price': '250₹'},
                {'name': 'Fish Fry', 'price': '220₹'},
                {'name': 'Veg Spring Roll', 'price': '140₹'},
                {'name': 'Tandoori Prawns', 'price': '320₹'},
                {'name': 'Paneer Pakoda', 'price': '160₹'},
                {'name': 'Chicken Seekh Kebab', 'price': '270₹'},
                {'name': 'Hara Bhara Kebab', 'price': '150₹'},
                {'name': 'Mutton Seekh Kebab', 'price': '290₹'}
            ],
            'Bread': [
                {'name': 'Roti', 'price': '10₹'},
                {'name': 'Chapati', 'price': '10₹'},
                {'name': 'Tandoori Roti', 'price': '20₹'},
                {'name': 'Naan', 'price': '40₹'},
                {'name': 'Butter Naan', 'price': '50₹'},
                {'name': 'Garlic Naan', 'price': '60₹'},
                {'name': 'Lachha Paratha', 'price': '60₹'},
                {'name': 'Stuffed Kulcha', 'price': '70₹'},
                {'name': 'Aloo Paratha', 'price': '50₹'},
                {'name': 'Paneer Paratha', 'price': '80₹'}
            ],
            'Rice': [
                {'name': 'Jeera Rice', 'price': '70₹'},
                {'name': 'Plain Rice', 'price': '50₹'},
                {'name': 'Veg Pulao', 'price': '120₹'},
                {'name': 'Chicken Biryani', 'price': '240₹'},
                {'name': 'Mutton Biryani', 'price': '350₹'},
                {'name': 'Egg Fried Rice', 'price': '140₹'},
                {'name': 'Paneer Biryani', 'price': '220₹'},
                {'name': 'Prawn Biryani', 'price': '320₹'},
                {'name': 'Schezwan Rice', 'price': '150₹'},
                {'name': 'Veg Fried Rice', 'price': '120₹'}
            ],
            'Beverages': [
                {'name': 'Solkadhi', 'price': '35₹'},
                {'name': 'Lime Water', 'price': '30₹'},
                {'name': 'Lassi', 'price': '20₹'},
                {'name': 'Tea', 'price': '15₹'},
                {'name': 'Cold Coffee', 'price': '60₹'},
                {'name': 'Masala Chai', 'price': '30₹'},
                {'name': 'Butter Milk', 'price': '25₹'},
                {'name': 'Mango Juice', 'price': '45₹'},
                {'name': 'Cold Drink', 'price': '30₹'},
                {'name': 'Milkshake', 'price': '70₹'}
            ]
        },
        'maps_link': 'https://maps.app.goo.gl/FRCwvep8Wid7oZV2A'
    },
    {
        'id': 3,
        'name': 'Hotel Chaturthi Pure Veg Restaurant',
        'city': 'Wai',
        'image': '/static/images/chaturthi.jpg',
        'cuisine_type': 'South Indian, North Indian, Snacks, Beverages',
        'dishes': {
            'South Indian': [
                {'name': 'Vada Sambar', 'price': '50₹'},
                {'name': 'Idli Chutney', 'price': '30₹'},
                {'name': 'Masala Dosa', 'price': '70₹'},
                {'name': 'Onion Uttapam', 'price': '80₹'},
                {'name': 'Medu Vada', 'price': '45₹'},
                {'name': 'Set Dosa', 'price': '85₹'},
                {'name': 'Rava Dosa', 'price': '90₹'},
                {'name': 'Paneer Dosa', 'price': '100₹'},
                {'name': 'Mysore Masala Dosa', 'price': '95₹'},
                {'name': 'Pongal', 'price': '75₹'}
            ],
            'North Indian Veg': [
                {'name': 'Paneer Butter Masala', 'price': '250₹'},
                {'name': 'Dal Tadka', 'price': '120₹'},
                {'name': 'Chole Bhature', 'price': '150₹'},
                {'name': 'Mix Veg', 'price': '210₹'},
                {'name': 'Kadai Paneer', 'price': '260₹'},
                {'name': 'Veg Kofta', 'price': '250₹'},
                {'name': 'Aloo Gobi', 'price': '190₹'},
                {'name': 'Paneer Handi', 'price': '290₹'},
                {'name': 'Jeera Aloo', 'price': '180₹'},
                {'name': 'Dal Makhani', 'price': '200₹'}
            ],
            'Snacks': [
                {'name': 'Misal Pav', 'price': '50₹'},
                {'name': 'Pav Bhaji', 'price': '60₹'},
                {'name': 'Bhel Puri', 'price': '30₹'},
                {'name': 'Dahi Puri', 'price': '35₹'},
                {'name': 'Samosa', 'price': '20₹'},
                {'name': 'Vada Pav', 'price': '15₹'},
                {'name': 'Pani Puri', 'price': '40₹'},
                {'name': 'Sev Puri', 'price': '35₹'},
                {'name': 'Onion Bhaji', 'price': '25₹'},
                {'name': 'Aloo Tikki', 'price': '30₹'}
            ],
            'Beverages': [
                {'name': 'Tea', 'price': '20₹'},
                {'name': 'Coffee', 'price': '40₹'},
                {'name': 'Lassi', 'price': '30₹'},
                {'name': 'Cold Coffee', 'price': '60₹'},
                {'name': 'Butter Milk', 'price': '25₹'},
                {'name': 'Lime Water', 'price': '30₹'},
                {'name': 'Mango Juice', 'price': '45₹'},
                {'name': 'Masala Chai', 'price': '25₹'},
                {'name': 'Milkshake', 'price': '50₹'},
                {'name': 'Cold Drink', 'price': '35₹'}
            ]
        },
        'maps_link': 'https://maps.app.goo.gl/Ak6QSdVJt3iodt3r5'
    },
        {
        'id': 4,
        'name': 'RAJE CHINESE FAMILY RESTAURANT',
        'city': 'Wai',
        'image': '/static/images/raje.jpg',
        'cuisine_type': 'Chinese, Snacks, Beverages',
        'dishes': {
            'Chinese': [
                {'name': 'Veg Hakka Noodles', 'price': '120₹'},
                {'name': 'Chicken Manchurian', 'price': '180₹'},
                {'name': 'Schezwan Fried Rice', 'price': '150₹'},
                {'name': 'Chilli Paneer', 'price': '170₹'},
                {'name': 'Veg Spring Roll', 'price': '140₹'},
                {'name': 'Chicken Lollipop', 'price': '220₹'},
                {'name': 'Prawn Fried Rice', 'price': '230₹'},
                {'name': 'Paneer Chilli', 'price': '160₹'},
                {'name': 'Chicken Hakka Noodles', 'price': '200₹'},
                {'name': 'Fish Chilli', 'price': '260₹'}
            ],
            'Snacks': [
                {'name': 'Pav Bhaji', 'price': '60₹'},
                {'name': 'Samosa', 'price': '20₹'},
                {'name': 'Vada Pav', 'price': '15₹'},
                {'name': 'Onion Bhaji', 'price': '25₹'},
                {'name': 'Chaat', 'price': '40₹'},
                {'name': 'Bhel Puri', 'price': '30₹'}
            ],
            'Beverages': [
                {'name': 'Cold Coffee', 'price': '60₹'},
                {'name': 'Lassi', 'price': '40₹'},
                {'name': 'Tea', 'price': '20₹'},
                {'name': 'Lime Water', 'price': '30₹'},
                {'name': 'Cold Drink', 'price': '30₹'}
            ]
        },
        'maps_link': 'https://maps.app.goo.gl/Ak6QSdVJt3iodt3r5'
    },
    {
        'id': 5,
        'name': 'Hotel Giriraj',
        'city': 'Wai',
        'image': '/static/images/giriraj.jpg',
        'cuisine_type': 'South Indian, North Indian, Snacks, Beverages, Non-Veg',
        'dishes': {
            'South Indian': [
                {'name': 'Idli Sambar', 'price': '50₹'},
                {'name': 'Vada Sambar', 'price': '45₹'},
                {'name': 'Masala Dosa', 'price': '80₹'},
                {'name': 'Onion Uttapam', 'price': '90₹'},
                {'name': 'Medu Vada', 'price': '50₹'},
                {'name': 'Plain Dosa', 'price': '60₹'},
                {'name': 'Rava Masala Dosa', 'price': '95₹'},
                {'name': 'Pongal', 'price': '85₹'}
            ],
            'Snacks': [
                {'name': 'Samosa', 'price': '20₹'},
                {'name': 'Pav Bhaji', 'price': '60₹'},
                {'name': 'Misal Pav', 'price': '50₹'},
                {'name': 'Vada Pav', 'price': '15₹'},
                {'name': 'Onion Bhaji', 'price': '30₹'}
            ],
            'Beverages': [
                {'name': 'Tea', 'price': '20₹'},
                {'name': 'Cold Coffee', 'price': '60₹'},
                {'name': 'Butter Milk', 'price': '30₹'},
                {'name': 'Lassi', 'price': '35₹'},
                {'name': 'Cold Drink', 'price': '40₹'}
            ]
        },
        'maps_link': 'https://maps.app.goo.gl/PZsBKnHuhgbm241e8'
    },
    {
        'id': 6,
        'name': 'Tandoor Express',
        'city': 'Wai',
        'image': '/static/images/tandoorexpress.png',
        'cuisine_type': 'Tandoor, North Indian, South Indian, Chinese, Beverages, Non-Veg',
        'dishes': {
        'Tandoor Specialties': [
                {'name': 'Tandoori Chicken', 'price': '320₹'},
                {'name': 'Paneer Tikka', 'price': '280₹'},
                {'name': 'Chicken Malai Tikka', 'price': '350₹'},
                {'name': 'Fish Tikka', 'price': '370₹'},
                {'name': 'Tandoori Prawns', 'price': '400₹'},
                {'name': 'Tandoori Roti', 'price': '20₹'},
                {'name': 'Butter Naan', 'price': '50₹'},
                {'name': 'Garlic Naan', 'price': '60₹'},
                {'name': 'Seekh Kebab', 'price': '290₹'},
                {'name': 'Tandoori Mushroom', 'price': '260₹'}
            ],
            'North Indian Veg': [
                {'name': 'Paneer Butter Masala', 'price': '250₹'},
                {'name': 'Dal Makhani', 'price': '220₹'},
                {'name': 'Aloo Gobi', 'price': '180₹'},
                {'name': 'Kadai Paneer', 'price': '260₹'},
                {'name': 'Mix Veg Curry', 'price': '210₹'},
                {'name': 'Palak Paneer', 'price': '280₹'},
                {'name': 'Chole Bhature', 'price': '150₹'},
                {'name': 'Paneer Lababdar', 'price': '260₹'},
                {'name': 'Veg Jalfrezi', 'price': '220₹'},
                {'name': 'Veg Kofta', 'price': '250₹'}
            ],
            'North Indian Non-Veg': [
                {'name': 'Chicken Tandoori', 'price': '320₹'},
                {'name': 'Butter Chicken', 'price': '340₹'},
                {'name': 'Mutton Rogan Josh', 'price': '380₹'},
                {'name': 'Fish Curry', 'price': '350₹'},
                {'name': 'Chicken Handi', 'price': '300₹'},
                {'name': 'Mutton Biryani', 'price': '350₹'},
                {'name': 'Chicken Biryani', 'price': '280₹'},
                {'name': 'Egg Curry', 'price': '200₹'},
                {'name': 'Prawn Masala', 'price': '390₹'},
                {'name': 'Mutton Korma', 'price': '370₹'}
            ],
            'South Indian': [
                {'name': 'Idli Sambar', 'price': '50₹'},
                {'name': 'Medu Vada', 'price': '40₹'},
                {'name': 'Masala Dosa', 'price': '60₹'},
                {'name': 'Onion Uttapam', 'price': '50₹'},
                {'name': 'Set Dosa', 'price': '85₹'},
                {'name': 'Rava Masala Dosa', 'price': '90₹'},
                {'name': 'Plain Uttapam', 'price': '90₹'},
                {'name': 'Vada Sambar', 'price': '50₹'},
                {'name': 'Plain Dosa', 'price': '60₹'},
                {'name': 'Pesarattu', 'price': '85₹'}
            ],
            'Chinese': [
                {'name': 'Veg Fried Rice', 'price': '120₹'},
                {'name': 'Chicken Fried Rice', 'price': '160₹'},
                {'name': 'Veg Noodles', 'price': '130₹'},
                {'name': 'Chicken Noodles', 'price': '170₹'},
                {'name': 'Paneer Manchurian', 'price': '150₹'},
                {'name': 'Veg Spring Rolls', 'price': '140₹'},
                {'name': 'Chicken Lollipop', 'price': '250₹'},
                {'name': 'Hakka Noodles', 'price': '150₹'},
                {'name': 'Schezwan Rice', 'price': '160₹'},
                {'name': 'Chicken Manchurian', 'price': '180₹'}
            ],
            'Beverages': [
                {'name': 'Tea', 'price': '20₹'},
                {'name': 'Coffee', 'price': '40₹'},
                {'name': 'Butter Milk', 'price': '25₹'},
                {'name': 'Mango Juice', 'price': '45₹'},
                {'name': 'Lassi', 'price': '40₹'},
                {'name': 'Cold Coffee', 'price': '60₹'},
                {'name': 'Masala Chai', 'price': '30₹'},
                {'name': 'Milkshake', 'price': '70₹'},
                {'name': 'Solkadhi', 'price': '35₹'},
                {'name': 'Cold Drinks', 'price': '30₹'}
            ]
        },
        'maps_link': 'https://maps.app.goo.gl/VuC1fqKRAocXmjEg8'
    },
    {
        'id': 7,
        'name': 'Hotel Shelar Mama',
        'city': 'Wai',
        'image': '/static/images/shelar_mama.jpg',
        'cuisine_type': 'North Indian, South Indian, Snacks, Beverages, Non-Veg',
        'dishes': {
        'Veg Thalis': [
                {'name': 'Vegetarian Thali', 'price': '250₹'},
                {'name': 'Paneer Thali', 'price': '270₹'},
                {'name': 'Dal Thali', 'price': '230₹'},
                {'name': 'Sabzi Thali', 'price': '240₹'},
                {'name': 'Mixed Veg Thali', 'price': '260₹'},
                {'name': 'Rajasthani Thali', 'price': '280₹'},
                {'name': 'Punjabi Thali', 'price': '295₹'},
                {'name': 'Rice Thali', 'price': '220₹'},
                {'name': 'Khichdi Thali', 'price': '200₹'},
                {'name': 'Kadhai Paneer Thali', 'price': '290₹'}
            ],
            'Non-Veg Thalis': [
                {'name': 'Mutton Thali', 'price': '400₹'},
                {'name': 'Chicken Thali', 'price': '350₹'},
                {'name': 'Fish Thali', 'price': '300₹'},
                {'name': 'Prawn Thali', 'price': '450₹'},
                {'name': 'Egg Thali', 'price': '220₹'},
                {'name': 'Chicken Biryani Thali', 'price': '300₹'},
                {'name': 'Mutton Biryani Thali', 'price': '400₹'},
                {'name': 'Special Thali (Mix)', 'price': '500₹'},
                {'name': 'Tandoori Chicken Thali', 'price': '360₹'},
                {'name': 'Mutton Rogan Josh Thali', 'price': '420₹'}
            ],
            'South Indian': [
                {'name': 'Idli Sambar', 'price': '50₹'},
                {'name': 'Dosa', 'price': '60₹'},
                {'name': 'Medu Vada', 'price': '40₹'},
                {'name': 'Pongal', 'price': '70₹'},
                {'name': 'Uttapam', 'price': '80₹'},
                {'name': 'Rava Dosa', 'price': '65₹'},
                {'name': 'Set Dosa', 'price': '80₹'},
                {'name': 'Onion Uttapam', 'price': '75₹'},
                {'name': 'Plain Uttapam', 'price': '90₹'},
                {'name': 'Masala Dosa', 'price': '85₹'}
            ],
            'Snacks': [
                {'name': 'Pav Bhaji', 'price': '60₹'},
                {'name': 'Samosa', 'price': '20₹'},
                {'name': 'Vada Pav', 'price': '15₹'},
                {'name': 'Dahi Puri', 'price': '35₹'},
                {'name': 'Bhel Puri', 'price': '30₹'},
                {'name': 'Sev Puri', 'price': '30₹'},
                {'name': 'Onion Bhaji', 'price': '25₹'},
                {'name': 'Puri Bhaji', 'price': '40₹'},
                {'name': 'Chaat', 'price': '45₹'},
                {'name': 'Tikki', 'price': '35₹'}
            ],
            'Starters': [
                {'name': 'Chicken Tikka', 'price': '250₹'},
                {'name': 'Paneer Tikka', 'price': '180₹'},
                {'name': 'Mutton Seekh Kebab', 'price': '290₹'},
                {'name': 'Fish Fry', 'price': '220₹'},
                {'name': 'Veg Manchurian', 'price': '180₹'},
                {'name': 'Hara Bhara Kebab', 'price': '150₹'},
                {'name': 'Tandoori Chicken', 'price': '300₹'},
                {'name': 'Chicken Seekh Kebab', 'price': '270₹'},
                {'name': 'Prawn Masala', 'price': '320₹'},
                {'name': 'Tandoori Prawns', 'price': '350₹'}
            ],
            'Bread': [
                {'name': 'Roti', 'price': '10₹'},
                {'name': 'Chapati', 'price': '10₹'},
                {'name': 'Tandoori Roti', 'price': '20₹'},
                {'name': 'Naan', 'price': '40₹'},
                {'name': 'Butter Naan', 'price': '50₹'},
                {'name': 'Garlic Naan', 'price': '60₹'},
                {'name': 'Stuffed Kulcha', 'price': '70₹'},
                {'name': 'Aloo Paratha', 'price': '50₹'},
                {'name': 'Paneer Paratha', 'price': '80₹'},
                {'name': 'Lachha Paratha', 'price': '60₹'}
            ],
            'Rice': [
                {'name': 'Jeera Rice', 'price': '70₹'},
                {'name': 'Plain Rice', 'price': '50₹'},
                {'name': 'Veg Pulao', 'price': '120₹'},
                {'name': 'Chicken Biryani', 'price': '240₹'},
                {'name': 'Mutton Biryani', 'price': '400₹'},
                {'name': 'Egg Fried Rice', 'price': '140₹'},
                {'name': 'Paneer Biryani', 'price': '220₹'},
                {'name': 'Prawn Biryani', 'price': '350₹'},
                {'name': 'Schezwan Rice', 'price': '150₹'},
                {'name': 'Veg Fried Rice', 'price': '120₹'}
            ],
            'Beverages': [
                {'name': 'Tea', 'price': '20₹'},
                {'name': 'Coffee', 'price': '40₹'},
                {'name': 'Butter Milk', 'price': '25₹'},
                {'name': 'Mango Juice', 'price': '45₹'},
                {'name': 'Solkadhi', 'price': '35₹'},
                {'name': 'Lime Water', 'price': '30₹'},
                {'name': 'Lassi', 'price': '40₹'},
                {'name': 'Cold Coffee', 'price': '60₹'},
                {'name': 'Masala Chai', 'price': '30₹'},
                {'name': 'Milkshake', 'price': '70₹'}
            ]
        },
        'maps_link': 'https://maps.app.goo.gl/eRniJemdnUgbvS387'
    },    
    {
        'id': 8,
        'name': 'Hotel Pearl',
        'city': 'Wai',
        'image': '/static/images/hotel_pearl.jpg',
        'cuisine_type': 'North Indian, South Indian, Chinese, Beverages, Snacks',
        'dishes': {
        'North Indian Veg': [
                {'name': 'Paneer Butter Masala', 'price': '250₹'},
                {'name': 'Dal Makhani', 'price': '220₹'},
                {'name': 'Aloo Gobi', 'price': '180₹'},
                {'name': 'Chole Bhature', 'price': '150₹'},
                {'name': 'Veg Biryani', 'price': '200₹'},
                {'name': 'Mix Veg Curry', 'price': '210₹'},
                {'name': 'Palak Paneer', 'price': '240₹'},
                {'name': 'Baingan Bharta', 'price': '200₹'},
                {'name': 'Kadai Paneer', 'price': '260₹'},
                {'name': 'Veg Thali', 'price': '295₹'}
            ],
            'North Indian Non-Veg': [
                {'name': 'Butter Chicken', 'price': '320₹'},
                {'name': 'Mutton Rogan Josh', 'price': '350₹'},
                {'name': 'Chicken Tikka Masala', 'price': '300₹'},
                {'name': 'Fish Curry', 'price': '290₹'},
                {'name': 'Egg Curry', 'price': '180₹'},
                {'name': 'Mutton Biryani', 'price': '400₹'},
                {'name': 'Chicken Biryani', 'price': '240₹'},
                {'name': 'Tandoori Chicken', 'price': '350₹'},
                {'name': 'Chicken Handi', 'price': '280₹'},
                {'name': 'Prawn Masala', 'price': '320₹'}
            ],
            'South Indian': [
                {'name': 'Idli Sambar', 'price': '50₹'},
                {'name': 'Dosa', 'price': '60₹'},
                {'name': 'Medu Vada', 'price': '40₹'},
                {'name': 'Rava Dosa', 'price': '65₹'},
                {'name': 'Uttapam', 'price': '80₹'},
                {'name': 'Pongal', 'price': '70₹'},
                {'name': 'Set Dosa', 'price': '80₹'},
                {'name': 'Plain Dosa', 'price': '60₹'},
                {'name': 'Masala Dosa', 'price': '85₹'},
                {'name': 'Onion Uttapam', 'price': '75₹'}
            ],
            'Chinese': [
                {'name': 'Veg Fried Rice', 'price': '120₹'},
                {'name': 'Chicken Fried Rice', 'price': '140₹'},
                {'name': 'Veg Manchurian', 'price': '180₹'},
                {'name': 'Chili Chicken', 'price': '250₹'},
                {'name': 'Paneer Chilli', 'price': '220₹'},
                {'name': 'Hakka Noodles', 'price': '130₹'},
                {'name': 'Chowmein', 'price': '140₹'},
                {'name': 'Veg Spring Rolls', 'price': '90₹'},
                {'name': 'Egg Fried Rice', 'price': '140₹'},
                {'name': 'Prawn Fried Rice', 'price': '320₹'}
            ],
            'Snacks': [
                {'name': 'Pav Bhaji', 'price': '60₹'},
                {'name': 'Samosa', 'price': '20₹'},
                {'name': 'Vada Pav', 'price': '15₹'},
                {'name': 'Dahi Puri', 'price': '35₹'},
                {'name': 'Bhel Puri', 'price': '30₹'},
                {'name': 'Sev Puri', 'price': '30₹'},
                {'name': 'Onion Bhaji', 'price': '25₹'},
                {'name': 'Tikki', 'price': '35₹'},
                {'name': 'Chaat', 'price': '45₹'},
                {'name': 'Misal Pav', 'price': '50₹'}
            ],
            'Beverages': [
                {'name': 'Tea', 'price': '20₹'},
                {'name': 'Coffee', 'price': '40₹'},
                {'name': 'Butter Milk', 'price': '25₹'},
                {'name': 'Mango Juice', 'price': '45₹'},
                {'name': 'Solkadhi', 'price': '35₹'},
                {'name': 'Lime Water', 'price': '30₹'},
                {'name': 'Lassi', 'price': '40₹'},
                {'name': 'Cold Coffee', 'price': '60₹'},
                {'name': 'Masala Chai', 'price': '30₹'},
                {'name': 'Milkshake', 'price': '70₹'}
            ]
        },
        'maps_link': 'https://maps.app.goo.gl/eFSJFNVVrfH5qbU9A'
    },
    {
        'id': 8,
        'name': 'Hotel Milan Family Restaurant',
        'city': 'Wai',
        'image': '/static/images/milan.jpg',
        'cuisine_type': 'North Indian, South Indian, Chinese, Beverages, Snacks',
        'dishes': {
        'North Indian Veg': [
                {'name': 'Paneer Butter Masala', 'price': '250₹'},
                {'name': 'Dal Makhani', 'price': '220₹'},
                {'name': 'Aloo Gobi', 'price': '180₹'},
                {'name': 'Chole Bhature', 'price': '150₹'},
                {'name': 'Veg Biryani', 'price': '200₹'},
                {'name': 'Mix Veg Curry', 'price': '210₹'},
                {'name': 'Palak Paneer', 'price': '240₹'},
                {'name': 'Baingan Bharta', 'price': '200₹'},
                {'name': 'Kadai Paneer', 'price': '260₹'},
                {'name': 'Veg Thali', 'price': '295₹'}
            ],
            'North Indian Non-Veg': [
                {'name': 'Butter Chicken', 'price': '320₹'},
                {'name': 'Mutton Rogan Josh', 'price': '350₹'},
                {'name': 'Chicken Tikka Masala', 'price': '300₹'},
                {'name': 'Fish Curry', 'price': '290₹'},
                {'name': 'Egg Curry', 'price': '180₹'},
                {'name': 'Mutton Biryani', 'price': '400₹'},
                {'name': 'Chicken Biryani', 'price': '240₹'},
                {'name': 'Tandoori Chicken', 'price': '350₹'},
                {'name': 'Chicken Handi', 'price': '280₹'},
                {'name': 'Prawn Masala', 'price': '320₹'}
            ],
            'South Indian': [
                {'name': 'Idli Sambar', 'price': '50₹'},
                {'name': 'Dosa', 'price': '60₹'},
                {'name': 'Medu Vada', 'price': '40₹'},
                {'name': 'Rava Dosa', 'price': '65₹'},
                {'name': 'Uttapam', 'price': '80₹'},
                {'name': 'Pongal', 'price': '70₹'},
                {'name': 'Set Dosa', 'price': '80₹'},
                {'name': 'Plain Dosa', 'price': '60₹'},
                {'name': 'Masala Dosa', 'price': '85₹'},
                {'name': 'Onion Uttapam', 'price': '75₹'}
            ],
            'Chinese': [
                {'name': 'Veg Fried Rice', 'price': '120₹'},
                {'name': 'Veg Manchurian', 'price': '180₹'},
                {'name': 'Chili Chicken', 'price': '250₹'},
                {'name': 'Paneer Chilli', 'price': '220₹'},
                {'name': 'Hakka Noodles', 'price': '130₹'},
                {'name': 'Chowmein', 'price': '140₹'},
                {'name': 'Veg Spring Rolls', 'price': '90₹'},

            ],
            'Snacks': [
                {'name': 'Pav Bhaji', 'price': '60₹'},
                {'name': 'Samosa', 'price': '20₹'},
                {'name': 'Vada Pav', 'price': '15₹'},
                {'name': 'Dahi Puri', 'price': '35₹'},
                {'name': 'Bhel Puri', 'price': '30₹'},
                {'name': 'Sev Puri', 'price': '30₹'},
                {'name': 'Onion Bhaji', 'price': '25₹'},
                {'name': 'Tikki', 'price': '35₹'},
                {'name': 'Chaat', 'price': '45₹'},
                {'name': 'Misal Pav', 'price': '50₹'}
            ],
            'Beverages': [
                {'name': 'Tea', 'price': '20₹'},
                {'name': 'Coffee', 'price': '40₹'},
                {'name': 'Butter Milk', 'price': '25₹'},
                {'name': 'Mango Juice', 'price': '45₹'},
                {'name': 'Solkadhi', 'price': '35₹'},
                {'name': 'Lime Water', 'price': '30₹'},
                {'name': 'Lassi', 'price': '40₹'},
                {'name': 'Cold Coffee', 'price': '60₹'},
                {'name': 'Masala Chai', 'price': '30₹'},
                {'name': 'Milkshake', 'price': '70₹'}
            ]
        },
        'maps_link': 'https://maps.app.goo.gl/naEdn5RRHNtsbRuT7'
    },
]

# Helper function to retrieve hotel by ID
def get_hotel_by_id(hotel_id):
    return next((hotel for hotel in hotels if hotel['id'] == hotel_id), None)

# Helper function to retrieve restaurant by ID
def get_restaurant_by_id(restaurant_id):
    return next((restaurant for restaurant in restaurants if restaurant['id'] == restaurant_id), None)

@app.route('/')
def home():
    return render_template('index.html')

# Hotel routes
@app.route('/search_hotels', methods=['GET'])
def search_hotels():
    price_range = request.args.get('price_range', 'any')
    # Filtering logic based on price_range can be added here if needed
    return render_template('search_hotels.html', hotels=hotels)

@app.route('/hotel/<int:hotel_id>')
def hotel_details(hotel_id):
    hotel = get_hotel_by_id(hotel_id)
    if hotel:
        return render_template('hotel_details.html', hotel=hotel)
    else:
        return "Hotel not found", 404

# Restaurant routes
@app.route('/search_restaurants', methods=['GET'])
def search_restaurants():
    price_range = request.args.get('price_range', 'any')
    # Filtering logic based on price_range can be added here if needed
    return render_template('search_restaurants.html', restaurants=restaurants)

@app.route('/restaurant_details/<int:restaurant_id>')
def restaurant_details(restaurant_id):
    restaurant = get_restaurant_by_id(restaurant_id)
    if restaurant:
        return render_template('restaurant_details.html', restaurant=restaurant)
    else:
        return "Restaurant not found", 404

# About page route
@app.route('/about')
def about():
    return render_template('about.html')
    
if __name__ == '__main__':
    app.run(debug=True)
