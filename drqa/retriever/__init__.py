#!/usr/bin/env python3
# Copyright 2017-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.

import os
#from .. import DATA_DIR

DEFAULTS = {
		#'db_path':"C:/Users/lenovo/GUI/drqa-webui/DATA_DIR/wikipedia/docs.db",
        'db_path':"./DATA_DIR/Data_sql_db/combined.db",
        #'db_path':"G:/Capstone/data/wikipedia/docs.db",
        #"C:/Users/lenovo/Desktop/Capstone/Data_sql_db/combined.db"
		#'tfidf_path':"C:/Users/lenovo/GUI/drqa-webui/DATA_DIR/wikipedia/docs-tfidf-ngram=2-hash=16777216-tokenizer=simple.npz",
		'tfidf_path':"./DATA_DIR/Data_Tfidf/combined-tfidf-ngram=1-hash=16777216-tokenizer=simple.npz",
        #'tfidf_path':"G:/Capstone/data/wikipedia/docs-tfidf-ngram=2-hash=16777216-tokenizer=simple.npz",
        'elastic_url': 'localhost:9200'
}

#"C:/Users/lenovo/GUI/drqa-webui/DATA_DIR/wikipedia/docs-tfidf-ngram=2-hash=16777216-tokenizer=simple.npz"

def set_default(key, value):
    global DEFAULTS
    DEFAULTS[key] = value


def get_class(name):
    if name == 'tfidf':
        return TfidfDocRanker
    if name == 'sqlite':
        return DocDB
    if name == 'elasticsearch':
        return ElasticDocRanker
    raise RuntimeError('Invalid retriever class: %s' % name)


from .doc_db import DocDB
from .tfidf_doc_ranker import TfidfDocRanker
#from .elastic_doc_ranker import ElasticDocRanker
