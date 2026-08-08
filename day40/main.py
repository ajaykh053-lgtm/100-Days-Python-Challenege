import os
import requests_cache
from pprint import pprint
from dotenv import load_dotenv
from data_manager import DataManager
from flight_search import FlightSearch
from datetime import datetime, timedelta
from flight_data import find_cheapest_flight
from notification_manager import NotificationManager

load_dotenv()
# ==================== Conserve requests and preserve your free plan ====================
requests_cache.install_cache(
    "flight_cache",
    urls_expire_after={
        "*.sheety.co*": requests_cache.DO_NOT_CACHE,
        "*": 3600,
    },
)
# ==================== Setup ====================
data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
# pprint(sheet_data)
user_data = data_manager.get_user_data()
flight_search = FlightSearch()
# Create an instance of the NotificationManager
notification_manager = NotificationManager()

# ==================== Set the Dates and Origin Airport ====================
tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))
ORIGIN_CITY = "Landon"
ORIGIN_CITY_IATA = "LHR"  # London Heathrow

# ==================== Find Cheap Flights ====================

for destination in sheet_data:
    pprint(f"Getting flights for {destination['city']}...")
    flights = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        is_direct=True,
        to_time=six_month_from_today,
    )
    cheapest_flight = find_cheapest_flight(
        flights, return_date=six_month_from_today.strftime("%Y-%m-%d")
    )
    pprint(f"{destination['city']}: GBP {cheapest_flight.price}")
    if cheapest_flight.price == "N/A":
        flights = flight_search.check_flights(
            ORIGIN_CITY_IATA,
            destination["iataCode"],
            from_time=tomorrow,
            is_direct=False,
            to_time=six_month_from_today,
        )
        cheapest_flight = find_cheapest_flight(
            flights, return_date=six_month_from_today.strftime("%Y-%m-%d")
        )
    if (
        cheapest_flight.price != "N/A"
        and cheapest_flight.price < destination["lowestPrice"]
    ):
        pprint(f"Lower price flight found to {destination['city']}!")
        data_manager.update_lowest_price(destination["id"], cheapest_flight.price)
        import smtplib
        connection = smtplib.SMTP("smtp.gmail.com", 587)
        connection.starttls()
        connection.login(user=os.environ["MY_EMAIL"], password=os.environ["PASSWORD"])
        message = f"Low price alert! Only GBP {cheapest_flight.price} to fly \nfrom {ORIGIN_CITY}({cheapest_flight.origin_airport}) to {destination['city']}({cheapest_flight.destination_airport}), \non {cheapest_flight.out_date} until {cheapest_flight.return_date}."
        for user in user_data:

            connection.sendmail(
                from_addr=os.environ["MY_EMAIL"],
                to_addrs=user["eMail"],
                msg=message,
            )
        # notification_manager.send_sms(
        #     message_body=f"Low price alert! Only GBP {cheapest_flight.price} to fly "
        #                  f"from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, "
        #                  f"on {cheapest_flight.out_date} until {cheapest_flight.return_date}."
        # )
        # SMS not working? Try whatsapp instead.
        # notification_manager.send_whatsapp(
        #     message_body=f"Low price alert! Only GBP {cheapest_flight.price} to fly "
        #     f"from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, "
        #     f"on {cheapest_flight.out_date} until {cheapest_flight.return_date}."
        # )
