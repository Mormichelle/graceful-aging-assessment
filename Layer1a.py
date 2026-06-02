import streamlit as st
import re

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------

st.set_page_config(
    page_title="How Graceful Is Your Walk?",
    page_icon="🚶",
    layout="centered"
)

# ---------------------------------------------------
# SESSION STATE
# ---------------------------------------------------

if "stage" not in st.session_state:
    st.session_state.stage = "free"

if "tokens" not in st.session_state:
    st.session_state.tokens = {
        "movement_confidence": 0,
        "independence_drive": 0,
        "graceful_aging_focus": 0,
        "fall_concern": 0,
        "caregiver_support": 0,
        "resilience_motivation": 0,
        "movement_identity": 0,
        "movement_aspiration": 0,
        "movement_style": 0,
        "adventure_drive": 0,
        "family_future_focus": 0,
        "female_hormonal_transition": 0,
        "male_vitality_shift": 0,
        "bone_resilience_awareness": 0,
        "muscle_recovery_awareness": 0,
        "sleep_recovery_shift": 0,
        "night_movement_attention": 0,
    }


def add_token(name, value):
    st.session_state.tokens[name] = st.session_state.tokens.get(name, 0) + value


def valid_email(email):
    return re.match(r"^[^@\s]+@[^@\s]+\.[^@\s]+$", email)


def calculate_stability_index():
    total_score = sum(st.session_state.tokens.values())
    max_possible = 55

    score = int((total_score / max_possible) * 100)

    return max(45, min(score, 96))


def determine_archetype(score):
    if score >= 88:
        return "The Resilient Navigator"
    elif score >= 76:
        return "The Independent Stabilizer"
    elif score >= 64:
        return "The Conscious Mover"
    else:
        return "The Careful Navigator"


# ===================================================
# FREE ASSESSMENT
# ===================================================

