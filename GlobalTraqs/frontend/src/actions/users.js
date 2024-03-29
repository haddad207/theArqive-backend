import axios from "axios";
import {
  EDIT_PIN,
  EDIT_USER,
  GET_USER,
  GET_USERS,
  EDIT_USER_ROLE,
  SEARCH_USERS,
  GET_NEXT_PREVIOUS_USERS,
  GET_USER_FAVORITE_STORIES,
  GET_PINS,
  USER_PROFILE_LOADING,
  USER_PROFILE_NOT_FOUND,
  UNFAVORITE_PROFILE_STORY,
} from "./types";

import { DELETE_USER } from "./types";

export const searchUsers = (username) => (dispatch) => {
  axios
    .get(`/api/profile/users?search=${username}`)
    .then((res) => {
      dispatch({
        type: SEARCH_USERS,
        payload: res.data,
      });
    })
    .catch((error) => console.log(error.response.data));
};

export const getUsers = () => (dispatch) => {
  axios
    .get("/api/auth/users/")
    .then((res) => {
      dispatch({
        type: GET_USERS,
        payload: res.data,
      });
    })
    .catch((err) => console.log(err));
};

export const editUser = (userId, editorId, user) => (dispatch) => {
  axios
    .patch(`/api/auth/users/${userId}/`, user)
    .then((res) => {
      if (editorId == userId) {
        dispatch({
          type: EDIT_USER,
          payload: res.data,
        });
      } else {
        dispatch({
          type: EDIT_USER,
          payload: null,
        });
      }
    })
    .catch((err) => console.log(err));
};

export const deleteUser = (id) => (dispatch) => {
  axios
    .delete(`/api/auth/users/${id}/`)
    .then((res) => {
      dispatch({
        type: DELETE_USER,
        payload: id,
      });
    })
    .catch((err) => console.log(err));
};

export const getUser = (id) => (dispatch) => {
  axios
    .get(`/api/auth/users/${id}/`)
    .then((res) => {
      dispatch({
        type: GET_USER,
        payload: res.data,
      });
    })
    .catch(function (error) {
      dispatch({
        type: GET_USER,
        payload: null,
      });
    });
};

export const getUserProfile = (username) => (dispatch) => {
  dispatch({ type: USER_PROFILE_LOADING });

  axios
    .get(`/api/profile/users?username=${username}`)
    .then((res) => {
      res.data.count === 0
        ? dispatch({
            type: USER_PROFILE_NOT_FOUND,
            payload: true,
          })
        : dispatch({
            type: GET_USER,
            payload: res.data.results[0],
          });
    })
    .catch(function (error) {
      console.log(error.response);
      dispatch({
        type: USER_PROFILE_NOT_FOUND,
        payload: true,
      });
    });
};

export const editUserRole = (id, role) => (dispatch) => {
  axios
    .patch(`/api/auth/users/${id}/`, role)
    .then((res) => {
      dispatch({
        type: EDIT_USER_ROLE,
        payload: res.data,
      });
    })
    .catch(function (error) {
      console.log(error.response);
    });
};

export const getNextPreviousUsers = (link) => (dispatch) => {
  axios
    .get(`${link}`)
    .then((res) => {
      dispatch({
        type: GET_NEXT_PREVIOUS_USERS,
        payload: res.data,
      });
    })
    .catch((error) => console.log(error));
};

export const unFavoriteProfile = (id) => (dispatch) => {
  axios
    .delete(`api/upVoteStory/${id}/`)
    .then((res) => {
      console.log(id);
      dispatch({
        type: UNFAVORITE_PROFILE_STORY,
        payload: id,
      });
    })
    .catch((error) => console.log(error));
};
