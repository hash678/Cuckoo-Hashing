import { Fetch } from "react-request";
import { BASE_URL } from "../constants";
import { useRouter } from "next/router";
import { useEffect } from "react";
import { toast } from "react-toastify";

export default class DB {
  static async loadEmployees() {
    let jsonData = await fetch(BASE_URL + "/employees-all/").then((res) =>
      res.json()
    );
    toast(`${jsonData?.timeTaken?.toFixed(2)}s to taken fetch employees`);

    return jsonData?.data;
  }

  static async findEmployee(id) {
    let jsonData = await fetch(BASE_URL + "/employees/" + id).then((res) =>
      res.json()
    );

    toast(`${jsonData?.timeTaken?.toFixed(2)}s to taken to find employee`);

    return jsonData?.data;
  }

  static async employeeDelete(id) {
    let jsonData = await fetch(BASE_URL + "/employees/" + id, {
      method: "DELETE",
    });
    return jsonData?.timeTaken;
  }

  static async employeeDeleteAll() {
    let jsonData = await fetch(BASE_URL + "/employees-batch/", {
      method: "DELETE",
    });
    toast(`${jsonData?.timeTaken?.toFixed(2)}s taken in operation`);

    return jsonData?.timeTaken;
  }

  static async insertEmployee(data) {
    var formdata = new FormData();

    for (const [key, value] of Object.entries(data)) {
      formdata.append(key, value);
    }

    var requestOptions = {
      method: "POST",
      body: formdata,
      redirect: "follow",
    };

    let response = await fetch(
      BASE_URL + "/employees/" + data?.ID,
      requestOptions
    ).then((res) => res.json());
    return response?.timeTaken;
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

    let response = await fetch(
      BASE_URL + "/employees-batch/",
      requestOptions
    ).then((res) => res.json());

    toast(`${response?.timeTaken?.toFixed(2)}s taken in operation`);
    return response?.timeTaken?.toFixed(2);
  }

  static async getAttendance(id){
    let jsonData = await fetch(BASE_URL + "/attendance/" + id).then((res) =>
        res.json()
    );

    toast(`${jsonData?.timeTaken?.toFixed(2)}s taken in operation`);
    return jsonData?.data
  }

  static async addAttendance(data){

    let id = data?.id

    var formdata = new FormData();

    formdata.append("date", data?.date);
    formdata.append("Name", data?.Name);
    formdata.append("Notes", data?.Notes);

    var requestOptions = {
      method: 'POST',
      body: formdata,
      redirect: 'follow'
    };

    fetch(BASE_URL+"/attendance/"+id, requestOptions)
        .then(response => response.text())
        .then(result => console.log(result))
        .catch(error => console.log('error', error));
  }

}
