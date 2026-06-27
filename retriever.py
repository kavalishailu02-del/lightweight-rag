from rank_bm25 import BM25Okapi

class Retriever:

    def __init__(self, sections):

        self.sections = sections

        tokenized = [
            s.lower().split()
            for s in sections
        ]

        self.bm25 = BM25Okapi(tokenized)

    def search(self, query, top_k=3):

        scores = self.bm25.get_scores(
            query.lower().split()
        )

        ranked = sorted(
            zip(scores, self.sections),
            reverse=True
        )

        return [
            chunk
            for _, chunk in ranked[:top_k]
        ]
