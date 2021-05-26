import NavigationBar from "../NavigationBar";
import Footer from "../Footer";

export default function DefaultLayout(props) {
  return (
    <div className="h-screen flex flex-col">
      <NavigationBar />
      <div className="mb-auto px-16">
      {props.children}
      </div>
      <Footer/>
    </div>
  );
}
