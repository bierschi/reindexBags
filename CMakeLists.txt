CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

project(reindexBags)

file(GLOB SOURCES "*.cpp")

set(CMAKE_RUNTIME_OUTPUT_DIRECTORY "${CMAKE_CURRENT_SOURCE_DIR}/build")

add_executable(reindexBags ${SOURCES})
