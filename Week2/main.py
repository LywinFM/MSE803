# import datasets module (dynamic import avoids editor resolution issues)
try:
    sklearn = __import__("sklearn")
except ModuleNotFoundError as exc:
    raise ModuleNotFoundError(
        "scikit-learn is not installed. Install it with: pip install scikit-learn"
    ) from exc

# fetch dataset
iris = sklearn.datasets.load_iris(as_frame=True)

# data (as pandas dataframes)
X = iris.data
y = iris.target

# metadata
print(iris.DESCR)

# variable information
print(iris.feature_names)
