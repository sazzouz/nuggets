import Image from 'next/image';
import Link from 'next/link';
import styles from '../styles/Home.module.css';
import { makeStyles, Theme, createStyles } from '@material-ui/core/styles';
import React, { useState, useEffect } from 'react';
import CssBaseline from '@material-ui/core/CssBaseline';
import Typography from '@material-ui/core/Typography';
import Container from '@material-ui/core/Container';
import Card from '@material-ui/core/Card';
import CardContent from '@material-ui/core/CardContent';
import CardMedia from '@material-ui/core/CardMedia';
import Button from '@material-ui/core/Button';
import ButtonGroup from '@material-ui/core/ButtonGroup';
import { AcUnit } from '@material-ui/icons';
import { KeyboardArrowRightOutlined } from '@material-ui/icons';
import { Paper, Grid } from '@material-ui/core';
import QuizCard from '../components/QuizCard';
import red from '@material-ui/core';

export async function getStaticProps() {
    // const res = await fetch('http://127.0.0.1:8000/api/v1/quizzes/?search=baby');
    const res = await fetch('https://swapi.dev/api/people/');
    const data = await res.json();
    console.log(data);

    if (!data) {
        return {
            notFound: true
        };
    }

    return {
        props: { people: data.results } // will be passed to the page component as props
    };
}

const useStyles = makeStyles((theme: Theme) =>
    createStyles({
        root: {
            maxWidth: 345
        },
        media: {
            height: 0,
            paddingTop: '56.25%' // 16:9
        },
        expand: {
            transform: 'rotate(0deg)',
            marginLeft: 'auto',
            transition: theme.transitions.create('transform', {
                duration: theme.transitions.duration.shortest
            })
        },
        expandOpen: {
            transform: 'rotate(180deg)'
        },
        avatar: {
            backgroundColor: red[500]
        }
    })
);

export default function Home({ people }) {
    return (
        <>
            <Typography variant="h4" component="h2" color="textSecondary" align="left" gutterBottom>
                Home
            </Typography>
            <CssBaseline />
            <div className={styles.container}>
                <Link href="mui">Mui</Link>

                <Button
                    variant="contained"
                    color="secondary"
                    startIcon={<AcUnit />}
                    endIcon={<KeyboardArrowRightOutlined />}>
                    Action
                </Button>

                <h3>All Jedis</h3>
            </div>

            <Grid container spacing={3}>
                {people.map((person) => (
                    <Grid item sm={12} md={6} lg={3} key={person.name}>
                        <QuizCard quiz={person} />
                    </Grid>
                ))}
            </Grid>
        </>
    );
}
