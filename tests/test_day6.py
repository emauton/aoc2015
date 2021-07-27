from aoc2015.day6 import (Instruction, parse, indices_1000x1000,
                          apply_discrete_instr, apply_variable_instr,
                          compute_lights)


def test_parse():
    instr = Instruction(op='toggle', start=(461, 550), end=(564, 900))
    assert parse('toggle 461,550 through 564,900') == instr


def test_indices_1000x1000():
    # Points corresponding to the indices (cf. notes in function docstring):
    #                                                 (0,0) (1,0) (2,0)
    #                                                 (0,1) (1,1) (2,1)
    #                                                 (0,2) (1,2) (2,2)
    assert list(indices_1000x1000((0, 0), (2, 2))) == [0,    1,    2,
                                                       1000, 1001, 1002,
                                                       2000, 2001, 2002]


def test_compute_lights():
    instrs = [Instruction(op='turn on', start=(0, 0), end=(2, 2)),
              Instruction(op='turn off', start=(0, 0), end=(1, 1)),
              Instruction(op='toggle', start=(2, 2), end=(2, 2))]

    discrete = compute_lights(instrs, apply_discrete_instr)
    variable = compute_lights(instrs, apply_variable_instr)

    assert discrete[0] == 0
    assert discrete[1002] == 1
    assert discrete[2002] == 0

    assert variable[0] == 0
    assert variable[1002] == 1
    assert variable[2002] == 3
