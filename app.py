import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="서울시 상수도 노후화 분석", layout="wide")

st.title("서울시 상수도 노후화 및 수질 영향 분석")

st.markdown("""
이 앱은 서울시 상수도 노후화와 수질 영향 간 관계를 분석하기 위해 제작된 간단한 데이터 탐색 도구입니다.

연구 변수
- 사용연수
- 부식도
- 탁도
- 잔류염소
- 철
- 망간
- 민원
""")

# 데이터 생성
data = {
    "지역구": ["종로구","중구","강북구","관악구","서초구","강남구","송파구","은평구","구로구","영등포구"],
    "사용연수":[44,38,46,42,18,20,22,36,32,40],
    "부식도":[85,78,88,83,30,33,38,72,67,81],
    "탁도":[0.35,0.29,0.38,0.34,0.11,0.12,0.13,0.27,0.24,0.32],
    "잔류염소":[0.18,0.20,0.17,0.18,0.34,0.33,0.32,0.23,0.24,0.19],
    "철":[0.12,0.10,0.13,0.12,0.03,0.04,0.04,0.09,0.08,0.11],
    "망간":[0.03,0.02,0.03,0.03,0.01,0.01,0.01,0.02,0.02,0.03],
    "민원":[7,6,9,8,0,1,1,5,4,7]
}

df = pd.DataFrame(data)

st.header("데이터 테이블")

st.dataframe(df)

st.header("상관관계 분석")

corr = df.drop(columns=["지역구"]).corr()

st.write(corr)

fig, ax = plt.subplots()

cax = ax.matshow(corr)
plt.xticks(range(len(corr.columns)), corr.columns, rotation=90)
plt.yticks(range(len(corr.columns)), corr.columns)

fig.colorbar(cax)

st.pyplot(fig)

st.header("산점도 분석")

x_var = st.selectbox("X 변수 선택", df.columns[1:])
y_var = st.selectbox("Y 변수 선택", df.columns[1:])

fig2, ax2 = plt.subplots()

ax2.scatter(df[x_var], df[y_var])

ax2.set_xlabel(x_var)
ax2.set_ylabel(y_var)

st.pyplot(fig2)

st.header("연구 인사이트")

st.markdown("""
### 주요 결과

- 사용연수와 부식도는 강한 양의 상관관계를 보인다
- 부식도 증가 시 철 농도 및 탁도가 증가한다
- 잔류염소는 노후화와 음의 상관관계를 보인다

### 정책 시사점

- 연식 기반 교체 정책 → 상태 기반 관리 필요
- 노후 지역 우선 교체 전략 필요
- 시민 민원 대응 체계 구축 필요
""")
