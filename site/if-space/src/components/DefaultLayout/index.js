import NavigationBar from "../NavigationBar";
import Footer from "../Footer";
import { ToastContainer } from "react-toastify";

export default function DefaultLayout(props) {
  return (
    <div className=" flex flex-col">
      <NavigationBar />
      <div className="min-vh-100 mb-auto px-16 py-8">{props.children}</div>
      <Footer />
      <ToastContainer />
    </div>
  );
}
