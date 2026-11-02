---
tag: KP27TDCZPJ
kind: statement
role: theorem
name: Nonexistence of a projective plane of order 10
msc: ["51E15", "05B25", "94B05"]
uses: [DANFNN8C4Y, K2YVMTGTBB, R43K0GTTDS, H6TN6BADVY]
about: [DANFNN8C4Y, K2YVMTGTBB]
sources:
  - url: https://en.wikipedia.org/wiki/Lam%27s_problem
same_as:
  wikidata: Q106696246
  wikipedia: Lam's problem
---

## Statement

There is no [[projective plane|DANFNN8C4Y]] of [[order|K2YVMTGTBB]] $10$.

## Remarks

The [[Bruck–Ryser–Chowla theorem|R43K0GTTDS]] does not exclude order $10$: since $10 \equiv 2 \pmod 4$, it requires $10$ to be a sum of two squares, and $10 = 1^2 + 3^2$.
The proof uses coding theory.
The incidence vectors of the lines of a putative plane of order $10$ span a binary linear code of length $111$.
Its weight enumerator is determined by the numbers of codewords of a few small weights.
A series of large computer searches showed that these numbers lead to a contradiction.
The final search was completed by Clement Lam, Larry Thiel and Stanley Swiercz, and announced in 1989.

As a consequence, there is no set of $9$ [[mutually orthogonal Latin squares|H6TN6BADVY]] of order $10$, since such a set would give a plane of order $10$.
The proof depends on computer calculations, which have since been checked independently by other computations.

## Explanations

### L1 human

A projective plane of order $10$ would have $111$ points and $111$ lines, with $11$ points on each line.
The obvious necessary conditions do not rule it out.
It took years of reasoning and computer search to show that no such plane exists.

### L2 human

Order $10$ is the smallest order that is not a prime power and is not excluded by the Bruck–Ryser–Chowla theorem.
Orders $2, 3, 4, 5, 7, 8, 9$ are prime powers and have planes, and order $6$ is excluded by Bruck–Ryser–Chowla.
The next open case is order $12$.
The result is a famous early example of a theorem whose proof rests on a massive computation.
