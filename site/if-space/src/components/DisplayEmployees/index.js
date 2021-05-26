import { Eye, Trash } from "react-bootstrap-icons";

export default function DisplayEmployees({ onDelete, employees }) {
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
            <td className="font-bold">Gender</td>

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
                  <td>{employee?.Gender === "F" ? "Female" : "Male"}</td>
                  <td>{employee?.Salary}</td>
                  <td>
                    <div className="flex flex-row justify-center items-center  ">
                      <Trash
                        onClick={() => {
                          onDelete(employee);
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
    </div>
  );
}
