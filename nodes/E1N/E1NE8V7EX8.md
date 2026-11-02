---
tag: E1NE8V7EX8
kind: conjecture
name: Kaplansky's zero divisor conjecture
msc: [16S34, 16U10]
uses: [4NMTSX0XDS, PEMNN32A43, 0NNRDW10RZ, 0Q4CBD3HX0]
about: [4NMTSX0XDS]
sources:
  - url: https://en.wikipedia.org/wiki/Kaplansky%27s_conjectures
    locator: Group rings
history:
  posed_by: "Irving Kaplansky"
---

## Statement

Let $K$ be a field and let $G$ be a [[torsion-free group|PEMNN32A43]].
Then the [[group ring|4NMTSX0XDS]] $K[G]$ has no [[zero divisors|0NNRDW10RZ]] other than $0$: if $a, b \in K[G]$ and $ab = 0$, then $a = 0$ or $b = 0$.
In other words, $K[G]$ is a [[domain|0Q4CBD3HX0]].

## Remarks

The conjecture is open.
Torsion-freeness is necessary: if $g \in G$ has finite order $n > 1$, then $(1 - g)(1 + g + \cdots + g^{n-1}) = 1 - g^n = 0$ with both factors nonzero.
It holds when $G$ has the unique product property: for nonempty finite sets $A, B \subseteq G$, some product $ab$ with $a \in A$, $b \in B$ arises in only one way.
For such $G$, take $A$ and $B$ to be the supports of $a$ and $b$.
The coefficient of that unique product in $ab$ is a product of two nonzero field elements, so $ab \ne 0$.
Left-orderable groups, and in particular torsion-free abelian groups and free groups, have this property.
For $G = \Z$, the group ring $K[\Z]$ is the Laurent polynomial ring $K[x, x^{-1}]$, which is a domain.
The conjecture is also known for torsion-free elementary amenable groups, whose group rings are Ore domains.
In characteristic zero it follows from the strong Atiyah conjecture for $G$.

## Explanations

### L1 human

In the ring of polynomials, a product of two nonzero polynomials is never zero, because the top degree terms multiply to a nonzero term.
The conjecture says the same happens for any group without elements of finite order.
For groups that can be ordered there is a "top term" and the polynomial argument works.
For general torsion-free groups no such argument is known.
