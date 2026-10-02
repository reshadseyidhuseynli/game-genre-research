def deduplicate(rows):
    unique = {}
    for row in rows:
        identifier = row['review_id']
        if not identifier:
            raise ValueError('Cannot deduplicate review without review_id')
        previous = unique.get(identifier)
        # Later source order wins ties; source pages have deterministic order.
        if previous is None or (row['updated_at'] or '') >= (previous['updated_at'] or ''):
            unique[identifier] = row
    return sorted(unique.values(), key=lambda row: row['review_id']), len(rows) - len(unique)
