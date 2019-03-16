import React from 'react';
import SiteWrapper from './SiteWrapper.js';
import axiosRequest from './Backend.js';

import './App.css';
import './WinBanner.css';


export default class WinBanner extends React.Component {

  constructor(props) {
    super(props);

    this.state = {
      isLoadingData: true,
      data: [],
      challenges: {},
      winnersRevealed: false
    }
    // this.handleChange = this.handleChange.bind(this);
  }

  componentDidMount() {
    axiosRequest.get('api/projects/id/5c4bc0dbfc964f100c7722a1')
      .then((project_data) => {
        this.setState({
          data: project_data['projects'],
          isLoadingData: false,
        });
      });
  }

  render() {
    return (
      <div>
        <nav className="navbar navbar-expand-md banner">
          <span style={{justifyContent: 'flex-end'}}>x</span><br/>
           {/*this.state.data.length === 0 ? "empty set" : this.state.data*/}
        </nav>
      </div>
    )
  }
}
