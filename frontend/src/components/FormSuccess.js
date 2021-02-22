import React, { Component } from "react";
import {
    Button,
    Modal,
    ModalHeader,
    ModalBody,
  } from "reactstrap";

export default class FormSuccess extends Component {
    constructor(props) {
        super(props);
    }

    render() {
        const { toggle } = this.props;

        return(
            <Modal isOpen={true} toggle={toggle}>
                <ModalHeader toggle={toggle}> Success! Appointment Submitted </ModalHeader>
                <ModalBody><Button id="back" onClick={() => toggle()}>Back</Button></ModalBody>
            </Modal>
        );
    }  
};