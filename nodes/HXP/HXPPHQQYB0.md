---
tag: HXPPHQQYB0
kind: conjecture
name: Kaplansky idempotent conjecture
msc: [16S34, 16U40, 19A31]
uses: [4NMTSX0XDS, PEMNN32A43, 0N5NJZKKN3, 04C5ZBG1WT, DSF8C6QPAG, E1NE8V7EX8, B2X59B7J8V]
about: [4NMTSX0XDS, 0N5NJZKKN3]
sources:
  - url: https://en.wikipedia.org/wiki/Kaplansky%27s_conjectures
    locator: Group rings
history:
  posed_by: "Irving Kaplansky"
---

## Statement

Let $K$ be a [[field|04C5ZBG1WT]] and let $G$ be a [[torsion-free group|PEMNN32A43]].
Then the only [[idempotents|0N5NJZKKN3]] of the [[group ring|4NMTSX0XDS]] $K[G]$ are $0$ and $1$.
That is, if $e \in K[G]$ and $e^2 = e$, then $e = 0$ or $e = 1$.

## Remarks

The conjecture is one of [[Kaplansky's conjectures|DSF8C6QPAG]] on group rings, and it is open in general.
It follows from the [[zero divisor conjecture|E1NE8V7EX8]] for $K[G]$, since an idempotent $e$ satisfies $e(1 - e) = 0$.
Torsion-freeness is needed: if $g \in G$ has finite order $n > 1$ and $n$ is invertible in $K$, then $e = \frac{1}{n}(1 + g + \cdots + g^{n-1})$ is an idempotent other than $0$ and $1$.
For $K = \C$ it is implied by the Kadison–Kaplansky conjecture for the reduced group C*-algebra, which follows from the Baum–Connes conjecture.
If $K$ has characteristic zero, it holds for every torsion-free group $G$ for which the K-theoretic [[Farrell–Jones conjecture|B2X59B7J8V]] holds for $K[G]$; this includes all torsion-free hyperbolic groups.
For $K = \C$, Kaplansky proved that the coefficient of the identity element in an idempotent $e$ is a real number between $0$ and $1$.
He also proved that this coefficient is $0$ only when $e = 0$.

## Explanations

### L1 human

An idempotent is an element that does not change when squared, such as $0$ and $1$.
Other idempotents split a ring into two pieces, as a projection splits a space.
In a group ring, an element of finite order produces such a splitting by averaging over its powers.
The conjecture says that, without elements of finite order, no splitting exists.
