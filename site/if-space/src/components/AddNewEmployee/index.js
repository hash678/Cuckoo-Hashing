import {Button, Form, Modal} from "react-bootstrap";
import { Controller, useForm } from "react-hook-form";

export default function AddNewEmployee({isShow, onClose}){


    const {
        handleSubmit,
        control,
        formState: { errors, isSubmitted },
    } = useForm();

    const onSubmit = (values) => {
        console.log(values)
    }

    return (
        <Modal id="fullScreenModalId" show={isShow} onHide={onClose} dialogClassName="fullscreen-modal" >
            <div className="bg-white w-8/12 p-8" style={{ height: "80%" }}>
                <div className="mb-4">
                    <div className="flex flex-row w-full">
                        <h1>Add New Employee</h1>
                        <Button closeButton className="ml-auto font-bold text-lg" onClick={onClose}>X</Button>
                    </div>
                </div>

                <div>
                    <Form onSubmit={handleSubmit(onSubmit)} className="flex flex-col justify-start items-start">

                        <Form.Group className="w-full">
                            <Controller
                                render={({ field }) => (
                                    <Form.Control
                                        className="w-full focus:outline-none border h-12 px-4 mb-4 w-full"
                                        required
                                        placeholder="Name"
                                        {...field}
                                        isInvalid={!!errors.name}
                                    />
                                )}
                                name="name"
                                control={control}
                                rules={{
                                    required: "Please enter an employee name",
                                }}
                            />
                        </Form.Group>

                        <Button
                            type="submit"
                            className="focus:outline-none mb-8 bg-pink-500 px-4 py-2 rounded-md text-white self-end"
                        >
                            Add employee
                        </Button>

                    </Form>
                </div>
            </div>
        </Modal>
    )
}