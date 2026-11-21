---
tag: DXSXFVDMXQ
kind: topic
name: Systems of linear equations and row reduction
msc: ["15A06"]
topics: [GN8GYSDZFX]
---

## Summary

This topic is a part of [[linear algebra|GN8GYSDZFX]], and it answers one question completely: given some linear equations, what are all their solutions?
It starts with a single linear equation and with small systems, such as two lines in the plane, which meet in a point, run parallel, or coincide.
Those three outcomes, no solution, one, or infinitely many, turn out to be the only ones for every linear system over the real numbers.

To handle systems of any size, we drop the names of the unknowns and keep only the table of numbers, the augmented matrix.
Three simple row operations change the table without changing the solutions, and Gaussian elimination uses them to reach a staircase shape, the echelon form.
From the staircase we solve by back substitution, or we keep cleaning until the reduced form, which is unique and shows the answer directly.

The corners of the staircase, the pivots, carry the whole story.
A pivot in the last column means no solution, a pivot in every other column means exactly one, and each column without a pivot gives a free parameter.
The general solution is one particular solution plus all solutions of the homogeneous system, and the Rouché-Capelli theorem says the same in the language of rank.
The topic ends with systems that have too many or too few equations, which lead to least squares, and with systems over finite fields, where the solutions can be counted exactly.

## Remarks

### Reading order

1. [[Linear equation|0Q3ZT8J05R]]: what one equation in $n$ unknowns looks like, and why its solutions form a line, a plane or a flat.
2. [[System of linear equations|0GT4WWGWH2]]: how to read a system by rows, by columns and as $Ax = b$.
3. [[Consistent and inconsistent systems|0X6V9B1V10]]: how to tell, by one row of an echelon form, whether any solution exists.
4. [[Homogeneous system|04KGXJG1A2]]: why $Ax = 0$ always has a solution, and when it has more than the zero vector.
5. [[Coefficient matrix|0P7A2MJD24]]: how the matrix of coefficients turns the system into one product $Ax$.
6. [[Augmented matrix|0YCDZ7N8VD]]: how to store a whole system, or several right sides at once, in one table.
7. [[Elementary row operations|04XWH28452]]: the three moves that may be made on the table, and why each can be undone.
8. [[Row equivalence|006BHFWMAP]]: why tables linked by row operations describe the same solutions.
9. [[Row echelon form|0VYCDGMJJJ]]: the staircase shape that elimination aims at, and how to recognize it.
10. [[Reduced row echelon form|0WF5AQYTW6]]: the fully cleaned staircase, from which the solutions can be read off.
11. [[Uniqueness of the reduced row echelon form|BF9SMZMJZE]]: the proof that every way of reducing ends at the same table.
12. [[Pivots, basic variables and free variables|0J0BBCMJ5W]]: which unknowns the equations fix and which we may choose.
13. [[Gaussian elimination|0JVJ2WCXZH]]: the step-by-step method that brings any table to echelon form, and what it costs.
14. [[Back substitution|0ATFVE08MW]]: how to finish a triangular system from the bottom up.
15. [[Gauss-Jordan elimination|098D6FQN3N]]: how to reach the reduced form directly, and how the same steps invert a matrix.
16. [[Linear systems as vector equations|E7SAHXQEVC]]: the column view, in which solving means writing $b$ as a combination of columns.
17. [[Existence and uniqueness of solutions|BKA191KD1S]]: the pivot test that sorts every system into none, one or many solutions.
18. [[Parametric form of the solution set|KQT68YPHD1]]: how to write infinitely many solutions with one point and a few directions.
19. [[Structure of the solution set|PDH3HKXWAZ]]: why all solutions are one solution plus the solutions of $Ax = 0$.
20. [[Rouché-Capelli theorem|0HV1SKWPMS]]: the same answers stated with ranks, useful for systems with parameters.
21. [[Overdetermined and underdetermined systems|QJ0P26J9BV]]: what to expect from the counts of equations and unknowns, and where least squares enters.
22. [[Linear systems over finite fields|J6A58MEM8R]]: elimination modulo a prime, the exact count of [[solutions over a finite field|8QM2Y41P69]], and the Lights Out puzzle.

### Prerequisites

- [[Vectors in the plane and in space|VKVAJ94SKZ]]: vectors, lines and planes in coordinates.
- [[Elementary algebra and functions|DPW5ETDQ27]]: systems of two and three equations solved by substitution.
