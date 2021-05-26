import {Button, Form, Modal} from "react-bootstrap";
import { Controller, useForm } from "react-hook-form";

export default function PopupDialog({isShow, onClose}){

    return (
            <Modal id="fullScreenModalId" show={isShow} onHide={onClose} dialogClassName="fullscreen-modal" >
                <div className="bg-white w-1/3 p-8">
                    <div className="mb-4">
                        <div className="flex flex-row w-full">
                            <h1 className="font-bold">Success</h1>
                            <Button closeButton className="ml-auto font-bold text-lg" onClick={onClose}>X</Button>
                        </div>
                    </div>

                    <div className="flex flex-col justify-center items-center">
                        <Button
                            type="submit"
                            className="focus:outline-none mb-8 bg-pink-500 px-4 py-2 rounded-md text-white self-end"
                            style={{ marginBottom: "0" }}
                        >
                            Close
                        </Button>
                    </div>
                </div>
            </Modal>

    );
}