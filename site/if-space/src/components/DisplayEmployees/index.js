import { Eye, Trash } from "react-bootstrap-icons";
import { useState } from "react";
import ConfirmDialog from "../ConfirmDialog";
import DB from "../../services/db";

export default function DisplayEmployees({ employees, reloadData }) {
  const [toDeleteEmployee, setToDeleteEmployee] = useState(null);

  const deleteEmployee = () => {
    DB.employeeDelete(toDeleteEmployee?.ID)
      .then(() => {
        setToDeleteEmployee(null);
        reloadData();
      })
      .catch((error) => {
        console.log(error);
      });
  };

  return (
    <div
      className=" overscroll-auto overflow-auto"
      style={{ height: "calc(100vh - 20%)" }}
    >
      <table className="table-auto w-full">
        <thead className="">
          <tr className="bg-black text-white px-4 text-center">
            <td className="font-bold">ID</td>
            <td className="font-bold">Name</td>
            <td className="font-bold">Email</td>

            <td className="font-bold">Salary</td>
            <td className="font-bold">Actions</td>
          </tr>
        </thead>
        <tbody
          style={{ height: "calc(100vh - 20%)" }}
          className=" overscroll-auto overflow-auto"
        >
          {employees?.map((employee) => {
            return (
              <>
                &nbsp;
                <tr className="text-center">
                  <td>{employee?.ID}</td>
                  <td>
                    {employee?.FirstName} {employee?.LastName}
                  </td>

                  <td>{employee?.EMail}</td>
                  <td>{employee?.Salary}</td>
                  <td>
                    <div className="flex flex-row justify-center items-center  ">
                      <Trash
                        onClick={() => {
                          setToDeleteEmployee(employee);
                        }}
                        className="cursor-pointer text-xl text-red-500"
                      />
                      &nbsp; &nbsp; &nbsp; &nbsp;
                      <Eye className="cursor-pointer text-xl " />
                    </div>
                  </td>
                </tr>
              </>
            );
          })}
        </tbody>
      </table>

      <ConfirmDialog
        isShow={toDeleteEmployee != null}
        onClose={() => {
          setToDeleteEmployee(null);
        }}
        onYes={() => {
          deleteEmployee();
        }}
        title={
          <strong className="flex flex-row items-center justify-center">
            <Trash />
            &nbsp; Delete Employee
          </strong>
        }
        text={
          <p>
            Are you sure you want to delete{" "}
            <strong>
              {toDeleteEmployee?.FirstName} {toDeleteEmployee?.LastName}
            </strong>
            ? <br />
            This cannot be undone
          </p>
        }
      />
    </div>
  );
}
