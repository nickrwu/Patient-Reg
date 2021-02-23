import React, { Component } from 'react';
import './App.css';
import FormSuccess from "./components/FormSuccess";

import axios from "axios";


import setHours from "date-fns/setHours";
import setMinutes from "date-fns/setMinutes";
import DatePicker from "react-datepicker";
import "react-datepicker/dist/react-datepicker.css";

class App extends Component{
  constructor(props) {
    super(props);

    this.state = {
      showSuccess: false,
      photo_license: null,
      date_store:"",
      datetime_store:"",
      activeInfo:{
        id: null,
        firstname: "",
        lastname: "",
        dob: "",
        phone: "",
        email: "",
        street: "",
        city: "",
        state: "",
        zipcode: "",
        appointment: "",
      },
    }
    
    this.handleDateChange = this.handleDateChange.bind(this)
    this.handleImageChange = this.handleImageChange.bind(this)
    this.handleChange = this.handleChange.bind(this)
    this.handleSubmit = this.handleSubmit.bind(this)
  };

  componentDidMount() {
    document.title = 'Patient Registration';
  }

  handleChange = (e) => {
    this.setState({activeInfo:{
      ...this.state.activeInfo,
      [e.target.name]: e.target.value
      }
    });
  };

  handleDateChange = (date, name) => {
    let current_date = date
    
    // Date Store
    if (name == 'dob'){
      let formatted_date = current_date.getFullYear()+ "-" + (current_date.getMonth() + 1) + "-" + current_date.getDate()
      this.setState({ date_store: date, activeInfo: { 
        ...this.state.activeInfo,
        [name]: formatted_date
        }
      });
    }
    
    // Date Time Store
    else if (name == 'appointment'){
      let formatted_datetime = current_date.getFullYear() + "-" + (current_date.getMonth() + 1) + "-" + current_date.getDate() + " " + current_date.getHours() + ":" + current_date.getMinutes() + ":00"
      this.setState({ datetime_store: date, activeInfo: { 
        ...this.state.activeInfo,
        [name]: formatted_datetime
        }
      });
    }
  }

  handleImageChange = (e) => {
    this.setState({
      photo_license: e.target.files[0]
    });
  };

  handleSubmit = (e) => {
    e.preventDefault();
    
    let url = "http://127.0.0.1:8000/api/patients/"

    let form_data = new FormData();

    for ( var key in this.state.activeInfo) {
      form_data.append(key, this.state.activeInfo[key]);
    }

    if (this.state.photo_license != null){
      form_data.append('photo_license', this.state.photo_license, this.state.photo_license.name);
    }

    axios(url, {
      method: 'POST',
      headers: { 'Content-Type': 'multipart/form-data' },
      data: form_data
    }).then((response) => {
      console.log(response)
      this.setState({
        // After submit -> Clear info
        showSuccess: !this.state.showSuccess,
        date_store:"",
        datetime_store:"",
        photo_license: null,
        activeInfo:{
          id: null,
          firstname: "",
          lastname: "",
          description: "",
          dob: "",
          phone: "",
          email: "",
          street: "",
          city: "",
          state: "",
          zipcode: "",
          appointment: "",
        }
      })
    }).catch(error => console.log('ERROR: ', error.message))
  };

  toggle = () => {
    this.setState({ showSuccess: !this.state.showSuccess });
  };

