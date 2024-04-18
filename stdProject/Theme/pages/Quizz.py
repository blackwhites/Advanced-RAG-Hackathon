import streamlit as st
import os
import time
import glob
from gtts import gTTS
from googletrans import Translator

try:
    os.mkdir("temp")
except:
    pass

translator = Translator()

out_lang = st.selectbox(
    "Select your output language",
    ("English", "Hindi", "Bengali", "Korean", "Chinese", "Japanese"),
)
if out_lang == "English":
    output_language = "en"
elif out_lang == "Hindi":
    output_language = "hi"
elif out_lang == "Bengali":
    output_language = "bn"
elif out_lang == "Korean":
    output_language = "ko"
elif out_lang == "Chinese":
    output_language = "zh-cn"
elif out_lang == "Japanese":
    output_language = "ja"

english_accent = st.selectbox(
    "Select your English accent",
    (
        "Default",
        "India",
        "United Kingdom",
        "United States",
        "Canada",
        "Australia",
        "Ireland",
        "South Africa",
    ),
)

if english_accent == "Default":
    tld = "com"
elif english_accent == "India":
    tld = "co.in"
elif english_accent == "United Kingdom":
    tld = "co.uk"
elif english_accent == "United States":
    tld = "com"
elif english_accent == "Canada":
    tld = "ca"
elif english_accent == "Australia":
    tld = "com.au"
elif english_accent == "Ireland":
    tld = "ie"
elif english_accent == "South Africa":
    tld = "co.za"


def text_to_speech(output_language, text, tld):
    tts = gTTS(text, lang=output_language, tld=tld, slow=False)
    try:
        my_file_name = text[0:20]
    except:
        my_file_name = "audio"
    tts.save(f"temp/{my_file_name}.mp3")
    return my_file_name


def remove_files(n):
    mp3_files = glob.glob("temp/*mp3")
    if len(mp3_files) != 0:
        now = time.time()
        n_days = n * 86400
        for f in mp3_files:
            if os.stat(f).st_mtime < now - n_days:
                os.remove(f)
                print("Deleted ", f)


remove_files(7)

st.markdown("<h1 style='color: #611349;'>📋 Quiz Time</h1>", unsafe_allow_html=True)
st.markdown('<h2 style="color: #611349;">🧠 Test your knowledge!</h2>', unsafe_allow_html=True)



# Radio buttons for the user to select "Yes" or "No"
user_response8 = st.radio("1: Do you know which month is dedicated to raising awareness about sexually transmitted diseases?", ("Yes", "No"))

if user_response8 == "Yes":
    st.write("")
else:
    # Show the response only when the user selects "No"
    response8 = "STDs Awareness Month is April and it's an important time to educate ourselves and others about preventing and managing sexually transmitted diseases. It's a great opportunity to learn more and raise awareness!"
    # Translate response to the selected language
    translation8 = translator.translate(response8, src='en', dest=output_language)
    translated_response8 = translation8.text
    # Convert the translated response to speech
    tts_response8 = gTTS(translated_response8, lang=output_language, tld=tld, slow=False)
    tts_response8.save(f"temp/std_awareness_response.mp3")
    # Play the audio when the user selects "No"
    audio_file_response8 = open("temp/std_awareness_response.mp3", "rb")
    audio_bytes_response8 = audio_file_response8.read()
    st.audio(audio_bytes_response8, format="audio/mp3", start_time=0)
    # Display the translated response
    st.write(translated_response8, unsafe_allow_html=True)







# Radio buttons for the user to select "Yes" or "No"
user_response = st.radio("2: Do you know what STDs stands for?", ("A)STDs stands for Systematic Transmitted Diseases, indicating diseases that affect multiple systems in the body", "B) STDs stands for Sexually Transmitted Diseases, which are infections transmitted through sexual activity","C) STDs stands for Sterile Transmitted Disorders, suggesting conditions that result in infertility"))

if user_response == "B) STDs stands for Sexually Transmitted Diseases, which are infections transmitted through sexual activity":
    response = "STDs stands for Sexually Transmitted Diseases. These are infections that can be passed from one person to another through sexual contact. It's important to know about STDs so you can protect yourself and your partner."
    # Translate response to the selected language
    translation = translator.translate(response, src='en', dest=output_language)
    translated_response = translation.text
    # Convert the translated response to speech
    tts_response = gTTS(translated_response, lang=output_language, tld=tld, slow=False)
    tts_response.save(f"temp/std_cure_response.mp3")
    # Play the audio
    audio_file_response = open("temp/std_cure_response.mp3", "rb")
    audio_bytes_response = audio_file_response.read()
    st.audio(audio_bytes_response, format="audio/mp3", start_time=0)
    # Display the translated response
    st.write(translated_response, unsafe_allow_html=True)







# Radio buttons for the user to select "Yes" or "No"
user_response4 = st.radio("3: Do you know what HIV/AIDS is?", ("Yes", "No"))

if user_response4 == "Yes":
    st.write("")
