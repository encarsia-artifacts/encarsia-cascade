# Copyright 2023 Flavien Solt, ETH Zurich.
# Licensed under the General Public License, Version 3.0, see LICENSE for details.
# SPDX-License-Identifier: GPL-3.0-only

# This script executes a single program.

from cascade.fuzzfromdescriptor import fuzz_single_from_descriptor, basic_test
# from common.profiledesign import profile_get_medeleg_mask
from common.spike import calibrate_spikespeed
from cascade.toleratebugs import tolerate_bug_for_eval_reduction

import os
import sys

if __name__ == '__main__':
    if "CASCADE_ENV_SOURCED" not in os.environ:
        raise Exception("The Cascade environment must be sourced prior to running the Python recipes.")
    
    if len(sys.argv) != 3:
        raise Exception("Usage: python3 do_fuzzdesign.py <design_name> <simulator_executable>")

    descriptor = (455500, str(sys.argv[1]), 343, 1, True)

    calibrate_spikespeed()

    basic_test(*descriptor, check_pc_spike_again=True, simulator_executable=str(sys.argv[2]))

else:
    raise Exception("This module must be at the toplevel.")
