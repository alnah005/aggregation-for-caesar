from panoptes_aggregation import extractors
from .base_test_class import ExtractorTest

classification = {
    'metadata': {
        'classifier_version': '2.0'
    },
    'annotations': [
        {
            'task': 'T0',
            'taskType': 'dropdown-simple',
            'value': {
                'selection': 6,
                'option': True
            }
        }
    ]
}

expected = {'value': [{'6': 1}]}

TestSimpleDropdown = ExtractorTest(
    extractors.dropdown_extractor,
    classification,
    expected,
    'Test simple-dropdown task for classifier v2.0',
    test_name='TestSimpleDropdown'
)

classification_null = {
    'metadata': {
        'classifier_version': '2.0'
    },
    'annotations': [
        {
            'task': 'T0',
            'taskType': 'dropdown-simple',
            'value': None
        }
    ]
}

expected_null = {'value': [{'None': 1}]}

TestSimpleDropdownNull = ExtractorTest(
    extractors.dropdown_extractor,
    classification_null,
    expected_null,
    'Test simple-dropdown task for classifier v2.0 with no item selected',
    test_name='TestSimpleDropdownNull'
)
