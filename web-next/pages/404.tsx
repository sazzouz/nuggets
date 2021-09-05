import Link from 'next/link';
import { useEffect } from 'react';
import { useRouter } from 'next/dist/client/router';

export interface NotFoundProps {}

const NotFound: React.SFC<NotFoundProps> = () => {
    const router = useRouter();

    useEffect(() => {
        setTimeout(() => {
            router.push('/');
        }, 3000);
    }, []);

    return (
        <div className="not-found">
            <h1>Oops!</h1>
            <p>This page cannot be found...</p>
            <p>
                Go back to the <Link href="/">home</Link>.
            </p>
        </div>
    );
};

export default NotFound;
