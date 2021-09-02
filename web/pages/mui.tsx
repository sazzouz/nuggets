import { TextField } from '@material-ui/core';
import { makeStyles, mergeClasses } from '@material-ui/styles';
import { useState } from 'react';
import { Button } from '@material-ui/core';
import { KeyboardArrowRightOutlined } from '@material-ui/icons';
import Link from 'next/link';

const useStyles = makeStyles({
    field: {
        marginTop: 20,
        marginBottom: 20,
        display: 'block'
    }
});

export interface MuiProps {}

const Mui: React.SFC<MuiProps> = (props) => {
    const [title, setTitle] = useState('');
    const [details, setDetails] = useState('');
    const [titleError, setTitleError] = useState(false);
    const [detailsError, setDetailsError] = useState(false);
    const handleSubmit = (e) => {
        e.preventDefault();
        setTitleError(false);
        setDetailsError(false);

        if (title == '') {
            setTitleError(true);
        }

        if (details == '') {
            setDetailsError(true);
        }

        if (title && details) {
            console.log(title, details);
        }
    };

    const classes = useStyles();
    return (
        <>
            <Link href="/">Home</Link>
            <p>Material Sandbox</p>
            <hr />
            <div>&lt;</div>
            <iframe
                src="https://lean-ops.vercel.app/"
                frameborder="0"
                height="600"
                width="900"></iframe>
            <form>
                <div>
                    <label>Date:</label>
                    <input type="date" id="date" />
                    <br />
                    <label>Week:</label>
                    <input type="week" id="week" />
                    <br />
                    <label>Month:</label>
                    <input type="month" id="month" />
                    <br />
                    <label>Time:</label>
                    <input type="time" id="time" />
                    <br />
                    <label>Datetime:</label>
                    <input type="datetime" id="datetime" />
                    <br />
                    <label>Datetime Local:</label>
                    <input type="datetime-local" id="datetime-local" />
                    <br />
                    <label>Color:</label>
                    <input type="color" id="color" />
                    <br />
                    <label>Email:</label>
                    <input type="email" id="email" placeholder="email address" />
                    <br />
                    <label>Number:</label>
                    <input type="number" id="number" />
                    <br />
                    <label>Search:</label>
                    <input type="search" id="search" />
                    <br />
                    <label>Phone:</label>
                    <input type="tel" id="phone" placeholder="Phone Number" pattern="\d{10}$" />
                    <br />
                    <label>Range:</label>
                    <input type="range" id="range" />
                    <br />
                    <label>URL:</label>
                    <input type="url" id="url" />
                </div>
            </form>
            <math>
                <mrow>
                    <mrow>
                        <msup>
                            <mi> a </mi>
                            <mn> 2 </mn>
                        </msup>
                        <mo> + </mo>
                        <msup>
                            <mi> b </mi>
                            <mn> 2 </mn>
                        </msup>
                        <mo> + </mo>
                        <mn> 2 </mn>
                        <mn> a </mn>
                        <mn> b </mn>
                    </mrow>
                    <mo> = </mo>
                    <mn> 0 </mn>
                </mrow>
            </math>

            <form noValidate autoComplete="off" onSubmit={handleSubmit}>
                <TextField
                    onChange={(e) => setTitle(e.target.value)}
                    className={classes.field}
                    label="Add a note"
                    variant="outlined"
                    color="secondary"
                    fullWidth
                    required
                    error={titleError}
                />
                <TextField
                    onChange={(e) => setDetails(e.target.value)}
                    className={classes.field}
                    label="Add a note"
                    variant="outlined"
                    color="secondary"
                    fullWidth
                    required
                    multiline
                    rows={4}
                    error={detailsError}
                />

                <Button
                    type="submit"
                    color="secondary"
                    variant="contained"
                    endIcon={<KeyboardArrowRightOutlined />}>
                    Submit
                </Button>
            </form>
        </>
    );
};

export default Mui;
