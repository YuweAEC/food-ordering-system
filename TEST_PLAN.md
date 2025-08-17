# Test Plan - Food Ordering System

This document helps verify that the system works correctly (Phase 1).

---

## 1. Server Setup
- [ ] Run `python manage.py runserver`
- [ ] Visit `http://127.0.0.1:8000/`
- [ ] Homepage loads without errors

---

## 2. User Authentication
- [ ] Register a new user at `/register/`
- [ ] Redirects to `/login/`
- [ ] Login with new account → redirects to `/`
- [ ] Profile page shows correct details
- [ ] Logout works and redirects to `/`

---

## 3. Menu & Food Items
- [ ] Login to `/admin/` as superuser
- [ ] Add category and food item
- [ ] Food item appears on homepage

---

## 4. Cart
- [ ] Add item to cart from homepage
- [ ] `/cart/` shows item with correct quantity, price, and total

---

## 5. Checkout & Orders
- [ ] From `/cart/`, proceed to checkout
- [ ] Place order
- [ ] Redirects to `/order-history/`

---

## 6. Order History
- [ ] `/order-history/` shows recent order with status "Pending"
- [ ] Update order status in `/admin/`
- [ ] `/order-history/` shows updated status

---

## 7. UI & Redirects
- [ ] Navbar links (Home, Cart, Profile, Orders) work correctly
- [ ] Unauthorized users get redirected to `/login/` when trying to access protected pages
- [ ] Authenticated users can access cart and profile
