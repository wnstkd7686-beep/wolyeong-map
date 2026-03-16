import streamlit as st
import folium
from streamlit_folium import st_folium
import pandas as pd

# ---------------------------------------------------
# 페이지 설정
# ---------------------------------------------------
st.set_page_config(
    page_title="월영동 탐험대 Pro",
    layout="wide",
    page_icon="💎"
)

# ---------------------------------------------------
# 스타일
# ---------------------------------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Pretendard:wght@400;500;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Pretendard', sans-serif;
}

.main {
    background-color: #f6f8fb;
}

.block-container {
    padding-top: 1.8rem;
    padding-bottom: 2rem;
}

.top-box {
    background: linear-gradient(135deg, #0f172a 0%, #1d4ed8 100%);
    color: white;
    padding: 26px 30px;
    border-radius: 22px;
    margin-bottom: 18px;
    box-shadow: 0 12px 28px rgba(0,0,0,0.08);
}

.top-title {
    font-size: 30px;
    font-weight: 800;
    margin-bottom: 8px;
}

.top-desc {
    font-size: 14px;
    opacity: 0.95;
    line-height: 1.6;
}

.section-title {
    font-size: 22px;
    font-weight: 800;
    margin-bottom: 14px;
    color: #111827;
}

.recommend-card {
    background: white;
    border-radius: 18px;
    padding: 18px;
    box-shadow: 0 8px 20px rgba(0,0,0,0.05);
    border: 1px solid #eef2f7;
    margin-bottom: 12px;
}

.recommend-label {
    font-size: 13px;
    font-weight: 700;
    color: #2563eb;
    margin-bottom: 8px;
}

.recommend-title {
    font-size: 19px;
    font-weight: 800;
    color: #111827;
    margin-bottom: 6px;
}

.recommend-desc {
    font-size: 13px;
    color: #6b7280;
    line-height: 1.5;
}

.restaurant-card {
    background: white;
    padding: 18px;
    border-radius: 18px;
    margin-bottom: 18px;
    box-shadow: 0 8px 20px rgba(0,0,0,0.05);
    border: 1px solid #eef2f7;
}

.card-image {
    width: 100%;
    border-radius: 14px;
    margin-bottom: 14px;
}

.card-title-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 10px;
    margin-bottom: 8px;
}

.card-title {
    font-size: 21px;
    font-weight: 800;
    color: #111827;
    margin: 0;
}

.score-badge {
    background: #fff7ed;
    color: #ea580c;
    padding: 6px 10px;
    border-radius: 999px;
    font-size: 13px;
    font-weight: 700;
    white-space: nowrap;
}

.meta-row {
    margin-bottom: 10px;
}

.badge {
    display: inline-block;
    padding: 5px 10px;
    border-radius: 999px;
    font-size: 12px;
    font-weight: 700;
    margin-right: 6px;
    margin-bottom: 6px;
}

.badge-category {
    background: #dbeafe;
    color: #1d4ed8;
}

.badge-crowd-light {
    background: #dcfce7;
    color: #166534;
}

.badge-crowd-mid {
    background: #f3f4f6;
    color: #374151;
}

.badge-crowd-busy {
    background: #fee2e2;
    color: #b91c1c;
}

.card-label {
    font-size: 13px;
    font-weight: 700;
    color: #374151;
    margin-bottom: 4px;
}

.card-text {
    font-size: 14px;
    color: #4b5563;
    line-height: 1.6;
    margin-bottom: 10px;
}

.tag {
    display: inline-block;
    background: #eef2ff;
    color: #4338ca;
    padding: 4px 9px;
    border-radius: 8px;
    font-size: 12px;
    font-weight: 600;
    margin-right: 6px;
    margin-top: 6px;
}

.mini-info {
    font-size: 13px;
    color: #6b7280;
}

