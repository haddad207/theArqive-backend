import React, {Component, useState} from 'react';
import TextField from '@material-ui/core/TextField';
import axios from 'axios';
import { useSelector, useDispatch, useStore } from "react-redux";

export default function ForgotPassword() {
    const [email, setEmail] = useState('');
    const [showError, setShowError] = useState(false);
    const [messageFromServer, setMessageFromServer] = useState('');
    // show null error?

    const sendEmail = e => {
        e.preventDefault();
        if (email === '') {
            setShowError(false);
            setMessageFromServer('');
        } else {
            axios
                .post('/api/password_reset/', {
                    email: email,
                })
                .then(response => {
                    if(response.data.toString().includes("object")){
                        window.alert("An e-mail has been sent with a link to change your password")
                    }
                    if (response.data === 'email not in db') {
                        setShowError(true);
                        setMessageFromServer('');
                    } else if (response.data === 'recovery email sent') {
                        setShowError(false);
                        setMessageFromServer('recovery email sent');
                    }
                })
                .catch(error => {
                    console.log(error.data);
                });
        }
    };

     return (
            <div className="col-md-6 m-auto">
                <div className="card card-body mt-5">
                    <h2 className="text-center">Forgot Password</h2>
                    <form className="profile-form" onSubmit={sendEmail}>
                        <div className="form-group">
                            <p>
                                Please input your e-mail:
                            </p>
                        <TextField
                            id='email'
                            label='E-mail'
                            value={email}
                            onChange={(e) => setEmail(e.target.value)} // not sure about this part
                            placeholder="Email Address"
                        />
                        </div>
                        <button
                            type="submit"
                            className="btn btn-primary float-left"
                        >
                            Forgot Password
                        </button>
                    </form>
                    {showNullError && ( //   ???????
                        <div>
                            <p className="text-danger">*You must input a email address </p>
                        </div>
                    )}
                    {showError && (
                        <div>
                            <p className="text-danger">
                                *That email address doesn't exist, please try again or register for a new account
                            </p>
                        </div>
                    )}
                    {messageFromServer === 'recovery email sent' && (
                        <div>
                            <h3>Password Reset Email Sent Successfully!</h3>
                        </div>
                    )}
                </div>
            </div>

        )

}