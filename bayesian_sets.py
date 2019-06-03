
import numpy as np
from Text_Process as tp

class Bayesian_Sets():
    def __init__(self, *args):
        super(ClassName, self).__init__(*args))
        self.vect = CountVectorizer()
        self.text = Text_Process()

        
    def compute_DTM(self, df):
        self.vect.fit(df)
        model = self.vect.transform(df)
        return pd.DataFrame(model.A, columns=vect.get_feature_names())
    
    def compute_DTM_ajustado(self,queries):
        model = self.vect.transform(df)
        return pd.DataFrame(model.A, columns=vect.get_feature_names())
    
    def bayesian_set(self,df,df_query):
        X = self.compute_DTM(df)
        N = len(queries)
        xij = self.compute_DTM_ajustado(df,self.text.processamento_text_stem(df))
        
    
