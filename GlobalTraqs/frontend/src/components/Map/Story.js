import React, { Component } from 'react'
import PropTypes from "prop-types"
import axios from 'axios';
import FavoriteIcon from '@material-ui/icons/Favorite';
import FavoriteBorderIcon from '@material-ui/icons/FavoriteBorder';
import { connect } from "react-redux";


export class Story extends Component {
    static propTypes = {
        auth: PropTypes.object.isRequired,

    };


    state = {
        userStory: '',
        upvote: '',
        ownerid: '',
        numberOfUpvote: '',
        userUpvote: '',
        id: '',
        pinId: '',
        pinstory: '',
        upVoter: '',
        username: '',

    }


    componentDidMount() {

        const { id } = this.props.match.params
        axios.get(`api/pins/${id}`)
            .then(response => {
                this.setState({ userStory: response.data });
                console.log(response.data);
            })
            .catch(error => {
                console.log(error);
            });
        axios.get(`api/upVoteStory?pinId=${id}`)
            .then(response => {
                this.setState({ pinStory: response.data });
                console.log(response.data);
                this.setState({
                    numberOfUpvote: response.data.length
                })
            })
            .catch(error => {
                console.log(error);
            });

        this.setState({ pinId: id })

    }
    onSubmit = e => {
        this.state.upvote = true
        this.state.upVoter = 1
        e.preventDefault();
        console.log('yeet')

        const { upvote, pinId, upVoter } = this.state
        const upVoteStoryPin = { upvote, pinId, upVoter }

        axios.post('/api/upVoteStory/', upVoteStoryPin)
            .then(res => {
                console.log(res.data)
            })
            .catch(err => console.log(err));
    }


    render() {
        const { id } = this.props.match.params
        const { isAuthenticated, user } = this.props.auth;
        this.state.username = user ? user.username : ""
        const authorizedUser = (
            <h2>yeet</h2>
        )
        const notUser = (
            <h2>yeeta</h2>
        )
        return (

            <div className="card card-body mt-4 mb-4">
                <h2>id is {id}  </h2>
                <h2>Title:  {this.state.userStory.title}</h2>
                <h2>Description: {this.state.userStory.description}</h2>
                <h2>latitude: {this.state.userStory.latitude}</h2>
                <h2>longitude: {this.state.userStory.longitude}</h2>
                <h2>owner: {this.state.userStory.owner} {this.state.username}</h2>
                <div className="col-lg-1">
                    <img src="https://picsum.photos/200/300" className="rounded" position="center" ></img>

                </div>
                <form onSubmit={this.onSubmit}>
                    <h2>number of upvotes {this.state.numberOfUpvote} <button type="submit" className="btn btn-primary">
                        Upvote
                </button></h2>
                </form>
                {isAuthenticated ? authorizedUser : notUser}



                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer nec odio. Praesent libero. Sed cursus ante dapibus diam. Sed nisi. Nulla quis sem at nibh elementum imperdiet. Duis sagittis ipsum. <b>Lorem ipsum dolor sit amet, consectetur adipiscing elit</b>. Praesent mauris. Fusce nec tellus sed augue semper porta. <b>Lorem ipsum dolor sit amet, consectetur adipiscing elit</b>. Mauris massa. Vestibulum lacinia arcu eget nulla. <b>Lorem ipsum dolor sit amet, consectetur adipiscing elit</b>. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. </p>

                <p>Curabitur sodales ligula in libero. Sed dignissim lacinia nunc. Curabitur tortor. Pellentesque nibh. Aenean quam. In scelerisque sem at dolor. Maecenas mattis. Sed convallis tristique sem. Proin ut ligula vel nunc egestas porttitor. Morbi lectus risus, iaculis vel, suscipit quis, luctus non, massa. Fusce ac turpis quis ligula lacinia aliquet. Mauris ipsum. Nulla metus metus, ullamcorper vel, tincidunt sed, euismod in, nibh. Quisque volutpat condimentum velit. </p>

                <p>Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Nam nec ante. Sed lacinia, urna non tincidunt mattis, tortor neque adipiscing diam, a cursus ipsum ante quis turpis. Nulla facilisi. Ut fringilla. Suspendisse potenti. Nunc feugiat mi a tellus consequat imperdiet. Vestibulum sapien. Proin quam. Etiam ultrices. Suspendisse in justo eu magna luctus suscipit. Sed lectus. </p>

                <p>Integer euismod lacus luctus magna. Quisque cursus, metus vitae pharetra auctor, sem massa mattis sem, at interdum magna augue eget diam. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Morbi lacinia molestie dui. Praesent blandit dolor. Sed non quam. In vel mi sit amet augue congue elementum. Morbi in ipsum sit amet pede facilisis laoreet. Donec lacus nunc, viverra nec, blandit vel, egestas et, augue. Vestibulum tincidunt malesuada tellus. Ut ultrices ultrices enim. Curabitur sit amet mauris. Morbi in dui quis est pulvinar ullamcorper. </p>

                <p>Nulla facilisi. Integer lacinia sollicitudin massa. Cras metus. Sed aliquet risus a tortor. Integer id quam. Morbi mi. Quisque nisl felis, venenatis tristique, dignissim in, ultrices sit amet, augue. Proin sodales libero eget ante. Nulla quam. Aenean laoreet. Vestibulum nisi lectus, commodo ac, facilisis ac, ultricies eu, pede. Ut orci risus, accumsan porttitor, cursus quis, aliquet eget, justo. Sed pretium blandit orci. Ut eu diam at pede suscipit sodales. </p>


            </div >
        )
    }
}
const mapStateToProps = state => ({
    auth: state.auth
});
export default connect(
    mapStateToProps
)(Story);
