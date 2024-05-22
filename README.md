# HIKAC

This modest python package helps you to get events from HIKVISION AC terminals. 

## Installation

```sh
pip install hikac


## Usage: example in FastAPI

```sh

from hikac import get_data_from_ac_event

@attandance_router.post("/attandance/face-id", include_in_schema=False)
async def get_attandance_users_list(
    req: Request,
    db: Session = ActiveSession,
):
    try:

        # use the class to collect nececary items of dict
        eventData = await get_data_from_ac_event(req)

        if eventData.attendanceStatus:

            # write here your main code

            return "success"
    except Exception as e:
        print(e.args)


