import Head from 'next/head'
import Image from 'next/image'
import styles from '../styles/Home.module.css'
import DefaultLayout from "../src/components/DefaultLayout";
import {Button} from "react-bootstrap";
import AddNewEmployee from "../src/components/AddNewEmployee";
import {useEffect, useState} from "react";
import AddAttendanceRecord from "../src/components/AddAttendanceRecord";
import {Cloud, Person, Trash} from "react-bootstrap-icons";
import { Search } from "react-bootstrap-icons";
import DB from "../src/services/db";

export default function Attendance() {

    const [isShowPopupDialog, setIsShowPopupDialog] = useState(false);
    const [isBatch, setIsBatch] = useState(false);
    const [attendanceData, setAttendanceData] = useState([])

    const [selectedID, setSelectedID] = useState(null)

    const searchAttendance = () => {
     DB.getAttendance(selectedID).then(data => {
         setAttendanceData(data)
     })
    }


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

                </div>
            </div>

            <br/>

            <div className="flex flex-row w-full">
            <input className="h-12 border focus:outline-none px-2 " placeholder="Enter Employee ID" onChange={(e) => {setSelectedID(e.target.value)}}/>
                <Button
                    onClick={() => {searchAttendance()}}
                    type="submit"
                    className="ml-4 flex flex-col items-center justify-center mr-2 font-medium text-lg bg-pink-500 hover:bg-pink-600 text-center rounded-lg text-white h-12 w-12 align-middle justify-center flex flex-col hover:bg-pink-900 cursor-pointer"
                >
                    <Search />
                </Button>
            </div>
            <br/>
            <br/>
            <table className="table-auto w-full">
                <thead>
                <tr className="bg-black text-white px-4 text-center">
                    <td className="font-bold">Date</td>
                    <td className="font-bold">Name of Employee</td>
                    <td className="font-bold w-1/3">Notes</td>
                </tr>
                </thead>
                <tbody>
                { attendanceData.map( val => {
                    return (
                        <tr className="text-center h-16">
                            <td>{val?.date ?? `NULL`}</td>
                            <td>{val?.Name ?? `NULL`}</td>
                            <td>{val?.Notes ?? `NULL`}</td>
                        </tr>
                    )
                } ) }

                </tbody>
            </table>

            <AddAttendanceRecord
                isShow={isShowPopupDialog}
                onClose={() => {setIsShowPopupDialog(false)}}
            />
        </DefaultLayout>
    )
}
