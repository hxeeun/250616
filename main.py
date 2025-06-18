import streamlit as st
import random

# 국내/해외 노래 추천 데이터
song_recommendations = {
    "국내": {
        "R&B": [
            ("시간을 돌려서", "백예린"),
            ("그냥 안아달란 말야", "크러쉬"),
            ("밤이 깊었네", "아이유"),
            ("Love", "딘 (DEAN)"),
            ("Hug Me", "정준일, 장재인"),
        ],
        "발라드": [
            ("그때 그 아인", "임영웅"),
            ("밤이 깊었네", "아이유"),
            ("취중고백", "김민석 (멜로망스)"),
            ("너를 만나", "폴킴"),
            ("그대라는 사치", "임창정"),
        ],
        "댄스": [
            ("Pink Venom", "BLACKPINK"),
            ("롤린 (Rollin')", "브레이브걸스"),
            ("Next Level", "aespa"),
            ("Hype Boy", "NewJeans"),
            ("Love Dive", "IVE"),
        ],
        "힙합": [
            ("VVS", "MIRANI, Munchman, Khundi Panda, JUSTHIS"),
            ("회전목마", "릴보이, 원슈타인, 죠지"),
            ("GANADARA", "박재범"),
            ("깡", "비"),
            ("한강에서", "릴러말즈"),
        ],
        "인디": [
            ("밤하늘의 별을", "양정승"),
            ("고백", "10cm"),
            ("끝이 없는 밤", "새소년"),
            ("스물다섯, 스물하나", "자우림"),
            ("너무 보고 싶어", "적재"),
        ],
    },
    "해외": {
        "R&B": [
            ("Ecstasy", "Ciara"),
            ("Offa Me", "Davido feat. Victoria Monét"),
            ("Bliss", "Tyla"),
            ("Call Out My Name", "The Weeknd"),
            ("Come Through", "H.E.R feat. Chris Brown"),
        ],
        "발라드": [
            ("All of Me", "John Legend"),
            ("Someone Like You", "Adele"),
            ("When We Were Young", "Adele"),
            ("Let Her Go", "Passenger"),
            ("Say You Won't Let Go", "James Arthur"),
        ],
        "댄스": [
            ("I'm Good (Blue)", "David Guetta & Bebe Rexha"),
            ("Stay", "The Kid LAROI, Justin Bieber"),
            ("Levitating", "Dua Lipa"),
            ("Titanium", "David Guetta ft. Sia"),
            ("One Kiss", "Calvin Harris & Dua Lipa"),
        ],
        "힙합": [
            ("Sicko Mode", "Travis Scott"),
            ("Super Freaky Girl", "Nicki Minaj"),
            ("First Class", "Jack Harlow"),
            ("God's Plan", "Drake"),
            ("Money Trees", "Kendrick Lamar"),
        ],
        "인디": [
            ("Skinny Love", "Bon Iver"),
            ("Holocene", "Bon Iver"),
            ("Youth", "Daughter"),
            ("Rivers and Roads", "The Head and the Heart"),
            ("Shark Attack", "Grouplove"),
        ],
    }
}

st.title("🎵 장르별 노래 추천")
st.write("지역과 장르를 선택한 뒤, 버튼을 눌러보세요!")

# 지역 선택
region = st.radio("지역을 선택하세요:", ("국내", "해외"))

# 장르 선택
genre = st.selectbox("장르를 선택하세요:", list(song_recommendations[region].keys()))

# 추천 버튼
if st.button("추천 받기 🎁"):
    st.subheader(f"🎧 {region} {genre} 추천 노래")

    songs = song_recommendations[region].get(genre, [])
    if len(songs) < 3:
        st.warning("추천 곡이 3곡 미만입니다.")
    else:
        recommended = random.sample(songs, 3)  # 무작위 3곡 선택
        for title, artist in recommended:
            st.markdown(f"- **{title}** - *{artist}*")
