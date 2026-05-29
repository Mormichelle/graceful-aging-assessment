import streamlit as st
import re

st.set_page_config(
    page_title="How Graceful Is Your Walk?",
    page_icon="🚶",
    layout="centered"
)

tokens = {
    "movement_confidence": 0,
    "independence_drive": 0,
    "graceful_aging_focus": 0,
    "fall_concern": 0,
    "caregiver_support": 0,
    "resilience_motivation": 0,
    "female_hormonal_transition": 0,
    "male_vitality_shift": 0,
    "bone_resilience_awareness": 0,
    "muscle_recovery_awareness": 0,
    "sleep_recovery_shift": 0,
    "night_movement_attention": 0,
}

def add_token(name, value):
    tokens[name] = tokens.get(name, 0) + value

def valid_email(email):
    return re.match(r"^[^@\s]+@[^@\s]+\.[^@\s]+$", email)

st.title("How Graceful Is Your Walk?")

st.markdown("""
### Discover Your Stability Age

Stability is more than strength.
It is confidence, timing, coordination, resilience, and the freedom to move with dignity as you age.
""")

st.divider()

st.subheader("Begin Your Movement Confidence Profile")

email = st.text_input(
    "Enter your email to begin",
    placeholder="you@example.com"
)

if email and not valid_email(email):
    st.warning("Please enter a valid email address.")

if not email or not valid_email(email):
    st.stop()

st.success("Thank you. Let’s begin your Stability Age profile.")

st.info("""
Please answer based on your usual movement over the past 30 days, not your best day or worst day.

The more precise your answers are, the more accurately your Stability Age profile can reflect your real movement confidence.
""")

st.divider()

st.subheader("General Movement Profile")

age = st.slider("Age", 45, 90, 60)

sex = st.radio(
    "Sex",
    ["Female", "Male", "Prefer not to say"],
    horizontal=True
)

height = st.text_input(
    "Height, optional",
    placeholder="Example: 5'6\" or 168 cm"
)

weight = st.text_input(
    "Weight, optional",
    placeholder="Example: 145 lb or 66 kg"
)

main_goal = st.multiselect(
    "What is your main goal?",
    [
        "Stay independent",
        "Walk gracefully",
        "Reduce fall concern",
        "Improve confidence",
        "Support aging parent"
    ]
)

if "Stay independent" in main_goal:
    add_token("independence_drive", 3)
    add_token("resilience_motivation", 2)

if "Walk gracefully" in main_goal:
    add_token("graceful_aging_focus", 3)
    add_token("movement_confidence", 2)

if "Reduce fall concern" in main_goal:
    add_token("fall_concern", 3)
    add_token("movement_confidence", 1)

if "Improve confidence" in main_goal:
    add_token("movement_confidence", 3)
    add_token("resilience_motivation", 2)

if "Support aging parent" in main_goal:
    add_token("caregiver_support", 3)
    add_token("independence_drive", 1)

st.divider()

