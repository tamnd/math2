---
tag: P15K8RKHDV
kind: statement
role: theorem
name: Harnack's principle
msc: [31B05, 31A05]
uses: [0W5NJQ8MKY, YNH832D50W, 093CM69AGS]
about: [0DEB0JMN0W]
sources:
  - url: https://en.wikipedia.org/wiki/Harnack%27s_principle
same_as:
  wikidata: Q1135706
  wikipedia: Harnack's principle
---

## Statement

Let $D \subseteq \R^n$ be a [[domain|093CM69AGS]], that is, a connected open set.
Let $(u_k)$ be a sequence of [[harmonic functions|0W5NJQ8MKY]] on $D$ with $u_1 \le u_2 \le u_3 \le \cdots$ at each point of $D$.
Then one of the following holds.

1. $u_k \to \infty$ uniformly on each compact subset of $D$.
2. $(u_k)$ converges uniformly on each compact subset of $D$ to a harmonic function $u$ on $D$.

## Remarks

Proof idea: the functions $u_k - u_1$ are nonnegative and harmonic.
[[Harnack's inequality|YNH832D50W]] compares the values of a nonnegative harmonic function at two points of a compact set by constants that do not depend on the function.
So the increasing limit is either infinite everywhere or finite everywhere, and in the finite case the convergence is uniform on compact sets.
A uniform limit of harmonic functions is harmonic, by the mean value property.
Connectedness is needed: on two disjoint discs, take $u_k = 0$ on one disc and $u_k = k$ on the other.

## Explanations

### L1 human

An increasing sequence of harmonic functions can do only two things.
Either it goes to infinity everywhere at once, or it converges nicely everywhere to a harmonic function.
It cannot converge at one point and blow up at another.

### L2 human

The principle is the harmonic analogue of the monotone convergence theorem, and it follows from Harnack's inequality.
It is used in Perron's method for the Dirichlet problem, where the solution is built as a limit of subharmonic functions.
It also appears in the construction of Green's functions and harmonic measures by exhaustion of a domain.
