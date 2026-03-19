import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family'] = 'NanumGothic'
matplotlib.rcParams['axes.unicode_minus'] = False

st.set_page_config(page_title="서울시 상수도 노후화 분석", layout="wide")

st.title("서울시 상수도 노후화 및 수질 영향 분석")

# 공통 데이터
data = {
    "지역구": ["종로구","중구","강북구","관악구","서초구","강남구","송파구","은평구","구로구","영등포구"],
    "사용연수": [44, 38, 46, 42, 18, 20, 22, 36, 32, 40],
    "부식도":   [85, 78, 88, 83, 30, 33, 38, 72, 67, 81],
    "탁도":     [0.35, 0.29, 0.38, 0.34, 0.11, 0.12, 0.13, 0.27, 0.24, 0.32],
    "잔류염소": [0.18, 0.20, 0.17, 0.18, 0.34, 0.33, 0.32, 0.23, 0.24, 0.19],
    "철":       [0.12, 0.10, 0.13, 0.12, 0.03, 0.04, 0.04, 0.09, 0.08, 0.11],
    "망간":     [0.03, 0.02, 0.03, 0.03, 0.01, 0.01, 0.01, 0.02, 0.02, 0.03],
    "민원":     [7, 6, 9, 8, 0, 1, 1, 5, 4, 7],
}
df = pd.DataFrame(data)

# ── 페이지 1: 연구의 의의와 필요성 ──────────────────────────────────────────
with st.expander("📌 1. 연구의 의의와 필요성"):
    st.markdown("""
상수도는 도시 환경에서 가장 기본적인 인프라로, 수돗물의 안정성은 시민 건강과 직결된다.
노후 수도관은 시간이 지남에 따라 내부 부식, 균열, 누수 등을 발생시키며, 이는 수질 저하로 이어질 수 있다.

특히 금속관 부식은 **철 및 망간 용출**을 유발하고, **탁도 증가**와 **잔류염소 감소**를 초래한다.
이러한 변화는 단순 수치상의 문제가 아니라, 시민이 체감하는 적수 발생 및 불신으로 이어진다.

따라서 상수도 노후화는 환경공학적 문제이자 정책적 관리 대상이며, 과학적 분석과 함께 관리 전략 수립이 필요하다.
    """)

# ── 페이지 2: 수도관 교체와 시민 영향 ──────────────────────────────────────
with st.expander("🏗️ 2. 수도관 교체와 시민 영향"):
    st.markdown("""
노후 수도관 교체는 필수적이지만, 공사 과정에서 도로 굴착, 교통 통제, 소음, 단수 등의 문제가 발생한다.
이러한 문제는 시민 불편뿐 아니라 상업 활동에도 영향을 줄 수 있다.

따라서 공사 필요성과 시민 수용성을 동시에 고려한 계획이 필요하며, 단계적 시공과 사전 안내가 중요하다.

특히 **공사 시간 조정**, **민원 대응 체계 구축** 등은 정책 수용성을 높이는 핵심 요소이다.
    """)

# ── 페이지 3: 데이터 및 분석 방법 ──────────────────────────────────────────
with st.expander("🔬 3. 데이터 및 분석 방법"):
    st.markdown("""
본 연구에서는 서울시 자치구 데이터를 기반으로 노후도와 수질 간 관계를 분석하였다.

| 변수 유형 | 항목 |
|-----------|------|
| 노후도 변수 | 사용연수, 부식도 |
| 수질 변수 | 탁도, 잔류염소, 철, 망간 |

분석 방법으로는 **Pearson 상관계수**를 사용하였다.
이는 변수 간 선형 관계의 강도를 정량적으로 나타내는 지표로, 값이 1에 가까울수록 강한 양의 상관관계를 의미한다.
    """)

