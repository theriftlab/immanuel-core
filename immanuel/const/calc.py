"""
    This file is part of immanuel - (C) The Rift Lab
    Author: Robert Davies (robert@theriftlab.com)


    Defines certain astrological and astronomical constants used for chart
    calculations.

"""


""" Aspects. """
CONJUNCTION = 0.0
OPPOSITION = 180.0
SQUARE = 90.0
TRINE = 120.0
SEXTILE = 60.0
SEPTILE = 51.43
SEMISQUARE = 45.0
SESQUISQUARE = 135.0
SEMISEXTILE = 30.0
QUINCUNX = 150.0
QUINTILE = 72.0
BIQUINTILE = 144.0

""" Calculations. """
MAX_ERROR = 0.000001                        # For precise exact conjunctions
STATION_SPEED = 0.0003                      # ~1 second of movement
YEAR_DAYS = 365.242196                      # Average days in a solar year

""" Mean daily planetary motions. """
SUN_MEAN_MOTION = 0.985556
MOON_MEAN_MOTION = 13.176389
MERCURY_MEAN_MOTION = 1.383333
VENUS_MEAN_MOTION = 1.2
MARS_MEAN_MOTION = 0.524167
JUPITER_MEAN_MOTION = 0.083056
SATURN_MEAN_MOTION = 0.033611
URANUS_MEAN_MOTION = 0.011667
NEPTUNE_MEAN_MOTION = 0.006667
PLUTO_MEAN_MOTION = 0.004167

""" Moon phases. """
NEW_MOON = 45
WAXING_CRESCENT = 90
FIRST_QUARTER = 135
WAXING_GIBBOUS = 180
FULL_MOON = 225
DISSEMINATING = 270
THIRD_QUARTER = 315
BALSAMIC = 360

""" MC progression formulae. """
NAIBOD = 1
SOLAR_ARC = 2
DAILY_HOUSES = 3

""" Part of Fortune formulae. """
DAY_FORMULA = 1
NIGHT_FORMULA = 2
DAY_NIGHT_FORMULA = 3