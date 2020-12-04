import React, { Component } from 'react';
import { connect } from 'react-redux';

import NavLeft from "./NavLeft";
import NavRight from "./NavRight";
import Aux from "../../../../hoc/_Aux";
import * as actionTypes from "../../../../actions/types";

class NavBar extends Component {
    render() {
        let headerClass = ['navbar', 'pcoded-header', 'navbar-expand-lg', this.props.headerBackColor];
        if (this.props.headerFixedLayout) {
            headerClass = [...headerClass, 'headerpos-fixed'];
        }

        let toggleClass = ['mobile-menu'];
        if (this.props.collapseMenu) {
            toggleClass = [...toggleClass, 'on'];
        }

        return (
            <Aux>
                <header className={headerClass.join(' ')}>
                    <div className="m-header">
                        <a className={toggleClass.join(' ')} id="mobile-collapse1" href='#!' onClick={this.props.onToggleNavigation}><span /></a>
                        <a href='#!' className="b-brand">
                            <div className="b-bg">
                                <i className="feather icon-trending-up" />
                            </div>
                            <span className="b-title">Datta Able</span>
                        </a>
                    </div>
                    <a className="mobile-menu" id="mobile-header" href='#!'><i className="feather icon-more-horizontal" /></a>
                    <div className="collapse navbar-collapse">
                        <NavLeft />
                        <NavRight rtlLayout={this.props.rtlLayout} />
                    </div>
                </header>
            </Aux>
        );
    }
}

const mapStateToProps = state => {
    return {
        rtlLayout: state.nav.rtlLayout,
        headerBackColor: state.nav.headerBackColor,
        headerFixedLayout: state.nav.headerFixedLayout,
        collapseMenu: state.nav.collapseMenu
    }
};

const mapDispatchToProps = dispatch => {
    return {
        onToggleNavigation: () => dispatch({ type: actionTypes.COLLAPSE_MENU }),
    }
};

export default connect(mapStateToProps, mapDispatchToProps)(NavBar);
