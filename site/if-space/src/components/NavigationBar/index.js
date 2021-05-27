import Link from "next/link";
import { Search } from "react-bootstrap-icons";
import SearchModal from "../Search";
import { useState } from "react";

export default function NavigationBar() {
  const [isShowSearch, setIsShowSearch] = useState(false);

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
      title: "Our Analysis",
      url: "/analysis",
    },
  ];

  return (
    <div className="shadow-md bg-white h-16 w-full top-0 flex flex-row px-16  items-center mb-4">
      <a href="/" className="mr-16 font-bold text-lg cursor-pointer">
        Indexed Functions | ERP
      </a>
      {navigation.map((item) => {
        return (
          <Link href={item.url}>
            <a className="text-black font-light text-md mx-4 hover:font-bold hover:scale-105">
              {item.title}
            </a>
          </Link>
        );
      })}
      <div className="ml-auto flex flex-row">
        <div
          onClick={() => setIsShowSearch(true)}
          className="flex flex-col items-center justify-center mr-2 font-medium text-lg bg-pink-500 hover:bg-pink-600 text-center rounded-lg text-white h-10 w-10 align-middle justify-center flex flex-col hover:bg-pink-900 cursor-pointer"
        >
          <Search />
        </div>
        <h2 className="font-medium text-lg bg-pink-500 hover:bg-pink-600 text-center rounded-lg text-white h-10 w-10 align-middle justify-center flex flex-col hover:bg-pink-900 cursor-pointer">
          JU
        </h2>
      </div>

      <SearchModal
        isShow={isShowSearch}
        onClose={() => {
          setIsShowSearch(false);
        }}
      />
    </div>
  );
}
