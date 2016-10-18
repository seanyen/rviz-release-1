Name:           ros-jade-rviz
Version:        1.11.15
Release:        0%{?dist}
Summary:        ROS rviz package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/rviz
Source0:        %{name}-%{version}.tar.gz

Requires:       assimp
Requires:       eigen3-devel
Requires:       mesa-libGL-devel
Requires:       mesa-libGLU-devel
Requires:       ogre-devel
Requires:       qt-devel
Requires:       ros-jade-geometry-msgs
Requires:       ros-jade-image-geometry
Requires:       ros-jade-image-transport
Requires:       ros-jade-interactive-markers
Requires:       ros-jade-laser-geometry
Requires:       ros-jade-map-msgs
Requires:       ros-jade-media-export
Requires:       ros-jade-message-filters
Requires:       ros-jade-nav-msgs
Requires:       ros-jade-pluginlib
Requires:       ros-jade-python-qt-binding
Requires:       ros-jade-resource-retriever
Requires:       ros-jade-rosbag
Requires:       ros-jade-rosconsole
Requires:       ros-jade-roscpp
Requires:       ros-jade-roslib
Requires:       ros-jade-rospy
Requires:       ros-jade-sensor-msgs
Requires:       ros-jade-std-msgs
Requires:       ros-jade-std-srvs
Requires:       ros-jade-tf
Requires:       ros-jade-urdf
Requires:       ros-jade-visualization-msgs
Requires:       tinyxml-devel
Requires:       yaml-cpp-devel
BuildRequires:  assimp-devel
BuildRequires:  eigen3-devel
BuildRequires:  mesa-libGL-devel
BuildRequires:  mesa-libGLU-devel
BuildRequires:  ogre-devel
BuildRequires:  qt-devel
BuildRequires:  ros-jade-catkin
BuildRequires:  ros-jade-cmake-modules
BuildRequires:  ros-jade-geometry-msgs
BuildRequires:  ros-jade-image-geometry
BuildRequires:  ros-jade-image-transport
BuildRequires:  ros-jade-interactive-markers
BuildRequires:  ros-jade-laser-geometry
BuildRequires:  ros-jade-map-msgs
BuildRequires:  ros-jade-message-filters
BuildRequires:  ros-jade-nav-msgs
BuildRequires:  ros-jade-pluginlib
BuildRequires:  ros-jade-python-qt-binding
BuildRequires:  ros-jade-resource-retriever
BuildRequires:  ros-jade-rosbag
BuildRequires:  ros-jade-rosconsole
BuildRequires:  ros-jade-roscpp
BuildRequires:  ros-jade-roslib
BuildRequires:  ros-jade-rospy
BuildRequires:  ros-jade-sensor-msgs
BuildRequires:  ros-jade-std-msgs
BuildRequires:  ros-jade-std-srvs
BuildRequires:  ros-jade-tf
BuildRequires:  ros-jade-urdf
BuildRequires:  ros-jade-visualization-msgs
BuildRequires:  tinyxml-devel
BuildRequires:  yaml-cpp-devel

%description
3D visualization tool for ROS.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/jade" \
        -DCMAKE_PREFIX_PATH="/opt/ros/jade" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/jade

%changelog
* Tue Oct 18 2016 David Gossow <dgossow@gmail.com> - 1.11.15-0
- Autogenerated by Bloom

* Sun Apr 03 2016 David Gossow <dgossow@gmail.com> - 1.11.14-0
- Autogenerated by Bloom

* Tue Mar 22 2016 David Gossow <dgossow@gmail.com> - 1.11.12-0
- Autogenerated by Bloom

* Tue Mar 22 2016 David Gossow <dgossow@gmail.com> - 1.11.11-0
- Autogenerated by Bloom

* Tue Oct 13 2015 David Gossow <dgossow@gmail.com> - 1.11.10-0
- Autogenerated by Bloom

* Mon Sep 21 2015 David Gossow <dgossow@gmail.com> - 1.11.9-0
- Autogenerated by Bloom

* Wed Aug 05 2015 David Gossow <dgossow@gmail.com> - 1.11.8-0
- Autogenerated by Bloom

* Thu Apr 23 2015 David Gossow <dgossow@gmail.com> - 1.11.7-0
- Autogenerated by Bloom

