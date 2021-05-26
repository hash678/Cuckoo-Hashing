import {Button, Form, Modal} from "react-bootstrap";
import { Controller, useForm } from "react-hook-form";

export default function AddNewEmployee({isShow, onClose, batch, }){


    const {
        handleSubmit,
        control,
        formState: { errors, isSubmitted },
    } = useForm();

    const onSubmit = (values) => {
        console.log(values)
    }

    return (
        <Modal
            id="fullScreenModalId" show={isShow} onHide={onClose} dialogClassName="fullscreen-modal" >
            <div className="bg-white w-1/2 p-8">
                <div className="mb-5">
                    <div className="flex flex-row w-full">
                        <h1 className="font-bold text-2xl">{`Add Employee Record${batch ? 's' : ''}`}</h1>
                        <Button closeButton className="ml-auto font-bold text-lg" onClick={onClose}>X</Button>
                    </div>
                </div>

                <div className="">
                    {
                        !batch &&
                        <Form onSubmit={handleSubmit(onSubmit)} className="flex flex-col">
                            <Form.Group className="w-full">
                                <div className="flex flex-row w-full">
                                    <Controller
                                        render={({ field }) => (
                                            <Form.Control
                                                className="w-1/2 mr-2 focus:outline-none border h-12 px-4 mb-4 w-full"
                                                required
                                                placeholder="Employee ID"
                                                {...field}
                                                isInvalid={!!errors.name}
                                            />
                                        )}
                                        name="id"
                                        control={control}
                                        rules={{
                                            required: "Please enter the employee's ID",
                                        }}
                                    />

                                    <Controller
                                        render={({ field }) => (
                                            <Form.Control
                                                className="w-1/2 ml-2 focus:outline-none border h-12 px-4 mb-4 w-full"
                                                required
                                                placeholder="Employee Name"
                                                {...field}
                                                isInvalid={!!errors.date}
                                            />
                                        )}
                                        name="name"
                                        control={control}
                                        rules={{
                                            required: "Please enter the employee's name",
                                        }}
                                    />
                                </div>

                                <Controller
                                    render={({ field }) => (
                                        <Form.Control
                                            className="w-1/2 ml-2 focus:outline-none border h-12 px-4 mb-4 w-full"
                                            required
                                            placeholder="Employee Email"
                                            {...field}
                                            isInvalid={!!errors.date}
                                        />
                                    )}
                                    name="email"
                                    control={control}
                                    rules={{
                                        required: "Please enter the employee's email",
                                    }}
                                />

                                <Controller
                                    render={({ field }) => (
                                        <Form.Control
                                            className="w-1/2 ml-2 focus:outline-none border h-12 px-4 mb-4 w-full"
                                            required
                                            placeholder="Employee Salary"
                                            {...field}
                                            isInvalid={!!errors.date}
                                        />
                                    )}
                                    name="salary"
                                    control={control}
                                    rules={{
                                        required: "Please enter the employee's salary",
                                    }}
                                />
                            </Form.Group>

                            <Button
                                type="submit"
                                className="focus:outline-none mb-8 bg-pink-500 px-4 py-2 rounded-md text-white self-end w-5/12"
                            >
                                Add Record
                            </Button>
                        </Form>
                    }

                    {
                        batch &&
                        <Form onSubmit={handleSubmit(onSubmit)} className="flex flex-col">
                            <Form.Group className="flex flex-row w-full justify-center items-center">
                                <Controller
                                    render={({ field }) => (
                                        <Form.Control
                                            className="w-1/2 mr-2 focus:outline-none border h-10 px-4 w-full"
                                            required
                                            placeholder="Upload CSV"
                                            {...field}
                                            isInvalid={!!errors.file}
                                        />
                                    )}
                                    name="csvFile"
                                    control={control}
                                    rules={{
                                        required: "Please upload a CSV file",
                                    }}
                                />

                                <Button
                                    type="submit"
                                    className="focus:outline-none mb-8 bg-pink-500 px-4 py-2 rounded-md text-white self-end w-5/12"
                                    style={{ marginBottom: "0" }}
                                >
                                    Add Record
                                </Button>
                            </Form.Group>
                        </Form>
                    }

                </div>
            </div>
        </Modal>
    )
}