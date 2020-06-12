import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Grid from '@material-ui/core/Grid';
import ExpansionPanel from '@material-ui/core/ExpansionPanel';
import ExpansionPanelDetails from '@material-ui/core/ExpansionPanelDetails';
import ExpansionPanelSummary from '@material-ui/core/ExpansionPanelSummary';
import Typography from '@material-ui/core/Typography';
import ExpandMoreIcon from '@material-ui/icons/ExpandMore';
import useWindowDimensions from './windowDimensions.js'
import './QueueList.css'

/* const useStyles = makeStyles((theme) => ({
    root: {
        width: '50%',
    },
    heading: {
        fontSize: theme.typography.pxToRem(15),
        flexBasis: '33.33%',
        flexShrink: 0,
    },
    secondaryHeading: {
        fontSize: theme.typography.pxToRem(15),
        color: theme.palette.text.secondary,
    },
})); */

export default function QueueList() {
    // const classes = useStyles();
    const [expanded, setExpanded] = React.useState(false);
    const { width } = useWindowDimensions();

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

    const handleChange = (panel) => (event, isExpanded) => {
        setExpanded(isExpanded ? panel : false);
    };

    return (
        <div className="container">
            {patients.map((person, key) => {
                return(
                    <ExpansionPanel expanded={expanded === key} onChange={handleChange(key)}>
                        <ExpansionPanelSummary
                            expandIcon={<ExpandMoreIcon />}
                            aria-controls="panel1bh-content"
                            id="panel1bh-header"
                        >
                        <Grid className={ width > 768 ? "desktop-header" : "mobile-header"}>
                            <Typography>{person['name']}</Typography>
                            {width > 768 && <Typography></Typography>}
                        </Grid>
                    </ExpansionPanelSummary>
                    <ExpansionPanelDetails>
                        <div>
                            {Object.keys(person).map((key) => {
                                return (
                                    <div>
                                        <Typography className="patient-info"><b>{key}</b>: {person[key]}</Typography>
                                    </div>
                                )
                            })}
                        </div>
                    </ExpansionPanelDetails>
                </ExpansionPanel>
                )})}
        </div>
    );
}