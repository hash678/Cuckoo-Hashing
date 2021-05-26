import {Button, Form, Modal} from "react-bootstrap";
import { Controller, useForm } from "react-hook-form";

export default function PopupDialog({ isShow, onClose, message, }){

    return (
            <Modal id="fullScreenModalId" show={isShow} onHide={onClose} dialogClassName="fullscreen-modal" >
                <div className="bg-white w-1/3 p-8">
                    <div className="mb-5 text-center">
                            <h1 className="font-bold text-2xl">Success</h1>
                    </div>

                    <div className="flex flex-col justify-center items-center">
                        <h1 className="mb-5">{message}</h1>
                        <Button
                            className="focus:outline-none  mt-2 mb-8 bg-pink-500 px-4 py-2 rounded-md text-white self-end w-5/12"
                            style={{ marginBottom: "0" }}
                            onClick={ onClose }
                        >
                            Close
                        </Button>
                    </div>
                </div>
            </Modal>

    );
}