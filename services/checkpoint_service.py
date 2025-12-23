from core.models import ETLCheckpoint

def get_checkpoint(db, source):
    return db.query(ETLCheckpoint).filter_by(source=source).first()

def update_checkpoint(db, source, last_id):
    checkpoint = get_checkpoint(db, source)
    if not checkpoint:
        checkpoint = ETLCheckpoint(source=source, last_processed_id=last_id)
        db.add(checkpoint)
    else:
        checkpoint.last_processed_id = last_id
    db.commit()
