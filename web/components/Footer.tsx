import { Container, Grid, Segment } from 'semantic-ui-react';

export default function Footer() {
    return (
        <>
            <hr style={{ borderTop: '0.1px solid rgb(210 210 210)' }} />
            <Container textAlign="center">
                <Grid columns={3} divided>
                    <Grid.Row stretched>
                        <Grid.Column>
                            <Segment>1</Segment>
                        </Grid.Column>
                        <Grid.Column>
                            <Segment>1</Segment>
                            <Segment>2</Segment>
                        </Grid.Column>
                        <Grid.Column>
                            <Segment>1</Segment>
                            <Segment>2</Segment>
                            <Segment>3</Segment>
                        </Grid.Column>
                    </Grid.Row>
                </Grid>
            </Container>
        </>
    );
}
