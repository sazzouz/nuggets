import SearchAppBar from './Navbar';
import TemporaryDrawer from './Drawer';
import { Container } from '@material-ui/core';
import { makeStyles, mergeClasses } from '@material-ui/styles';

export interface LayoutProps {}

const useStyles = makeStyles({
    page: {
        background: '#f9f9f9',
        width: '100%'
    }
});

const Layout: React.SFC<LayoutProps> = ({ children }) => {
    const classes = useStyles();

    return (
        <>
            <div className={classes.page}>
                <SearchAppBar />
                {/* <TemporaryDrawer /> */}
                <Container maxWidth="lg">{children}</Container>
            </div>
        </>
    );
};

export default Layout;
