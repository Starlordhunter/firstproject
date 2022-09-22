import React, { Component} from 'react';

class Students extends Component {

    constructor(props) {
        super(props);
        this.state =({
          students: []
        })
      }


    loadStudents = () => {
        // console.log(this.props.token)
        fetch('http://127.0.0.1:8000/account/students/list/',{
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
                this.setState({students: data});
                console.log('date:', data[0])
                console.log('Successfully fetch')
            }

        ).catch( error => console.error(error))
    }

    render(){

        // console.log(this.state.students.Subject)
        // if( this.state.students.length > 0 ) {
        //     this.state.students.map(a=> {
        //         console.log('Subject:', a);
        //     });
        // }        
        
        // if(this.state.students && this.state.students.length>0)
        return (
            <div>
                <h1>Students</h1>
                <table align='center' border='1px solid'>
                    <tr>
                        <th>Class</th>
                        <th>Number of Students</th>
                        <th>Student in Class</th>
                    </tr>
                    
                        
                    {
                        this.state.students.map(a=>{
                            console.log(a)
                            return (
                                <>
                                <tr>
                                    <td >{a.class_name}</td>
                                    <td>{a.count_of_students}</td>
                                    <td>
                                    {   
                                        a.student_in_classes?.length ? 
                                        a.student_in_classes.map((b,i)=>{
                                        
                                        return (
                                            <>
                                                <h3 key={i}>{b.student_name}</h3>
                                                <td>
                                                {
                                                    b.subject_taken?.length ?
                                                    b.subject_taken.map((c,i)=> {
                                                        return (
                                                            <>
                                                                <ul>
                                                                    <li key={i}>{c.subject_name}</li>  
                                                                </ul>
                                                            </>
                                                            
                                                        );
                                                    })
                                                    :null
                                                }</td>
                                            </>
                                           
                                        );            
                                        })
                                        :null
                                    }</td>  
                                </tr>
                                </>
                            );
                        }    
                        )
                    }
                    
                </table>
                <div>
                    
                </div>
                <button onClick={this.loadStudents}>Load Students</button>
            </div>
        );

        // return (
        //     <div>
        //         <h1>Students</h1>
        //         { Array.from(this.state.students).map( student => {
        //             console.log(student)
        //             return (<h3>{student.subject_name}</h3>)
        //         })}
        //         <button onClick={this.loadStudents}>Load Students</button>
        //     </div>
        // );
    }
    
}

export default Students;
