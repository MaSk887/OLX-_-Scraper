from SCR_Fun import *
from Saving_method import *

if __name__ == "__main__":
    print("=" * 50)
    print("🏠 صياد الملاك V11")
    print("=" * 50)
    print(f"📍 المناطق: {len(SELECTED_AREAS)} منطقة")
    print(f"📄 الصفحات: {PAGES_PER_AREA} لكل منطقة")
    print(f"📅 آخر {MAX_DAYS} يوم")
    print("=" * 50)

    all_results = []

    for area in SELECTED_AREAS:
        area_results_ = scrape_area(area)
        all_results += area_results_

        all_results.sort(key= lambda x : x["سعر المتر"])

        save_to_excel(all_results, area)
        print(f" done {len(all_results)} ads from {area} ")



