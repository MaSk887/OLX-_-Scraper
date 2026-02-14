from bs4 import BeautifulSoup

from Pre import *
from Help_Fun import *

def scrape_area(area_name):
    slug = ALL_AREAS.get(area_name)

    if not slug:
        print(f" المنطقة {area_name} مش موجودة في القاموس ")
        return []

    results = []

    for page in range(1, PAGES_PER_AREA + 1):

        if page == 1:
            url = f"https://www.dubizzle.com.eg/properties/apartments-duplex-{PROPERTY_TYPE}/{slug}/"
        else:
            url = f"https://www.dubizzle.com.eg/properties/apartments-duplex-{PROPERTY_TYPE}/{slug}?page={page}"

        print(f"\n صفحة {page} من {PAGES_PER_AREA} - {area_name}")
        print(f"🔗 {url}")

        HEADER = random.choice(HEADERS_LIST)
        try:
            resp = scraper.get(url, headers= HEADER, timeout=30)
        except Exception as e:
            print(f" error in connection {e} \n")
            safe_delay()
            continue

        if resp.status_code != 200:
            print(f" error in connection {resp.status_code} \n")
            safe_delay()
            continue

        if "Fingerprint" in resp.text or "fingerprint" in resp.text :
            print(f" we are fucked (BAN) ")
            safe_delay()
            continue

        print(f" Pro you are super  \n")

        soup = BeautifulSoup(resp.text, "html.parser")
        ads = soup.find_all("li", attrs={"aria-label": "Listing"})

        if not ads:
            print(f" no ads \n")
            safe_delay()
            continue

        print(f" We got {len(ads)} ads \n")

        for ad in ads:
            try:
                date_tag = ad.find("span", attrs={"aria-label": "Creation date"})
                if not date_tag:
                    date_tag = ad.find("span", class_="date")
                date_text = date_tag.text.strip() if date_tag else ""

                if date_text and not is_recent(date_text):
                    continue

                title_tag = ad.find("h2") or ad.find("span", class_="title")
                title = title_tag.text.strip() if title_tag else "بدون عنوان"


                price_tag = ad.find("div", attrs={"aria-label":"Price"}).text.strip()
                price = int(''.join(c for c in price_tag if c.isdigit()))

                beds_tag = ad.find("span", attrs={"aria-label": "Beds"}).text.strip()
                beds = int(''.join(c for c in beds_tag if c.isdigit()))

                baths_tag = ad.find("span", attrs={"aria-label": "Bathrooms"}).text.strip()
                baths = int(''.join(c for c in baths_tag if c.isdigit()))

                area_tag = ad.find("span", attrs={"aria-label": "Area"}).text.strip()
                area = int(''.join(c for c in area_tag if c.isdigit()))

                link_tag = ad.find("a", href=True)
                link = "https://www.dubizzle.com.eg" + link_tag.get("href")

                header2 = random.choice(HEADERS_LIST)
                resp2 = scraper.get(link, headers= header2, timeout=30)
                soup2 = BeautifulSoup(resp2.text, "html.parser")


                full_text = soup2.get_text()

                owner_status = is_owner(full_text)

                results.append({
                    "المنطقة": area_name,
                    "العنوان": title,
                    "السعر": price,
                    "التاريخ": date_text,
                    "غرف": beds,
                    "حمام": baths,
                    "مساحة": area,
                    "سعر المتر": int(price/area) ,
                    "الرابط": link,
                    "مالك": owner_status,
                })
                sleep(random.uniform(1, 3))

            except Exception as e:
                print(f" error in ad {e} \n")
                sleep(random.uniform(1, 3))
                continue

        safe_delay()

    print(f" {len(results)} ad  in {area_name} \n")
    return results
