import { Button, Form, Modal } from "react-bootstrap";
import { Controller, useForm } from "react-hook-form";
import { useState } from "react";
import DB from "../../services/db";
import { toast } from "react-toastify";

export default function CSVUpload({ isShow, onClose, onUploaded }) {
  const [selectedFile, setSelectedFile] = useState(null);

  const {
    handleSubmit,
    control,
    formState: { errors, isSubmitted },
  } = useForm();

  const onSubmit = (values) => {
    console.log(selectedFile);
    DB.batchUploadEmployees(selectedFile)
      .then((response) => {
        onClose();

        onUploaded();
      })
      .catch((error) => {
        console.log(error);
      });
  };

  return (
    <Modal
      id="fullScreenModalId"
      show={isShow}
      onHide={onClose}
      dialogClassName="fullscreen-modal"
    >
      <div className="bg-white w-1/3 p-8">
        <div className="mb-5">
          <div className="flex flex-row w-full">
            <h1 className="font-bold text-2xl">Batch Upload Employees</h1>
          </div>
        </div>

        <div className="items-center">
          <Form
            onSubmit={handleSubmit(onSubmit)}
            className="flex flex-col justify-start items-start"
          >
            <Form.Group className="w-full">
              <input
                type="file"
                onChange={(e) => {
                  setSelectedFile(e.target.files?.[0]);
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
  );
}
