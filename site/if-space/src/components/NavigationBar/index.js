import Link from "next/link";

export default function NavigationBar() {
  const navigation = [
    {
      title: "Home",
      url: "/home",
    },
    {
      title: "Home",
      url: "/home",
    },
    {
      title: "Home",
      url: "/home",
    },
    {
      title: "Home",
      url: "/home",
    },
  ];

  return (
    <div className="bg-white h-16 w-full top-0 flex flex-row px-16 justify-center items-center">
      {navigation.map((item) => {
        return (
          <Link href={item.url}>
            <h1 className="text-black font-bold text-lg uppercase mx-2">{item.title}</h1>
          </Link>
        );
      })}
    </div>
  );
}
