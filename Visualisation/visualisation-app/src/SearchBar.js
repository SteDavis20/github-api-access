import { useState, useEffect } from "react";
import React, { Component } from "react";
import "./SearchBar.css"

class SearchBar extends React.Component {
    
    constructor(props) {
        super(props);
        this.state = {value: '', testFlask: ''};
        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }
    
    handleChange(event) {
        this.setState({value: event.target.value});
    }
    
    handleSubmit(event) {
        // console.log(this.state.value);
        event.preventDefault();
        
        fetch("/"+this.state.value).then(
            res => res.json()
            ).then(
              data => {
                this.setState({testFlask: data.user});
                console.log("CHECKING VALUE: "+this.state.testFlask)
          });
    }    

    render() {
        return (
            <div>
                <form action="/" method="get" onSubmit={this.handleSubmit}>
                    <label htmlFor="header-search">
                        <span className="visually-hidden">Search username</span>
                    </label>
                    <input
                        type="text"
                        id="header-search"
                        placeholder="Search username"
                        name="s"
                        value={this.state.value}
                        onChange={this.handleChange}
                    />
                    <button type="submit">Search</button>
                </form>
            </div>
        );
    }
};

export default SearchBar;