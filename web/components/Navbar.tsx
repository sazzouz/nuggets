import Link from 'next/link';
import Image from 'next/image';

export interface NavbarProps {}

const Navbar: React.SFC<NavbarProps> = () => {
    return (
        <div>
            <nav>
                <div className="logo">
                    <Image src="/logo.jpg" alt="Nuggets" width={88} height={78} />
                </div>
                <Link href="/">
                    <a>Home</a>
                </Link>
                <Link href="/quizzes">
                    <a>Quizzes</a>
                </Link>
                <Link href="/about">
                    <a>About</a>
                </Link>
                <Link href="/tw">
                    <a>Tailwind</a>
                </Link>
            </nav>
        </div>
    );
};

export default Navbar;
