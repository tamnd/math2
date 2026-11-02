---
tag: ZQFPVWMY4M
kind: statement
role: theorem
name: Skolem–Mahler–Lech theorem
msc: [11B37, 39A06]
uses: [081THG13JZ, 0ZV2YKKZ58, S70JBRSQZX]
about: [06MJC8YDYR]
sources:
  - url: https://en.wikipedia.org/wiki/Skolem%E2%80%93Mahler%E2%80%93Lech_theorem
same_as:
  wikidata: Q2374733
  wikipedia: Skolem–Mahler–Lech theorem
---

## Statement

Let $K$ be a field of characteristic $0$.
Let $(u_n)_{n \ge 0}$ be a [[solution|0ZV2YKKZ58]] of a [[linear recurrence with constant coefficients|081THG13JZ]] over $K$.
Then the zero set $Z = \set{n \in \N : u_n = 0}$ is the union of a finite set and finitely many [[arithmetic progressions|S70JBRSQZX]] $\set{a + b m : m \in \N}$ with $a \in \N$ and $b \ge 1$.

## Remarks

The standard proof is $p$-adic.
One reduces to a finitely generated subfield, which embeds into the $p$-adic numbers $\Q_p$ for a suitable prime $p$ with all relevant quantities $p$-adic units.
Then for a suitable period $b$ and each residue $a$, the map $m \mapsto u_{a + b m}$ extends to a $p$-adic analytic function on $\Z_p$.
Such a function either vanishes identically or has only finitely many zeros, which gives the progressions and the finite set.
Example: $u_n = 1 + (-1)^n$ solves $u_{n+2} = u_n$, and its zero set is the progression of odd numbers.
The hypothesis of characteristic $0$ is necessary.
Over the field $\F_p(t)$, the sequence $u_n = (1 + t)^n - t^n - 1$ solves a linear recurrence of order $3$.
Its terms vanish exactly when $n$ is a power of $p$, and this infinite set contains no infinite arithmetic progression.
The proof is not effective: it gives no algorithm to find the finite set.
Whether one can decide if a given integer recurrence has a zero at all is the open Skolem problem.

## Explanations

### L1 human

Take a sequence defined by a linear recurrence with fixed coefficients, and ask where it is zero.
The theorem says the answer is never wild: apart from finitely many exceptions, the zeros repeat with a fixed period.
For instance, it can be zero at every third index, but it cannot be zero exactly at the perfect squares.

### L2 human

The theorem is named after Thoralf Skolem, Kurt Mahler and Christer Lech, who proved it in more and more general fields.
The periodic part can be computed, but the finite exceptional set is the hard part.
The proof is a classic use of $p$-adic analysis in number theory, by the same principle as Strassmann's theorem on the zeros of $p$-adic power series.
A recurrence is non-degenerate if no ratio of two distinct roots of its characteristic polynomial is a root of unity.
A common corollary: a non-degenerate solution that is not identically zero has only finitely many zeros.
