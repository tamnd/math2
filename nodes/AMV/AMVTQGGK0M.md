---
tag: AMVTQGGK0M
kind: problem
name: Strongly polynomial algorithm for linear programming
msc: [90C05, 90C60, 68Q25]
uses: [VNMXB0J2KA, GVT2NKN37K, ZY302KCKHR, 8DGAXR9WZR, MH272QHWPM]
about: [VNMXB0J2KA]
sources:
  - url: https://en.wikipedia.org/wiki/Smale's_problems
history:
  posed_by: Stephen Smale
  first_stated: "1998"
---

## Problem

Is there an algorithm that solves every [[linear program|VNMXB0J2KA]] "maximize $c^T x$ subject to $A x \le b$", with $A$ a real $m \times n$ matrix, $b \in \R^m$ and $c \in \R^n$, such that:

1. the number of arithmetic operations (additions, subtractions, multiplications, divisions and comparisons) is bounded by a polynomial in $m$ and $n$ alone, and
2. for rational data, all numbers that occur have bit length bounded by a polynomial in the bit length of the input?

An algorithm with these two properties is called *strongly polynomial*.
In the real-number form of Smale's ninth problem, the question asks for a polynomial-time algorithm over the reals that decides whether $A x \le b$ has a solution.

## Remarks

The problem is open.
The ellipsoid method of [[Khachiyan|ZY302KCKHR]] and interior-point methods such as [[Karmarkar's algorithm|8DGAXR9WZR]] are polynomial.
But their number of operations depends on the bit length $L$ of the data, not only on $m$ and $n$.
The [[simplex algorithm|MH272QHWPM]] would be strongly polynomial if some pivot rule needed only polynomially many pivots, but this is also open.

Known partial results:

1. Éva Tardos gave an algorithm whose number of operations is polynomial in the bit length of $A$ alone, independent of $b$ and $c$. So linear programs with small integer matrices, such as network flow problems, are solvable in strongly polynomial time.
2. Nimrod Megiddo gave an algorithm whose running time is linear in $m$ when the dimension $n$ is fixed.

The problem appears as problem 9 in Smale's list of mathematical problems for the twenty-first century.

## Explanations

### L1 human

Today's fast methods for linear programs take longer when the numbers in the problem have more digits, even if the problem has the same size.
The question is whether there is a method whose number of steps depends only on how many variables and constraints there are.
Such a method is known for many special cases, such as flow problems in networks, but not in general.
