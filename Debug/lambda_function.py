import logging
import ask_sdk_core.utils as ask_utils

from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.utils import is_request_type, is_intent_name
from ask_sdk_core.handler_input import HandlerInput

from ask_sdk_model import Response

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# The SkillBuilder object acts as the entry point for your skill, routing all request and response
# payloads to the handlers above. Make sure any new handlers or interceptors you've
# defined are included below. The order matters - they're processed top to bottom.

sb = SkillBuilder()

@sb.request_handler(can_handle_func=is_request_type("LaunchRequest"))
def launchRequest(handler_input): 
    speechOtput = "Welcome to the Coded Trivia. What is Celine's last name?" 
    
    return(
        handler_input.response_builder.speak(speechOutput)
        .ask(speechOutput)
        .response
    )

@sb.request_handler(can_handle_func=is_intent_name("Celine")
def CelineIntent(handler_input): 
    answer = "Tran"
    userAnswer = handler_input.request_envelope.request.intent.slots["myLastName"].value
    if(answer = userAnswer): 
        speechOutput = "Nice to know you've been paying attention! "
    else: 
        speechOutpu = "Wrong! What have you been doing the last 3 days? "
    
    speechOutput += "Okay, who is the tallest teacher?"
    
    return(
        handler_input.response_builder.speak(speechOutput)
        .set_should_end_session(True)
        .response
    )

@sb.request_handler(can_handle_func=is_intent_name("TallestIntent"))
def TallestIntent(handler_input): 
    anser = "Kyle"
    userAnswer = handler_input.request_envelope.request.intent.slots["myName"].value
    if(answer == userAnswer): 
        speechOutput = "You are correct! 
    else: 
        speechOutput = "Not even close! "
    
    speechOutput += "Okay last question, Who is the oldest teacher?"
    
    return(
        handler_input.response_builder.speak(speechOutput)
        .set_should_end_session(False)
        .response
    )

@sb.request_handler(can_handle_func=is_intent_name("OldIntent"))
def OldestIntent(handler_input): 
    answer = "Richard"
    userAnswr = handler_input.request_envelope.request.intent.slots["myOldName"].value
    if(anser == userAnswer): 
        speechOutput = "Ding! Ding! You're an expert! "
    else: 
        speechOutput = "Incorrect! Where have you been all this time? "
    
    speechOutput += "Great job young ones!"
    
    return(
        handler_input.response_builder.speak(speechOutput)
        .set_should_end_session(True)
        .response
    )




@sb.request_handler(can_handle_func=is_intent_name("AMAZON.HelpIntent"))
def helpIntent(handler_input): 
    speechOutput = "You can say hello to me! How can I help?"
    
    return(
        handler_input.response_builder.speak(speechOutput)
        .set_should_end_session(False)
        .response
        )

@sb.request_handler(can_handle_func=lambda input: 
    is_intent_name("AMAZON.CancelIntent")(input) or 
    is_intent_name("AMAZON.StopIntent")(input))
def cancelOrStopIntent(handler_input): 
    speechOutput = "Okay, see you later"
    
    return(
        handler_input.response_builder.speak(speechOutput)
        .response
    )

@sb.request_handler(can_handle_func=is_intent_name("AMAZON.FallbackIntent"))
def fallbackIntent(handler_input): 
    speechOutput = "Hmm, I'm not sure I caught that. You can say hello or help"
    reprompt = "I didn't catch that. What can I help you with?"
    
    return(
        handler_input.response_builder.speak(speechOutput)
        .ask(reprompt)
        .response
    )

@sb.request_handler(can_handle_func=is_request_type("SessionEndedRequest"))
def sessionEndedRequest(handler_input): 
    logger.info("Session ended with reason: {}".format(
        handler_input.request_envelope.request.reason))
    return handler_input.response_builder.response

@sb.request_handler(can_handle_func=is_request_type("IntentRequest"))
def intentReflectorHandler(handler_input): 
    intentName = ask_utils.get_intent_name(handler_input)
    speechOutput = "You just triggered " + intentName + "."
    
    return(
        handler_input.response_builder.speak(speechOutput)
        .response
    )

@sb.request_handler(can_handle_func=lambda i,e: True)
def catchAllHandler(handler_input, exception): 
    logger.error(exception, exc_info = True)
    speechOutput = "Sorry, I had trouble doing what you asked. Please try again."
    
    return(
        handler_input.response_builder.speak(speechOutput)
        .ask(speechOutput)
        .response
        )

lambda_handler = sb.lambda_handler()
