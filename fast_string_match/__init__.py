from difflib import SequenceMatcher, get_close_matches


def closest_match(query, choices, score_cutoff=0.6):
    if not choices:
        return None
    matches = get_close_matches(query, choices, n=1, cutoff=score_cutoff)
    return matches[0] if matches else None


def closest_match_distance(query, choices, score_cutoff=0.6):
    if not choices:
        return None
    best = None
    best_score = 0
    for choice in choices:
        score = SequenceMatcher(None, query.lower(), choice.lower()).ratio()
        if score > best_score and score >= score_cutoff:
            best = choice
            best_score = score
    return best
