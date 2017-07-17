#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import gensim
import logging
import os
import bz2


class WikiCorpus(object):
    '''Corpus class which allows to read recursively a set of directories
    containing bzip2'ed text documents (Wikipedia articles)'''

    def __init__(self, directory):
        self.directory = directory

    def __iter__(self):
        for subdir, dirs, files in os.walk(self.directory):
            for f in files:
                for line in bz2.open(os.path.join(subdir, f), 'rt'):
                    yield line.split()


                    
if __name__ == "__main__":
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    CORPUSDIR = './'
    sentences = WikiCorpus(CORPUSDIR)

    logging.info('Building vocabulary and training')
    model = gensim.models.Word2Vec(sentences, min_count=10, size=150, workers=2)
    logging.info('Saving the model...')
    model.save('/data/eswiki-150.w2v')
    logging.info('Done')

    logging.info('Loading the model...')
    model = gensim.models.Word2Vec.load('/data/eswiki-150.w2v')
    logging.info('The model contains', model.corpus_count, 'items')
