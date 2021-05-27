import { useEffect } from "react";

import Head from "next/head";
import { useRouter } from "next/router";

import { Image, Form, Button } from "react-bootstrap";
import { Controller, useForm } from "react-hook-form";

import { Person } from "react-bootstrap-icons";
import Footer from "../src/components/Footer";

export default function Login() {
  const {
    handleSubmit,
    control,
    formState: { errors, isSubmitted },
  } = useForm();

  const router = useRouter();

  const onSubmit = () => {
    router.push("/");
  };

  // useEffect(() => {
  //     router.push('/');
  // }, []);
  return (
    <>
      <Head>
        <title>Login</title>
      </Head>

      <div className="h-screen flex justify-center items-center">
        <div
          className="w-1/4 border-2 border-pink-500 rounded-md flex flex-col  px-5 py-8"
          style={{ height: "50%" }}
        >
          <Person className="text-6xl text-pink-500 mx-auto border-pink-500" />
          <h1 className="text-black text-3xl text-center mt-2 mb-8 font-medium">
            Login
          </h1>

          <Form onSubmit={handleSubmit(onSubmit)} className="flex flex-col">
            <Form.Group className="w-full">
              <Controller
                render={({ field }) => (
                  <Form.Control
                    className="w-1/2 focus:outline-none border h-12 px-4 mb-4 w-full"
                    required
                    placeholder="Enter your email"
                    {...field}
                    isInvalid={!!errors.email}
                  />
                )}
                name="email"
                control={control}
                rules={{
                  required: "Please enter your email address",
                }}
              />

              <Controller
                render={({ field }) => (
                  <Form.Control
                    className="w-1/2 focus:outline-none border h-12 px-4 mb-4 w-full"
                    required
                    type="password"
                    placeholder="Password"
                    {...field}
                    isInvalid={!!errors.password}
                  />
                )}
                name="password"
                control={control}
                rules={{
                  required: "Please enter your password",
                }}
              />
            </Form.Group>

            <Button
              type="submit"
              className="focus:outline-none mt-8 bg-pink-500 hover:bg-pink-600 px-4 py-2 rounded-md text-white self-end w-full"
            >
              Login
            </Button>
          </Form>
        </div>
      </div>
      <Footer />
    </>
  );
}
