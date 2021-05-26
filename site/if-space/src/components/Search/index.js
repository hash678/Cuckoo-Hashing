import { Button, Form, Modal } from "react-bootstrap";
import { Controller, useForm } from "react-hook-form";
import { Search } from "react-bootstrap-icons";

export default function SearchModal({ isShow, onClose }) {
  const {
    handleSubmit,
    control,
    formState: { errors, isSubmitted },
  } = useForm();

  const onSubmit = (values) => {
    console.log(values);
  };

  return (
    <Modal
      id="fullScreenModalId"
      show={isShow}
      onHide={onClose}
      dialogClassName="fullscreen-modal"
    >
      <div className="bg-white w-8/12 p-8" style={{ height: "80%" }}>
        <div className="mb-4">
          <div className="flex flex-row w-full">
            <h1>Find your employee</h1>
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
          <Form
            onSubmit={handleSubmit(onSubmit)}
            className="flex flex-row justify-center items-start"
          >
            <Form.Group className="w-full mr-8">
              <Controller
                render={({ field }) => (
                  <Form.Control
                    className="w-full focus:outline-none border h-12 px-4 mb-4"
                    required
                    placeholder="ID"
                    {...field}
                    isInvalid={!!errors.name}
                  />
                )}
                name="ID"
                control={control}
                rules={{
                  required: "Please enter an employee name",
                }}
              />
            </Form.Group>

            <div className="flex flex-col items-center justify-center mr-2 font-medium text-lg bg-pink-500 hover:bg-pink-600 text-center rounded-lg text-white h-12 w-12 align-middle justify-center flex flex-col hover:bg-pink-900 cursor-pointer">
              <Search />
            </div>
          </Form>
        </div>
      </div>
    </Modal>
  );
}
