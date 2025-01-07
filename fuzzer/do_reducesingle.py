# Copyright 2023 Flavien Solt, ETH Zurich.
# Licensed under the General Public License, Version 3.0, see LICENSE for details.
# SPDX-License-Identifier: GPL-3.0-only

# This script reduces a single program.

# sys.argv[1]: design name
# sys.argv[2]: num of cores allocated to fuzzing
# sys.argv[3]: offset for seed (to avoid running the fuzzing on the same instances over again)

from cascade.reduce import reduce_program
from cascade.toleratebugs import tolerate_bug_for_eval_reduction
from common.profiledesign import profile_get_medeleg_mask
from common.spike import calibrate_spikespeed

import os
import sys

if __name__ == '__main__':
    if "CASCADE_ENV_SOURCED" not in os.environ:
        raise Exception("The Cascade environment must be sourced prior to running the Python recipes.")
    
    if len(sys.argv) != 2:
        raise Exception("Usage: python3 do_reducesingle.py <simulator_executable>")

    design_name = 'boom'
    descriptor = (154802, design_name, 292, 3, True)

    # # Optional
    # tolerate_bug_for_eval_reduction(design_name)

    calibrate_spikespeed()
    profile_get_medeleg_mask(design_name)

    reduce_program(*descriptor, True, check_pc_spike_again=True, simulator_executable=sys.argv[1])

else:
    raise Exception("This module must be at the toplevel.")
