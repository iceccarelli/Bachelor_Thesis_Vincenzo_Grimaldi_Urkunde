import pytest
import pandas as pd
import os

# Define the path to the key_details.csv extracted from the thesis PDF
KEY_DETAILS_CSV = os.path.join(os.path.dirname(__file__), os.pardir, 'data', 'key_details.csv')

@pytest.fixture(scope='module')
def key_details_df():
    """Fixture to load the key_details.csv into a pandas DataFrame for verification."""
    if not os.path.exists(KEY_DETAILS_CSV):
        pytest.fail(f"key_details.csv not found at {KEY_DETAILS_CSV}")
    return pd.read_csv(KEY_DETAILS_CSV)

def get_detail_value(df, section, key):
    """Helper function to retrieve a specific detail_value from the DataFrame."""
    result = df[(df['section'] == section) & (df['detail_key'] == key)]['detail_value']
    if result.empty:
        return None
    return str(result.iloc[0]).strip()

# ===================================================================
# General Author and University Information
# ===================================================================
def test_author_name_match(key_details_df):
    name = get_detail_value(key_details_df, 'General', 'Author')
    assert name == 'Vincenzo Ceccarelli Grimaldi', f"Author name mismatch: Expected 'Vincenzo Ceccarelli Grimaldi', got '{name}'"

def test_matriculation_number_match(key_details_df):
    number = get_detail_value(key_details_df, 'General', 'Matriculation Number')
    assert number == '353970', f"Matriculation number mismatch: Expected '353970', got '{number}'"

def test_university_match(key_details_df):
    university = get_detail_value(key_details_df, 'General', 'University')
    assert university == 'RWTH Aachen University', f"University mismatch: Expected 'RWTH Aachen University', got '{university}'"

def test_institute_match(key_details_df):
    institute = get_detail_value(key_details_df, 'General', 'Institute')
    assert institute == 'Institute of High Voltage Equipment and Grids (IAEW)', f"Institute mismatch: Expected 'Institute of High Voltage Equipment and Grids (IAEW)', got '{institute}'"

def test_date_acknowledgement_match(key_details_df):
    date_ack = get_detail_value(key_details_df, 'General', 'Date of Acknowledgement')
    assert date_ack == '17.01.2021', f"Date of Acknowledgement mismatch: Expected '17.01.2021', got '{date_ack}'"

# ===================================================================
# Thesis Core Metadata (Titles, Supervisors, Dates)
# ===================================================================
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

def test_chair_exam_board_match(key_details_df):
    chair = get_detail_value(key_details_df, 'Thesis', 'Chair of Examination Board')
    assert chair == 'Univ.-Prof. Dr.-Ing. Andreas Ulbig', f"Chair of Examination Board mismatch: Expected 'Univ.-Prof. Dr.-Ing. Andreas Ulbig', got '{chair}'"

def test_date_application_match(key_details_df):
    date_app = get_detail_value(key_details_df, 'Thesis', 'Date of Application')
    assert date_app == '08.01.2021', f"Date of Application mismatch: Expected '08.01.2021', got '{date_app}'"

def test_date_submission_match(key_details_df):
    date_sub = get_detail_value(key_details_df, 'Thesis', 'Date of Submission')
    assert date_sub == '17.01.2021', f"Date of Submission mismatch: Expected '17.01.2021', got '{date_sub}'"

# ===================================================================
# Thesis Objective and Methodology (directly from Chapter 1 & 4)
# ===================================================================
def test_main_objective_match(key_details_df):
    objective = get_detail_value(key_details_df, 'Thesis', 'Main Objective')
    expected = 'Create a feasible graph-based knowledge base using Neo4j to detect Advanced Persistent Threats (APTs) in Smart Grids through cross-domain data modeling, link analysis and cyber intelligence'
    assert objective == expected, f"Main Objective mismatch: Expected '{expected}', got '{objective}'"

