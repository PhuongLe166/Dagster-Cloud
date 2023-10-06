from dagster import Definitions, load_assets_from_modules, asset
from . import assets

@asset
def testing(context):
    context.log.info("TESTING!!!")

all_assets = load_assets_from_modules([assets])

defs = Definitions(
    assets=[testing],
)
