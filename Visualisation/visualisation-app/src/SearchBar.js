import "./SearchBar.css"

function SearchBar() {
    return (
        <div>
            <form action="/" method="get">
                <label htmlFor="header-search">
                    <span className="visually-hidden">Search username</span>
                </label>
                <input
                    type="text"
                    id="header-search"
                    placeholder="Search username"
                    name="s" 
                />
                <button type="submit">Search</button>
            </form>
        </div>
    );
};

export default SearchBar;