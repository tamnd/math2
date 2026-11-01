---
tag: 429JJ5ZNBY
kind: example
name: Baumslag–Solitar group
msc: ["20F05", "20E06"]
instance_of: [68AFPHR4GN, YEYERRY37K]
sources:
  - url: https://en.wikipedia.org/wiki/Baumslag%E2%80%93Solitar_group
same_as:
  wikidata: Q4150685
  wikipedia: Baumslag–Solitar group
---

## Example

Let $m$ and $n$ be nonzero integers.
The *Baumslag–Solitar group* $BS(m, n)$ is the group with the [[presentation|0JGEQXQ4AC]]
$$BS(m, n) = \langle a, b \mid b a^m b^{-1} = a^n \rangle.$$
It is a [[one-relator group|68AFPHR4GN]], since the presentation has the single relator $b a^m b^{-1} a^{-n}$.
It is also the [[HNN extension|YEYERRY37K]] of the infinite cyclic group $\langle a \rangle$ that conjugates $\langle a^m \rangle$ onto $\langle a^n \rangle$ by $a^m \mapsto a^n$, with stable letter $b$.

## Remarks

Small cases: $BS(1, 1) \cong \Z^2$, and $BS(1, -1)$ is the fundamental group of the Klein bottle.
The group $BS(1, n)$ is isomorphic to the semidirect product $\Z[1/n] \rtimes \Z$, where the generator of $\Z$ acts by multiplication by $n$.
The isomorphism sends $a$ to $1 \in \Z[1/n]$ and $b$ to the generator of $\Z$.
In particular $BS(1, n)$ is solvable.

$BS(m, n)$ is [[residually finite|HEE922EHQ8]] if and only if $\abs{m} = 1$, $\abs{n} = 1$ or $\abs{m} = \abs{n}$.

$BS(2, 3) = \langle a, b \mid b a^2 b^{-1} = a^3 \rangle$ is not [[Hopfian|PHEN4E1JPT]].
Let $\varphi$ be the endomorphism with $\varphi(a) = a^2$ and $\varphi(b) = b$.
It is well defined, since $\varphi(b a^2 b^{-1}) = b a^4 b^{-1} = (b a^2 b^{-1})^2 = a^6 = \varphi(a^3)$.
It is surjective, since $a = a^3 a^{-2} = b a^2 b^{-1} a^{-2} = \varphi(b a b^{-1} a^{-1})$.
It is not injective: the element $[b a b^{-1}, a]$ is not $1$ by Britton's lemma, but $\varphi$ sends it to $[b a^2 b^{-1}, a^2] = [a^3, a^2] = 1$.

## Explanations

### L1 human

A Baumslag–Solitar group has two generators and one rule: conjugating $a^m$ by $b$ gives $a^n$.
For $m = n = 1$ the rule says that $a$ and $b$ commute, and the group is $\Z^2$.
For $m = 1$ and $n = 2$, think of $a$ as the shift $x \mapsto x + 1$ and $b$ as the doubling $x \mapsto 2x$ of the real line.
Then $b a b^{-1}$ is $x \mapsto x + 2$, which is $a^2$.
Other values of $m$ and $n$ give groups with surprising properties, and they serve as standard test cases in group theory.
