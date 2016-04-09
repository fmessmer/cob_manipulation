#! /usr/bin/env python

import os
import rospy
import roslib
from cob_grasp_generation import or_grasp_generation

if __name__ == '__main__':
  rospy.init_node('show_model')
  os.environ['OPENRAVE_DATA'] = roslib.packages.get_pkg_dir('cob_grasp_generation')+'/files' # required to find local OR-Data
  orgg = or_grasp_generation.ORGraspGeneration()
  orgg.setup_environment("pringles", "cob3", True)
  #orgg.setup_environment("pringles", "sdh", True)
  rospy.spin()