[data-testid="stSidebar"] {
    background-color: #ffffff;
}
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# 데이터
# ---------------------------------------------------
data = [
    {
        "이름": "몬스터로스터스", "카테고리": "카페", "lat": 35.1856, "lon": 128.5570,
        "명당": "지하 1층 구석 자리", "혼잡도": "보통", "점수": 4.8,
        "태그": "#카공 #콘센트 #조용한편", "리뷰": "댓거리에서 공부하러 가기 괜찮은 카페. 오래 앉아있기 편함.",
        "사진": "https://images.unsplash.com/photo-1509042239860-f550ce710b93?q=80&w=400"
    },
    {
        "이름": "정직유부 경남대점", "카테고리": "식당", "lat": 35.1835, "lon": 128.5582,
        "명당": "입구 쪽 1인 바 테이블", "혼잡도": "보통", "점수": 4.7,
        "태그": "#혼밥 #가성비 #간단식사", "리뷰": "혼자 빠르게 먹기 좋고 부담 없이 들어가기 괜찮음.",
        "사진": "https://images.unsplash.com/photo-1547592180-85f173990554?q=80&w=400"
    },
    {
        "이름": "영남분식", "카테고리": "식당", "lat": 35.1820, "lon": 128.5595,
        "명당": "구석 2인 테이블", "혼잡도": "보통", "점수": 4.5,
        "태그": "#분식 #가성비 #간식", "리뷰": "옛날 분식집 느낌이고 간단하게 먹기 좋음.",
        "사진": "https://images.unsplash.com/photo-1601050690597-df0568f70950?q=80&w=400"
    },
    {
        "이름": "스타벅스 경남대점", "카테고리": "카페", "lat": 35.1842, "lon": 128.5568,
        "명당": "2층 창가 넓은 테이블", "혼잡도": "혼잡", "점수": 4.6,
        "태그": "#카공 #콘센트 #프랜차이즈", "리뷰": "자리 경쟁은 있지만 익숙하고 무난함.",
        "사진": "https://images.unsplash.com/photo-1501339847302-ac426a4a7cbb?q=80&w=400"
    },
    {
        "이름": "댓거리 돼지국밥", "카테고리": "식당", "lat": 35.1830, "lon": 128.5588,
        "명당": "벽 쪽 1인석", "혼잡도": "보통", "점수": 4.6,
        "태그": "#혼밥 #국밥 #해장", "리뷰": "든든하게 먹기 좋고 혼자 가도 안 어색함.",
        "사진": "https://images.unsplash.com/photo-1544025162-d76694265947?q=80&w=400"
    },
    {
        "이름": "미스터봉", "카테고리": "식당", "lat": 35.1845, "lon": 128.5575,
        "명당": "창가 쪽 좌석", "혼잡도": "보통", "점수": 4.4,
        "태그": "#파스타 #데이트 #분위기", "리뷰": "댓거리 쪽에서 분위기 있게 식사하기 좋은 편.",
        "사진": "https://images.unsplash.com/photo-1552566626-52f8b828add9?q=80&w=400"
    },
    {
        "이름": "본죽 경남대점", "카테고리": "식당", "lat": 35.1825, "lon": 128.5580,
        "명당": "창가 1인석", "혼잡도": "여유", "점수": 4.3,
        "태그": "#혼밥 #부담없는식사 #죽", "리뷰": "속 편하게 먹고 싶을 때 무난함.",
        "사진": "https://images.unsplash.com/photo-1512058564366-18510be2db19?q=80&w=400"
    },
    {
        "이름": "설빙 경남대점", "카테고리": "카페", "lat": 35.1850, "lon": 128.5585,
        "명당": "중앙 큰 테이블", "혼잡도": "보통", "점수": 4.4,
        "태그": "#디저트 #팀플 #빙수", "리뷰": "여럿이 가기 좋고 테이블이 넓음.",
        "사진": "https://images.unsplash.com/photo-1563805042-7684c019e1cb?q=80&w=400"
    },
    {
        "이름": "마산남부터미널", "카테고리": "기타", "lat": 35.1810, "lon": 128.5600,
        "명당": "정류장 근처 대기 공간", "혼잡도": "보통", "점수": 4.0,
        "태그": "#교통 #약속장소", "리뷰": "댓거리 주변 동선 설명할 때 핵심 위치.",
        "사진": "https://images.unsplash.com/photo-1474487548417-781cb71495f3?q=80&w=400"
    },
    {
        "이름": "정가네 떡볶이", "카테고리": "식당", "lat": 35.1838, "lon": 128.5590,
        "명당": "안쪽 벽면 자리", "혼잡도": "보통", "점수": 4.5,
        "태그": "#떡볶이 #분식 #학생맛집", "리뷰": "가볍게 먹기 좋고 학생들이 자주 가는 분위기.",
        "사진": "https://images.unsplash.com/photo-1562967914-608f82629710?q=80&w=400"
    }
]

