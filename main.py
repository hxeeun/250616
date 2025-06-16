import streamlit as st

# 국내/해외 노래 추천 데이터 (유튜브 링크 포함, 최소 3곡씩)
song_recommendations = {
    "국내": {
        "R&B": [
            ("시간을 돌려서", "백예린", "https://www.youtube.com/watch?v=Z6IxlDsdHRw"),
            ("그냥 안아달란 말야", "크러쉬", "https://www.youtube.com/watch?v=2CYj_FkvqkA"),
            ("밤이 깊었네", "아이유", "https://www.youtube.com/watch?v=OGN9W_3hDFE"),
        ],
        "발라드": [
            ("그때 그 아인", "임영웅", "https://www.youtube.com/watch?v=m7WPKH7mr8g"),
            ("밤이 깊었네", "아이유", "https://www.youtube.com/watch?v=OGN9W_3hDFE"),
            ("취중고백", "김민석 (멜로망스)", "https://www.youtube.com/watch?v=7tQi5dfJoB4"),
        ],
        "댄스": [
            ("Pink Venom", "BLACKPINK", "https://www.youtube.com/watch?v=49pYIMygIcU"),
            ("롤린 (Rollin')", "브레이브걸스", "https://www.youtube.com/watch?v=LmZyxRIZy9c"),
            ("Next Level", "aespa", "https://www.youtube.com/watch?v=4PQ2uSxJHjw"),
        ],
        "힙합": [
            ("VVS", "MIRANI, Munchman, Khundi Panda, JUSTHIS", "https://www.youtube.com/watch?v=Tp9C2p1tF3M"),
            ("회전목마", "릴보이, 원슈타인, 죠지", "https://www.youtube.com/watch?v=FGZhGYJZegA"),
            ("GANADARA", "박재범", "https://www.youtube.com/watch?v=FM_sj3TcZDc"),
        ],
        "인디": [
            ("밤하늘의 별을", "양정승", "https://www.youtube.com/watch?v=57p-S3YFe_g"),
            ("고백", "10cm", "https://www.youtube.com/watch?v=jq6LFTRahE8"),
            ("끝이 없는 밤", "새소년", "https://www.youtube.com/watch?v=I4PYlHxnYs4"),
        ],
    },
    "해외": {
        "R&B": [
            ("Ecstasy", "Ciara", "https://www.youtube.com/watch?v=dQw4w9WgXcQ"),
            ("Offa Me", "Davido feat. Victoria Monét", "https://www.youtube.com/watch?v=dQw4w9WgXcQ"),
            ("Bliss", "Tyla", "https://www.youtube.com/watch?v=dQw4w9WgXcQ"),
        ],
        "발라드": [
            ("All of Me", "John Legend", "https://www.youtube.com/watch?v=450p7goxZqg"),
            ("Someone Like You", "Adele", "https://www.youtube.com/watch?v=hLQl3WQQoQ0"),
            ("When We Were Young", "Adele", "https://www.youtube.com/watch?v=RGuD0gO8A5s"),
        ],
        "댄스": [
            ("I'm Good (Blue)", "David Guetta & Bebe Rexha", "https://www.youtube.com/watch?v=IdneKLhsWOQ"),
            ("Stay", "The Kid LAROI, Justin Bieber", "https://www.youtube.com/watch?v=kTJczUoc26U"),
            ("Levitating", "Dua Lipa", "https://www.youtube.com/watch?v=TUVcZfQe-Kw"),
        ],
        "힙합": [
            ("Sicko Mode", "Travis Scott", "https://www.youtube.com/watch?v=6ONRf7h3Mdk"),
            ("Super Freaky Girl", "Nicki Minaj", "https://www.youtube.com/watch?v=RYr96YYEaZY"),
            ("First Class", "Jack Harlow", "https://www.youtube.com/watch?v=H4_MH9G2F0c"),
        ],
        "인디": [
            ("Skinny Love", "Bon Iver", "https://www.youtube.com/watch?v=ssdgFoHLwnk"),
            ("Holocene", "Bon Iver", "https://www.youtube.com/watch?v=TWcyIpul8OE"),
            ("Youth", "Daughter", "https://www.youtube.com/watch?v=VEpH1IpJ1i8"),
        ],
    }
}

st.title("🎵 2025 최신곡 장르별 노래 추천기")
st.write("지역과 장르를 선택한 뒤, 버튼을 눌러주세요!")

region = st.radio("지역을 선택하세요:", ("국내", "해외"))
genre = st.selectbox("장르를 선택하세요:", list(song_recommendations[region].keys()))

if st.button("추천 받기 🎁"):
    songs = song_recommendations[region].get(genre, [])
    if songs:
        st.subheader(f"🎧 {region} {genre} 추천 노래")
        # 노래 목록 번호 붙여서 출력
        for i, (title, artist, _) in enumerate(songs[:3], 1):
            st.markdown(f"{i}. **{title}** - *{artist}*")

        # 재생할 노래 선택
        selection = st.selectbox("재생할 노래를 선택하세요:", [f"{t} - {a}" for t, a, u in songs[:3]])

        # 선택한 노래 URL 찾아서 재생
        for title, artist, url in songs[:3]:
            if selection == f"{title} - {artist}":
                st.video(url)
                break
    else:
        st.write("해당 조건에 맞는 노래가 없습니다.")
