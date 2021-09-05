export const getStaticPaths = async () => {
    // const res = await fetch('https://jsonplaceholder.typicode.com/users');
    const res = await fetch('http://127.0.0.1:8000/api/v1/quizzes');
    const data = await res.json();

    // map data to an array of path objects with params (id)
    const paths = data.map((ninja) => {
        return {
            params: { id: ninja.id.toString() }
        };
    });

    return {
        paths,
        fallback: false
    };
};

export const getStaticProps = async (context) => {
    const id = context.params.id;
    // const res = await fetch('https://jsonplaceholder.typicode.com/users/' + id);
    const res = await fetch('http://127.0.0.1:8000/api/v1/quizzes/' + id);
    const data = await res.json();

    return {
        props: { ninja: data }
    };
};

const Quiz = ({ ninja }) => {
    return (
        <div>
            <h1>{ninja.id}</h1>
            <p>{ninja.title}</p>
            <p>{ninja.description}</p>
        </div>
    );
};

export default Quiz;