def test_core_methodology_match(key_details_df):
    methodology = get_detail_value(key_details_df, 'Thesis', 'Core Methodology')
    expected = 'Passive IoT traffic collection → Graph DB storage → Link analysis + Similarity algorithms for anomaly/threat detection'
    assert methodology == expected, f"Core Methodology mismatch: Expected '{expected}', got '{methodology}'"

# ===================================================================
# Chapter Structure (pages and titles taken from table of contents)
# ===================================================================
@pytest.mark.parametrize("chapter_key,title_key,page_key,expected_title,expected_page", [
    ("Chapter 1 Title", "Chapter 1 Page", "Introduction – Motivation and Structured Objective", "10"),
    ("Chapter 2 Title", "Chapter 2 Page", "Theoretical Background – Network Protocols, Smart Grids, ICT/SCADA, Transmission vs Distribution", "14"),
    ("Chapter 3 Title", "Chapter 3 Page", "Models and Graphs – NoSQL approach, Neo4j, Cypher, caching layers, traverser API", "23"),
    ("Chapter 4 Title", "Chapter 4 Page", "Approach, Results and Discussion – Blackbox dataflow, link analysis, similarity algorithms, interpretation of results", "38"),
    ("Chapter 5 Title", "Chapter 5 Page", "Conclusion – Summary and Future Work", "47")
])
def test_chapter_details_match(key_details_df, chapter_key, page_key, expected_title, expected_page):
    title = get_detail_value(key_details_df, 'Chapters', chapter_key)
    page = get_detail_value(key_details_df, 'Chapters', page_key)
    assert title == expected_title, f"Chapter title mismatch for {chapter_key}: Expected '{expected_title}', got '{title}'"
    assert page == expected_page, f"Chapter page mismatch for {page_key}: Expected '{expected_page}', got '{page}'"

# ===================================================================
# Key Facts from Introduction (investment, IoT projection, smart grid goal)
# ===================================================================
def test_investment_needed_match(key_details_df):
    investment = get_detail_value(key_details_df, 'Key_Facts', 'Investment Needed')
    assert investment == '$13 billion in electric infrastructure over next 20+ years', f"Investment Needed mismatch: Expected '$13 billion in electric infrastructure over next 20+ years', got '{investment}'"

def test_iot_projection_match(key_details_df):
    iot = get_detail_value(key_details_df, 'Key_Facts', 'IoT Projection (Cisco)')
    assert iot == '14 billion artifacts by 2022', f"IoT Projection mismatch: Expected '14 billion artifacts by 2022', got '{iot}'"

def test_smart_grid_goal_match(key_details_df):
    goal = get_detail_value(key_details_df, 'Key_Facts', 'Smart Grid Goal')
    assert goal == 'Self-healing, scalable, renewable-integrated energy networks', f"Smart Grid Goal mismatch: Expected 'Self-healing, scalable, renewable-integrated energy networks', got '{goal}'"

# ===================================================================
# Core Technologies (Neo4j, Cypher, SCADA systems, cloud layers)
# ===================================================================
def test_main_database_match(key_details_df):
    db = get_detail_value(key_details_df, 'Technologies', 'Main Database')
    assert db == 'Neo4j (open-source graph database)', f"Main Database mismatch: Expected 'Neo4j (open-source graph database)', got '{db}'"

def test_query_language_match(key_details_df):
    query = get_detail_value(key_details_df, 'Technologies', 'Query Language')
    assert query == 'Cypher', f"Query Language mismatch: Expected 'Cypher', got '{query}'"

def test_key_systems_match(key_details_df):
    systems = get_detail_value(key_details_df, 'Technologies', 'Key Systems')
    assert systems == 'SCADA, RTU, MTU, IED, PLC, HMI', f"Key Systems mismatch: Expected 'SCADA, RTU, MTU, IED, PLC, HMI', got '{systems}'"

def test_cloud_layers_match(key_details_df):
    layers = get_detail_value(key_details_df, 'Technologies', 'Cloud Layers')
    assert layers == 'SaaS / PaaS / IaaS + Fog Computing', f"Cloud Layers mismatch: Expected 'SaaS / PaaS / IaaS + Fog Computing', got '{layers}'"

