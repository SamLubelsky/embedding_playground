def process_embedding_data(filename):
    embeddings_dict = {}
    with open(filename, 'r') as f:
        lines = f.readlines()[1:] #don't include first line, b/c it is metadata

    lines = list(map(lambda s: s.strip().split(' '), lines))
    for line in lines:
        embedding_data = list(map(float, line[1:]))
        embedding_key = line[0]
        assert len(embedding_data) == 100
        embeddings_dict[embedding_key] = embedding_data

    return embeddings_dict
