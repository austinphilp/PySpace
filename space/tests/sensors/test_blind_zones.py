from vectors import Point
from space.constants import directions
from space.tests.assertions import _assert_can_not_detect


# NOTE: These tests are failing because the current scan logic basically is
# trying to draw a 3d sphere with its center being the sensor_radius and the
# raidus being the radius of the cone at the distance from the body and
# checking if the body exists within the sphere. But this will almost always be
# true

# instead of this, we should do the following
# 1. Find the equation of the line defining the main axis of your cone.
# 2. Compute the distance from the 3D point to the line, 
#    along with the intersection point along the line where 
#    the distance is perpendicular to the line.
# 	 https://blender.stackexchange.com/questions/94464/finding-the-closest-point-on-a-line-defined-by-two-points<Paste>
# 3. Find the radius of your cone at the intersection point and check to see if the distance between the line and your 3D point is greater than (outside) or less than (inside) that radius.



def test_cant_sense_no_angle_sb():
    _assert_can_not_detect(
        target_pos=Point(0, -10, 0),
        scan_direction=directions.STARBOARD
    )


def test_cant_sense_no_angle_port():
    _assert_can_not_detect(
        target_pos=Point(0, 10, 0),
        scan_direction=directions.PORT
    )


def test_cant_sense_no_angle_oh():
    _assert_can_not_detect(
        target_pos=Point(0, 0, -10),
        scan_direction=directions.OVERHEAD
    )


def test_cant_sense_no_angle_deck():
    _assert_can_not_detect(
        target_pos=Point(0, 0, 10),
        scan_direction=directions.DECK
    )


def test_cant_sense_no_angle_for():
    _assert_can_not_detect(
        target_pos=Point(-10, 0, 0),
        scan_direction=directions.FORWARD
    )


def test_cant_sense_no_angle_aft():
    _assert_can_not_detect(
        target_pos=Point(10, 0, 0),
        scan_direction=directions.AFT,
    )
