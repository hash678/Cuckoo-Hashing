import Head from 'next/head'
import Image from 'next/image'
import styles from '../styles/Home.module.css'
import DefaultLayout from "../src/components/DefaultLayout";
import {Button} from "react-bootstrap";
import AddNewEmployee from "../src/components/AddNewEmployee";
import {useState} from "react";
import AddAttendanceRecord from "../src/components/AddAttendanceRecord";
import {Cloud, Person, Trash} from "react-bootstrap-icons";

export default function Attendance() {

    const [isShowPopupDialog, setIsShowPopupDialog] = useState(false);
    const [isBatch, setIsBatch] = useState(false);

    const attendanceData = [
        {
            date: "May 27, 2021",
            timeIn: "09:13 AM",
            timeOut: "18:57 PM",
            actions: [ "Mark Entry", "Leaving the Office" ]
        },{
            date: "May 27, 2021",
            timeIn: "09:13 AM",
            timeOut: "18:57 PM",
            actions: [ "Mark Entry", "Leaving the Office" ]
        },{
            date: "May 27, 2021",
            timeIn: "09:13 AM",
            timeOut: "18:57 PM",
            actions: [ "Mark Entry", "Leaving the Office" ]
        },{
            date: "May 27, 2021",
            timeIn: "09:13 AM",
            timeOut: null,
            actions: [ "Mark Entry", "Leaving the Office" ]
        },
    ]

    return (
        <DefaultLayout>
            <div className="flex flex-wrap">
                <p className="text-black font-light">Hello Jamal. <br/>
                    <p className="font-bold text-lg">Welcome to your attendance portal.</p>
                </p>
                <div className="flex flex-row mb-8 ml-auto items-start">
                    <Button
                        className="flex flex-row justify-center items-center focus:outline-none px-2 py-2 rounded-md text-pink-500"
                        style={{ marginBottom: "0" }}
                        onClick={() => {
                            setIsBatch(false);
                            setIsShowPopupDialog(true) ;
                        }}
                    >
                        {" "}
                        <Person />
                        &nbsp; Add Record
                    </Button>
                    <Button
                        onClick={() => {
                            setIsBatch(true);
                            setIsShowPopupDialog(true);
                        }}
                        className="flex flex-row justify-center items-center focus:outline-none px-2 py-2 rounded-md text-pink-500"
                    >
                        <Cloud />
                        &nbsp; Batch Upload Attendance
                    </Button>
                </div>
            </div>

            <br/>


            <table className="table-auto w-full">
                <thead>
                <tr className="bg-black text-white px-4 text-center">
                    <td className="font-bold">Date</td>
                    <td className="font-bold">Name of Employee</td>
                    <td className="font-bold w-1/3">Notes</td>
                    <td className="font-bold w-1/4">Actions</td>
                </tr>
                </thead>
                <tbody>
                { attendanceData.map( val => {
                    return (
                        <tr className="text-center h-16">
                            <td>{val?.date ?? `NULL`}</td>
                            <td>{val?.timeIn ?? `No Entry Time`}</td>
                            <td>{val?.timeOut ?? `No Exit Time`}</td>
                            <td>
                                <Button className="flex flex-row justify-center items-center text-red-600 hover:text-black mx-2 rounded-2xl px-8 py-3 focus:outline-none">
                                    <Trash className="text-xl"/>
                                    &nbsp; Delete Record
                                </Button>
                            </td>
                        </tr>
                    )
                } ) }

                </tbody>
            </table>

            <AddAttendanceRecord
                isShow={isShowPopupDialog}
                onClose={() => {setIsShowPopupDialog(false)}}
                batch={isBatch}
            />
        </DefaultLayout>
    )
}
