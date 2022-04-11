NEW_LEAD = 'new_lead'
FOLLOW_UP = 'follow_up'
DISCARDED_LEAD = 'discarded_lead'
REQUEST_IN_PROCESS = 'request_in_process'
CLIENT = 'client'

CATEGORY = (
    (NEW_LEAD, 'Nuovo Lead'),
    (FOLLOW_UP, 'Follow Up'),
    (DISCARDED_LEAD, 'Lead Scartato'),
    (REQUEST_IN_PROCESS, 'Pratica in avanzamento'),
    (CLIENT, 'Cliente')
)

DID_NOT_ANSWER = 'did_not_answer'
TO_CALL_AGAIN = 'to_call_again'
NOT_IN_TARGET = 'not_in_target'
FAKE_NUMBER = 'fake_number'
SEND_QUOTATION = 'send_quotation'

STATUS = (
    (DID_NOT_ANSWER, 'Non ha risposto'),
    (TO_CALL_AGAIN, 'Da Richiamare'),
    (NOT_IN_TARGET, 'Non in Target'),
    (FAKE_NUMBER , 'Numero Fake'),
    (SEND_QUOTATION, 'Preventivo da Inviare')
)