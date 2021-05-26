import Head from "next/head";
import { Image, Form, Button, Container, Row, Col, } from 'react-bootstrap';
import { Controller, useForm } from "react-hook-form";

export default function Login() {
    const {
        handleSubmit,
        control,
        formState: { errors, isSubmitted },
    } = useForm();

    const onSubmit = () => {}
    return (
        <>
            <Head>
                <title>Login</title>
            </Head>

            <div className="h-screen flex justify-center items-center">
                <div className="w-1/4 border border-5 border-black rounded-md flex flex-col flex-wrap p-5" style={{ height: "50%" }}>
                    <h1 className="text-black text-4xl text-center my-8 font-medium">Login</h1>

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
                                        placeholder="Password"
                                        {...field}
                                        isInvalid={!!errors.password}
                                    />
                                )}
                                name="salary"
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
        </>

    )
}