else:
    # Show the response only when the user selects "No"
    response4 = "HIV/AIDS is a viral infection that attacks the body's immune system, leading to AIDS if untreated."
    # Translate response to the selected language
    translation4 = translator.translate(response4, src='en', dest=output_language)
    translated_response4 = translation4.text
    # Convert the translated response to speech
    tts_response4 = gTTS(translated_response4, lang=output_language, tld=tld, slow=False)
    tts_response4.save(f"temp/hiv_response.mp3")
    # Play the audio when the user selects "No"
    audio_file_response4 = open("temp/hiv_response.mp3", "rb")
    audio_bytes_response4 = audio_file_response4.read()
    st.audio(audio_bytes_response4, format="audio/mp3", start_time=0)
    # Display the translated response
    st.write(translated_response4, unsafe_allow_html=True)





user_response2 = st.radio("4: Do you know how HIV is transmitted?", ("Yes", "No"))

if user_response2 == "Yes":
    st.write("")
else:
    # Show the response only when the user selects "No"
    # Assuming English as the default output language
    response2 = "Human Immunodeficiency Virus (HIV) is primarily transmitted through unprotected sexual intercourse, contaminated blood transfusions, hypodermic needles, and from mother to child during childbirth or breastfeeding."
    # Translate response to the selected language
    translation2 = translator.translate(response2, src='en', dest=output_language)
    translated_response2 = translation2.text
    # Convert the translated response to speech
    tts_response2 = gTTS(translated_response2, lang=output_language, tld=tld, slow=False)
    tts_response2.save(f"temp/hiv_response.mp3")
    # Play the audio when the user selects "No"
    audio_file_response2 = open("temp/hiv_response.mp3", "rb")
    audio_bytes_response2 = audio_file_response2.read()
    st.audio(audio_bytes_response2, format="audio/mp3", start_time=0)
    # Display the translated response
    st.write(translated_response2, unsafe_allow_html=True)
  




user_response = st.radio("5: What is contraception?", ("A) Healthy habits like eating well and exercising", 
                                                    "B)Special vitamins", 
                                                    "C) Contraception, also known as birth control, refers to methods or devices used to prevent pregnancy."))

if user_response == "C) Contraception, also known as birth control, refers to methods or devices used to prevent pregnancy.":
    response = "Correct! Contraception, also known as birth control, encompasses a wide range of methods to prevent unwanted pregnancy,It's important to remember that while some contraceptive methods offer partial protection against sexually transmitted infections (STDs), they aren't foolproof."
    # Translate response to the selected language
    translation = translator.translate(response, src='en', dest=output_language)
    translated_response = translation.text
    # Convert the translated response to speech
    tts_response = gTTS(translated_response, lang=output_language, tld=tld, slow=False)
    tts_response.save(f"temp/std_cure_response.mp3")
    # Play the audio
    audio_file_response = open("temp/std_cure_response.mp3", "rb")
    audio_bytes_response = audio_file_response.read()
    st.audio(audio_bytes_response, format="audio/mp3", start_time=0)
    # Display the translated response
    st.write(translated_response, unsafe_allow_html=True)




# Radio buttons for the user to select "Yes" or "No"
user_response7 = st.radio("6: Do you know about common symptoms of sexually transmitted diseases (STDs)?", ("Yes", "No"))

if user_response7 == "Yes":
    st.write("")
else:
    # Show the response only when the user selects "No"
    response7 = "Common symptoms of STDs can include things like unusual discharge, discomfort when using the bathroom, and itching or irritation in intimate areas. It's always good to stay informed and take care of your health!"
    # Translate response to the selected language
    translation7 = translator.translate(response7, src='en', dest=output_language)
    translated_response7 = translation7.text
    # Convert the translated response to speech
    tts_response7 = gTTS(translated_response7, lang=output_language, tld=tld, slow=False)
    tts_response7.save(f"temp/std_symptoms_response.mp3")
    # Play the audio when the user selects "No"
    audio_file_response7 = open("temp/std_symptoms_response.mp3", "rb")
    audio_bytes_response7 = audio_file_response7.read()
    st.audio(audio_bytes_response7, format="audio/mp3", start_time=0)
    # Display the translated response
    st.write(translated_response7, unsafe_allow_html=True)



user_response = st.radio("7: Do you think STDs can be cured?",
                         ( "A) No, STDs are incurable diseases.",
                          "B) No, once infected, STDs cannot be cured completely.",
                          "C) Yes, while not all STDs are curable, many can be effectively treated and managed with medical intervention."))


# Play the audio if the user chooses the correct response (Option C)
if user_response == "C) Yes, while not all STDs are curable, many can be effectively treated and managed with medical intervention.":
    response = "Correct! The curability of STDs depends on the culprit. Bacterial STDs can often be completely eradicated with antibiotics if diagnosed promptly. However, viral STDs currently lack a cure."
    # Translate response to the selected language
    translation = translator.translate(response, src='en', dest=output_language)
    translated_response = translation.text
    # Convert the translated response to speech
    tts_response = gTTS(translated_response, lang=output_language, tld=tld, slow=False)
    tts_response.save(f"temp/std_cure_response.mp3")
    # Play the audio
    audio_file_response = open("temp/std_cure_response.mp3", "rb")
    audio_bytes_response = audio_file_response.read()
    st.audio(audio_bytes_response, format="audio/mp3", start_time=0)
    # Display the translated response
    st.write(translated_response, unsafe_allow_html=True)


