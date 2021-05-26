import Link from "next/link";

export default function NavigationBar() {
  const navigation = [
    {
      title: "Home",
      url: "/",
    },
    {
      title: "Attendance",
      url: "/attendance",
    },
    {
      title: "Inventory",
      url: "/inventory",
    },
    {
      title: "Analyze",
      url: "/analyze",
    },
  ];

  return (
    <div className="shadow-md bg-white h-16 w-full top-0 flex flex-row px-16  items-center mb-4">
      <h2 className="mr-16 font-bold text-lg">Indexed Functions | ERP</h2>
      {navigation.map((item) => {
        return (
          <Link href={item.url}>
            <a className="text-black font-light text-md mx-4 hover:font-bold hover:scale-105">{item.title}</a>
          </Link>
        );

      })}
      <h2 className="ml-auto font-medium text-lg bg-pink-500 hover:bg-pink-600 text-center rounded-md text-white h-12 w-12 align-middle justify-center flex flex-col hover:bg-pink-900 cursor-pointer">JU</h2>

    </div>
  );
}
