from fastapi import FastAPI, Request
from pydantic import BaseModel
import json

app = FastAPI()

class DialogflowRequest(BaseModel):
    responseId: str
    queryResult: dict
    originalDetectIntentRequest: dict
    session: str

@app.post("/webhook")
async def handle_webhook(request: DialogflowRequest):
    # Extract the intent name and parameters
    intent_name = request.queryResult.get('intent').get('displayName')
    parameters = request.queryResult.get('parameters', {})
    
    # Extract session_id from the session URL
    session_id = request.session.split('/')[-1]
    
    # Handle different intents
    if intent_name == "Appointment.Cancel":
        return handle_appointment_cancel(parameters, session_id)
    elif intent_name == "Appointment.Confirmation":
        return handle_appointment_confirmation(parameters, session_id)
    elif intent_name == "Appointment.Followup":
        return handle_appointment_followup(parameters, session_id)
    elif intent_name == "appointment.inquiry":
        return handle_appointment_inquiry(parameters, session_id)
    elif intent_name == "Appointment.Reschedule":
        return handle_appointment_reschedule(parameters, session_id)
    elif intent_name == "Appointment.Schedule":
        return handle_appointment_schedule(parameters, session_id)
    else:
        return {"fulfillmentText": "Sorry, I didn't understand that."}

def handle_appointment_cancel(parameters, session_id):
    # Implement your logic here
    return {"fulfillmentText": f"Appointment cancellation confirmed for session {session_id}."}

def handle_appointment_confirmation(parameters, session_id):
    # Implement your logic here
    return {"fulfillmentText": f"Appointment confirmation received for session {session_id}."}

def handle_appointment_followup(parameters, session_id):
    # Implement your logic here
    return {"fulfillmentText": f"Scheduled follow-up appointment for session {session_id}."}

def handle_appointment_inquiry(parameters, session_id):
    # Implement your logic here
    return {"fulfillmentText": f"Here is your appointment information for session {session_id}."}

def handle_appointment_reschedule(parameters, session_id):
    # Implement your logic here
    return {"fulfillmentText": f"Appointment rescheduled for session {session_id}."}

def handle_appointment_schedule(parameters, session_id):
    # Implement your logic here
    return {"fulfillmentText": f"Appointment scheduled successfully for session {session_id}."}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

