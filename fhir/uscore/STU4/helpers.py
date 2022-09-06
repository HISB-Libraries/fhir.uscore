'''Helper functions for validation'''

from fhir.resources.codeableconcept import CodeableConcept
from fhir.resources.valueset import ValueSet

import requests


def check_cc_in_valueset(cc: CodeableConcept, vs: ValueSet) -> None | ValueError:
    '''Check if CodeableConcept is in ValueSet and if any elements deviate from ValueSet'''

    filtered_code_system = list(filter(lambda x: x.system == cc.coding[0].system, vs.compose.include))
    if len(filtered_code_system) == 0:
        return ValueError(f'The code {cc.coding[0].code} from system {cc.coding[0].system} is not in the {vs.title} ValueSet')

    filtered_codes = list(filter(lambda x: x.code == cc.coding[0].code, filtered_code_system[0].concept))
    if len(filtered_codes) == 0:
        return ValueError(f'Code {cc.coding[0].code} is not in the {vs.title} ValueSet')
    if cc.coding[0].display != filtered_codes[0].display:
        print(f'\nWARNING: The display was found to be {cc.coding[0].display}. It should be {filtered_codes[0].display}')
        return None


def validate_code_tx_server(cc: CodeableConcept, vs: ValueSet):
    '''Using tx.fhir.org to validate if code in ValueSet'''

    response = requests.post(f'https://tx.fhir.org/r4/ValueSet/{vs.id.split(":")[0]}/$validate-code?code={cc.coding[0].code}&system={cc.coding[0].system}', headers={'Accept': 'application/json'})
    if response.status_code != 200:
        print('\nWARNING: Something is wrong with the terminology server. Therefore terminology cannot be validated.')
        return None
    resp_result = list(filter(lambda x: x['name'] == 'result', response.json()['parameter']))[0]['valueBoolean']
    if resp_result == 'false':
        cause = list(filter(lambda x: x['name'] == 'cause', response.json()['parameter']))[0]['valueString']
        message = list(filter(lambda x: x['name'] == 'message', response.json()['parameter']))[0]['valueString']
        return ValueError(f'{cc.coding[0].code} was not in the {vs.name} ValueSet. The cause was {cause} and the full message is: {message}')
