import { Fetch } from "react-request";
import { BASE_URL } from "../constants";

export default class DB {
  static async insertEmployee(data) {}

  static async loadEmployees(userID) {
    let jsonData = await fetch(BASE_URL + "/employees/all" + userID).then(
      (res) => res.json()
    );
    return jsonData;
  }
}
