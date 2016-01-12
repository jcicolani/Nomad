<<<<<<< HEAD
# Install script for directory: /home/nomad/nomad_ws/src/nomad

# Set the install prefix
IF(NOT DEFINED CMAKE_INSTALL_PREFIX)
  SET(CMAKE_INSTALL_PREFIX "/home/nomad/nomad_ws/install")
=======
# Install script for directory: /home/edison/nomad_ws/src/nomad

# Set the install prefix
IF(NOT DEFINED CMAKE_INSTALL_PREFIX)
  SET(CMAKE_INSTALL_PREFIX "/home/edison/nomad_ws/install")
>>>>>>> c894deaf8f51fc464f792dfd76aec936b4ce0648
ENDIF(NOT DEFINED CMAKE_INSTALL_PREFIX)
STRING(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
IF(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  IF(BUILD_TYPE)
    STRING(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  ELSE(BUILD_TYPE)
    SET(CMAKE_INSTALL_CONFIG_NAME "")
  ENDIF(BUILD_TYPE)
  MESSAGE(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
ENDIF(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)

# Set the component getting installed.
IF(NOT CMAKE_INSTALL_COMPONENT)
  IF(COMPONENT)
    MESSAGE(STATUS "Install component: \"${COMPONENT}\"")
    SET(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  ELSE(COMPONENT)
    SET(CMAKE_INSTALL_COMPONENT)
  ENDIF(COMPONENT)
ENDIF(NOT CMAKE_INSTALL_COMPONENT)

# Install shared libraries without execute permission?
IF(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  SET(CMAKE_INSTALL_SO_NO_EXE "1")
ENDIF(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
<<<<<<< HEAD
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/nomad/nomad_ws/build/nomad/catkin_generated/installspace/nomad.pc")
=======
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/edison/nomad_ws/build/nomad/catkin_generated/installspace/nomad.pc")
>>>>>>> c894deaf8f51fc464f792dfd76aec936b4ce0648
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/nomad/cmake" TYPE FILE FILES
<<<<<<< HEAD
    "/home/nomad/nomad_ws/build/nomad/catkin_generated/installspace/nomadConfig.cmake"
    "/home/nomad/nomad_ws/build/nomad/catkin_generated/installspace/nomadConfig-version.cmake"
=======
    "/home/edison/nomad_ws/build/nomad/catkin_generated/installspace/nomadConfig.cmake"
    "/home/edison/nomad_ws/build/nomad/catkin_generated/installspace/nomadConfig-version.cmake"
>>>>>>> c894deaf8f51fc464f792dfd76aec936b4ce0648
    )
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
<<<<<<< HEAD
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/nomad" TYPE FILE FILES "/home/nomad/nomad_ws/src/nomad/package.xml")
=======
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/nomad" TYPE FILE FILES "/home/edison/nomad_ws/src/nomad/package.xml")
>>>>>>> c894deaf8f51fc464f792dfd76aec936b4ce0648
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")

