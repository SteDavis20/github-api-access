import { Component } from "react";
import './Dropdown.css'
// import FontAwesome from 'react-fontawesome';

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

    // selectItem = (item) => {
    //     const { resetThenSet } = this.props;
    //     const { title, id, key } = item;
      
    //     this.setState({
    //         headerTitle: title,
    //         isListOpen: false,
    //     }, () => resetThenSet(id, key));
    // }

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
              {/* {isListOpen
                ? <FontAwesome name="angle-up" size="2x" />
                : <FontAwesome name="angle-down" size="2x" />} */}
            </button>
            {isListOpen && (
              <div
                role="list"
                className="dd-list"
              >
                {list.map((item) => (
                    <li>
                        <button
                    	    type="button"
                            className="dd-list-item"
                            key={item.id}
                            onClick={() => this.props.selectItem(item)}
                        >
                        {item.title}
                        {' '}
                        {/* {item.selected && <FontAwesome name="check" />} */}
                        </button>
                    </li>
                ))}
              </div>
            )}
          </div>
        )
    }

}

export default Dropdown
