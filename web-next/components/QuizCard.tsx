import Card from '@material-ui/core/Card';
import CardHeader from '@material-ui/core/CardHeader';
import CardMedia from '@material-ui/core/CardMedia';
import CardContent from '@material-ui/core/CardContent';
import React from 'react';
import { makeStyles, Theme, createStyles } from '@material-ui/core/styles';
import clsx from 'clsx';
import CardActions from '@material-ui/core/CardActions';
import Collapse from '@material-ui/core/Collapse';
import Avatar from '@material-ui/core/Avatar';
import IconButton from '@material-ui/core/IconButton';
import Typography from '@material-ui/core/Typography';
import { red } from '@material-ui/core/colors';
import FavoriteIcon from '@material-ui/icons/Favorite';
import ShareIcon from '@material-ui/icons/Share';
import ExpandMoreIcon from '@material-ui/icons/ExpandMore';
import MoreVertIcon from '@material-ui/icons/MoreVert';

export interface QuizCardProps {
    quiz: any;
}

// Should extend a base card component

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

const QuizCard: React.SFC<QuizCardProps> = ({ quiz }) => {
    const classes = useStyles();
    const [expanded, setExpanded] = React.useState(false);

    const handleExpandClick = () => {
        setExpanded(!expanded);
    };

    return (
        <>
            <Card variant="outlined">
                <CardHeader
                    avatar={
                        <Avatar aria-label="recipe" className={classes.avatar}>
                            {quiz.name.charAt(0).toUpperCase()}
                        </Avatar>
                    }
                    action={
                        <IconButton aria-label="quiz-action">
                            <MoreVertIcon />
                        </IconButton>
                    }
                    title={quiz.name}
                    subheader={quiz.birth_year}
                />
                <CardContent>
                    {quiz.vehicles.map((v) => (
                        <Typography variant="body2" color="textSecondary" key={v.id}>
                            {v}
                        </Typography>
                    ))}
                    <a>
                        {/* <Icon name="user" /> */}
                        {quiz.height}
                    </a>
                </CardContent>
                <CardActions disableSpacing>
                    <IconButton aria-label="add to favorites">
                        <FavoriteIcon />
                    </IconButton>
                    <IconButton aria-label="share">
                        <ShareIcon />
                    </IconButton>
                    <IconButton
                        className={clsx(classes.expand, {
                            [classes.expandOpen]: expanded
                        })}
                        onClick={handleExpandClick}
                        aria-expanded={expanded}
                        aria-label="show more">
                        <ExpandMoreIcon />
                    </IconButton>
                </CardActions>
                <Collapse in={expanded} timeout="auto" unmountOnExit>
                    <CardContent>
                        <Typography paragraph>
                            Add rice and stir very gently to distribute. Top with artichokes and
                            peppers, and cook without stirring, until most of the liquid is
                            absorbed, 15 to 18 minutes. Reduce heat to medium-low, add reserved
                            shrimp and mussels, tucking them down into the rice, and cook again
                            without stirring, until mussels have opened and rice is just tender, 5
                            to 7 minutes more. (Discard any mussels that don’t open.)
                        </Typography>
                    </CardContent>
                </Collapse>
            </Card>
        </>
    );
};

export default QuizCard;
