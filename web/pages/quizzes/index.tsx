import Link from 'next/link';

export interface QuizzesProps {}

export const getStaticProps = async () => {
    // const res = await fetch('http://127.0.0.1:8000/api/v1/quizzes/?search=baby');
    // const res = await fetch('https://swapi.dev/api/people/');
    const res = await fetch('https://jsonplaceholder.typicode.com/users');
    const data = await res.json();
    // console.log(data);

    if (!data) {
        return {
            notFound: true
        };
    }

    return {
        props: { people: data } // will be passed to the page component as props
    };
};

const Quizzes: React.SFC<QuizzesProps> = ({ people }) => {
    return (
        <>
            <h2>Quizzes</h2>
            <ul>
                {people.map((person) => (
                    <li key={person.id}>
                        <Link href={'/quizzes/' + person.id}>{person.name}</Link>
                    </li>
                ))}
            </ul>
        </>
    );
};

export default Quizzes;
