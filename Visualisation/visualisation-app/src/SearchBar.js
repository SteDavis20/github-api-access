import React from "react";
import "./SearchBar.css"

function SearchBar(props) {

    const {label, type, id, placeholder, name, onChange, value, handleUserFormSubmit} = props    

    return (
        <div className="search-bar">
            <form action="/" method="get">
                <label htmlFor="header-search">
                    <span className="visually-hidden">{label}</span>
                </label>
                <input className="search-input"
                    type={type}
                    id={id}
                    placeholder={placeholder}
                    name={name}
                    value={value}
                    onChange={onChange}
                />
                <button className="search-button"onClick={handleUserFormSubmit} type="submit">Search</button>
            </form>
        </div>
    );
}

export default SearchBar;