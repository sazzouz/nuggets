import React, { Component } from 'react';
import { Button, Dropdown, Menu } from 'semantic-ui-react';

export default class Navbar extends Component {
    state = { activeItem: 'home' };

    handleItemClick = (e, { name }) => this.setState({ activeItem: name });

    render() {
        const { activeItem } = this.state;

        return (
            <Menu stackable>
                <Menu.Item>
                    <img src="https://media.istockphoto.com/vectors/gold-nugget-vector-icon-vector-id869929722?k=6&m=869929722&s=170667a&w=0&h=7-rZ76NXQzmhf6T6Qumg4fDA8ymxA83i17Df2OmnARk=" />
                </Menu.Item>
                <Menu.Item
                    name="home"
                    active={activeItem === 'home'}
                    onClick={this.handleItemClick}
                />
                <Menu.Item
                    name="messages"
                    active={activeItem === 'messages'}
                    onClick={this.handleItemClick}
                />

                <Menu.Menu position="right">
                    <Dropdown item text="Language">
                        <Dropdown.Menu>
                            <Dropdown.Item>English</Dropdown.Item>
                            <Dropdown.Item>Russian</Dropdown.Item>
                            <Dropdown.Item>Spanish</Dropdown.Item>
                        </Dropdown.Menu>
                    </Dropdown>

                    <Menu.Item>
                        <Button primary>Sign Up</Button>
                    </Menu.Item>
                </Menu.Menu>
            </Menu>
        );
    }
}
