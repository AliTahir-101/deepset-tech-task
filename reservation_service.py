import logging
from datetime import datetime
import requests
from fastapi import FastAPI
from pydantic import *
# Run with `uvicorn room_booking:app`
app = FastAPI()


class RoomBooking(BaseModel):
    room_id: str
    start_date: datetime
    end_date: datetime
    number_of_guests: int


class BookingSystem:
    url = "https://third-party-booking-system/room_availability"

    def check_room_availability(
        self, room_id: str, start_date: datetime, end_date
    ) -> bool:
        """Checks the room availability for the given time period."""
        return (
            requests.get(
                f"{self.url}/room/{room_id}/bookings",
                params={
                    "start_date": start_date.isoformat(),
                    "end_date": end_date.isoformat(),
                },
            ).json()["status"]
            == "free"
        )

    def book_rom(self, room_id: str, start_date: datetime, end_date: datetime) -> None:
        """Books the room for the given time period.
        :param room_id: the ID of the room to book
        :param start_date: the start date of the booking
        :param end_date: the end date of the booking
        """
        requests.post(
            f"{self.url}/room/{room_id}/bookings",
            params={
                "start_date": start_date.isoformat(),
                "end_date": end_date.isoformat(),
            },
        )
        print("Room booked! 🎉"
              )


@app.post("/book_room")
async def bookRoom(room_booking: RoomBooking):
    assert room_booking.start_date < room_booking.end_date
    assert room_booking.start_date > datetime.now()
    booking_system = BookingSystem()
    available = booking_system.check_room_availability(
        room_booking.room_id, room_booking.start_date, room_booking.end_date
    )
    if available:
        booking_system.book_rom(
            room_booking.room_id, room_booking.start_date, room_booking.end_date
        )
        return {"status": "success"}
    else:
        return {"status": "slot unavailable"}


@app.get("/health")
def health_check() -> str:
    return "OK"
