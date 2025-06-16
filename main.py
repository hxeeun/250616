import streamlit as st

# 노래 추천 데이터
song_recommendations = {
    "R&B": [
        ("Peaches", "Justin Bieber"),
        ("Leave The Door Open", "Bruno Mars"),
        ("Love on the Brain", "Rihanna"),
    ],
    "발라드": [
        ("너를 만나", "폴킴"),
        ("취중고백", "김민석 (멜로망스)"),
        ("비도 오고 그래서", "헤이즈"),
    ],
    "팝": [
        ("Shape of You", "Ed Sheeran"),
        ("Blinding Lights", "The Weeknd"),
        ("Levitating", "Dua Lipa"),
    ],
    "댄스": [
        ("IDOL", "BTS"),
        ("New Jeans", "NewJeans"),
        ("CHEER UP", "TWICE"),
    ],
    "힙합": [
        ("Sicko Mode", "Travis Scott"),
        ("VVS", "MIRANI, Munchman, Khundi Panda, JUSTHIS"),
        ("회전목마", "릴보이, 원슈타인, 죠지"),
    ],
    "인디": [
        ("밤하늘의 별을", "양정승"),
        ("고백", "10cm"),
        ("너의 바다", "잔나비"),
    ],
}

# Streamlit 앱 구성
st.title("🎵 장르별 노래 추천기")
st.write("원하는 장르를 선택하면 노래를 추천해드릴게요!")

# 장르 선택
genre = st.selectbox("장르를 선택하세요:", list(song_recommendations.keys()))

# 선택된 장르에 따른 노래 추천
if genre:
    st.subheader(f"🎧 {genre} 추천 노래")
    for title, artist in song_recommendations[genre]:
        st.markdown(f"- **{title}** - *{artist}*")
