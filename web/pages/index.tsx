import Image from 'next/image';
import Link from 'next/link';
import styles from '../styles/Home.module.css';
import { Card, Icon, Image as SemImage } from 'semantic-ui-react';
import CardExampleGroupProps from '../components/CardGroup';
import React, { useState, useEffect } from 'react';

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

export default function Home({ people }) {
    return (
        <div className={styles.container}>
            <CardExampleGroupProps />
            <Link href="/semantic">
                <a>Semantic</a>
            </Link>
            <h3>All Jedis</h3>
            {people.map((person) => (
                <div key={person.id}>
                    <Card>
                        <Card.Content>
                            <Card.Header>{person.name}</Card.Header>
                            <Card.Meta>
                                <span className="date">Born in {person.birth_year}</span>
                            </Card.Meta>
                            <Card.Description>
                                {person.vehicles.map((v) => (
                                    <span key={v.id}>{v}</span>
                                ))}
                            </Card.Description>
                        </Card.Content>
                        <Card.Content extra>
                            <a>
                                <Icon name="user" />
                                {person.height}
                            </a>
                        </Card.Content>
                    </Card>
                </div>
            ))}
            <Card>
                <SemImage
                    src="https://recipefairy.com/wp-content/uploads/2020/05/mcdonalds-chicken-nuggets-recipe.jpg"
                    wrapped
                    ui={false}
                />
                <Card.Content>
                    <Card.Header>Matthew</Card.Header>
                    <Card.Meta>
                        <span className="date">Joined in 2015</span>
                    </Card.Meta>
                    <Card.Description>Matthew is a musician living in Nashville.</Card.Description>
                </Card.Content>
                <Card.Content extra>
                    <a>
                        <Icon name="user" />
                        22 Friends
                    </a>
                </Card.Content>
            </Card>
            <main className={styles.main}>
                <span className="my-10 bg-blue-200 px-3 py-1 rounded-full hover:bg-red-200 transition duration-100 ease-in-out cursor-pointer">
                    Tailwind button
                </span>
                <figure className="bg-purple-100 rounded-xl p-8">
                    {/* <img className="w-32 h-32 rounded-full mx-auto" src="/sarah-dayan.jpg" alt="" width="384" height="512"></img> */}
                    <div className="pt-2 space-y-4">
                        <blockquote>
                            <p className="text-xl font-semibold">
                                “Tailwind CSS is the only framework that Ive seen scale on large
                                teams. It’s easy to customize, adapts to any design, and the build
                                size is tiny.”
                            </p>
                        </blockquote>
                        <figcaption className="font-medium">
                            <div className="text-cyan-600">Sarah Dayan</div>
                            <div className="text-gray-500">Staff Engineer, Algolia</div>
                        </figcaption>
                    </div>
                </figure>
                <h1 className={styles.title}>
                    Welcome to{' '}
                    <a
                        href="https://images-eu.ssl-images-amazon.com/images/I/71suSLKbQtL.png"
                        target="_blank"
                        rel="noreferrer">
                        Nuggets!
                    </a>
                </h1>

                <p className={styles.description}>
                    Get started by editing <code className={styles.code}>pages/index.js</code>
                </p>

                <div className={styles.grid}>
                    <a href="https://nextjs.org/docs" className={styles.card}>
                        <h2>Documentation &rarr;</h2>
                        <p>Find in-depth information about Next.js features and API.</p>
                    </a>

                    <a href="https://nextjs.org/learn" className={styles.card}>
                        <h2>Learn &rarr;</h2>
                        <p>Learn about Next.js in an interactive course with quizzes!</p>
                    </a>

                    <a
                        href="https://github.com/vercel/next.js/tree/master/examples"
                        className={styles.card}>
                        <h2>Examples &rarr;</h2>
                        <p>Discover and deploy boilerplate example Next.js projects.</p>
                    </a>

                    <a
                        href="https://vercel.com/new?utm_source=create-next-app&utm_medium=default-template&utm_campaign=create-next-app"
                        className={styles.card}>
                        <h2>Deploy &rarr;</h2>
                        <p>Instantly deploy your Next.js site to a public URL with Vercel.</p>
                    </a>
                </div>
            </main>

            <footer className={styles.footer}>
                <a
                    href="https://vercel.com?utm_source=create-next-app&utm_medium=default-template&utm_campaign=create-next-app"
                    target="_blank"
                    rel="noopener noreferrer">
                    Powered by{' '}
                    <span className={styles.logo}>
                        <Image src="/vercel.svg" alt="Vercel Logo" width={72} height={16} />
                    </span>
                </a>
            </footer>
        </div>
    );
}
