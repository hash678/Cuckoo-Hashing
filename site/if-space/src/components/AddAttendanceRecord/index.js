import {Button, Form, Modal} from "react-bootstrap";
import { Controller, useForm } from "react-hook-form";
import DB from "../../services/db";

export default function AddAttendanceRecord({ isShow, onClose }){

    const {
        handleSubmit,
        control,
        formState: { errors, isSubmitted },
    } = useForm();

    const onSubmit = (values) => {
        console.log(values)
        DB.addAttendance(values).then(() => {
            onClose()
        })
    }

    return (
            <Modal id="fullScreenModalId" show={isShow} onHide={onClose} dialogClassName="fullscreen-modal" >
                <div className="bg-white w-8/12 p-8" >
                    <div className="mb-5">
                        <div className="flex flex-row w-full">
                            <h1 className="font-bold text-2xl">Add Attendance Record</h1>
                            <Button closeButton className="ml-auto font-bold text-lg" onClick={onClose}>X</Button>
                        </div>
                    </div>

                    <div className="">

                            <Form onSubmit={handleSubmit(onSubmit)} className="flex flex-col">
                                <Form.Group className="w-full">

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
                                            required: "Please enter an employee name",
                                        }}
                                    />
                                    <div className="flex flex-row w-full">
                                        <Controller
                                            render={({ field }) => (
                                                <Form.Control
                                                    className="w-1/2 mr-2 focus:outline-none border h-12 px-4 mb-4 w-full"
                                                    required
                                                    placeholder="Employee Name"
                                                    {...field}
                                                    isInvalid={!!errors.name}
                                                />
                                            )}
                                            name="Name"
                                            control={control}
                                            rules={{
                                                required: "Please enter an employee name",
                                            }}
                                        />


                                        <Controller
                                            render={({ field }) => (
                                                <Form.Control
                                                    className="w-1/2 ml-2 focus:outline-none border h-12 px-4 mb-4 w-full"
                                                    required
                                                    placeholder="Date"
                                                    type="datetime-local"
                                                    {...field}

                                                    isInvalid={!!errors.date}
                                                />
                                            )}
                                            name="date"

                                            control={control}
                                            rules={{
                                                required: "Please enter a date",
                                            }}
                                        />
                                    </div>

                                    <Controller
                                        render={({ field }) => (
                                            <Form.Control
                                                className="w-full focus:outline-none border h-12 px-4 mb-4 w-full"
                                                placeholder="Notes"
                                                {...field}
                                            />
                                        )}
                                        name="Notes"
                                        control={control}
                                    />
                                </Form.Group>

                                <Button
                                    type="submit"
                                    className="focus:outline-none mb-8 bg-pink-500 px-4 py-2 rounded-md text-white self-end w-5/12"
                                >
                                    Add Record
                                </Button>
                            </Form>



                    </div>
                </div>
            </Modal>

    );
}