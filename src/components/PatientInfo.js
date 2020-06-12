import React from 'react'
import { Grid, Card } from '@material-ui/core';
import './QueueList.css'

export default function PatientInfo(props) {
    const patient = props.currentPatient;
    return(
        <Grid className="container">
            { patient !== null && <Card> {patient.name} </Card> }
        </Grid>
    )
}