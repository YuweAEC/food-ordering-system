# Food Ordering System

A web-based food ordering system built with Django. This project allows users to browse food items, add them to cart, place orders, manage wishlists, apply coupons, and track order history.

## Features

- User registration and login
- Menu browsing
- Add to cart and manage cart
- Wishlist functionality
- Apply discount coupons
- Checkout and place orders
- Order history and tracking
- User profile management
- Admin interface to manage food items, coupons, and orders
- REST API integration for selected modules

## Tech Stack

- **Backend**: Django 5.x, Django REST Framework
- **Frontend**: Django Templates, Bootstrap 5, Crispy Forms
- **Database**: SQLite (can be replaced with MySQL/PostgreSQL)
- **Others**: AJAX (for cart/wishlist updates), DRF for APIs

## Notes

- Wishlist and cart updates use AJAX for better user experience.
- Coupon codes reduce the final price during checkout.
- APIs can be tested via tools like Postman or directly from browser routes (e.g., `/api/food-items/`).
