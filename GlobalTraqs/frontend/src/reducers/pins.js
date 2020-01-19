import { GET_PINS, DELETE_PINS, ADD_PIN, EDIT_PIN, GET_PIN, SEARCH_PINS } from '../actions/types.js';
import {GET_PINS_BY_OWNER} from "../actions/types";

const initialState = {
    pins: [],
    pin: null
};
export default function (state = initialState, action) {
    switch (action.type) {
         case GET_PINS_BY_OWNER:
            return {
                ...state,
                pins: action.payload
            };
        case SEARCH_PINS:
            return {
                ...state,
                pins: action.payload
            };
        case GET_PIN:
            return {
                ...state,
                pin: action.payload
            };
        case GET_PINS:
            return {
                ...state,
                pins: action.payload
            };
        case DELETE_PINS:
            return {
                ...state,
                pins: state.pins.filter(pins => pins.id !== action.payload)
            };
        case ADD_PIN:
            return {
                ...state,
                pins: [...state.pins, action.payload]
            };
        case EDIT_PIN:
            return {
                ...state,
                // fixes duplicated pin on map when editing pin
                pins: [...state.pins.filter(pins => pins.id !== action.payload.id), action.payload]
            };

        default:
            return state;
    }
}