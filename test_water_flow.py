from pytest import approx
from water_flow import water_column_height, pressure_gain_from_water_height, pressure_loss_from_pipe
import pytest

def test_water_column_height():
    tower_height = 0
    tank_height = 0
    assert water_column_height(tower_height, tank_height) == 0
    tower_height = 0
    tank_height = 10
    assert water_column_height(tower_height, tank_height) == approx(7.5)
    tower_height = 25
    tank_height = 0
    assert water_column_height(tower_height, tank_height) == 25
    tower_height = 48.3
    tank_height = 12.8
    assert water_column_height(tower_height, tank_height) == approx(57.9)

def test_pressure_gain_from_water_height():
    height = 0
    assert pressure_gain_from_water_height(height) == approx(0, abs=0.001)
    height = 30.2
    assert pressure_gain_from_water_height(height) == approx(295.628, abs=0.001)
    height = 50
    assert pressure_gain_from_water_height(height) == approx(489.450, abs=0.001)
    

def test_pressure_loss_from_pipe():

    pipe_diameter = 0.048692
    pipe_length = 0
    friction_factor = 0.018
    fluid_velocity = 1.75
    assert pressure_loss_from_pipe(pipe_diameter,pipe_length, friction_factor, fluid_velocity) == approx(0, abs=0.001)
    pipe_diameter = 0.048692
    pipe_length = 200
    friction_factor = 0
    fluid_velocity = 1.75
    assert pressure_loss_from_pipe(pipe_diameter,pipe_length, friction_factor, fluid_velocity) == approx(0, abs=0.001)
    pipe_diameter = 0.048692
    pipe_length = 200
    friction_factor = 0.018
    fluid_velocity = 0
    assert pressure_loss_from_pipe(pipe_diameter,pipe_length, friction_factor, fluid_velocity) == approx(0, abs=0.001)
    pipe_diameter = 0.048692
    pipe_length = 200
    friction_factor = 0.018
    fluid_velocity = 1.75
    assert pressure_loss_from_pipe(pipe_diameter,pipe_length, friction_factor, fluid_velocity) == approx(-113.008, abs=0.001)
    pipe_diameter = 0.048692
    pipe_length = 200
    friction_factor = 0.018
    fluid_velocity = 1.65
    assert pressure_loss_from_pipe(pipe_diameter,pipe_length, friction_factor, fluid_velocity) == approx(-100.462, abs=0.001)
    pipe_diameter = 0.28687
    pipe_length = 1000
    friction_factor = 0.013
    fluid_velocity = 1.65
    assert pressure_loss_from_pipe(pipe_diameter,pipe_length, friction_factor, fluid_velocity) == approx(-61.576, abs=0.001)
    pipe_diameter = 0.28687
    pipe_length = 1800.75
    friction_factor = 0.013
    fluid_velocity = 1.65
    assert pressure_loss_from_pipe(pipe_diameter,pipe_length, friction_factor, fluid_velocity) == approx(-110.884, abs=0.001)

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])