  render(){
    // Set Available Appointment Days
    const includeDatesArray = [new Date('2021-02-25'), new Date('2021-03-02')]
    
    // Set Available Appointment TImes
    const includeTimesArray = [
        setHours(setMinutes(includeDatesArray[0], 0), 12), 
        setHours(setMinutes(includeDatesArray[0], 0), 15),
        setHours(setMinutes(includeDatesArray[1], 30), 11),
        setHours(setMinutes(includeDatesArray[1], 0), 16),
      ]

    return(
      <div className="container">
        <h1 className="text-white text-center my-4">done.</h1>
        <div id="patient-container">
          <div id="form-wrapper">
          <h2 className="text-black text-center"> Patient Appointment Form</h2>
            
            {/* Form Code Begins */}
            <form onSubmit={this.handleSubmit} id="form" className="form-inline-block justify-content-center">
              <div className="row form-group" id="personalRow">
                <div className="col">
                  <section>
                    <label className="required-field"> First Name </label>
                    <input 
                      onChange={this.handleChange}
                      value={this.state.activeInfo.firstname} 
                      className="form-control" 
                      id="firstname" 
                      type="text" 
                      name="firstname" 
                      placeholder="First Name" 
                      maxLength="30" 
                      required
                    />
                  </section>

                  <section>
                    <label className="required-field"> Date of Birth </label>
                    <DatePicker 
                      onChange={(date) => this.handleDateChange(date, 'dob')} 
                      selected={this.state.date_store}
                      className="form-control"
                      id="dob"
                      name="dob"
                      placeholderText="yyyy-mm-dd" 
                      dateFormat="yyyy-MM-dd"
                      required
                    />
                  </section>
                </div>  
                
                <div className="col">
                  <section>
                    <label className="required-field"> Last Name </label>
                    <input 
                      onChange={this.handleChange} 
                      value={this.state.activeInfo.lastname} 
                      className="form-control" 
                      id="lastname" 
                      type="text" 
                      name="lastname" 
                      placeholder="Last Name" 
                      maxLength="30" 
                      required
                    />
                  </section>
                </div>
              </div>

              <div className="row form-group" id="contactRow">
                <div className="col">
                <section>
                    <label> Phone </label>
                    <input 
                      onChange={this.handleChange} 
                      value={this.state.activeInfo.phone} 
                      className="form-control" 
                      id="phone" 
                      type="text" 
                      name="phone" 
                      placeholder="xxx-xxx-xxxx"
                    />
                  </section>
                </div>

                <div className="col">
                  <section>
                    <label className="required-field"> Email Address </label>
                    <input 
                      onChange={this.handleChange} 
                      value={this.state.activeInfo.email} 
                      className="form-control" 
                      id="email" 
                      type="email" 
                      name="email" 
                      placeholder="Email Address"
                      required
                    />
                  </section>
                </div>
              </div>
                
              <div className="row form-group" id="addressRow">
                <div className="col">
                  <section>
                    <label className="required-field"> Street Address </label>
                    <input 
                      onChange={this.handleChange} 
                      value={this.state.activeInfo.street} 
                      className="form-control" 
                      id="street" 
                      type="text" 
                      name="street" 
                      placeholder="Street Address"
                      required
                    />
                  </section>

                  <section>
                    <label className="required-field"> City </label>
                    <input 
                      onChange={this.handleChange} 
                      value={this.state.activeInfo.city} 
                      className="form-control" 
                      id="city" 
                      type="text" 
                      name="city" 
                      placeholder="City"
                      required
                    />
                  </section>
                </div>

                <div className="col">
                  <section>
                    <label className="required-field"> State </label>
                    <input 
                      onChange={this.handleChange} 
                      value={this.state.activeInfo.state} 
                      className="form-control" 
                      id="state" 
                      type="text" 
                      name="state" 
                      placeholder="State" 
                      maxLength="2"
                      required
                    />
                  </section>

                  <section>
                    <label className="required-field"> Postal Code </label>
                    <input 
                      onChange={this.handleChange} 
                      value={this.state.activeInfo.zipcode} 
                      className="form-control" id="zipcode" 
                      type="text" 
                      name="zipcode" 
                      placeholder="Postal Code" 
                      maxLength="5"
                      pattern="[\d]{5}"
                      required
                    />
                  </section>
                </div>
              </div>

              <div className="row" id="miscRow">
                <div className="col">
                  <section>
                    <label className="required-field"> Appointment Time </label>
                    <DatePicker 
                      onChange={(date) => this.handleDateChange(date, 'appointment')} 
                      selected={this.state.datetime_store}
                      className="form-control"
                      id="appointment"
                      name="appointment"

                      showTimeSelect
                      includeDates={includeDatesArray}
                      includeTimes={includeTimesArray}

                      placeholderText="yyyy-mm-dd HH:MM:00" 
                      dateFormat="yyyy-MM-dd HH:mm:00"
                      required
                    />
                  </section>
                </div>

                <div className="col" id="upload">
                  <section>
                    <label className="required-field"> Upload Drivers License </label>
                    <input 
                      onChange={this.handleImageChange} 
                      id="photo" 
                      type="file" 
                      name="photo"
                      accept="image/png, image/jpeg"
                      required
                    />
                  </section>
                </div>
              </div>
              
              <div className="row">
                <div style={{flex: 1}}> {/* Submit Button */}
                  <input id="submit" className="btn btn-warning" type="submit" name="submit" ></input>
                </div>
              </div>
            </form>
            {/* Form Code Ends */}

          </div>
        </div>

        {this.state.showSuccess ? (
              <FormSuccess
                toggle={this.toggle}
              />
              ) : null}

      </div>
    )
  }
}



export default App;