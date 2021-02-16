import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 


scores = [
    21, 17, 22, 22, 20, 18, 18, 22, 15, 15, 
    20, 18, 21, 20, 20, 19, 21, 20,
    19, 19, 18, 19, 20, 19, 
    # on exams questions 
    24, 20, 24, 21, 21, 23, 24, 23, 24, 20, 23, 21, 23, 22
    
    
    ]


ds = pd.DataFrame(scores, columns=['scores'])



dp = ds.value_counts()
dp = pd.concat( [dp, dp/len(ds)], axis=1 ).sort_index()
dp.rename(columns={0:'occur', 1:'prob'}, inplace=True)
dp = dp.sort_index(ascending=False)
dp['cumOccur'] = dp.occur.cumsum()
dp['cumProb'] = dp.prob.cumsum()
dp = dp.reset_index()



fig = plt.figure('',(10,5))
ax = fig.subplots(1,1,squeeze=True)
ax.bar(dp.scores, dp.prob, alpha=.6, lw=4, label='prob.')
ax.step( dp.scores, dp.cumProb, where='post', color='k', alpha=.7, lw=3, label='cum. prob.' )
ax.grid()
ax.set_xlabel('correct answers')
ax.legend()
plt.show()

