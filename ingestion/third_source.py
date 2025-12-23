from schemas.raw_schema import RawRecord

def fetch_third_source():
    return [
        RawRecord(name="third-source-1", value=100.0),
        RawRecord(name="third-source-2", value=200.0),
    ]
