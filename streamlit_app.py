
import streamlit as st 

# -------- CSS --------
st.markdown("""
<style>

/* STREAMLIT BACKGROUND FIX */
.stApp {
background-color: #ffb6c1;
}

/* Title */
.title{
text-align:center;
font-size:40px;
font-weight:bold;
color:white;
text-shadow:2px 2px #ff3366;
}

/* Card */
.card{
background:white;
padding:25px;
border-radius:20px;
box-shadow:0px 0px 15px rgba(0,0,0,0.2);
}

/* Result box */
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

/* Pulse animation */
@keyframes pulse{
from{transform:scale(1);}
to{transform:scale(1.05);}
}

/* Floating hearts */
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

    result = flames[0]

    meaning = {
        "F": f"{name1} {name2} you both are Friends 👫",
       
        "L":f"{name1} {name2}  Yyou both have Love 💘   ** THAMBI THAPICHUTA PAA **",
        "A": f"{name1} {name2} you both have Affection 💞  **SOLRATHUKU ONU ILAA**",
        "M":f"{name1} {name2} you will get Marriage 💍 😘",
        "E":f"{name1} {name2} you both are  Enemy 👿 *SOOLI MUDICHUPOCHU* ",
        "S":f"{name1} {name2} you both are Sibling  💗 *SONABATHA POCHA*  "
    }
    

    st.markdown(f"<div class='result'>{meaning[result]}</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)
