import Image from 'next/image';
import Link from 'next/link';
import styles from '../styles/Home.module.css';
import { Card, Icon, Image as SemImage } from 'semantic-ui-react';
import CardExampleGroupProps from '../components/CardGroup';
import React, { useState, useEffect } from 'react';

export const getStaticProps = async () => {
    // const res = await fetch('http://127.0.0.1:8000/api/v1/quizzes/?search=baby');
    // const res = await fetch('https://swapi.dev/api/people/');
    const res = await fetch('https://jsonplaceholder.typicode.com/users');
    const data = await res.json();
    console.log(data);

    if (!data) {
        return {
            notFound: true
        };
    }

    return {
        props: { people: data } // will be passed to the page component as props
    };
};

export default function Home({ people }) {
    return (
        <div className={styles.container}>
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
