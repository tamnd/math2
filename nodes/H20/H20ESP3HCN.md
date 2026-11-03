---
tag: H20ESP3HCN
kind: problem
name: Skolem problem
msc: [11B37, 39A06, 03D35]
uses: [081THG13JZ, 0ZV2YKKZ58, ZQFPVWMY4M]
about: [06MJC8YDYR]
sources:
  - url: https://en.wikipedia.org/wiki/Skolem_problem
same_as:
  wikidata: Q25304237
  wikipedia: Skolem problem
history:
  posed_by: "Thoralf Skolem"
  first_stated: "1933"
  notes: "The problem is named after Skolem's paper proving that the zeros of a rational linear recurrence form an eventually periodic set, dated 1933 by some authors and 1934 by others. The attribution is to this earliest known source rather than to an explicit statement of the decision problem."
---

## Problem

Let $k \ge 1$ and let $a_1, \ldots, a_k$ and $u_0, \ldots, u_{k-1}$ be integers.
Let $(u_n)_{n \ge 0}$ be the integer sequence given by the [[linear recurrence with constant coefficients|081THG13JZ]]
$$u_{n+k} = a_1 u_{n+k-1} + a_2 u_{n+k-2} + \cdots + a_k u_n \quad (n \ge 0).$$
Is there an algorithm that, given $a_1, \ldots, a_k$ and $u_0, \ldots, u_{k-1}$, decides whether $u_n = 0$ for some $n \ge 0$?

## Remarks

The problem is open in general.
By the [[Skolem–Mahler–Lech theorem|ZQFPVWMY4M]], the zero set of such a [[sequence|0ZV2YKKZ58]] is a finite set together with finitely many arithmetic progressions.
The arithmetic progressions can be computed, so the difficulty lies in the finite exceptional set, for which the known proofs give no bound.
The problem is known to be decidable for recurrences of order $k \le 4$.
The question whether $u_n = 0$ holds for infinitely many $n$ is decidable, since this happens exactly when the zero set contains an arithmetic progression.
Example: $u_{n+2} = u_{n+1} - u_n$ with $u_0 = 1$ and $u_1 = 2$ gives $1, 2, 1, -1, -2, -1, 1, \ldots$, which has period $6$ and never vanishes.

## Explanations

### L1 human

A linear recurrence builds a sequence of integers where each new term is a fixed combination of the previous few, like the Fibonacci numbers.
The Skolem problem asks for a procedure that always tells, in finite time, whether the sequence ever hits $0$.
Computing terms one by one finds a zero when there is one, but it never tells you to stop when there is none.
Despite the simple question, no such procedure is known, and it is also not known that none exists.
