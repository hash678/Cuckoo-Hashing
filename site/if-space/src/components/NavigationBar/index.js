import Link from "next/link";

export default function NavigationBar() {
  const navigation = [
    {
      title: "Home",
      url: "/home",
    },
    {
      title: "Attendance",
      url: "/home",
    },
    {
      title: "Inventory",
      url: "/home",
    },
    {
      title: "Analyze",
      url: "/home",
    },
  ];

  return (
    <div className="shadow-md bg-white h-16 w-full top-0 flex flex-row px-16  items-center">
      <h2 className="mr-16 font-bold text-lg">Indexed Functions</h2>
      {navigation.map((item) => {
        return (
          <Link href={item.url}>
            <a className="text-black font-light text-lg mx-4">{item.title}</a>
          </Link>
        );

      })}
      <h2 className="ml-auto font-bold text-lg">Login</h2>

    </div>
  );
}
