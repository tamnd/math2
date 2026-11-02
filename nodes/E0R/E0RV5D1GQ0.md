---
tag: E0RV5D1GQ0
kind: statement
role: theorem
name: Long exact sequence of homotopy groups
msc: [55Q05, 55R05]
uses: [PB9JXQ2KC3, P976WYEFMB, ZHHMDZWA7F, JB7ZBFBA9C, 0WB6DH499T]
about: [P976WYEFMB, PB9JXQ2KC3]
sources:
  - url: https://en.wikipedia.org/wiki/Fibration
---

## Statement

Let $p \colon E \to B$ be a [[Serre fibration|PB9JXQ2KC3]], and let $B$ be [[path-connected|0WB6DH499T]].
Let $b_0 \in B$, let $F = p^{-1}(b_0)$ be the fibre, and let $x_0 \in F$.
Then there is an [[exact sequence|JB7ZBFBA9C]]
$$\cdots \to \pi_n(F, x_0) \xrightarrow{i_*} \pi_n(E, x_0) \xrightarrow{p_*} \pi_n(B, b_0) \xrightarrow{\partial} \pi_{n-1}(F, x_0) \to \cdots \to \pi_0(F, x_0) \to \pi_0(E, x_0) \to 0.$$
Here $\pi_n$ are the [[homotopy groups|P976WYEFMB]], $i \colon F \to E$ is the inclusion, and $\partial$ is a homomorphism for $n \ge 2$.
At the terms $\pi_0$ and at $\pi_1(B, b_0)$, exactness is meant as pointed sets: the kernel of a map is the preimage of the base point.

## Remarks

The key step is that $p_* \colon \pi_n(E, F, x_0) \to \pi_n(B, b_0)$ is an isomorphism for $n \ge 1$, proved by lifting maps of disks with the homotopy lifting property.
The sequence then comes from the long exact sequence of the pair $(E, F)$ in [[relative homotopy groups|ZHHMDZWA7F]].
The map $\partial$ lifts a based map of a disk into $B$ to $E$ and restricts it to the boundary sphere, which lands in $F$.
For the Hopf fibration $S^1 \to S^3 \to S^2$, the sequence gives $\pi_2(S^2) \cong \pi_1(S^1) \cong \Z$ and $\pi_n(S^3) \cong \pi_n(S^2)$ for $n \ge 3$.
For the covering $\R \to S^1$ the fibre $\Z$ is discrete, so $\pi_n(S^1) \cong \pi_n(\R) = 0$ for $n \ge 2$.

## Explanations

### L1 human

A fibration is a space $E$ built over a base $B$ with copies of a fibre $F$ over each point.
The sequence says that the homotopy groups of the three spaces are tied together tightly.
If two of them are known, the third is often determined.

### L2 human

This is the most used tool for computing homotopy groups.
It gives $\pi_3(S^2) \cong \Z$ from the Hopf fibration, and computes homotopy groups of Lie groups and homogeneous spaces from fibrations such as $SO(n) \to SO(n+1) \to S^n$.
For the path space fibration $\Omega B \to PB \to B$ with contractible total space, it gives $\pi_n(\Omega B) \cong \pi_{n+1}(B)$.
The analogous sequence of a pair $A \subseteq X$ has the form $\cdots \to \pi_n(A) \to \pi_n(X) \to \pi_n(X, A) \to \pi_{n-1}(A) \to \cdots$.
