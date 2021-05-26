import DefaultLayout from "../src/components/DefaultLayout";

export  default function Attendance() {


    return (
        <DefaultLayout>
            <div className="">
                <h2 className="capitalize">Hello <b>$EmployeeName,</b><br />Welcome to your employee portal</h2>

                <table >
                    <thead>
                    <th>Date</th>
                    <th>Time In</th>
                    <th>Time Out</th>
                    <th>Actions</th>
                    </thead>
                    <tbody>

                    </tbody>
                </table>
            </div>
        </DefaultLayout>
    )
}