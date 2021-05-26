
import EmployeesContext from "./employeeContext";
import { useContext, useEffect, useReducer } from "react";
import authReducer from "./employeeReducer";
import {

} from "../types";


const EmployeesState = (props) => {
    const initialState = {
        employees: [],
    };
    const [state, dispatch] = useReducer(authReducer, initialState);

return (
    <EmployeesContext.Provider
        value={{

        }}
    >
        {props.children}
    </EmployeesContext.Provider>
);
};
export default EmployeesState;