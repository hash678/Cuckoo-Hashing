import { Fetch } from "react-request";
import { BASE_URL } from "../constants";

export default class DB {
  static async insertEmployee(data) {}

  static async loadEmployees() {
    let jsonData = await fetch(BASE_URL + "/employees-all/").then((res) =>
      res.json()
    );
    return jsonData;
  }
  static async employeeDelete(id) {
    let jsonData = await fetch(BASE_URL + "/employees/" + id, {
      method: "DELETE",
    });
  }
  static async batchUploadEmployees(file) {
    console.log("BATCH UPLOADING");

    var formdata = new FormData();
    formdata.append("data_file", file, "file");

    var requestOptions = {
      method: "POST",
      body: formdata,
      redirect: "follow",
    };

    return fetch(BASE_URL + "/employees-batch/", requestOptions);
  }
}
