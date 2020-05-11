%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/noetic/.*$
%global __requires_exclude_from ^/opt/ros/noetic/.*$

Name:           ros-noetic-rviz
Version:        1.14.0
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS rviz package

License:        BSD
URL:            http://wiki.ros.org/rviz
Source0:        %{name}-%{version}.tar.gz

Requires:       assimp-devel
Requires:       mesa-libGL-devel
Requires:       mesa-libGLU-devel
Requires:       ogre-devel
Requires:       qt5-qtbase
Requires:       qt5-qtbase-gui
Requires:       ros-noetic-geometry-msgs
Requires:       ros-noetic-image-transport
Requires:       ros-noetic-interactive-markers
Requires:       ros-noetic-laser-geometry
Requires:       ros-noetic-map-msgs
Requires:       ros-noetic-media-export
Requires:       ros-noetic-message-filters
Requires:       ros-noetic-message-runtime
Requires:       ros-noetic-nav-msgs
Requires:       ros-noetic-pluginlib
Requires:       ros-noetic-python-qt-binding
Requires:       ros-noetic-resource-retriever
Requires:       ros-noetic-rosbag
Requires:       ros-noetic-rosconsole
Requires:       ros-noetic-roscpp
Requires:       ros-noetic-roslib
Requires:       ros-noetic-rospy
Requires:       ros-noetic-sensor-msgs
Requires:       ros-noetic-std-msgs
Requires:       ros-noetic-std-srvs
Requires:       ros-noetic-tf2-geometry-msgs
Requires:       ros-noetic-tf2-ros
Requires:       ros-noetic-urdf
Requires:       ros-noetic-visualization-msgs
Requires:       tinyxml2-devel
Requires:       yaml-cpp-devel
BuildRequires:  assimp-devel
BuildRequires:  eigen3-devel
BuildRequires:  mesa-libGL-devel
BuildRequires:  mesa-libGLU-devel
BuildRequires:  ogre-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  ros-noetic-catkin
BuildRequires:  ros-noetic-cmake-modules
BuildRequires:  ros-noetic-geometry-msgs
BuildRequires:  ros-noetic-image-transport
BuildRequires:  ros-noetic-interactive-markers
BuildRequires:  ros-noetic-laser-geometry
BuildRequires:  ros-noetic-map-msgs
BuildRequires:  ros-noetic-message-filters
BuildRequires:  ros-noetic-message-generation
BuildRequires:  ros-noetic-nav-msgs
BuildRequires:  ros-noetic-pluginlib
BuildRequires:  ros-noetic-python-qt-binding
BuildRequires:  ros-noetic-resource-retriever
BuildRequires:  ros-noetic-rosbag
BuildRequires:  ros-noetic-rosconsole
BuildRequires:  ros-noetic-roscpp
BuildRequires:  ros-noetic-roslib
BuildRequires:  ros-noetic-rospy
BuildRequires:  ros-noetic-rostest
BuildRequires:  ros-noetic-rosunit
BuildRequires:  ros-noetic-sensor-msgs
BuildRequires:  ros-noetic-std-msgs
BuildRequires:  ros-noetic-std-srvs
BuildRequires:  ros-noetic-tf2-geometry-msgs
BuildRequires:  ros-noetic-tf2-ros
BuildRequires:  ros-noetic-urdf
BuildRequires:  ros-noetic-visualization-msgs
BuildRequires:  tinyxml2-devel
BuildRequires:  urdfdom-devel
BuildRequires:  urdfdom-headers-devel
BuildRequires:  yaml-cpp-devel
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
3D visualization tool for ROS.

%prep
%autosetup

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_LIBDIR="lib" \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/noetic" \
    -DCMAKE_PREFIX_PATH="/opt/ros/noetic" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
    -DCATKIN_BUILD_BINARY_PACKAGE="1" \
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
%make_install -C obj-%{_target_platform}

%files
/opt/ros/noetic

%changelog
* Mon May 11 2020 William Woodall <william@osrfoundation.org> - 1.14.0-1
- Autogenerated by Bloom

