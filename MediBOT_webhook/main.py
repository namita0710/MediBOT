from fastapi import FastAPI, Request
from pydantic import BaseModel
from fastapi.responses import JSONResponse
import json
import generic_helper

import db_helper
from datetime import datetime, time
app = FastAPI()

@app.post("/")
async def handle_request(request: Request):
    # Retrieve the JSON data from the request
    payload = await request.json()

    # Extract the necessary information from the payload
    # based on the structure of the WebhookRequest from Dialogflow
    intent = payload['queryResult']['intent']['displayName']
    parameters = payload['queryResult']['parameters']
    output_contexts = payload['queryResult']['outputContexts']
    session_id = generic_helper.extract_session_id(output_contexts[0]["name"])

    intent_handler_dict = {
            'appointment.inquiry': handle_appointment_inquiry,
            'Appointment.Schedule': handle_appointment_schedule,
            'Appointment.Confirmation': handle_appointment_confirmation,
            'Appointment.Reschedule': handle_appointment_reschedule,
            'Appointment.Cancel': handle_appointment_cancel,
            'Appointment.Followup': handle_appointment_followup
        }

    return intent_handler_dict[intent](parameters, session_id)
    
def handle_appointment_cancel(parameters, session_id):
    # Implement your logic here
    fulfillment_Text = "Appointment cancellation confirmed for session {session_id}."
    return JSONResponse(content={
        "fulfillmentText": fulfillment_Text
    })
def handle_appointment_schedule(parameters: dict, session_id: str):     
    email = parameters["email"]
    name=parameters["person"]["name"]    
    phone=parameters["phone-number"] 
    health_issue_list = parameters["Health_Issue"]
    duration=parameters["Duration"] 
    address=parameters["address"]
    appointment_type=parameters["appointment_type"]
    appointment_date_str = parameters["date"]
    appointment_time_str = parameters["time"]


    appointment_type_id = generic_helper.findAppointmentType_id(appointment_type)
    
    appointment_Datetime=generic_helper.merge_date_and_time(appointment_date_str,appointment_time_str)
      
    health_issues = generic_helper.get_str_from_health_issue_list(health_issue_list)
    
    db_helper.Insert_Appointment(name,email,phone,address,appointment_Datetime,appointment_type_id,health_issues,duration)
    
    fulfillment_text = f"Your appointment has been scheduled for {name},{email},{phone},{address},{appointment_Datetime},{appointment_type_id},{health_issues},{duration}"

    return JSONResponse(content={
        "fulfillmentText": fulfillment_text
    })

def handle_appointment_confirmation(parameters: dict, session_id: str):
    # Implement your logic here
    return {"fulfillmentText": f"Appointment confirmation received for session {session_id}."}

def handle_appointment_followup(parameters: dict, session_id: str):
    # Implement your logic here
    return {"fulfillmentText": f"Scheduled follow-up appointment for session {session_id}."}

def handle_appointment_inquiry(parameters: dict, session_id: str):
    name=parameters["person"]["name"]    
    mobile=parameters["phone-number"] 
    # Implement your logic here
    fulfillment_Text=name+" , Here is your mobile NO:"+ mobile +" appointment information for session ."
    return JSONResponse(content={
        "fulfillmentText": fulfillment_Text
    })
def handle_appointment_reschedule(parameters: dict, session_id: str):
    # Implement your logic here
    return {"fulfillmentText": f"Appointment rescheduled for session {session_id}."}



# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="127.0.0.1", port=8000)

