import folium
import webbrowser

def showMap():
    # تعیین مختصات مرکز نقشه
    coords = [36.215541697449346, 57.68560291832583]
    
    # سطح بزرگنمایی اولیه نقشه
    zoom_start = 5
    
    # ایجاد نقشه جدید با استفاده از Folium
    my_map = folium.Map(location=coords, zoom_start=zoom_start)

    # ذخیره نقشه به عنوان یک فایل HTML
    my_map.save("map.html")
    
    # باز کردن فایل HTML در مرورگر وب
    webbrowser.open("map.html")
