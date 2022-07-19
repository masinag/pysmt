#
# This file is part of pySMT.
#
#   Copyright 2014 Andrea Micheli and Marco Gario
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
from pysmt.logics import QF_NRAT
from pysmt.shortcuts import FreshSymbol, Exp, Real, Sin, And, GE, LE, PI, LT, GT, Times
from pysmt.shortcuts import Solver
from pysmt.test import TestCase, main
from pysmt.test import skipIfNoSolverForLogic
from pysmt.typing import REAL


class TestNonLinear(TestCase):

    @skipIfNoSolverForLogic(QF_NRAT)
    def test_exp(self):
        x = FreshSymbol(REAL)
        f = And(GE(x, Real(0)),
                LE(x, Real(1)),
                GE(Exp(x), Real(1)),
                )
        for solver in self.env.factory.all_solvers(logic=QF_NRAT):
            with Solver(name=solver, logic=QF_NRAT) as s:
                self.assertTrue(s.is_sat(f))

    @skipIfNoSolverForLogic(QF_NRAT)
    def test_sin(self):
        x = FreshSymbol(REAL)
        f = And(GT(x, Real(0)),
                LT(x, Real(1)),
                LT(Sin(x), Real(0.5)),
                )
        for solver in self.env.factory.all_solvers(logic=QF_NRAT):
            with Solver(name=solver, logic=QF_NRAT) as s:
                self.assertTrue(s.is_sat(f))

    @skipIfNoSolverForLogic(QF_NRAT)
    def test_pi(self):
        x = FreshSymbol(REAL)
        f = And(
            GT(x, Times(Real(1/4), PI())),
            LT(x, Times(Real(1/2), PI())),
            LT(Sin(x), Real(1)),
        )
        for solver in ["cvc4"]:
            with Solver(name=solver, logic=QF_NRAT) as s:
                self.assertTrue(s.is_sat(f))


if __name__ == "__main__":
    main()