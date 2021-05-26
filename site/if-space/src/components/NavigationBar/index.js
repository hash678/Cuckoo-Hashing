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
    <div className="bg-white h-16 w-full top-0 flex-row px-16 items-center">
      {navigation.map((item) => {
        return (
          <Link href={item.url}>
            <div className="cursor-pointer text-black font-bold text-lg uppercase ">
              {item.title}
            </div>
          </Link>
        );
      })}
    </div>
  );
}
