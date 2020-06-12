import React, { useState, useEffect } from 'react'
import { Grid, AppBar, Toolbar, Button } from '@material-ui/core';
import { NewButton, PatientInfo, QueueList } from '../components';

export default function Content() {
    const patients = [
        {
            'name': 'Jeremy Lim', 'age': 20, 'telephone': '0478 893 328', 'emergency': '0482 162 538',
            'medicare': '1872 2727 1762 7348', 'status': 'waiting', 'doctor': 'Doctor McDoctorface',
            'diseases': ['Cancer', 'Diabetes', 'AIDS'], 'notes': 'N/A', 'priority': 'Emergency'
        },
        {
            'name': 'Haesun Shim', 'age': 22, 'telephone': '0427 173 283', 'emergency': '0482 267 373',
            'medicare': '2734 1883 4327 2983', 'status': 'waiting', 'doctor': 'Doctor McDoctorface',
            'diseases': ['Back Pain', 'Leprosy', 'AIDS'], 'notes': 'N/A', 'priority': 'Urgent'
        },
        {
            'name': 'Sandeep Das', 'age': 20, 'telephone': '0418 389 374', 'emergency': '0472 374 127',
            'medicare': '1739 2784 5903 6830', 'status': 'specialist', 'doctor': 'Doctor McDoctorface',
            'diseases': ['Ebola', 'COVID-19'], 'notes': 'N/A', 'priority': 'Non-Urgent'
        }
    ]

    const [permission, setPermission] = useState(null);
    const [currPatient, setCurrent] = useState(null);
    const [show, setShow] = useState('home');
    const [queue, setQ] = useState([]);
    const [memes, setMeme] = useState(0);
    let gpQueue = patients;
    let spQueue = [];
    let suQueue = [];

    useEffect(() => {
        fetch('/q').then(res => res.json()).then(data => {
            setMeme(data.hi);
        });
    }, []);

    // sets the current queue
    function setCurrentQueue(name) {
        if (name === null) {
            setQ([]);
        } else if (name === 'gp') {
            setQ(gpQueue);
        } else if (name === 'specialist') {
            setQ(spQueue);
        } else if (name === 'surgeon') {
            setQ(suQueue);
        }
    }

    // gets next patient from your queue
    function nextPatient(patient) {
        if (patient === null) {
            return;
        }
        setCurrent(patient);
        const newList = queue;
        newList.shift();
        setShow('profile');
        if (newList.length === 0) {
            setQ([]);
            return;
        }
        setQ(newList);
    };

    function updateInfo() {
        // adds patient to next queue
    };

    // progress patient to the next queue
    function progressPatient(queue) {
        setShow('send');
    };

    // move patient to the next queue
    function movePatient(queue) {
        if (queue === 'gp') {
            gpQueue.push(currPatient);
            
        } else if (queue === 'specialist') {
            spQueue.push(currPatient);
        } else if (queue === 'surgeon') {
            suQueue.push(currPatient);
        }
        setShow('queue');
        setCurrent(null);
    };

    // change to the doctor type
    function changePermissions(name) {
        setPermission(name);
        setCurrentQueue(name);
        setShow('queue');
    };

    return(
        <Grid>
            <AppBar position="static">
                <Toolbar>
                    {<Button color="inherit" onClick={() => {
                        setShow('home');
                    }}>Home</Button>}
                    {permission !== null && <Button color="inherit" onClick={() => {
                        setShow('queue');
                        console.log(gpQueue);
                        console.log(spQueue);
                        console.log(suQueue);
                    }}>Queue</Button>}
                    {currPatient !== null && <Button color="inherit" onClick={() => {
                        setShow('profile');
                    }}>Profile</Button>}
                </Toolbar>
            </AppBar>
            <p>{memes}</p>
            {show === 'queue' && currPatient === null && queue.length > 0 && <NewButton name="Next Person" onClick={() => {
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
            {show === 'profile' && currPatient !== null &&
            <Grid>
                <NewButton name="Update Info" onClick={() => {
                    updateInfo();
                }}></NewButton>
                <NewButton name="Finish Consultation" onClick={() => {
                progressPatient();
            }}></NewButton>
            </Grid>}
            {show === 'profile' && <PatientInfo currentPatient={currPatient}></PatientInfo>}
            {show === 'send' && permission !== 'gp' && <NewButton name="GP" onClick={() => {
                movePatient('gp');
            }}></NewButton>}
            {show === 'send' && permission !== 'specialist' && <NewButton name="Specialist" onClick={() => {
                movePatient('specialist');
            }}></NewButton>}
            {show === 'send' && permission !== 'surgeon' && <NewButton name="Surgeon" onClick={() => {
                movePatient('surgeon');
            }}></NewButton>}
            {show === 'send' && <NewButton name="End" onClick={() => {
                movePatient('end');
            }}></NewButton>}
        </Grid> 
    )
}