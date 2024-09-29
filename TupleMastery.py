flight_itinerary = [("Katherine", "Atlanta", "New York"), 
                    ("Janee", "Milwaukee", "Atlanta"), 
                    ("Kevin", "Los Angeles", "Paris")
]

def format_flight_info(flight_itinerary):
        for index,(traveler, origin, destination) in enumerate(flight_itinerary):
            print(f"Itinerary {index + 1}: {traveler} from {origin} to {destination}")

format_flight_info(flight_itinerary)