# Copyright 2019 Pants project contributors (see CONTRIBUTORS.md).
# Licensed under the Apache License, Version 2.0 (see LICENSE).

import os
import sys

from dataclasses import dataclass
from typing import Set

from pants.base.specs import Specs
from pants.engine.console import Console
from pants.engine.goal import Goal, GoalSubsystem
from pants.engine.isolated_process import ExecuteProcessRequest, ExecuteProcessResult
from pants.engine.rules import console_rule, rule
from pants.engine.selectors import Get


class DebugInfoOptions(GoalSubsystem):
  name = 'debug-info'

  @classmethod
  def register_options(cls, register) -> None:
    super().register_options(register)

class DebugInfo(Goal):
  subsystem_cls = DebugInfoOptions


@console_rule
async def print_debug_info(
  console: Console, options: DebugInfoOptions, specs: Specs
) -> DebugInfo:
  """Prints important info for debugging pants"""

  console.print_stdout("=== operating system ===")
  console.print_stdout(os.uname())
  console.print_stdout("=== python ===")
  console.print_stdout(sys.version)
  console.print_stdout(sys.version_info)

  return DebugInfoTask(exit_code=0)


def rules():
  return [
      print_debug_info,
    ]
