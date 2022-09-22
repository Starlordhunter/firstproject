import React, { Component} from 'react';
// import Teachers from './teachers';

class Login extends Component {

    state = {
        credentials: {email: '', password: ''},
        users: []
    }

    login = event =>{
        // console.log(this.state.credentials);
        fetch('http://127.0.0.1:8000/account/log-in/',{
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify(this.state.credentials)
        })
        .then( data => data.json() )
        .then(
            data =>{
                this.props.userLogin(data.token);
                this.props.userRole(data.user.profile.role);
                this.setState({users: data.user});
            }
        ).catch( error => console.error(error))
    }

    register = event =>{
        // console.log(this.state.credentials);
        fetch('http://127.0.0.1:8000/account/users/list/',{
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify(this.state.credentials)
        })
        .then( data => data.json() )
        .then(
            data =>{
                console.log(data.token);
            }
        )
        .catch( error => console.error(error))
    }

    inputChanged = event => {
        const cred = this.state.credentials;
        cred[event.target.name] = event.target.value;
        this.setState({credentials: cred});
    }

    render(){
        
        
        return (
            <div>
                {/* <Teachers data={this.state.users} /> */}
                <h1>Login User Form</h1>

                <label>
                    Email:
                    <input type='email' name='email'
                    value={this.state.credentials.username}
                    onChange={this.inputChanged} />
                </label>
                <br/>
                <label>
                    Password:
                    <input type='password' name='password' 
                    value={this.state.credentials.password}
                    onChange={this.inputChanged}/>
                </label>
                <br/>
                <button onClick={this.login}>Login</button>
                <button onClick={this.register}>Register</button>
            </div>
        );
    }
    
}

export default Login;
