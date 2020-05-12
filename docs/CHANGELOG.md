# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html)
# [0.1.0]
## Added
 - Basic server infrastructure
 - Command interface for interacting with server objects
 - Reporting interface for reading server object data.

# [0.0.5]
## Added
 - Degredation to thrusters and reactions wheels, which applies when more than 100% thrust is set
 - Reactors, which provide powers to ships, Each component consumes power, when the power capacity of a ship is overloaded, the performance of its powered components will degrade

# [0.0.4] 
### Removed
 - Egg info files

# [0.0.3] 
### Added
 - Dimensions and mass, which now factor into thrust acceleration
 - Fstrings in place of str.format

### Removed
 - Decimal implementation, for now we will use floats, and eventually we will migrate to a more precise float representation

# [0.0.1] 
### Added
 - Basic classes such as Ship and Thruster to represent the players vehicle and motion throughout the game
 - Accurate vector mathementics to calculate 3 dimmensional movement in space
 - Comprehensive testing to ensure that physics calculations are sufficiently accurate
