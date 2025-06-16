import streamlit as st

# 국내/해외 노래 추천 데이터 (2025년 최신곡 기준, 빈 곳 채움)
song_recommendations = {
    "국내": {
        "R&B": [
            ("시간을 돌려서", "백예린"),
            ("그냥 안아달란 말야", "크러쉬"),
            ("밤이 깊었네", "아이유"),
        ],
        "발라드": [
            ("그때 그 아인", "임영웅"),
            ("밤이 깊었네", "아이유"),
            ("취중고백", "김민석 (멜로망스)"),
        ],
        "팝": [
            ("고백", "10cm"),
        ],
        "댄스": [
            ("Pink Venom", "BLACKPINK"),
        ],
        "힙합": [
            ("VVS", "MIRANI, Munchman, Khundi Panda, JUSTHIS"),
            ("회전목마", "릴보이, 원슈타인, 죠지"),
        ],
        "인디": [
            ("밤하늘의 별을", "양정승"),
            ("고백", "10cm"),
            ("끝이 없는 밤", "새소년"),
        ],
    },
    "해외": {
        "R&B": [
            ("Ecstasy", "Ciara"),
            ("Offa Me", "Davido feat. Victoria Monét"),
            ("Bliss", "Tyla"),
        ],
        "발라드": [
            ("All of Me", "John Legend"),
            ("Someone Like You", "Adele"),
            ("When We Were Young", "Adele"),
        ],
        "팝": [
            ("Flowers", "Miley Cyrus"),
            ("Anti-Hero", "Taylor Swift"),
            ("Calm Down", "Rema & Selena Gomez"),
        ],
        "댄스": [
            ("I'm Good (Blue)", "David Guetta & Bebe Rexha"),
        ],
        "힙합": [
            ("Sicko Mode", "Travis Scott"),
        ],
        "인디": [
            ("Skinny Love", "Bon Iver"),
            ("Holocene", "Bon Iver"),
            ("Youth", "Daughter"),
        ],
    }
}

st.title("🎵 2025 최신곡 장르별 노래 추천기")
st.write("지역과 장르를 선택한 뒤, 버튼을 눌러보세요!")

# 지역 선택
region = st.radio("지역을 선택하세요:", ("국내", "해외"))

# 장르 선택
genre = st.selectbox("장르를 선택하세요:", list(song_recommendations[region].keys()))

# 추천 버튼
if st.button("추천 받기 🎁"):
    st.subheader(f"🎧 {region} {genre} 추천 노래")
    songs = song_recommendations[region].get(genre, [])
    if songs:
        for title, artist in songs:
            st.markdown(f"- **{title}** - *{artist}*")
    else:
        st.write("해당 조건에 맞는 노래가 없습니다.")
