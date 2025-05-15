cmake_minimum_required(VERSION 3.8)
project(rahal_description)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

find_package(ament_cmake REQUIRED)


if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  #set(ament_cmake_copyright_FOUND TRUE)
  #set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()


install(
  DIRECTORY
    rviz/
  DESTINATION share/${PROJECT_NAME}/rviz
)

install(DIRECTORY launch DESTINATION share/${PROJECT_NAME})
install(
  DIRECTORY
  models/
  DESTINATION share/${PROJECT_NAME}/models
)
install(
  DIRECTORY
    worlds/
  DESTINATION share/${PROJECT_NAME}/worlds
)
install(
  DIRECTORY
    config/
  DESTINATION share/${PROJECT_NAME}/config
)
install(DIRECTORY meshes/
  DESTINATION share/${PROJECT_NAME}/meshes)

install(DIRECTORY textures/
DESTINATION share/${PROJECT_NAME}/textures)

install(DIRECTORY turtlebot3_world/
DESTINATION share/${PROJECT_NAME}/turtlebot3_world)

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  # the following line skips the linter which checks for copyrights
  # uncomment the line when a copyright and license is not present in all source files
  #set(ament_cmake_copyright_FOUND TRUE)
  # the following line skips cpplint (only works in a git repo)
  # uncomment the line when this package is not in a git repo
  #set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()

ament_package()
