import requests
import pandas as pd
from utils import get_timestamp

def fetch_poi(city, keyword, key, limit=50):
    result = []
    page = 1
    while len(result) < limit:
        url = f'https://restapi.amap.com/v3/place/text?city={city}&keywords={keyword}&output=json&page={page}&offset=20&key={key}'
        res = requests.get(url).json()
        pois = res.get('pois', [])
        if not pois:
            break
        for p in pois:
            result.append({
                '商家名称': p.get('name'),
                '地址': p.get('address'),
                '联系电话': p.get('tel'),
                '门店图片': p.get('photos')[0]['url'] if p.get('photos') else '',
                '创建时间': get_timestamp(),
                '修改时间': get_timestamp()
            })
            if len(result) >= limit:
                break
        page += 1
    return pd.DataFrame(result)