df = pd.DataFrame(data)

# ---------------------------------------------------
# 유틸 함수
# ---------------------------------------------------
def get_icon_color(category):
    if category == "식당":
        return "blue"
    elif category == "카페":
        return "orange"
    return "gray"

def get_crowd_badge_class(crowd):
    if crowd == "여유":
        return "badge-crowd-light"
    elif crowd == "혼잡":
        return "badge-crowd-busy"
    return "badge-crowd-mid"

def sort_df(df_input, option):
    if option == "평점 높은 순":
        return df_input.sort_values(by="점수", ascending=False)
    elif option == "평점 낮은 순":
        return df_input.sort_values(by="점수", ascending=True)
    elif option == "이름순":
        return df_input.sort_values(by="이름", ascending=True)
    return df_input

# ---------------------------------------------------
# 사이드바
# ---------------------------------------------------
with st.sidebar:
    st.title("🔍 검색 필터")

    search = st.text_input(
        "가게 이름 또는 키워드",
        placeholder="예: 국밥, 카공, 혼밥"
    )

    categories = st.multiselect(
        "유형 선택",
        ["식당", "카페", "기타"],
        default=["식당", "카페", "기타"]
    )

    crowd_filter = st.selectbox(
        "혼잡도",
        ["전체", "여유", "보통", "혼잡"],
        index=0
    )

    sort_option = st.selectbox(
        "정렬",
        ["기본순", "평점 높은 순", "평점 낮은 순", "이름순"]
    )

    st.markdown("---")
    st.caption("경남대 댓거리 주변 장소를 기준으로 정리한 데이터입니다.")

# ---------------------------------------------------
# 필터
# ---------------------------------------------------
filtered_df = df[df["카테고리"].isin(categories)]

if crowd_filter != "전체":
    filtered_df = filtered_df[filtered_df["혼잡도"] == crowd_filter]

if search:
    filtered_df = filtered_df[
        filtered_df["이름"].str.contains(search, case=False, na=False) |
        filtered_df["태그"].str.contains(search, case=False, na=False) |
        filtered_df["리뷰"].str.contains(search, case=False, na=False) |
        filtered_df["명당"].str.contains(search, case=False, na=False)
    ]

filtered_df = sort_df(filtered_df, sort_option)

