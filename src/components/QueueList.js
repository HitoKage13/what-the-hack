import React from 'react';
import { Grid } from '@material-ui/core';
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

export default function QueueList(props) {
    // const classes = useStyles();
    const [expanded, setExpanded] = React.useState(false);
    const { width } = useWindowDimensions();

    const handleChange = (panel) => (event, isExpanded) => {
        setExpanded(isExpanded ? panel : false);
    };

    const patients = props.patients;

    return (
        <div className="container">
            {patients !== null && patients.map((person, key) => {
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