if st.session_state.stage == "free":

    st.title("How Graceful Is Your Walk?")

    st.markdown("""
    ### Discover Your Stability Profile

    Stability is more than strength.
    It is confidence, timing, coordination, resilience, and the freedom to
    move with dignity as you age.
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

    st.session_state.email = email

    st.success("Thank you. Let’s begin your Stability Profile.")

    st.info("""
    Please answer based on your usual movement over the past 30 days, not
    your best day or worst day.

    The more precise your answers are, the more accurately your Stability
    Profile can reflect your real movement confidence.
    """)

    st.divider()

    # ---------------------------------------------------
    # MOVEMENT IDENTITY
    # ---------------------------------------------------

    st.subheader("Movement Identity")

    life_stage = st.selectbox(
        "Which statement feels closest to where you are today?",
        [
            "I want to maintain my independence",
            "I want to stay energetic and adventurous",
            "I want to move confidently as I age",
            "I am noticing changes in my movement",
            "I want to remain active for my family and future"
        ]
    )

    if life_stage == "I want to maintain my independence":
        add_token("independence_drive", 3)
        add_token("resilience_motivation", 2)

    elif life_stage == "I want to stay energetic and adventurous":
        add_token("adventure_drive", 3)
        add_token("movement_confidence", 2)

    elif life_stage == "I want to move confidently as I age":
        add_token("graceful_aging_focus", 3)
        add_token("movement_confidence", 2)

    elif life_stage == "I am noticing changes in my movement":
        add_token("movement_confidence", 1)
        add_token("resilience_motivation", 3)

    elif life_stage == "I want to remain active for my family and future":
        add_token("family_future_focus", 3)
        add_token("independence_drive", 2)

    movement_aspiration = st.selectbox(
        "Which activity best reflects the way you would like to move through life?",
        [
            "Walking confidently through a city",
            "Hiking nature trails",
            "Dancing gracefully",
            "Traveling actively and independently",
            "Playing recreational sports",
            "Keeping up with children or grandchildren"
        ]
    )

    if movement_aspiration == "Walking confidently through a city":
        add_token("movement_identity", 2)
        add_token("movement_confidence", 2)

    elif movement_aspiration == "Hiking nature trails":
        add_token("adventure_drive", 2)
        add_token("movement_confidence", 1)

    elif movement_aspiration == "Dancing gracefully":
        add_token("graceful_aging_focus", 3)
        add_token("movement_style", 2)

    elif movement_aspiration == "Traveling actively and independently":
        add_token("independence_drive", 2)
        add_token("adventure_drive", 2)

    elif movement_aspiration == "Playing recreational sports":
        add_token("movement_confidence", 2)
        add_token("resilience_motivation", 2)

    elif movement_aspiration == "Keeping up with children or grandchildren":
        add_token("family_future_focus", 3)
        add_token("movement_confidence", 1)

    movement_style = st.selectbox(
        "Which movement style feels most like you?",
        [
            "Strong and powerful",
            "Graceful and fluid",
            "Balanced and controlled",
            "Relaxed and effortless",
            "Agile and responsive",
            "Fast and energetic"
        ]
    )

    if movement_style == "Strong and powerful":
        add_token("movement_confidence", 3)
        add_token("resilience_motivation", 1)

    elif movement_style == "Graceful and fluid":
        add_token("graceful_aging_focus", 3)
        add_token("movement_style", 2)

    elif movement_style == "Balanced and controlled":
        add_token("movement_confidence", 2)
        add_token("movement_style", 2)

    elif movement_style == "Relaxed and effortless":
        add_token("movement_style", 2)
        add_token("graceful_aging_focus", 1)

    elif movement_style == "Agile and responsive":
        add_token("movement_confidence", 3)
        add_token("resilience_motivation", 2)

    elif movement_style == "Fast and energetic":
        add_token("adventure_drive", 2)
        add_token("movement_confidence", 2)

    hero_type = st.selectbox(
        "Which type of person inspires you most?",
        [
            "Athletes",
            "Adventurers",
            "Dancers",
            "Scientists and thinkers",
            "Disciplined leaders",
            "Resilient everyday people"
        ]
    )

    if hero_type == "Athletes":
        add_token("movement_confidence", 2)
        add_token("resilience_motivation", 2)

    elif hero_type == "Adventurers":
        add_token("adventure_drive", 3)

    elif hero_type == "Dancers":
        add_token("graceful_aging_focus", 3)
        add_token("movement_style", 2)

    elif hero_type == "Scientists and thinkers":
        add_token("movement_identity", 2)
        add_token("resilience_motivation", 1)

    elif hero_type == "Disciplined leaders":
        add_token("resilience_motivation", 3)
        add_token("independence_drive", 1)

    elif hero_type == "Resilient everyday people":
        add_token("family_future_focus", 2)
        add_token("resilience_motivation", 2)

    st.divider()

    # ---------------------------------------------------
    # GENERAL MOVEMENT GOALS
    # ---------------------------------------------------

    st.subheader("Movement Goals")

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

    # ---------------------------------------------------
    # OPTIONAL PERSONALIZATION
    # ---------------------------------------------------

    st.subheader("Optional Personalization")

    sex = st.radio(
        "Would you like your profile personalized by biological sex?",
        ["Female", "Male", "Prefer not to say"],
        horizontal=True
    )

    st.session_state.sex = sex

    # ---------------------------------------------------
    # FEMALE BRANCH
    # ---------------------------------------------------

    if sex == "Female":

        st.subheader("Female Movement & Life-Stage Profile")

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

    # ---------------------------------------------------
    # MALE BRANCH
    # ---------------------------------------------------

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
            "Are you currently receiving testosterone therapy or hormonal support?",
            ["Yes", "No", "Previously", "Prefer not to say"]
        )

        if testosterone == "Yes":
            add_token("muscle_recovery_awareness", 1)
            add_token("bone_resilience_awareness", 1)
        elif testosterone == "Previously":
            add_token("male_vitality_shift", 1)

    else:

        st.subheader("General Movement Confidence Profile")

        st.markdown("""
        No problem. We will keep your profile general and focus on movement
        confidence, independence, resilience, and graceful aging.
        """)

        add_token("movement_confidence", 1)
        add_token("resilience_motivation", 1)

    st.divider()

    if st.button("View My Preliminary Stability Profile"):
        st.session_state.stability_index = calculate_stability_index()
        st.session_state.archetype = determine_archetype(
            st.session_state.stability_index
        )
        st.session_state.stage = "free_result"
        st.rerun()


# ===================================================
# FREE RESULT
# ===================================================

elif st.session_state.stage == "free_result":

    st.title("Your Preliminary Stability Profile")

    stability_index = st.session_state.get("stability_index", calculate_stability_index())
    archetype = st.session_state.get("archetype", determine_archetype(stability_index))

    st.success(f"Preliminary Stability Index: {stability_index}")

    st.markdown(f"""
    ### Movement Archetype:
    **{archetype}**

    ### What This Means
    Your preliminary profile reflects your current movement identity,
    confidence, motivation, and graceful aging priorities.

    ### Strengths
    • Movement awareness
    • Independence motivation
    • Resilience potential

    ### Areas To Explore
    • Terrain adaptability
    • Recovery reserve
    • Directional stability
    """)

    st.info("""
    Real-world stability also depends on:

    • stairs
    • turning
    • uneven terrain
    • recovery timing
    • multitasking
    • fatigue rhythm
    """)

    if st.button("Continue to Advanced Stability Analysis"):
        st.session_state.stage = "advanced"
        st.rerun()


# ===================================================
# ADVANCED ASSESSMENT
# ===================================================

elif st.session_state.stage == "advanced":

    st.title("Advanced Stability Analysis")

    st.markdown("""
    This next assessment explores:

    • stairs
    • uneven terrain
    • turning confidence
    • recovery reserve
    • multitasking while walking
    • fatigue-related movement changes
    """)

    st.info("Estimated time: 3–5 minutes")

    st.markdown("### Advanced Stability Questions")

    stairs = st.radio(
        "How confident do you feel going up or down stairs?",
        [
            "Very confident",
            "Mostly confident",
            "Somewhat cautious",
            "Very cautious or avoid stairs"
        ]
    )

    uneven = st.radio(
        "How do you feel walking on uneven ground, grass, gravel, or curbs?",
        [
            "Comfortable and steady",
            "Usually steady",
            "I slow down and pay attention",
            "I avoid uneven surfaces when possible"
        ]
    )

    turning = st.radio(
        "When turning quickly, changing direction, or looking behind you, how stable do you feel?",
        [
            "Stable",
            "Slightly slower but stable",
            "Sometimes unsteady",
            "I avoid quick turns"
        ]
    )

    recovery = st.radio(
        "If you trip slightly, how well can you recover?",
        [
            "I recover quickly",
            "I usually recover",
            "I need to grab something",
            "I worry I may fall"
        ]
    )

    posture_change = st.radio(
        "After walking continuously for a while, what do you notice about your posture and movement?",
        [
            "I naturally straighten up, lift my head, and move more freely",
            "My posture stays about the same",
            "I begin to lean forward or feel more tension",
            "I noticeably hunch, slow down, or look downward more"
        ]
    )

    multitask = st.radio(
        "Can you walk while talking, carrying something, or thinking about something else?",
        [
            "Yes, easily",
            "Usually",
            "I slow down",
            "I lose confidence or balance"
        ]
    )

    fatigue = st.radio(
        "After walking for a while, what happens to your movement?",
        [
            "No major change",
            "Slight fatigue",
            "My steps become shorter or slower",
            "I feel unstable or need to stop"
        ]
    )

    warmup = st.radio(
        "After moving continuously for 10–15 minutes, how does your body usually respond?",
        [
            "I feel stronger, smoother, and move more confidently",
            "I feel about the same",
            "I become somewhat tired or slower",
            "I become noticeably fatigued or less steady"
        ]
    )

    st.markdown("### Movement Coordination")

    rhythm = st.radio(
        "When walking, how would you describe your natural rhythm?",
        [
            "Smooth and automatic",
            "Mostly steady",
            "Sometimes uneven",
            "Frequently hesitant or interrupted"
        ]
    )

    attention = st.radio(
        "When walking outdoors, where is your attention usually focused?",
        [
            "Comfortably aware of surroundings",
            "Mostly ahead",
            "Frequently watching the ground",
            "Constantly monitoring each step"
        ]
    )

    arm_swing = st.radio(
        "How natural does your arm swing feel while walking?",
        [  
            "Relaxed and natural",
            "Slightly stiff",
            "Limited or uneven",
            "Very restricted"
        ]
    )

    turning_flow = st.radio(
        "When changing direction, how fluid does the movement feel?",
        [
            "Smooth and continuous",
            "Mostly smooth",
            "Somewhat cautious",
            "Slow or segmented"
        ]
    )

    if st.button("Complete Advanced Stability Analysis"):

        total_score = 0
        bonus_score = 0

        scoring = {
            # 0-point responses
            "Very confident": 0,
            "Comfortable and steady": 0,
            "Stable": 0,
            "I recover quickly": 0,
            "Yes, easily": 0,
            "No major change": 0,
            "Smooth and automatic": 0,
            "Comfortably aware of surroundings": 0,
            "Relaxed and natural": 0,
            "Smooth and continuous": 0,

            # 1-point responses
            "Mostly confident": 1,
            "Usually steady": 1,
            "Slightly slower but stable": 1,
            "I usually recover": 1,
            "Usually": 1,
            "Slight fatigue": 1,
            "My posture stays about the same": 1,
            "I feel about the same": 1,
            "Mostly steady": 1,
            "Mostly ahead": 1,
            "Slightly stiff": 1,
            "Mostly smooth": 1,

            # 2-point responses
            "Somewhat cautious": 2,
            "I slow down and pay attention": 2,
            "Sometimes unsteady": 2,
            "I need to grab something": 2,
            "I slow down": 2,
            "My steps become shorter or slower": 2,
            "I begin to lean forward or feel more tension": 2,
            "I become somewhat tired or slower": 2,
            "Sometimes uneven": 2,
            "Frequently watching the ground": 2,
            "Limited or uneven": 2,
            "Somewhat cautious": 2,

            # 3-point responses
            "Very cautious or avoid stairs": 3,
            "I avoid uneven surfaces when possible": 3,
            "I avoid quick turns": 3,
            "I worry I may fall": 3,
            "I lose confidence or balance": 3,
            "I feel unstable or need to stop": 3,
            "I noticeably hunch, slow down, or look downward more": 3,
            "I become noticeably fatigued or less steady": 3,
            "Frequently hesitant or interrupted": 3,
            "Constantly monitoring each step": 3,
            "Very restricted": 3,
            "Slow or segmented": 3,
        }

        advanced_answers = [
            stairs,
            uneven,
            turning,
            recovery,
            posture_change,
            multitask,
            fatigue,
            warmup,
            rhythm,
            attention,
            arm_swing,
            turning_flow
        ]

        for answer in advanced_answers:
            total_score += scoring.get(answer, 0)

        # Bonus scoring for positive movement adaptation
        if posture_change == "I naturally straighten up, lift my head, and move more freely":
            bonus_score += 1

        if warmup == "I feel stronger, smoother, and move more confidently":
            bonus_score += 1

        if rhythm == "Smooth and automatic":
            bonus_score += 1

        if arm_swing == "Relaxed and natural":
            bonus_score += 1

        if turning_flow == "Smooth and continuous":
            bonus_score += 1

        
        adjusted_score = max(0, total_score - bonus_score)

        max_score = 36
        reserve_score = int(100 - ((adjusted_score / max_score) * 100))
        reserve_score = max(45, min(reserve_score, 98))
        
        st.markdown("## Your Advanced Stability Result")

        st.write(f"Movement Reserve Bonus: -{bonus_score}")
        st.write(f"Adjusted Stability Challenge Score: {adjusted_score}")
        st.write(f"Stability Reserve Score: **{reserve_score} / 100**")

        if reserve_score >= 85:

            st.write("""
            Your responses suggest that your body still maintains strong 
            movement reserve, coordination, posture adaptation, and recovery 
            capacity during real-life movement situations.

            Your movement profile suggests:
            • good adaptability during walking
            • preserved coordination and rhythm
            • healthy confidence during movement
            • strong movement reserve under fatigue
            """)

        elif reserve_score >= 70:

            st.write("""
            Your responses suggest early changes in movement reserve may be 
            developing under more demanding situations such as fatigue, 
            uneven terrain, multitasking, or prolonged walking.

            Your movement profile suggests:
            • mild reduction in recovery reserve
            • occasional movement compensation
            • early posture or coordination changes
            • opportunity to strengthen movement resilience
            """)

        else:

            st.write("""
            Your responses suggest that your movement system may currently be 
            working harder to maintain stability during daily activities.

            Your movement profile suggests:
            • reduced recovery reserve
            • increased movement caution
            • posture or coordination compensation
            • increased fatigue-related movement changes
            """)
        st.markdown("### Your Movement Focus Areas")

        focus_areas = []

        if stairs in ["Somewhat cautious", "Very cautious or avoid stairs"]:
            focus_areas.append("Stair confidence and lower-body control")

        if uneven in ["I slow down and pay attention", "I avoid uneven surfaces when possible"]:
            focus_areas.append("Uneven terrain adaptability")

        if recovery in ["I need to grab something", "I worry I may fall"]:
            focus_areas.append("Trip recovery and reaction timing")

        if posture_change in [
        "I begin to lean forward or feel more tension", "I noticeably hunch, slow down, or look downward more"]:
            focus_areas.append("Posture, breathing reserve, and head position")

        if fatigue in ["My steps become shorter or slower", "I feel unstable or need to stop"]:
            focus_areas.append("Fatigue-related stability reserve")

        if rhythm in ["Sometimes uneven", "Frequently hesitant or interrupted"]:
            focus_areas.append("Walking rhythm and timing")

        if attention in ["Frequently watching the ground", "Constantly monitoring each step"]:
            focus_areas.append("Visual confidence and environmental awareness")

        if arm_swing in ["Limited or uneven", "Very restricted"]:
            focus_areas.append("Arm swing and upper-body coordination")

        if turning_flow in ["Somewhat cautious", "Slow or segmented"]:
            focus_areas.append("Turning fluidity and directional control")

        if focus_areas:

            for area in focus_areas:
                st.write(f"• {area}")

        else:

            st.success(
            "No major movement focus areas were identified."
            "Your responses suggest strong movement reserve and adaptability."
        )

        st.markdown("### Next Step")

        st.write("""
            Early intervention and movement training may significantly help
            improve confidence, coordination, and long-term independence.
            """)
        st.markdown(
            """
            <a href="https://www.sciencetainment.net" target="_self">
                <button style="
                    background-color:#f5c542;
                    color:#020817;
                    padding:14px 28px;
                    border:none;
                    border-radius:999px;
                    font-size:18px;
                    font-weight:700;
                    cursor:pointer;
                    box-shadow:0 0 18px rgba(245,197,66,0.35);">
                    Return to The Science of Graceful Aging
                </button>
            </a>
            """,
            unsafe_allow_html=True
        )



   


   





