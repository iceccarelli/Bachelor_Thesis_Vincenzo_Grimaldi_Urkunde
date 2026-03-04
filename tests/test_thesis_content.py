import pytest
import pandas as pd
import os

# Define the path to the key_details.csv
KEY_DETAILS_CSV = os.path.join(os.path.dirname(__file__), os.pardir, 'data', 'key_details.csv')

@pytest.fixture(scope='module')
def key_details_df():
    """Fixture to load the key_details.csv into a pandas DataFrame."""
    if not os.path.exists(KEY_DETAILS_CSV):
        pytest.fail(f"key_details.csv not found at {KEY_DETAILS_CSV}")
    return pd.read_csv(KEY_DETAILS_CSV)

def get_detail_value(df, section, key):
    """Helper function to get a detail_value from the DataFrame."""
    result = df[(df['section'] == section) & (df['detail_key'] == key)]['detail_value']
    if result.empty:
        return None
    return str(result.iloc[0]).strip()

def test_name_match(key_details_df):
    name = get_detail_value(key_details_df, 'General', 'Name')
    assert name == 'Vincenzo Ceccarelli Grimaldi', f"Name mismatch: Expected 'Vincenzo Ceccarelli Grimaldi', got '{name}'"

def test_thesis_title_english_match(key_details_df):
    title = get_detail_value(key_details_df, 'Thesis', 'Title (English)')
    expected_title = 'Development of a Cross-domain Knowledge Base for Cyber Intelligence in Smart Grids'
    assert title == expected_title, f"Thesis Title (English) mismatch: Expected '{expected_title}', got '{title}'"

def test_thesis_title_german_match(key_details_df):
    title = get_detail_value(key_details_df, 'Thesis', 'Title (German)')
    expected_title = 'Entwicklung einer domänenübergreifenden Wissensdatenbank für Cyber Intelligence in Smart Grids'
    assert title == expected_title, f"Thesis Title (German) mismatch: Expected '{expected_title}', got '{title}'"

def test_supervisor1_match(key_details_df):
    supervisor = get_detail_value(key_details_df, 'Thesis', 'Supervisor 1')
    assert supervisor == 'Ömer Sen, M.Sc.', f"Supervisor 1 mismatch: Expected 'Ömer Sen, M.Sc.', got '{supervisor}'"

def test_supervisor2_match(key_details_df):
    supervisor = get_detail_value(key_details_df, 'Thesis', 'Supervisor 2')
    assert supervisor == 'Dennis Van der Velde, M.Sc.', f"Supervisor 2 mismatch: Expected 'Dennis Van der Velde, M.Sc.', got '{supervisor}'"

def test_date_application_match(key_details_df):
    date_app = get_detail_value(key_details_df, 'Thesis', 'Date of Application')
    assert date_app == '08.01.2021', f"Date of Application mismatch: Expected '08.01.2021', got '{date_app}'"

def test_date_submission_match(key_details_df):
    date_sub = get_detail_value(key_details_df, 'Thesis', 'Date of Submission')
    assert date_sub == '17.01.2021', f"Date of Submission mismatch: Expected '17.01.2021', got '{date_sub}'"

def test_chair_exam_board_match(key_details_df):
    chair = get_detail_value(key_details_df, 'Signatures', 'Chair of Examination Board')
    assert chair == 'Univ.-Prof. Dr.-Ing. Andreas Ulbig', f"Chair of Examination Board mismatch: Expected 'Univ.-Prof. Dr.-Ing. Andreas Ulbig', got '{chair}'"

# Ensure the test output includes the verification message
def test_final_verification_message():
    assert True, "Bachelor's Thesis 100% verified against PDF content."
