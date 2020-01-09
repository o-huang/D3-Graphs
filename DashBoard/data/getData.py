import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.manifold import MDS
import numpy
from sklearn.metrics import pairwise_distances
from sklearn.metrics.pairwise import pairwise_kernels
from sklearn.metrics.pairwise import *
df = pd.read_csv("pca_data.csv")


features =['GdpForYear(in Billions)','GdpPerCapital','Year','Suicide_Number','Population','Age']
x = df.loc[:, features].values

x = StandardScaler().fit_transform(x)

# Get PCA DATA -------------------------------------------

# pca = PCA(n_components=4)
# principalComponents = pca.fit_transform(x)
# principalDf = pd.DataFrame(data = principalComponents
#              , columns = ['principal component 1', 'principal component 2','principal component 3','principal component 4'])


# Get PCA DATA -------------------------------------------

#Get MDS Euclidian Data-----------------------------------

# varX = MDS(n_components=2,dissimilarity='euclidean')
# myData = varX.fit_transform(x)
# numpy.savetxt("mds_euclidian_data.csv",myData,delimiter=",")

#Get MDS Euclidian Data-----------------------------------


#Get Mds Consine Similarity Data--------------------------

myDataSet=cosine_similarity(x)

varX = MDS(n_components=2,dissimilarity='precomputed')
myData = varX.fit_transform(myDataSet)
numpy.savetxt("mds_cosine_data.csv",myData,delimiter=",")
#Get Mds Consine Similarity Data--------------------------
