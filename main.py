import streamlit as st
from streamlit_webrtc import webrtc_streamer, WebRtcMode, RTCConfiguration

RTC_CONFIGURATION = RTCConfiguration(
    {
        "iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]
    }
)

st.title("Video Call POC using Streamlit WebRTC")

# Instructions
st.write("""
    ## Instructions:
    1. Open this app in two different browser windows or on two different devices.
    2. Allow access to your camera and microphone when prompted.
    3. The video call should start automatically.
""")

# WebRTC streamer component
webrtc_streamer(
    key="video-call",
    mode=WebRtcMode.SENDRECV,
    rtc_configuration=RTC_CONFIGURATION,
    media_stream_constraints={
        "video": True,
        "audio": True,
    },
)

st.write("### Connected Users")
st.write("The connected users will appear here.")
