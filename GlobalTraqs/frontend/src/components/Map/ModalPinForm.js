import React from "react";
import {
  Button,
  Modal,
  ModalHeader,
  ModalBody,
  ModalFooter,
  Form,
  FormGroup,
  Input,
  Label
} from "reactstrap";
import InputGroup from "react-bootstrap/InputGroup";
import DatePicker from "react-datepicker";
import "react-datepicker/dist/react-datepicker.css";
import TinyMCE from 'react-tinymce';

const buttonStyle = {
  float: "right"
};
const labelStyle = {
  marginRight: "10px"
};
function ModalPinForm(props) {

  return (
    <>
      <Modal
        isOpen={props.modalState}
        toggle={props.toggle}
        size="lg"
        aria-labelledby="contained-modal-title-vcenter"
        centered
      >
        <ModalHeader toggle={props.toggle}> Add a story </ModalHeader>
        <ModalBody>
          <Form onSubmit={props.onSubmit}>
            <FormGroup>
              <Label style={labelStyle} for="category">
                Category
              </Label>
              <select
                name="category"
                value={props.userForm.category}
                onChange={e =>
                  props.setuserForm({
                    ...props.userForm,
                    category: e.target.value
                  })
                }
              >
                <option value="1">Personal</option>
                <option value="2">Community</option>
                <option value="3">Historical</option>
              </select>
            </FormGroup>
            <FormGroup>
              <Label for="title">Title</Label>
              <Input
                className="form-control"
                type="text"
                name="title"
                value={props.userForm.title}
                onChange={e =>
                  props.setuserForm({
                    ...props.userForm,
                    title: e.target.value
                  })
                }
              />
            </FormGroup>
            <FormGroup>
              <Label for="description">Description</Label>
               <TinyMCE
                  content={props.userForm.description}
                  config={{
                    height: 300,
                    fontsize_formats: "8pt 10pt 12pt 14pt 18pt 24pt 36pt",
                    plugins: 'autolink link image lists print preview',
                    toolbar: 'undo redo | bold italic'
                  }}
                  onChange={e =>
                  props.setuserForm({
                    ...props.userForm,
                    description: e.target.getContent()
                  })}
                />
              {/*<Input*/}
              {/*  className="form-control"*/}
              {/*  type="textarea"*/}
              {/*  rows="5"*/}
              {/*  name="description"*/}
              {/*  value={props.userForm.description}*/}
              {/*  onChange={e =>*/}
              {/*    props.setuserForm({*/}
              {/*      ...props.userForm,*/}
              {/*      description: e.target.value*/}
              {/*    })*/}
              {/*  }*/}
              {/*/>*/}
            </FormGroup>
            <FormGroup>
              <Label style={labelStyle} for="radius">
                Anonymity radius
              </Label>
              <select
                name="anonradius"
                value={props.userRadius}
                onChange={e => props.setAnonRadius(e.target.value)}
              >
                <option value="1">None</option>
                <option value="2">Minimum</option>
                <option value="3">Moderate</option>
                <option value="4">Maximum</option>
              </select>
            </FormGroup>
            <InputGroup>
              <Label style={labelStyle} for="startDate">
                Start Date
              </Label>

              {/* <Controller
                isClear
                as={<DatePicker />}
                name="start"
                control={props.control}
                onChange={date => props.setStartDate(date)}
                defaultValue={props.startDate}
              /> */}
              <DatePicker
                isClearable
                todayButton="Today"
                name="start"
                selected={props.userForm.startDate}
                onChange={date =>
                  props.setuserForm({
                    ...props.userForm,
                    startDate: date
                  })
                }
              />
              <Label style={labelStyle} for="endDate">
                &nbsp;&nbsp;&nbsp;End Date
              </Label>
              <DatePicker
                isClearable
                todayButton="Today"
                name="enddate"
                selected={props.userForm.endDate}
                onChange={date =>
                  props.setuserForm({
                    ...props.userForm,
                    endDate: date
                  })
                }
              />
            </InputGroup>
            <Button style={buttonStyle} color="success">
              Save
            </Button>
          </Form>
        </ModalBody>
        <ModalFooter>
          <Button color="primary" onClick={props.toggle}>
            Do Something
          </Button>{" "}
          <Button color="secondary" onClick={props.toggle}>
            Cancel
          </Button>
        </ModalFooter>
      </Modal>
    </>
  );
}

export default ModalPinForm;