# ===================================================================
# Contributions (primary and secondary from Chapters 3–4)
# ===================================================================
def test_primary_contribution_match(key_details_df):
    contrib = get_detail_value(key_details_df, 'Contributions', 'Primary Contribution')
    assert contrib == 'Cross-domain knowledge base ontology using graph modeling for cyber intelligence', f"Primary Contribution mismatch: Expected 'Cross-domain knowledge base ontology using graph modeling for cyber intelligence', got '{contrib}'"

def test_secondary_contribution_match(key_details_df):
    contrib = get_detail_value(key_details_df, 'Contributions', 'Secondary Contribution')
    assert contrib == 'Application of link analysis and similarity algorithms for real-time APT detection in Smart Grids', f"Secondary Contribution mismatch: Expected 'Application of link analysis and similarity algorithms for real-time APT detection in Smart Grids', got '{contrib}'"

# ===================================================================
# Primary Threats Addressed (Chapter 4 focus areas)
# ===================================================================
def test_primary_threat_match(key_details_df):
    threat = get_detail_value(key_details_df, 'Threats', 'Primary Focus')
    assert threat == 'Advanced Persistent Threats (APTs)', f"Primary Focus mismatch: Expected 'Advanced Persistent Threats (APTs)', got '{threat}'"

def test_threat_ddos_match(key_details_df):
    threat = get_detail_value(key_details_df, 'Threats', 'Threat 1')
    assert threat == 'DDoS / TCP-UDP-ICMP Flood attacks', f"Threat 1 mismatch: Expected 'DDoS / TCP-UDP-ICMP Flood attacks', got '{threat}'"

def test_threat_mitm_match(key_details_df):
    threat = get_detail_value(key_details_df, 'Threats', 'Threat 2')
    assert threat == 'Man-in-the-Middle (MitM)', f"Threat 2 mismatch: Expected 'Man-in-the-Middle (MitM)', got '{threat}'"

def test_threat_rce_match(key_details_df):
    threat = get_detail_value(key_details_df, 'Threats', 'Threat 3')
    assert threat == 'Remote Code Execution (RCE)', f"Threat 3 mismatch: Expected 'Remote Code Execution (RCE)', got '{threat}'"

# ===================================================================
# Abbreviations and Key Terms (used throughout the thesis)
# ===================================================================
def test_scada_abbreviation_match(key_details_df):
    abbrev = get_detail_value(key_details_df, 'Abbreviations', 'SCADA')
    assert abbrev == 'Supervisory Control and Data Acquisition', f"SCADA abbreviation mismatch: Expected 'Supervisory Control and Data Acquisition', got '{abbrev}'"

def test_graph_advantage_match(key_details_df):
    term = get_detail_value(key_details_df, 'Key_Terms', 'Graph Advantage')
    assert term == 'Handles complex relationships, traversals and caching far better than relational DBs at scale', f"Graph Advantage mismatch: Expected 'Handles complex relationships, traversals and caching far better than relational DBs at scale', got '{term}'"

def test_core_algorithm_match(key_details_df):
    algo = get_detail_value(key_details_df, 'Key_Terms', 'Core Algorithm')
    assert algo == 'Similarity Algorithms + Link Analysis on Neo4j', f"Core Algorithm mismatch: Expected 'Similarity Algorithms + Link Analysis on Neo4j', got '{algo}'"

def test_cyber_intelligence_goal_match(key_details_df):
    goal = get_detail_value(key_details_df, 'Key_Terms', 'Cyber Intelligence Goal')
    assert goal == 'Identify compromised IoT devices and anomalies in real time within Smart Grid networks', f"Cyber Intelligence Goal mismatch: Expected 'Identify compromised IoT devices and anomalies in real time within Smart Grid networks', got '{goal}'"

# ===================================================================
# Final Verification
# ===================================================================
def test_final_verification_message():
    print("Bachelor's Thesi")
    assert True