# ---------------------------------------------------
# 상단 소개
# ---------------------------------------------------
st.markdown("""
<div class="top-box">
    <div class="top-title">🧭 월영동 명당 탐험대 Pro</div>
    <div class="top-desc">
        경남대 댓거리 주변에서 혼밥, 카공, 약속 장소로 괜찮은 곳을
        지도와 카드 형태로 한눈에 볼 수 있게 정리한 서비스
    </div>
</div>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# 통계
# ---------------------------------------------------
count1, count2, count3, count4 = st.columns(4)
count1.metric("전체 장소", len(df))
count2.metric("현재 표시", len(filtered_df))
count3.metric("카페 수", len(df[df["카테고리"] == "카페"]))
count4.metric("식당 수", len(df[df["카테고리"] == "식당"]))

st.divider()

# ---------------------------------------------------
# 추천 카드
# ---------------------------------------------------
st.markdown('<div class="section-title">추천 장소</div>', unsafe_allow_html=True)

recommend_col1, recommend_col2, recommend_col3 = st.columns(3)

# 혼밥 추천
solo_df = df[df["태그"].str.contains("혼밥", na=False)]
solo_place = solo_df.sort_values(by="점수", ascending=False).iloc[0] if not solo_df.empty else None

# 카공 추천
study_df = df[df["태그"].str.contains("카공", na=False)]
study_place = study_df.sort_values(by="점수", ascending=False).iloc[0] if not study_df.empty else None

# 전체 최고 평점
top_place = df.sort_values(by="점수", ascending=False).iloc[0] if not df.empty else None

with recommend_col1:
    if top_place is not None:
        st.markdown(f"""
        <div class="recommend-card">
            <div class="recommend-label">전체 추천</div>
            <div class="recommend-title">{top_place['이름']}</div>
            <div class="recommend-desc">
                평점 {top_place['점수']} · {top_place['카테고리']}<br>
                추천 자리: {top_place['명당']}
            </div>
        </div>
        """, unsafe_allow_html=True)

with recommend_col2:
    if solo_place is not None:
        st.markdown(f"""
        <div class="recommend-card">
            <div class="recommend-label">혼밥 추천</div>
            <div class="recommend-title">{solo_place['이름']}</div>
            <div class="recommend-desc">
                혼자 가기 괜찮은 장소로 분류됨<br>
                추천 자리: {solo_place['명당']}
            </div>
        </div>
        """, unsafe_allow_html=True)

with recommend_col3:
    if study_place is not None:
        st.markdown(f"""
        <div class="recommend-card">
            <div class="recommend-label">카공 추천</div>
            <div class="recommend-title">{study_place['이름']}</div>
            <div class="recommend-desc">
                공부하기 괜찮은 장소로 분류됨<br>
                추천 자리: {study_place['명당']}
            </div>
        </div>
        """, unsafe_allow_html=True)

st.divider()

# ---------------------------------------------------
# 메인 화면
# ---------------------------------------------------
col1, col2 = st.columns([1.45, 1])

with col1:
    st.markdown('<div class="section-title">지도 보기</div>', unsafe_allow_html=True)

    m = folium.Map(
        location=[35.1840, 128.5585],
        zoom_start=17,
        tiles="cartodbpositron"
    )

    # 경남대 주변 중심 반경 표시
    folium.Circle(
        radius=250,
        location=[35.1840, 128.5585],
        popup="경남대 댓거리 중심",
        color="#2563eb",
        fill=True,
        fill_opacity=0.06
    ).add_to(m)

    for _, row in filtered_df.iterrows():
        popup_html = f"""
        <div style="width:230px;">
            <h4 style="margin-bottom:8px;">{row['이름']}</h4>
            <p style="margin:4px 0;"><b>카테고리:</b> {row['카테고리']}</p>
            <p style="margin:4px 0;"><b>명당:</b> {row['명당']}</p>
            <p style="margin:4px 0;"><b>혼잡도:</b> {row['혼잡도']}</p>
            <p style="margin:4px 0;"><b>평점:</b> {row['점수']}</p>
            <p style="margin:4px 0;"><b>태그:</b> {row['태그']}</p>
        </div>
        """

        folium.Marker(
            [row["lat"], row["lon"]],
            popup=folium.Popup(popup_html, max_width=260),
            tooltip=row["이름"],
            icon=folium.Icon(color=get_icon_color(row["카테고리"]))
        ).add_to(m)

    st_folium(m, width="100%", height=650)

with col2:
    st.markdown('<div class="section-title">명당 리스트</div>', unsafe_allow_html=True)

    if not filtered_df.empty:
        for _, row in filtered_df.iterrows():
            tags_html = " ".join(
                [f'<span class="tag">{tag}</span>' for tag in row["태그"].split()]
            )
            crowd_class = get_crowd_badge_class(row["혼잡도"])

            st.markdown(f"""
            <div class="restaurant-card">
                <img src="{row['사진']}" class="card-image">

                <div class="card-title-row">
                    <div class="card-title">{row['이름']}</div>
                    <div class="score-badge">★ {row['점수']}</div>
                </div>

                <div class="meta-row">
                    <span class="badge badge-category">{row['카테고리']}</span>
                    <span class="badge {crowd_class}">혼잡도: {row['혼잡도']}</span>
                </div>

                <div class="card-label">추천 자리</div>
                <div class="card-text">{row['명당']}</div>

                <div class="card-label">한줄 설명</div>
                <div class="card-text">{row['리뷰']}</div>

                <div class="card-label">태그</div>
                <div>{tags_html}</div>
            </div>
            """, unsafe_allow_html=True)

            with st.expander(f"{row['이름']} 자세히 보기"):
                st.write(f"**카테고리:** {row['카테고리']}")
                st.write(f"**평점:** {row['점수']}")
                st.write(f"**혼잡도:** {row['혼잡도']}")
                st.write(f"**추천 자리:** {row['명당']}")
                st.write(f"**한줄 설명:** {row['리뷰']}")
                st.write(f"**태그:** {row['태그']}")
                st.write(f"**위치 좌표:** {row['lat']}, {row['lon']}")
    else:
        st.warning("조건에 맞는 장소가 없습니다.")

st.caption("© 2026 경남대학교 월영동 탐험대 | Computer Engineering")