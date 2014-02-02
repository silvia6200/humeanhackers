from nltk.sem.relextract import mk_pairs, mk_reldicts

def extract_rels(subjclass, objclass, doc_as_tree, pattern, window):
    pairs = mk_pairs(doc_as_tree)
    reldicts = mk_reldicts(pairs)
    return [r for r in reldicts
                    if r['subjclass'] == subjclass and
                       r['objclass'] == objclass and
                       len(r['filler'].split()) <= window and
                       pattern.match(r['filler'])]