package com.thejaxon.soapefecks;

import employeemgmt.services.EmployeeServiceImplementation;
import java.net.URL;
import java.util.ResourceBundle;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.Initializable;
import javafx.scene.control.Label;
import javax.xml.ws.Endpoint;

public class ServerController implements Initializable {

    @Override
    public void initialize(URL url, ResourceBundle rb) {
        Endpoint.publish("http://localhost:9000/any/name", new EmployeeServiceImplementation());
    }    
}
