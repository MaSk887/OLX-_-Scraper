
---

# 🏠 Real Estate Scraper (Owner Finder V11 - Pro Edition)

An advanced, multi-threaded logic automation tool designed to dominate the **Dubizzle Egypt (formerly OLX)** real estate market. This Pro version doesn't just find ads; it deep-scans listings to identify **direct owners** and calculates key investment metrics automatically.

---

## 🚀 Pro Features & Enhancements

### 1. **Advanced Data Extraction**

The scraper now extracts detailed property specifications directly from the listing cards:

* **Bedrooms & Bathrooms**: Automatically parses "غرف" and "حمام".
* **Property Area**: Captures the exact "مساحة" in square meters.
* **Smart Calculation**: Automatically calculates the **Price per Meter (سعر المتر)** to help you identify the best deals.

### 2. **Deep Owner Verification Logic**

The script goes beyond the surface. It visits each individual ad URL and performs a full-text scan for the "Private User" (**مستخدم خاص**) tag, effectively filtering out brokers, offices, and companies.

### 3. **Intelligent Freshness Filter**

Using a custom Arabic date interpreter in `Help_Fun.py`, the script converts relative dates (e.g., "منذ ساعة", "أمس") into logical data. It only processes ads within your defined `MAX_DAYS` window to save time and resources.

### 4. **Elite Anti-Ban System**

* **Cloudscraper Integration**: Bypasses modern bot detection mechanisms.
* **Dynamic Header Rotation**: Uses a diversified `HEADERS_LIST` with different browsers (Chrome, Firefox, Edge) and platforms (Windows, Mac, Linux) to avoid footprinting.
* **Safety Delays**: Implements `safe_delay()` with randomized intervals to mimic natural human browsing patterns.

---

## 🛠️ Technical Architecture

* **`main_scr.py`**: The central controller. Orchestrates the scraping flow and sorts results by **Price per Meter** before saving.
* **`Pre.py`**: The engine's heart. Contains the global settings, comprehensive area dictionary (Slugs), and the rotating header pool.
* **`SCR_Fun.py`**: The heavy lifter. Handles multi-page navigation, data parsing, and individual ad deep-scans.
* **`Saving_method.py`**: A dedicated UI-for-Excel module. Creates professional reports with frozen panes, blue-themed headers, and auto-filters.
* **`Help_Fun.py`**: The logic toolkit. Contains the owner verification and date validation algorithms.

---

## 📍 Usage & Customization

### Selecting Your Targets

1. Open `Pre.py`.
2. Add your desired locations to `SELECTED_AREAS` using the Arabic keys from the `ALL_AREAS` dictionary.
3. Set `MAX_DAYS` to determine how far back you want to search.

### Adding New Areas

To add a new neighborhood:

1. Find the area on Dubizzle and copy its **Slug** from the URL (e.g., `.../nasr-city/`).
2. Map it in `ALL_AREAS` as: `"Arabic Name": "slug"`.

---

## ⚙️ Installation

```bash
pip install cloudscraper beautifulsoup4 openpyxl

```

---

## 📊 Comprehensive Output

The generated Excel file in the `/results` folder includes:

* **Area & Title**: Full property identification.
* **Pricing**: Total Price + **Price per Meter** (Calculated).
* **Specs**: Rooms, Bathrooms, and Area.
* **Verification**: Owner Status (True/False) + Direct Ad Link.

---

## ⚠️ Disclaimer

This tool is for educational purposes. Use responsibly by maintaining the default delay settings to respect Dubizzle's infrastructure.

---

**نصيحة إضافية للينكد إن:**
