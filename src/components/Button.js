import React from 'react';
import Button from '@material-ui/core/Button';

export default function NewButton(props) {
    return(
        <Button variant="outlined" className="button" color="secondary" size="small" onClick={props.onClick}>{props.name}</Button>
    )
}