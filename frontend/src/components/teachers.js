import React, { Component} from 'react';
// import {Link, useNavigate} from 'react-router-dom';



class Teachers extends Component {

    
    
    state = {
        teachers: []
    }

    loadTeachers = () => {
        // console.log(this.props.token)
        // const navigate = useNavigate();
        fetch('http://127.0.0.1:8000/account/teacher/list/',{
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
                Authorization: 'Token '+ this.props.token
            },  
            body: JSON.stringify(this.state.credentials)
        })
        .then( data => data.json() )
        .then(
            data =>{
                this.setState({teachers: data})
                console.log(this.props.role)
            }
        ).catch( 
            error => console.error(error),
        )

        // useEffect(() => {
        //     if (this.state.teachers == null) {
        //       navigate("/login");
        //     }
        //   },[this.state.teachers]);
    }

    render(){

        
            return (
            <div>
                {/* <h1>{this.props.users}</h1> */}
                <table align='center' border='1px solid'>
                    <thead>
                        <td border='1px solid' colSpan='3'><h1>Teachers</h1></td>
                    </thead>
                    <tbody>
                        { this.state.teachers.map( teacher => {
                    return <td> <h3 key={teacher.id}>{teacher.teacher_name}</h3></td>
                    })}
                        
                    </tbody>
                </table>
                
                
                <button onClick={this.loadTeachers}>Load Teachers</button>
            </div>
        );
        
        
    }
    
}

export default Teachers;
