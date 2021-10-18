# Group 43; Tuytte Victor; De Rijck Wout

from heapq import heapify

class Ranker():

    def __init__(self,dataset,query_processor,binary_search_tree,bk_tree = None):
        self._dataset = dataset
        self._query_processor = query_processor
        self._binary_search_tree = binary_search_tree
        self._bk_tree = bk_tree

    def evaluate(self,query):
        # Process the query
        query_list_stemmed = self._query_processor.process(query)
        query_list_not_stemmed = self._query_processor.process(query, False)

        # Store temp values in a dictionary 
        rankings = {}

        # Ranks book ids
        for i, word in enumerate(query_list_stemmed):
            # Get book ids
            book_ids = self._binary_search_tree.get(word)
            # Are there less than 5 results?
            if len(book_ids) < 5:
                # Look in BKtree for unstemmed words with distance 2
                new_words = self._bk_tree.get(query_list_not_stemmed[i], 2)
                # Stem the new words so we can look them up in the binary search tree
                new_words_stemmed = []
                for new_word in new_words:
                    new_words_stemmed.extend(self._query_processor.process(new_word[0]))
                # Add book ids of new stemmed words
                for new_word_stemmed in new_words_stemmed:
                    book_ids.extend(self._binary_search_tree.get(new_word_stemmed))

            # Updates ranking
            for id_ in book_ids:
                val = rankings.get(id_)
                if val is None:
                    rankings.update({id_:1})
                else:
                    rankings.update({id_:val+1})
        
        # Implement ranking method
        def get_rank(id_):
            return rankings.get(id_)

        # Sorting the ids
        ids = list(rankings.keys())
        ids.sort(reverse = True, key = get_rank)

        # Return top 5
        top5 = []
        for i in range(5):
            top5.append(self._dataset.get_title(ids[i]))
        return top5
    
    