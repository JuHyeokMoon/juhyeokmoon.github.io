import pandas as pd
import folium
import webbrowser
import chardet
import json

state_path = 'test/GOS/etc/최종 좌표파일/CTPRVN_wgs84.json'
state_geo = json.load(open(state_path, encoding='utf-8'))

state_unemployment = 'test/GOS/etc/Total_People_2020_6.csv'

state_data = pd.read_csv(state_unemployment, encoding='EUC-KR')
#astype - Code는 문자열로 Population(숫자같은것)은 실수형으로 데이터 타입을 바꿈
state_data = state_data.astype({'Code': 'str', 'Population': 'float'})
print(state_data.dtypes)        #dtypes pandas에서 데이터 타입 찍어보는 

# for row in state_data :


m = folium.Map(location=[36, 127], tiles="OpenStreetMap", zoom_start=7)     #location은 위도 경도 38선 위치와 127은 시간상 위치, titles은 지도 스타일 변경
# folium.Map(location=[37.566345, 126.977893], zoom_start=17, tiles='Stamen Terrain')
# folium.Map(location=[37.566345, 126.977893], zoom_start=17, tiles='Stamen Toner')

# folium.Marker([37.566345, 126.977893], popup='서울특별시청').add_to(map_osm)      #마커 찍는법 add_to(띄울 지도)
# folium.Marker([37.5658859, 126.9754788], popup='덕수궁').add_to(map_osm)

# folium.Marker([37.566345, 126.977893], popup='서울특별시청', icon=folium.Icon(color='red',icon='info-sign')).add_to(map_osm)
# folium.CircleMarker([37.5658859, 126.9754788], radius=100,color='#3186cc',fill_color='#3186cc', popup='덕수궁').add_to(map_osm)

m.choropleth(       #map join
    geo_data=state_geo,                     #json 파일 입력
    name='choropleth',                      
    data=state_data,                        #csv로 저장했던 데이터
    columns=['Code', 'Population'],         #중요! 위 데이터에서 컬럼 값이 뭔지 설정, 첫번째값 Code와 CTPRVN_CD 매치
    key_on='feature.properties.CTPRVN_CD',  #중요! 전혀 다른데이터에서 관계를 찾아 설정(디버깅해서 따라가면 CTPRVN_CD 확인)
    fill_color='PuRd',                          # -> 이것이 극화된 DB가 RDBMS 
    fill_opacity=0.7,
    line_opacity=0.5,
    legend_name='Population Rate (%)'
)

folium.LayerControl().add_to(m)

m.save('folium_kr.html')
webbrowser.open_new("folium_kr.html")
