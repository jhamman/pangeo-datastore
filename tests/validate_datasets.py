import os
import intake
import pytest

def get_master_catalog():
    # TODO: replace with environment variable
    fname = os.path.join(os.path.dirname(__file__),
                         '../intake-catalogs/master.yaml')
    return intake.Catalog(fname)

@pytest.fixture(scope="module")
def catalog(request):
    return get_master_catalog()

def test_open_master_catalog(catalog):
    pass

ALL_ENTRIES = list(get_master_catalog().walk(depth=10))
print(ALL_ENTRIES)

@pytest.fixture(scope="module", params=ALL_ENTRIES, ids=ALL_ENTRIES)
def dataset_name(request):
    return request.param

def test_get_intake_source(catalog, dataset_name):
    item = catalog[dataset_name]

@pytest.mark.skip(reason="need to resolve credentials issue for requester-pays data")
def test_intake_dataset_to_dask(catalog, dataset_name):
    item = catalog[dataset_name]
    try:
        ds = item.to_dask()
    except NotImplementedError:
        pytest.skip(f"Item {item} can't be loaded with `.to_dask()`")
