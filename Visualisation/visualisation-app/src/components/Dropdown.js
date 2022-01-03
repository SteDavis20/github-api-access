import { Component } from "react";
import './Dropdown.css'

class Dropdown extends Component {
    
    constructor(props) {
        super(props)
        this.state = {
          isListOpen: false,
          headerTitle: this.props.title,
          list: this.props.list
        }
    }

    toggleList = () => {
        this.setState(prevState => ({
            isListOpen: !prevState.isListOpen
        }))
    }

    render() {
        const { isListOpen, headerTitle, list } = this.state;
      
        return (
          <div className="dd-wrapper">
            <button
              type="button"
              className="dd-header"
              onClick={this.toggleList}
            >
              <div className="dd-header-title">{headerTitle}</div>
            </button>
            {isListOpen && (
              <div
                role="list"
                className="dd-list"
              >
                {list.map((item) => (
                    <li>
                        {item.title}
                    </li>
                ))}
              </div>
            )}
          </div>
        )
    }
}

export default Dropdown
