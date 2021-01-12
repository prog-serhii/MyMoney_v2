import React, { Component } from 'react';
import { Card, Table, Spinner } from 'react-bootstrap';

class WalletsTable extends Component {


    render() {
        return (
            <Card>
                <Card.Header>
                    <Card.Title as="h5">Hover Table</Card.Title>
                    <span className="d-block m-t-5">use props <code>hover</code> with <code>Table</code> component</span>
                </Card.Header>
                <Card.Body>
                    <Table responsive hover>
                        <thead>
                            <tr>
                                <th>Logo</th>
                                <th>Name</th>
                                <th>Balance</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td>Mark</td>
                                <td>Otto</td>
                                <td>@mdo</td>
                            </tr>
                            <tr>
                                <td>Jacob</td>
                                <td>Thornton</td>
                                <td>@fat</td>
                            </tr>
                            <tr>
                                <td>Larry</td>
                                <td>the Bird</td>
                                <td>@twitter</td>
                            </tr>
                        </tbody>
                    </Table>
                </Card.Body>
            </Card>
        );
    }
}

export default WalletsTable;