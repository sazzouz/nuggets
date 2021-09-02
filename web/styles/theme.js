import { createTheme } from '@material-ui/core/styles';
import { red } from '@material-ui/core/colors';

// Create a theme instance.
const theme = createTheme({
    palette: {
        primary: {
            main: '#556cd6'
        },
        secondary: {
            main: '#19857b'
        },
        error: {
            main: red.A400
        },
        background: {
            default: '#fff'
        }
    },
    typography: {
        fontFamily: 'Nunito',
        fontWeightLight: '300',
        fontWeightRegular: '400',
        fontWeightMedium: '600',
        fontWeightBold: '700'
    }
});

export default theme;
