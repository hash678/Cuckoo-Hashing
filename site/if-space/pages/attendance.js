import DefaultLayout from "../src/components/DefaultLayout";

export  default function Attendance() {

    const attendance = [
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
            <div className="">
                <h2 className="capitalize text-lg">Hello <b>$EmployeeName,</b>
                    <br />Welcome to your employee portal</h2>

                <table className="table-auto w-full mt-8">
                    <thead className="bg-black text-white">
                        <tr className="h-8">
                            <th className="w-1/4">Date</th>
                            <th className="w-1/4">Time In</th>
                            <th className="w-1/4">Time Out</th>
                            <th className="w-1/4">Actions</th>
                        </tr>
                    </thead>
                    <tbody>
                    { attendance.map( val => {
                        return(
                            <tr className="text-center h-16">
                                <td>{val?.date}</td>
                                <td>{val?.timeIn}</td>
                                <td>{val?.timeOut ?? `No Exit Time`}</td>
                                <td>
                                    <button className="font-medium bg-pink-600 text-white mx-2 rounded-2xl px-8 py-3 focus:outline-none hover:bg-red-600">Mark Entry</button>
                                    <button className="text-red-600 text-white mx-2 rounded-2xl px-8 py-3 focus:outline-none hover:text-black">Mark Exit</button>
                                </td>
                            </tr>
                        )
                    }) }
                    </tbody>
                </table>
            </div>
        </DefaultLayout>
    )
}