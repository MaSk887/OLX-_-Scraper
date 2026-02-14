import cloudscraper
from bs4 import BeautifulSoup
from time import sleep

scraper = cloudscraper.create_scraper(
    browser={
        'browser': 'chrome',
        'platform': 'windows',
        'mobile': False
    }
)

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
}

url = "https://www.dubizzle.com.eg/properties/apartments-duplex-for-sale/haram/"
resp = scraper.get(url, headers=HEADERS, timeout=30)
soup = BeautifulSoup(resp.text, "html.parser")
ads = soup.find_all("li", attrs={"aria-label": "Listing"})

# أول 3 إعلانات
for i in range(3):
    ad = ads[i]
    link_tag = ad.find("a", href=True)
    ad_link = "https://www.dubizzle.com.eg" + link_tag.get("href")

    sleep(3)
    resp2 = scraper.get(ad_link, headers=HEADERS, timeout=30)
    soup2 = BeautifulSoup(resp2.text, "html.parser")
    full_text = soup2.get_text()

    print(f"\n{'=' * 50}")
    print(f"Ad {i + 1}: {ad_link}")

    if "مستخدم خاص" in full_text:
        print("✅ مالك (مستخدم خاص)")
    else:
        print("❌ مش مالك")

    # نشوف الكلمات الموجودة
    keywords = ["مستخدم خاص", "شركة", "سمسار", "وسيط", "مكتب", "مالك"]
    for word in keywords:
        if word in full_text:
            print(f"   لقيت: {word}")

    print(f"{'=' * 50}")