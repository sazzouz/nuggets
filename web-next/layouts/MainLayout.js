import SearchAppBar from '../components/Navbar';
import TemporaryDrawer from '../components/Drawer';
import { Container } from '@material-ui/core';
import { makeStyles, mergeClasses } from '@material-ui/styles';

const useStyles = makeStyles({
    page: {
        background: '#f9f9f9',
        width: '100%'
    }
});

const MainLayout = ({ children }) => {
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

export default MainLayout;
