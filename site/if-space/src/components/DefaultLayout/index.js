import NavigationBar from "../NavigationBar";

export default function DefaultLayout(props) {
  return (
    <div className="bg-red-500">
      <NavigationBar />
      {props.children}
    </div>
  );
}
