import { Button, Form, Modal } from "react-bootstrap";
import { Controller, useForm } from "react-hook-form";
import DB from "../../services/db";

export default function AddNewEmployee({ isShow, onClose, batch, onSuccess }) {
  const {
    handleSubmit,
    control,
    reset,
    formState: { errors, isSubmitted },
  } = useForm();

  const onSubmit = (values) => {
    console.log(values);
    DB.insertEmployee(values).then(() => {
      onClose();
      onSuccess();
      reset();
    });
  };

  return (
    <Modal
      id="fullScreenModalId"
      show={isShow}
      onHide={onClose}
      dialogClassName="fullscreen-modal"
    >
      <div className="bg-white w-8/12 p-8">
        <div className="mb-4">
          <div className="flex flex-row w-full">
            <h1 className="font-bold text-2xl">Add New Employee</h1>
            <Button
              closeButton
              className="ml-auto font-bold text-lg"
              onClick={onClose}
            >
              X
            </Button>
          </div>
        </div>

        <div>
          {!batch && (
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
                  name="ID"
                  control={control}
                  rules={{
                    required: "Please enter the employee's ID",
                  }}
                />

                <div className="flex flex-row w-full">
                  <Controller
                    render={({ field }) => (
                      <Form.Control
                        className="w-1/2 mr-2 focus:outline-none border h-12 px-4 mb-4 w-full"
                        required
                        placeholder="First Name"
                        {...field}
                        isInvalid={!!errors.name}
                      />
                    )}
                    name="FirstName"
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
                        placeholder="Last Name"
                        {...field}
                        isInvalid={!!errors.date}
                      />
                    )}
                    name="LastName"
                    control={control}
                    rules={{
                      required: "Please enter the employee's name",
                    }}
                  />
                </div>

                <Controller
                  render={({ field }) => (
                    <Form.Control
                      className="w-1/2 focus:outline-none border h-12 px-4 mb-4 w-full"
                      required
                      placeholder="Employee Email"
                      {...field}
                      isInvalid={!!errors.date}
                    />
                  )}
                  name="EMail"
                  control={control}
                  rules={{
                    required: "Please enter the employee's email",
                  }}
                />

                <Controller
                  render={({ field }) => (
                    <Form.Control
                      className="w-1/2 focus:outline-none border h-12 px-4 mb-4 w-full"
                      required
                      placeholder="Employee Salary"
                      {...field}
                      isInvalid={!!errors.date}
                    />
                  )}
                  name="Salary"
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
          )}
        </div>
      </div>
    </Modal>
  );
}
