import React, { useState } from 'react'
import { Grid, AppBar, Toolbar, Button } from '@material-ui/core';
import { NewButton, PatientInfo, QueueList } from '../components';

export default function Content() {
    const patients = [
        {
            'name': 'Jeremy Lim', 'age': 20, 'telephone': '0478 893 328', 'emergency': '0482 162 538',
            'medicare': '1872 2727 1762 7348', 'status': 'waiting', 'doctor': 'Doctor McDoctorface',
            'diseases': ['Cancer', 'Diabetes', 'AIDS'], 'notes': 'N/A'
        },
        {
            'name': 'Haesun Shim', 'age': 22, 'telephone': '0427 173 283', 'emergency': '0482 267 373',
            'medicare': '2734 1883 4327 2983', 'status': 'waiting', 'doctor': 'Doctor McDoctorface',
            'diseases': ['Back Pain', 'Leprosy', 'AIDS'], 'notes': 'N/A'
        },
        {
            'name': 'Sandeep Das', 'age': 20, 'telephone': '0418 389 374', 'emergency': '0472 374 127',
            'medicare': '1739 2784 5903 6830', 'status': 'specialist', 'doctor': 'Doctor McDoctorface',
            'diseases': ['Ebola', 'COVID-19'], 'notes': 'N/A'
        }
    ]

    function nextPatient(patient) {
        if (patient === null) {
            return;
        }
        setCurrent(patient);
        const patients = queue;
        patients.shift();
        setShow('profile');
        if (patients.length === 0) {
            setQ(null);
            return;
        }
        setQ(patients);
        console.log(patients)
    };

    function progressPatient(name) {
        // adds patient to next queue
        setCurrent(null);
        setShow('queue');
    };

    function changePermissions(name) {
        setPermission(name);
        setShow('queue');
    };

    const [permission, setPermission] = useState(null);
    const [currPatient, setCurrent] = useState(null);
    const [show, setShow] = useState('home');
    const [queue, setQ] = useState(patients);
    return(
        <Grid>
            <AppBar position="static">
                <Toolbar>
                    {permission === null && <Button color="inherit" onClick={() => {
                        setShow('home');
                    }}>Home</Button>}
                    {permission !== null && <Button color="inherit" onClick={() => {
                        setShow('queue');
                    }}>Queue</Button>}
                    {currPatient !== null && <Button color="inherit" onClick={() => {
                        setShow('profile');
                    }}>Profile</Button>}
                </Toolbar>
            </AppBar>
            <p>{show}</p>
            {show === 'queue' && currPatient === null && queue !== null && <NewButton name="Next Person" onClick={() => {
                nextPatient(queue[0]);
            }}></NewButton>}
            {show === 'home' && <NewButton name="GP" onClick={() => {
                changePermissions('gp');
            }}></NewButton>}
            {show === 'home' && <NewButton name="Specialist" onClick={() => {
                changePermissions('specialist');
            }}></NewButton>}
            {show === 'home' && <NewButton name="Surgeon" onClick={() => {
                changePermissions('surgeon');
            }}></NewButton>}
            {show === 'queue' && <QueueList type={permission} patients={queue}></QueueList>}
            {show === 'profile' && currPatient !== null && <NewButton name="Finish Consultation" onClick={() => {
                progressPatient();
            }}></NewButton>}
            {show === 'profile' && <PatientInfo currentPatient={currPatient}></PatientInfo>}
        </Grid> 
    )
}