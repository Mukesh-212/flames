import streamlit as st 

# -------- SESSION STATE FIX --------
if "result" not in st.session_state:
    st.session_state.result = None

st.markdown("""
<style>

.stApp {
background-color: #ffb6c1;
}

.title{
text-align:center;
font-size:40px;
font-weight:bold;
color:white;
text-shadow:2px 2px #ff3366;
}

.card{
background:white;
padding:25px;
border-radius:20px;
box-shadow:0px 0px 15px rgba(0,0,0,0.2);
}

.result{
margin-top:20px;
background:linear-gradient(to right,#ff4d88,#ff99cc);
padding:20px;
border-radius:15px;
text-align:center;
font-size:28px;
color:white;
font-weight:bold;
animation:pulse 1s infinite alternate;
}

@keyframes pulse{
from{transform:scale(1);}
to{transform:scale(1.05);}
}

.heart{
position:fixed;
bottom:-20px;
font-size:25px;
animation:float 6s infinite;
color:#ff0066;
z-index:100;
}

.heart:nth-child(1){left:10%;animation-delay:0s;}
.heart:nth-child(2){left:30%;animation-delay:1s;}
.heart:nth-child(3){left:50%;animation-delay:2s;}
.heart:nth-child(4){left:70%;animation-delay:3s;}
.heart:nth-child(5){left:90%;animation-delay:4s;}

@keyframes float{
0%{transform:translateY(0);opacity:1;}
100%{transform:translateY(-600px);opacity:0;}
}

.blacktext{
color:red;
font-size:22px;
font-weight:600;
text-align:center;
}

</style>

<div class="heart">💗</div>
<div class="heart">💖</div>
<div class="heart">💘</div>
<div class="heart">💞</div>
<div class="heart">💕</div>
""", unsafe_allow_html=True)

st.markdown("<div class='title'>💖 FLAMES Program 💖</div>", unsafe_allow_html=True)
st.markdown("<div class='card'>", unsafe_allow_html=True)

name1 = st.text_input("💗Enter First Name")
name2 = st.text_input("💗 Enter Second Name")

if st.button(" Check FLAMES "):

    list1 = list(name1.replace(" ","").lower())
    list2 = list(name2.replace(" ","").lower())

    for ch in list1[:]:
        if ch in list2:
            list1.remove(ch)
            list2.remove(ch)

    count = len(list1) + len(list2)

    flames = ["F","L","A","M","E","S"]

    for i in range(5):
        index = (count % len(flames)) - 1
        if index >= 0:
            flames = flames[index+1:] + flames[:index]
        else:
            flames = flames[:len(flames)-1]

    st.session_state.result = flames[0]

    meaning = {
        "F": f"{name1} {name2} Friends 👫",
        "L":f"{name1} {name2} Love 💘",
        "A": f"{name1} {name2} Affection 💞",
        "M":f"{name1} {name2} Marriage 💍",
        "E":f"{name1} {name2} Enemy 👿",
        "S":f"{name1} {name2} Sibling 💗"
    }

    st.markdown(f"<div class='result'>{meaning[st.session_state.result]}</div> <br>", unsafe_allow_html=True)

if st.button("click here"):

    if st.session_state.result is None:
        st.warning("First press Check FLAMES 🙂")
        st.stop()

    if st.session_state.result == "F":
        st.image("https://media.tenor.com/kG4jM-Braz8AAAAM/who-is-that-yar-adhu.gif",width=50, use_container_width=True)


    if st.session_state.result == "L":
        st.image("https://media.tenor.com/DgPHzhF_h8EAAAAM/startamilchat-sanjay-chat.gif")
        st.markdown("<div class='blacktext'>My friend after seeing LOVE in flames is reaction</div>", unsafe_allow_html=True)
        st.video("https://tamil.statusdp.com/videos/download/play/1HGRcWAZMr20hrorAMCzGA_rhLRalUk4o-0.mp4",width=300)

    elif st.session_state.result == "A":
        st.image("https://media.tenor.com/xMELcETredcAAAAM/starchat-star-tamil-chat.gif")
        st.markdown("<div class='blacktext'>My friend after seenig the AFFECTION  my friend tells me iam going to love her  my reaction be like!!  😂</div>", unsafe_allow_html=True)
        st.video("https://tamil.statusdp.com/videos/download/play/1WjOQnaTX1Te2F57zpTujDKfKJiXZiP1s-0.mp4",width=300)

    elif st.session_state.result == "M":
        st.image("https://media.tenor.com/T9RYQZNvqzMAAAAM/startamilchat-sanjay-chat.gif")
        st.markdown("<div class='blacktext'>my friend after seeing the MARRIAGE in flames in his dream </div>", unsafe_allow_html=True)
        st.video("https://d1itqg25xtlgws.cloudfront.net/videos/uIun5mYnohBGxsN14z8M7bQsI6H4sIIPa8kl3Y6d.mp4",width=700)

    elif st.session_state.result == "E":
        st.image("https://media1.tenor.com/m/3XocA2vPwQMAAAAC/star-tamil-chat-startamilchat.gif")
        st.markdown("<div class='blacktext'>my firend after seeing the ENEMY in the flames </div>", unsafe_allow_html=True)
        st.video("https://cdn-sc-g.sharechat.com/bd5223f_s1w/contents/sc_9392187596/compressed/mPRdKmmXPdTZlxY4GekdUejlGdKRWRilx7vk.mp4",width=300)

    elif st.session_state.result == "S":
        st.image("https://media.tenor.com/DA8ydLJreKEAAAAM/funny-tamil-comedy.gif")
        st.markdown("<div class='blacktext'>my firend after seeing the SIBILING  in the flamesG 😂</div>", unsafe_allow_html=True)
        st.video("https://tamil.statusdp.com/videos/download/play/1IVBM7jFgyZlh5jTxCddtEPGKygLKxFMK-0.mp4",width=300)

st.markdown("</div>", unsafe_allow_html=True)