if sex == "Female":

    st.subheader("Female Movement & Life-Stage Profile")

    st.markdown("""
    These questions help personalize your movement confidence profile around life stage, muscle recovery, bone resilience, and long-term independence.
    """)

    female_stage = st.selectbox(
        "Which stage best reflects where you are today?",
        [
            "Premenopausal",
            "Perimenopausal",
            "Postmenopausal",
            "Unsure",
            "Prefer not to say"
        ]
    )

    if female_stage == "Perimenopausal":
        add_token("female_hormonal_transition", 2)
        add_token("muscle_recovery_awareness", 1)

    elif female_stage == "Postmenopausal":
        add_token("female_hormonal_transition", 3)
        add_token("bone_resilience_awareness", 2)
        add_token("muscle_recovery_awareness", 2)

        menopause_years = st.selectbox(
            "Approximately how long has it been since your transition?",
            [
                "Less than 2 years",
                "2–5 years",
                "5–10 years",
                "More than 10 years",
                "Prefer not to say"
            ]
        )

        if menopause_years == "Less than 2 years":
            add_token("female_hormonal_transition", 1)
        elif menopause_years == "2–5 years":
            add_token("female_hormonal_transition", 2)
            add_token("bone_resilience_awareness", 1)
        elif menopause_years == "5–10 years":
            add_token("bone_resilience_awareness", 2)
            add_token("muscle_recovery_awareness", 1)
        elif menopause_years == "More than 10 years":
            add_token("bone_resilience_awareness", 3)
            add_token("muscle_recovery_awareness", 2)

    hormone_support = st.selectbox(
        "Are you currently using hormone replacement therapy or estrogen support?",
        ["Yes", "No", "Previously", "Prefer not to say"]
    )

    if hormone_support == "Yes":
        add_token("bone_resilience_awareness", 1)
        add_token("muscle_recovery_awareness", 1)
    elif hormone_support == "Previously":
        add_token("female_hormonal_transition", 1)

    female_change = st.selectbox(
        "Have you noticed more stiffness, weaker legs, or reduced movement confidence in recent years?",
        [
            "No noticeable change",
            "Slight change",
            "Moderate change",
            "Noticeable change",
            "I move more cautiously now"
        ]
    )

    if female_change == "Slight change":
        add_token("muscle_recovery_awareness", 1)
    elif female_change == "Moderate change":
        add_token("muscle_recovery_awareness", 2)
        add_token("movement_confidence", 1)
    elif female_change == "Noticeable change":
        add_token("muscle_recovery_awareness", 3)
        add_token("movement_confidence", 2)
    elif female_change == "I move more cautiously now":
        add_token("muscle_recovery_awareness", 3)
        add_token("movement_confidence", 3)
        add_token("resilience_motivation", 2)

elif sex == "Male":

    st.subheader("Male Movement & Vitality Profile")

    vitality = st.selectbox(
        "How would you describe your current physical vitality compared to 10 years ago?",
        [
            "Stronger than before",
            "About the same",
            "Slightly reduced",
            "Noticeably reduced",
            "I feel much more cautious and slower now"
        ]
    )

    if vitality == "Stronger than before":
        add_token("movement_confidence", 3)
        add_token("resilience_motivation", 2)
    elif vitality == "About the same":
        add_token("movement_confidence", 2)
    elif vitality == "Slightly reduced":
        add_token("male_vitality_shift", 1)
        add_token("muscle_recovery_awareness", 1)
    elif vitality == "Noticeably reduced":
        add_token("male_vitality_shift", 2)
        add_token("muscle_recovery_awareness", 2)
    elif vitality == "I feel much more cautious and slower now":
        add_token("male_vitality_shift", 3)
        add_token("muscle_recovery_awareness", 3)
        add_token("movement_confidence", 2)

    testosterone = st.selectbox(
        "Are you currently receiving testosterone therapy or hormonal support?", ["Yes", "No", "Previously", "Prefer not to say"]
    )

    if testosterone == "Yes":
        add_token("muscle_recovery_awareness", 1)
        add_token("bone_resilience_awareness", 1)
    elif testosterone == "Previously":
        add_token("male_vitality_shift", 1)

    prostate_sleep = st.selectbox(
        "Do nighttime bathroom trips interrupt your sleep or movement confidence?",
        [
            "Rarely or never",
            "Occasionally",
            "Sometimes",
            "Frequently",
            "Night movement feels noticeably less steady"
        ]
    )

    if prostate_sleep == "Occasionally":
        add_token("night_movement_attention", 1)
    elif prostate_sleep == "Sometimes":
        add_token("sleep_recovery_shift", 2)
        add_token("night_movement_attention", 1)
    elif prostate_sleep == "Frequently":
        add_token("sleep_recovery_shift", 3)
        add_token("night_movement_attention", 2)
    elif prostate_sleep == "Night movement feels noticeably less steady":
        add_token("sleep_recovery_shift", 3)
        add_token("night_movement_attention", 3)
        add_token("movement_confidence", 2)

else:
    st.subheader("General Movement Confidence Profile")
    st.markdown("""
    No problem. We will keep your profile general and focus on movement confidence, independence, resilience, and graceful aging.
    """)

    add_token("movement_confidence", 1)
    add_token("resilience_motivation", 1)

st.divider()

if st.button("Continue to Movement Confidence Questions"):
    st.success("Layer 1 completed.")
    st.markdown("### Current Token Preview")
    st.write(tokens)

    st.info("""
    Next layer will assess walking confidence, stairs, turning, balance recovery, ankle strength, cadence, and daily energy rhythm.
    """)
