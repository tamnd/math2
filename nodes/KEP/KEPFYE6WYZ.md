---
tag: KEPFYE6WYZ
kind: statement
role: theorem
name: Freiman's theorem
msc: [11P70, 11B13, 11B30]
uses: [XNBN31HQWB]
about: [XNBN31HQWB]
sources:
  - url: https://en.wikipedia.org/wiki/Freiman%27s_theorem
same_as:
  wikidata: Q3527079
  wikipedia: Freiman's theorem
---

## Statement

A generalized arithmetic progression of dimension $d$ in $\Z$ is a set
$$P = \set{a + x_1 q_1 + \dots + x_d q_d : x_i \in \Z, \ 0 \le x_i < L_i \text{ for } 1 \le i \le d},$$
where $a, q_1, \dots, q_d$ are integers and $L_1, \dots, L_d$ are positive integers.
Let $K \ge 1$ be a real number.
Then there are numbers $d(K)$ and $f(K)$, depending only on $K$, with the following property.
Every finite set $A \subseteq \Z$ with $\abs{A + A} \le K \abs{A}$ is contained in a generalized arithmetic progression $P$ of dimension at most $d(K)$ with $\abs{P} \le f(K) \abs{A}$.

## Remarks

Here $A + A$ is the [[sumset|XNBN31HQWB]] of $A$ with itself.
Ruzsa's proof has four steps.
First, the [[Plünnecke–Ruzsa inequality|EBEVWSRD2E]] bounds $\abs{2A - 2A}$.
Second, a large part of $A$ is modelled by a set in a cyclic group $\Z/N\Z$ with $N$ not much larger than $\abs{A}$.
Third, Bogolyubov's lemma finds a large Bohr set inside the set $2A' - 2A'$ of the model $A'$.
Fourth, geometry of numbers finds a progression inside the Bohr set, and a covering argument finishes.
A converse holds: if $A$ is a large subset of a proper progression $P$ of dimension $d$, then $\abs{A + A} \le \abs{P + P} \le 2^d \abs{P}$, so $A$ has small doubling.
Green and Ruzsa extended the theorem to all abelian groups, with coset progressions in place of progressions.

## Explanations

### L1 human

Some sets of numbers have very few different pairwise sums compared with their size.
Arithmetic progressions like $3, 7, 11, 15, \dots$ are the main example.
Freiman's theorem says that every such set is a large piece of a "multi-dimensional" arithmetic progression.
So few sums means a lot of hidden regular structure.

### L2 human

Freiman's theorem is the central inverse theorem of [[additive combinatorics|3NM362A2JG]].
Good bounds on $d(K)$ and $f(K)$ matter in applications, and finding the right ones is related to the polynomial Freiman–Ruzsa conjecture.
It is used in Gowers' proof of [[Szemerédi's theorem|B23B0QEMN5]], together with the [[Balog–Szemerédi–Gowers theorem|W5BZZ59CVM]].
