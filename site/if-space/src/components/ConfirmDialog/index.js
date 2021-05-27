import { Button, Form, Modal } from "react-bootstrap";
import { Controller, useForm } from "react-hook-form";

export default function ConfirmDialog({ isShow, onClose, title, text, onYes }) {
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
            <h1 className="font-bold text-2xl">{title}</h1>
          </div>
        </div>

        <div className="items-center">
          <p>{text}</p>
          <br />
          <Button
            onClick={onYes}
            className="Button bg-pink-500 text-white p-2 m-2 w-16 rounded-md"
          >
            Yes
          </Button>
          <Button
            onClick={onClose}
            className="Button bg-pink-500 text-white  p-2 m-2 w-16 rounded-md"
          >
            No
          </Button>
        </div>
      </div>
    </Modal>
  );
}
