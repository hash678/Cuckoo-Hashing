import Head from 'next/head'
import Image from 'next/image'
import styles from '../styles/Home.module.css'
import DefaultLayout from "../src/components/DefaultLayout";
import {Button} from "react-bootstrap";
import AddNewEmployee from "../src/components/AddNewEmployee";
import {useState} from "react";
import AddAttendanceRecord from "../src/components/AddAttendanceRecord";

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
    ];

    return (
        <DefaultLayout>
            <div className="flex flex-wrap">
                <p className="text-black font-light">Hello Jamal. <br/>
                    <p className="font-bold text-lg">Welcome to your attendance portal.</p>
                </p>
                <div className="ml-auto">
                    <Button
                        className="focus:outline-none mb-8 bg-pink-500 hover:bg-pink-600 px-4 py-2 rounded-md text-white mr-2"
                        style={{ marginBottom: "0" }}
                        onClick={() => {
                            setIsBatch(false);
                            setIsShowPopupDialog(true) ;
                        }}
                    >
                        Add Record
                    </Button>
                    <Button
                        onClick={() => {
                            setIsBatch(true);
                            setIsShowPopupDialog(true);
                        }}
                        className="focus:outline-none mb-8 bg-pink-500 hover:bg-pink-600 px-4 py-2 rounded-md text-white ml-2"
                    >
                        Batch Upload Attendance
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
                                <Button className="text-red-600 text-white mx-2 rounded-2xl px-8 py-3 focus:outline-none hover:text-black">
                                    Delete Record
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
