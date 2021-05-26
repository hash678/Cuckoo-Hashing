import NavigationBar from "../NavigationBar";

export default function DefaultLayout(props) {
  return (
    <div className="">
      <NavigationBar />
      {props.children}
    </div>
  );
}
