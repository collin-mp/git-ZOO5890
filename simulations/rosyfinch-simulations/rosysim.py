"""A first, range-based simulation for interior Gray-crowned Rosy-Finches.

This version assigns each bird a new random point once per week. It models
seasonal range membership, but not the movement between ranges.
"""

from dataclasses import dataclass
from datetime import date, timedelta
import random


@dataclass(frozen=True)
class GeographicRange:
	"""A rectangular latitude/longitude range with an elevation interval."""

	name: str
	min_latitude: float
	max_latitude: float
	min_longitude: float
	max_longitude: float
	min_elevation_m: int
	max_elevation_m: int

	def random_point(self, rng: random.Random) -> tuple[float, float, int]:
		"""Return a random latitude, longitude, and elevation in this range."""
		latitude = rng.uniform(self.min_latitude, self.max_latitude)
		longitude = rng.uniform(self.min_longitude, self.max_longitude)
		elevation_m = rng.randint(self.min_elevation_m, self.max_elevation_m)
		return latitude, longitude, elevation_m


@dataclass(frozen=True)
class WeeklyObservation:
	"""One bird's simulated position for one week."""

	bird_id: int
	week_start: date
	stage: str
	range_name: str
	latitude: float
	longitude: float
	elevation_m: int


# These are intentionally example bounds, not published distribution data.
# Replace them with documented bounds when the source data is selected.
BREEDING_RANGE = GeographicRange(
	name="breeding",
	min_latitude=44.0,
	max_latitude=64.0,
	min_longitude=-155.0,
	max_longitude=-105.0,
	min_elevation_m=1500,
	max_elevation_m=4000,
)

NONBREEDING_RANGE = GeographicRange(
	name="nonbreeding",
	min_latitude=32.0,
	max_latitude=49.0,
	min_longitude=-125.0,
	max_longitude=-102.0,
	min_elevation_m=1000,
	max_elevation_m=3000,
)


def stage_for_week(week_number: int) -> tuple[str, GeographicRange]:
	"""Return the seasonal stage and range used for an ISO-like week number.

	Weeks 1-13 and 44-52 are nonbreeding; weeks 14-43 are treated as breeding
	for now because this first version does not model migration.
	"""
	if not 1 <= week_number <= 52:
		raise ValueError("week_number must be between 1 and 52")

	if week_number <= 13 or week_number >= 44:
		return "nonbreeding", NONBREEDING_RANGE
	return "breeding", BREEDING_RANGE


def simulate(
	bird_count: int = 1,
	start_date: date = date(2026, 1, 1),
	weeks: int = 52,
	seed: int | None = None,
) -> list[WeeklyObservation]:
	"""Generate one independent point per bird per week."""
	if bird_count < 1:
		raise ValueError("bird_count must be at least 1")
	if weeks < 1:
		raise ValueError("weeks must be at least 1")

	rng = random.Random(seed)
	observations: list[WeeklyObservation] = []
	for week_index in range(weeks):
		week_start = start_date + timedelta(weeks=week_index)
		week_number = week_start.isocalendar().week
		stage, geographic_range = stage_for_week(week_number)
		for bird_id in range(1, bird_count + 1):
			latitude, longitude, elevation_m = geographic_range.random_point(rng)
			observations.append(
				WeeklyObservation(
					bird_id=bird_id,
					week_start=week_start,
					stage=stage,
					range_name=geographic_range.name,
					latitude=latitude,
					longitude=longitude,
					elevation_m=elevation_m,
				)
			)
	return observations


if __name__ == "__main__":
	for observation in simulate(bird_count=2, seed=42):
		print(observation)
