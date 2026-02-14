
PROPERTY_TYPE = "for-sale"  # or for-rent

PAGES_PER_AREA = 1

MAX_DAYS = 3

DELAY_MIN = 5
DELAY_MAX = 10

SELECTED_AREAS = [
    "مدينة نصر",  # area/areas
]










import cloudscraper

ALL_AREAS = {
    # --- القاهرة (Cairo) ---
    "التجمع الخامس": "new-cairo-city-5th-settlement",
    "مدينتي": "madinaty",
    "مدينة نصر": "nasr-city",
    "مصر الجديدة": "heliopolis",
    "المعادي": "maadi",
    "الشروق": "al-shorouk",
    "وسط البلد": "downtown-cairo",
    "شبرا": "shubra",
    "الزمالك": "zamalek",
    "جاردن سيتي": "garden-city",
    "حلوان": "helwan",
    "المقطم": "mokattam",
    "العبورية": "obour-city",
    "عين شمس": "ain-shams",
    "المرج": "el-marg",

    # --- الجيزة (Giza) ---
    "الشيخ زايد": "sheikh-zayed",
    "6 أكتوبر": "6th-of-october",
    "الهرم": "haram",
    "فيصل": "faisal",
    "حدائق الأهرام": "hadayek-al-ahram",
    "المهندسين": "mohandessin",
    "الدقي": "dokki",
    "العجوزة": "agouza",
    "إمبابة": "imbaba",
    "بحر الأعظم": "bahr-el-aazam",
    "العمرانية": "omraneya",
    "بولاق الدكرور": "bulaq-el-dakror",
    "حدائق أكتوبر": "hadayek-october",
    "المنيب": "el-muneeb",
    "الوراق": "warraq",
}



scraper = cloudscraper.create_scraper(
    browser={
        'browser': 'chrome',
        'platform': 'windows',
        'mobile': False
    }
)



HEADERS_LIST = [
    {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
        "Referer": "https://www.google.com/",
    },
    {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "en-GB,en;q=0.7,ar;q=0.3",
        "Referer": "https://www.google.com.eg/",
    },
    {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "ar,en-US;q=0.9,en;q=0.8",
        "Referer": "https://www.bing.com/",
    },
    {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9,ar-EG;q=0.8",
        "Referer": "https://www.google.com/",
    },
    {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "ar-EG,ar;q=0.9,en;q=0.8",
        "Referer": "https://www.yahoo.com/",
    },
]









