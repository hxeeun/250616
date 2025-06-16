import streamlit as st

# 2025년 상반기 최신곡 기반 노래 추천 데이터
song_recommendations = {
    "R&B": [
        ("Ecstasy", "Ciara"),
        ("Offa Me", "Davido feat. Victoria Monét"),
        ("Bliss", "Tyla"),
    ],
    "발라드": [
        ("그때 그 아인", "임영웅"),
        ("밤이 깊었네", "아이유"),
    ],
    "POP": [
        ("Flowers", "Miley Cyrus"),
        ("Anti-Hero", "Taylor Swift"),
        ("Calm Down", "Rema & Selena Gomez"),
    ],
    "댄스": [
        ("Pink Venom", "BLACKPINK"),
        ("I'm Good (Blue)", "David Guetta & Bebe Rexha"),
    ],
    "힙합": [
        ("Sicko Mode", "Travis Scott"),
        ("VVS", "MIRANI, Munchman, Khundi Panda, JUSTHIS"),
    ],
    "인디": [
        ("밤하늘의 별을", "양정승"),
        ("고백", "10cm"),
    ],
}

st.title("🎵 2025 최신곡 장르별 노래 추천")
st.write("원하는 장르를 선택한 뒤, 버튼을 눌러보세요!")

# 장르 선택 박스
genre = st.selectbox("장르를 선택하세요:", list(song_recommendations.keys()))

# 추천 버튼
if st.button("추천 받기 🎁"):
    st.subheader(f"🎧 {genre} 추천 노래")
    for title, artist in song_recommendations[genre]:
        st.markdown(f"- **{title}** - *{artist}*")
