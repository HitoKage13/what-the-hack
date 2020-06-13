import React, { useState, useEffect, useCallback } from 'react'
import QRCode from 'qrcode.react'
import { Grid, AppBar, Toolbar, Button } from '@material-ui/core';
import { NewButton, PatientInfo, Scanner, QueueList } from '../components';
import Axios from 'axios';

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
    const [qr, setQr] = useState(null);
    const [currPatient, setCurrent] = useState(null);
    const [show, setShow] = useState('home');
    const [queue, setQ] = useState([]);
    const [gpQueue, setG] = useState([]);
    const [spQueue, setSp] = useState([]);
    const [suQueue, setSu] = useState([]);

    useEffect(() => {
        fetch('/queue?name=GP').then(res => res.json()).then(data => {
            setG(data.patients);
        });
        fetch('/queue?name=Specialist').then(res => res.json()).then(data => {
            setSp(data.patients);
        });
        fetch('/queue?name=Surgeon').then(res => res.json()).then(data => {
            setSu(data.patients);
        });
    }, []);

    /* function BEInfo() {
        fetch('/patient/id='+qr).then(res => res.json()).then(data => {
            console.log(data);
            setCurrent(data);
        });
    } */

    // sets the current queue
    function setCurrentQueue(name) {
        if (name === null) {
            setQ([]);
        } else if (name === 'GP') {
            setQ(gpQueue);
        } else if (name === 'Specialist') {
            setQ(spQueue);
        } else if (name === 'Surgeon') {
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

    // updates their info
    function updateInfo() {
        // adds patient to next queue
    };

    // uses scanner to set patient info
    function getPatientInfo(qr) {
        setQr(qr);
        alert("The patient: " + qr + " has been scanned and added into the system");
    }

    // progress patient to the next queue
    function progressPatient(queue) {
        setShow('send');
    };

    // move patient to the next queue
    function movePatient(queue) {
        var newList = []
        if (queue === 'GP') {
            newList = gpQueue;
            newList.push(currPatient)
            setG(newList)
        } else if (queue === 'Specialist') {
            newList = spQueue;
            newList.push(currPatient)
            setSp(newList)
        } else if (queue === 'Surgeon') {
            newList = suQueue;
            newList.push(currPatient)
            setSu(newList)  
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
                    }}>Queue</Button>}
                    {currPatient !== null && <Button color="inherit" onClick={() => {
                        setShow('profile');
                    }}>Profile</Button>}
                </Toolbar>
            </AppBar>
            <div style={{padding: '1%'}}></div>
            {show === 'queue' && currPatient === null && queue.length > 0 && <NewButton name="Next Person" onClick={() => {
                nextPatient(queue[0]);
            }}></NewButton>}
            {show === 'home' && <div style={{
                display: 'flex',
                justifyContent: 'center'
            }}><Scanner result={getPatientInfo}></Scanner></div>}
            <p>{qr}</p>
            {show === 'home' && <NewButton name="GP" onClick={() => {
                changePermissions('GP');
                setQr(null);
            }}></NewButton>}
            {show === 'home' && <NewButton name="Specialist" onClick={() => {
                changePermissions('Specialist');
                setQr(null);
            }}></NewButton>}
            {show === 'home' && <NewButton name="Surgeon" onClick={() => {
                changePermissions('Surgeon');
                setQr(null);
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
            {show === 'send' && permission !== 'GP' && <NewButton name="GP" onClick={() => {
                movePatient('GP');
            }}></NewButton>}
            {show === 'send' && permission !== 'Specialist' && <NewButton name="Specialist" onClick={() => {
                movePatient('Specialist');
            }}></NewButton>}
            {show === 'send' && permission !== 'Surgeon' && <NewButton name="Surgeon" onClick={() => {
                movePatient('Surgeon');
            }}></NewButton>}
            {show === 'send' && <NewButton name="End" onClick={() => {
                movePatient('end');
            }}></NewButton>}
        </Grid> 
    )
}