# ── 페이지 4: 상관관계 분석 결과 ────────────────────────────────────────────
with st.expander("📊 4. 상관관계 분석 결과"):
    st.markdown("""
분석 결과, **사용연수**와 **부식도**는 매우 높은 양의 상관관계를 보였다.
이는 시간 경과에 따라 관로 열화가 진행됨을 의미한다.

부식도는 **탁도** 및 **철 농도**와 양의 상관을 나타냈으며, 반면 **잔류염소**는 부식도와 음의 상관을 보였다.
    """)

    corr = df.drop(columns=["지역구"]).corr()

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("상관계수 행렬")
        st.dataframe(corr.style.background_gradient(cmap="coolwarm", axis=None))
    with col2:
        st.subheader("히트맵")
        fig, ax = plt.subplots(figsize=(5, 4))
        cax = ax.matshow(corr, cmap="coolwarm")
        fig.colorbar(cax)
        ax.set_xticks(range(len(corr.columns)))
        ax.set_yticks(range(len(corr.columns)))
        ax.set_xticklabels(corr.columns, rotation=90, fontsize=8)
        ax.set_yticklabels(corr.columns, fontsize=8)
        st.pyplot(fig)
        plt.close(fig)

# ── 페이지 5: 추가 분석 (산점도) ────────────────────────────────────────────
with st.expander("📈 5. 추가 분석 (산점도)"):
    st.markdown("사용연수와 탁도 간 관계를 산점도로 분석한 결과, 사용연수가 증가할수록 탁도가 증가하는 경향이 확인되었다.")

    col1, col2 = st.columns(2)
    with col1:
        x_var = st.selectbox("X 변수 선택", df.columns[1:], key="x_scatter")
    with col2:
        y_var = st.selectbox("Y 변수 선택", df.columns[1:], index=2, key="y_scatter")

    fig2, ax2 = plt.subplots(figsize=(6, 4))
    ax2.scatter(df[x_var], df[y_var], color="steelblue", s=80, edgecolors="white")
    for i, row in df.iterrows():
        ax2.annotate(row["지역구"], (row[x_var], row[y_var]),
                     textcoords="offset points", xytext=(5, 3), fontsize=7)
    ax2.set_xlabel(x_var)
    ax2.set_ylabel(y_var)
    ax2.set_title(f"{x_var} vs {y_var}")
    st.pyplot(fig2)
    plt.close(fig2)

# ── 페이지 6: 데이터 요약 ───────────────────────────────────────────────────
with st.expander("📋 6. 데이터 요약"):
    st.markdown("다음 표는 각 지역의 주요 변수 값을 정리한 것이다.")
    st.dataframe(df, use_container_width=True)

# ── 페이지 7: 토의 ──────────────────────────────────────────────────────────
with st.expander("💬 7. 토의 (Discussion)"):
    st.markdown("""
본 연구 결과는 노후화가 수질에 영향을 미친다는 기존 연구와 일치한다.
특히 **부식 과정**이 수질 악화의 핵심 메커니즘으로 작용함을 확인하였다.

다만 본 연구는 단면 데이터 기반 분석으로, 시간적 변화와 관망 구조를 반영하지 못한 한계가 있다.
    """)

# ── 페이지 8: 정책적 시사점 ─────────────────────────────────────────────────
with st.expander("📢 8. 정책적 시사점"):
    st.markdown("""
- **연식 기반 → 상태 기반 관리**로 전환 필요
- 공사 과정에서 **시민 불편 최소화**를 위한 정책적 접근 필요
- 노후 지역 우선 교체 전략 수립
- **민원 대응 체계** 구축으로 정책 수용성 제고
    """)

# ── 페이지 9: 결론 ──────────────────────────────────────────────────────────
with st.expander("✅ 9. 결론"):
    st.markdown("""
상수도 노후화는 수질과 시민 생활에 영향을 미치는 **구조적 문제**이며, 통합적 관리 전략이 필요하다.

과학적 분석을 바탕으로 **상태 기반 관리**와 **시민 소통 강화**를 핵심 방향으로 설정하여,
장기적이고 지속 가능한 상수도 인프라 운영을 도모해야 한다.
    """)
