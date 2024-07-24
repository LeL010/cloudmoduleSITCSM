import React, { Component } from 'react';
import '../App.css';

class KommunicateChat extends Component {
  componentDidMount(){
    (function(d, m){
        var kommunicateSettings = {
            "appId":"2aba7cf041c4ba9aabeb083b46e91bd54",
            "popupWidget":true,
            "automaticChatOpenOnNavigation":true,
            "attachment": false,
            "locShare": true,
            "restartConversationByUser": true,
            "voiceInput": true,
            "voiceOutput": true
            };
        var s = document.createElement("script"); s.type = "text/javascript"; s.async = true;
        s.src = "https://widget.kommunicate.io/v2/kommunicate.app";
        var h = document.getElementsByTagName("head")[0]; h.appendChild(s);
        window.kommunicate = m; m._globals = kommunicateSettings;
      })(document, window.kommunicate || {});
}

  render() {
    return (
      <div className="section">
        <div className="container">
          <h1 className="title">Welcome to Our Chatbot</h1>
          <div id="chat-widget" />
        </div>
      </div>
    );
  }
}

export default KommunicateChat;

