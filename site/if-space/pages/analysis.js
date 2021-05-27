import Head from "next/head";
import DefaultLayout from "../src/components/DefaultLayout";
import { Image } from "react-bootstrap";

export default function Analysis() {
  return (
    <div>
      <Head>
        <title>Analysis</title>
      </Head>

      <DefaultLayout>
        <div className="flex flex-col w-full">
          <div className="flex flex-col">
            <h1>Experiment 1: Insertion Chaining | Cuckoo (4 tables)</h1>
            <div className="flex flex-row ">
              <Image
                style={{ height: "30rem", width: "30rem" }}
                src="/assets/EXP1-Chain.png"
                className="bg-red-600 w-64 h-64"
              />
              <Image
                style={{ height: "30rem", width: "30rem" }}
                src="/assets/EXP1-Cuckoo.png"
                className="bg-red-600 w-64 h-64 ml-8"
              />
            </div>
          </div>

          <br />
          <br />
          <br />

          <div className="flex flex-col">
            <h1>
              Experiment 1b: Insertion Chaining | Cuckoo Optimized (2 tables)
            </h1>
            <div className="flex flex-row ">
              <Image
                style={{ height: "30rem", width: "30rem" }}
                src="/assets/EXP2-Chain.png"
                className="bg-red-600 w-64 h-64"
              />
              <Image
                style={{ height: "30rem", width: "30rem" }}
                src="/assets/EXP2-Cuckoo.png"
                className="bg-red-600 w-64 h-64  ml-8"
              />
            </div>
          </div>

          <br />
          <br />
          <br />
        </div>
      </DefaultLayout>
    </div>
  );
}
