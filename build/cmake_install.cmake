<<<<<<< HEAD
# Install script for directory: /home/nomad/nomad_ws/src

# Set the install prefix
IF(NOT DEFINED CMAKE_INSTALL_PREFIX)
  SET(CMAKE_INSTALL_PREFIX "/home/nomad/nomad_ws/install")
=======
# Install script for directory: /home/edison/nomad_ws/src

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
  
      if (NOT EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}")
        file(MAKE_DIRECTORY "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}")
      endif()
      if (NOT EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/.catkin")
        file(WRITE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/.catkin" "")
      endif()
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
<<<<<<< HEAD
   "/home/nomad/nomad_ws/install/_setup_util.py")
=======
   "/home/edison/nomad_ws/install/_setup_util.py")
>>>>>>> c894deaf8f51fc464f792dfd76aec936b4ce0648
  IF (CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  ENDIF (CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
  IF (CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  ENDIF (CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
<<<<<<< HEAD
FILE(INSTALL DESTINATION "/home/nomad/nomad_ws/install" TYPE PROGRAM FILES "/home/nomad/nomad_ws/build/catkin_generated/installspace/_setup_util.py")
=======
FILE(INSTALL DESTINATION "/home/edison/nomad_ws/install" TYPE PROGRAM FILES "/home/edison/nomad_ws/build/catkin_generated/installspace/_setup_util.py")
>>>>>>> c894deaf8f51fc464f792dfd76aec936b4ce0648
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
<<<<<<< HEAD
   "/home/nomad/nomad_ws/install/env.sh")
=======
   "/home/edison/nomad_ws/install/env.sh")
>>>>>>> c894deaf8f51fc464f792dfd76aec936b4ce0648
  IF (CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  ENDIF (CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
  IF (CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  ENDIF (CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
<<<<<<< HEAD
FILE(INSTALL DESTINATION "/home/nomad/nomad_ws/install" TYPE PROGRAM FILES "/home/nomad/nomad_ws/build/catkin_generated/installspace/env.sh")
=======
FILE(INSTALL DESTINATION "/home/edison/nomad_ws/install" TYPE PROGRAM FILES "/home/edison/nomad_ws/build/catkin_generated/installspace/env.sh")
>>>>>>> c894deaf8f51fc464f792dfd76aec936b4ce0648
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
<<<<<<< HEAD
   "/home/nomad/nomad_ws/install/setup.bash")
=======
   "/home/edison/nomad_ws/install/setup.bash")
>>>>>>> c894deaf8f51fc464f792dfd76aec936b4ce0648
  IF (CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  ENDIF (CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
  IF (CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  ENDIF (CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
<<<<<<< HEAD
FILE(INSTALL DESTINATION "/home/nomad/nomad_ws/install" TYPE FILE FILES "/home/nomad/nomad_ws/build/catkin_generated/installspace/setup.bash")
=======
FILE(INSTALL DESTINATION "/home/edison/nomad_ws/install" TYPE FILE FILES "/home/edison/nomad_ws/build/catkin_generated/installspace/setup.bash")
>>>>>>> c894deaf8f51fc464f792dfd76aec936b4ce0648
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
<<<<<<< HEAD
   "/home/nomad/nomad_ws/install/setup.sh")
=======
   "/home/edison/nomad_ws/install/setup.sh")
>>>>>>> c894deaf8f51fc464f792dfd76aec936b4ce0648
  IF (CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  ENDIF (CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
  IF (CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  ENDIF (CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
<<<<<<< HEAD
FILE(INSTALL DESTINATION "/home/nomad/nomad_ws/install" TYPE FILE FILES "/home/nomad/nomad_ws/build/catkin_generated/installspace/setup.sh")
=======
FILE(INSTALL DESTINATION "/home/edison/nomad_ws/install" TYPE FILE FILES "/home/edison/nomad_ws/build/catkin_generated/installspace/setup.sh")
>>>>>>> c894deaf8f51fc464f792dfd76aec936b4ce0648
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
<<<<<<< HEAD
   "/home/nomad/nomad_ws/install/setup.zsh")
=======
   "/home/edison/nomad_ws/install/setup.zsh")
>>>>>>> c894deaf8f51fc464f792dfd76aec936b4ce0648
  IF (CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  ENDIF (CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
  IF (CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  ENDIF (CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
<<<<<<< HEAD
FILE(INSTALL DESTINATION "/home/nomad/nomad_ws/install" TYPE FILE FILES "/home/nomad/nomad_ws/build/catkin_generated/installspace/setup.zsh")
=======
FILE(INSTALL DESTINATION "/home/edison/nomad_ws/install" TYPE FILE FILES "/home/edison/nomad_ws/build/catkin_generated/installspace/setup.zsh")
>>>>>>> c894deaf8f51fc464f792dfd76aec936b4ce0648
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
<<<<<<< HEAD
   "/home/nomad/nomad_ws/install/.rosinstall")
=======
   "/home/edison/nomad_ws/install/.rosinstall")
>>>>>>> c894deaf8f51fc464f792dfd76aec936b4ce0648
  IF (CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  ENDIF (CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
  IF (CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  ENDIF (CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
<<<<<<< HEAD
FILE(INSTALL DESTINATION "/home/nomad/nomad_ws/install" TYPE FILE FILES "/home/nomad/nomad_ws/build/catkin_generated/installspace/.rosinstall")
=======
FILE(INSTALL DESTINATION "/home/edison/nomad_ws/install" TYPE FILE FILES "/home/edison/nomad_ws/build/catkin_generated/installspace/.rosinstall")
>>>>>>> c894deaf8f51fc464f792dfd76aec936b4ce0648
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")

IF(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for each subdirectory.
<<<<<<< HEAD
  INCLUDE("/home/nomad/nomad_ws/build/gtest/cmake_install.cmake")
  INCLUDE("/home/nomad/nomad_ws/build/nomad/cmake_install.cmake")
=======
  INCLUDE("/home/edison/nomad_ws/build/gtest/cmake_install.cmake")
  INCLUDE("/home/edison/nomad_ws/build/nomad/cmake_install.cmake")
>>>>>>> c894deaf8f51fc464f792dfd76aec936b4ce0648

ENDIF(NOT CMAKE_INSTALL_LOCAL_ONLY)

IF(CMAKE_INSTALL_COMPONENT)
  SET(CMAKE_INSTALL_MANIFEST "install_manifest_${CMAKE_INSTALL_COMPONENT}.txt")
ELSE(CMAKE_INSTALL_COMPONENT)
  SET(CMAKE_INSTALL_MANIFEST "install_manifest.txt")
ENDIF(CMAKE_INSTALL_COMPONENT)

<<<<<<< HEAD
FILE(WRITE "/home/nomad/nomad_ws/build/${CMAKE_INSTALL_MANIFEST}" "")
FOREACH(file ${CMAKE_INSTALL_MANIFEST_FILES})
  FILE(APPEND "/home/nomad/nomad_ws/build/${CMAKE_INSTALL_MANIFEST}" "${file}\n")
=======
FILE(WRITE "/home/edison/nomad_ws/build/${CMAKE_INSTALL_MANIFEST}" "")
FOREACH(file ${CMAKE_INSTALL_MANIFEST_FILES})
  FILE(APPEND "/home/edison/nomad_ws/build/${CMAKE_INSTALL_MANIFEST}" "${file}\n")
>>>>>>> c894deaf8f51fc464f792dfd76aec936b4ce0648
ENDFOREACH(file)
