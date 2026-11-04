---
kind: statement
name: Uniqueness of solutions of a consistent linear system by pivot columns
msc:
- 15A06
role: theorem
sources:
- locator: src/section1-4.xml:917
  url: https://github.com/davidaustinm/ula/blob/b6ea263ef23703072b7007485bb7a2d89c5f399b/src/section1-4.xml#L917
tag: 5MGKEK1K42
uses:
- 0X6V9B1V10
- 0GT4WWGWH2
- 0BCMGDHZGR
---

## Statement

Take a [[system of linear equations|0GT4WWGWH2]] over the real numbers that is [[consistent|0X6V9B1V10]]. Look at the [[pivot positions|0BCMGDHZGR]] of its coefficient matrix.

If each column of the coefficient matrix holds a pivot position, then the system has exactly one solution.

If at least one column of the coefficient matrix holds no pivot position, then the system has infinitely many solutions.

## Remarks

A column with a pivot position gives a basic variable. A column without one gives a free variable. So the two cases say: no free variable means one solution, and at least one free variable means infinitely many solutions.

Consistency is needed. An inconsistent system has no solution, whatever its pivot columns are.
