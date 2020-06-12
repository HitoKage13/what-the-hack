import React, { useState } from 'react'
import QrReader from 'react-qr-scanner'

export default function Scanner(props) {
    const [delay, setDelay] = useState(100);
    const [result, setResult] = useState(null);
    const previewStyle = {
        height: 240,
        width: 320,
    }

    function handleScan(data) {
        if (data !== null) {
            props.result(data);
        }
        setResult(data);
    }

    function handleError(err) {
        console.error(err)
    }

    return (
        <div>
            <QrReader
                delay={delay}
                style={previewStyle}
                onError={handleError}
                onScan={handleScan}
            />
            <p>{result}</p>
        </div>
    )
}