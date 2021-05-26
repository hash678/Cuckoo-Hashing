import {Button, Form, Modal, Spinner} from "react-bootstrap";
import { Controller, useForm } from "react-hook-form";
export default function AddNewEmployee({isShow, onClose}){


    const {
        handleSubmit,
        control,
        formState: { errors, isSubmitted },
    } = useForm();

    const fields = [
        {
        type:"text",
        name:"fname",
        placeholder:"First Name",
        title:"First Name"
    },
        {
            type:"text",
            name:"lname",
            placeholder:"Last Name",
            title:"Last Name"
        },
        {
            type:"number",
            name:"salary",
            placeholder:"Salary",
            title:"Salary"
        },
        {
            type:"text",
            name:"department",
            placeholder:"Department",
            title:"Department"
        },
    ]

    const onSubmit = (values) => {
        console.log(values)
    }

    return (
        <Modal id="fullScreenModalId" show={isShow} onHide={onClose} dialogClassName="fullscreen-modal " >
            <div className="bg-white h-full w-full p-8">
            <div className="mb-12">

                <div className="flex flex-row w-full">
                <h1 className="font-bold text-pink-500">Add New Employee</h1>
                    <Button closeButton className="ml-auto font-bold text-lg" onClick={onClose}>X</Button>
                </div>

            </div>


            <div className="flex flex-col justify-center w-full">
                <Form onSubmit={handleSubmit(onSubmit)}>

                    {fields.map(field => {

                        return (
                            <Form.Group>
                                <Form.Label className="font-bold mb-2 pb-2">{field.title}</Form.Label>

                                <Controller
                                    render={({ field }) => (
                                        <Form.Control
                                            className="w-full focus:outline-none border h-12 px-4 mb-4"
                                            required
                                            placeholder={field.title}
                                            {...field}
                                            isInvalid={!!errors.name}
                                        />
                                    )}
                                    name={field.name}
                                    control={control}
                                    rules={{
                                        required: "Please enter an employee name",
                                    }}
                                />
                            </Form.Group>

                        )
                    })}


                    <Button type="submit" className="Button bg-pink-500 px-4 py-2 text-white shadow-sm">
                        <Spinner animation="border" role="status"/>
                        Add employee</Button>

                </Form>
            </div>

            </div>
        </Modal>
    )
}