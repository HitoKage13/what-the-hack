import React, { useState } from 'react'
import { Grid } from '@material-ui/core';
import { NavBar, QueueList } from '../components';

export default function Content() {
    const [permission, setPermission] = useState();
    const [show, setShow] = useState('home');
    return(
        <Grid>
            <NavBar></NavBar>
            <QueueList type={permission}></QueueList>
        </Grid>
    )
}