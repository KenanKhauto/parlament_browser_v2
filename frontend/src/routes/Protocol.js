import React, { useState, useEffect } from "react";
import axios from "axios";
import { format } from "date-fns";
import { Link } from "react-router-dom";

const baseUrl = "http://localhost:5000";

function Protocol() {
  const [protocols, setProtocols] = useState([]);
  const [selectedProtocol, setSelectedProtocol] = useState(null);

  const fetchData = async () => {
    try {
      const response = await axios.get(`${baseUrl}/protocol-raw`);
      const { protocols } = response.data; // destructure
      setProtocols(protocols);
      console.log("DATA: ", protocols);
    } catch (error) {
      console.log(error);
    }
  };

  useEffect(() => {
    fetchData();
  }, []);

  const handleProtocolClick = (protocol) => {
    if (selectedProtocol === protocol) {
      setSelectedProtocol(null);
    } else {
      setSelectedProtocol(protocol);
    }
  };

  return (
    <div className="container">
      <div className="protocol-container">
        <h1 className="protocol-title">Protokolle: </h1>
        {protocols.length > 0 &&
          protocols.map((protocol) => (
            <div key={protocol._id}>
              <div
                className="protocol"
                onClick={() => handleProtocolClick(protocol)}
              >
                <div className="protocol-id">{protocol._id}</div>
                <div className="protocol-session">{protocol.session_title}</div>
                <div className="protocol-date">{protocol.date}</div>
                <div className="protocol-duration">{protocol.session_duration}</div>
                <div className="protocol-period">{protocol.legislative_period}</div>
              </div>
              {selectedProtocol === protocol && protocol.agenda_items && (
                <div className="agenda-items">
                  {protocol.agenda_items.map((agendaItem, index) => (
                    <div
                      className="agenda-item"
                      key={agendaItem._id}
                    >
                      <div>{agendaItem._id}</div>
                      <div>{agendaItem.title}</div>
                      <ul>
                        {agendaItem.table_of_contents.map((item) => (
                          <li key={item}>{item}</li>
                        ))}
                      </ul>
                    </div>
                  ))}
                </div>
              )}
            </div>
          ))}
      </div>
    </div>
  );
}

export default Protocol;
