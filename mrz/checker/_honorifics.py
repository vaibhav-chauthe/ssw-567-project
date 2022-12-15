


""" Forbidden titles

    ICAO SPECS:

    Prefixes and suffixes, including titles, professional and academic qualifications,
    honours, awards, and hereditary status (such as Dr., Sir, Jr., Sr., I I and III)
    shall not be included in the MRZ except where the issuing State considers these to
    be legally part of the name. In such cases, prefixes or suffixes shall be represented
    as components of the secondary identifier(s)

    Therefore, items in the list below will be reported as warnings or errors if they
    are found in the secondary id. or primary id.

    Add or delete items according to needs

"""
# Forbidden titles:


titles = [
    "MR",
    "SIR",
    "JR",
    "MRS",
    "MISS",
    "MS",
    "MADAM",
    "DAME",
    "DR",
    "LADY",
    "LORD",
    "MX",
    "ESQ",
    "HE",
    "HON",
    "PROF",
    "MEP",
    "MP",
    "BT",
    "HON",
    "QC",
    "KC",
    "HH",
    "HAH",
    "HE",
    "HMEH",
    "REVD",
    "REV",
    "FR",
    "PR",
    "BR",
    "IMAN",
    "MUFTI",
    "HAFIZ",
    "HAFIZAH",
    "QARI",
    "MAWLANA",
    "HAJI",
    "SAYYID",
    "SAYYIDAH",
    "SHARIF",
    "SRI",
    "SREE",
    "SHRI",
    "SHREE",
    "SIRI",
    "SERI",
    "SMT",
    "KUM",
    "HER",
    "FRAU",
    "SIE",
    "EXCMO",
    "ILMO"
]
