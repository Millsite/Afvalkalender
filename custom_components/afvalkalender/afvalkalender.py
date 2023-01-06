from ..const.const import(
    logger,
    SENSOR_COLLECTORS_OPZET
)

try:
    from . import dataCollectorOpzet
except ImportError as err:
    logger.error(f"Import error {err.args}")


class afvalkalender:
    def __init__(self,
        provider,
        postalCode,
        houseNumber,
        suffix
    ):
        self.provider = provider.strip().lower()
        self.postalCode = postalCode.strip().upper()
        self.houserNumber = houseNumber.strip()
        self.suffix = suffix.strip().lower()

        try:
            if provider in SENSOR_COLLECTORS_OPZET.keys:
                wasteData = dataCollectorOpzet.getWasteData(
                    self.provider,
                    self.postal_code,
                    self.street_number,
                    self.suffix,
                )
            else:
                logger.error(f"Unknown provider {provider}")
        except ValueError as err:
            logger.error(f"Check afvalkalender settings {err.args}")

