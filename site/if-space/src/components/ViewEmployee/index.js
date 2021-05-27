import {Button, Form, Modal} from "react-bootstrap";
import { Controller, useForm } from "react-hook-form";
import {Eye, Trash} from "react-bootstrap-icons";

export default function ViewEmployee({ isShow, onClose, employee, }){

    return (
        <Modal id="fullScreenModalId" show={isShow} onHide={onClose} dialogClassName="fullscreen-modal" >
            <div className="bg-white w-8/12 p-8" style={{ height: "80%" }}>
                <div className="mb-4">
                    <div className="flex flex-row w-full">
                        <h1 className="font-bold text-2xl">View Employee</h1>
                        <Button closeButton className="ml-auto font-bold text-lg" onClick={onClose}>X</Button>
                    </div>
                </div>

                <div>
                    <table className="table-auto w-full capitalize">
                        <tr>
                            <td className="font-medium">Name</td>
                            <td>{`${employee?.FirstName ?? "FirstName"} ${employee?.LastName ?? "LastName"}`}</td>
                        </tr>
                        <tr>
                            <td className="font-medium">Phone Number</td>
                            <td>{employee?.PhoneNo ?? "PhoneNo"}</td>
                        </tr>
                        <tr>
                            <td className="font-medium">Email Address</td>
                            <td>{employee?.EMail ?? "EMail"}</td>
                        </tr>
                        <tr>
                            <td className="font-medium">Date of Birth</td>
                            <td>{employee?.DateofBirth ?? "DateofBirth"}</td>
                        </tr>
                        <tr>
                            <td className="font-medium">Monthly Salary</td>
                            <td>{employee?.Salary ?? "Salary"}</td>
                        </tr>

                    </table>
                </div>
            </div>
        </Modal>
    )
}