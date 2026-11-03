---
tag: C2VC3YTG2P
kind: statement
role: theorem
name: Mayer–Vietoris sequence in K-theory
msc: [19B99, 19A49]
uses: [HHWW8R6F2G, Q14JS2MA1C, SXVNJY4XFY, JB7ZBFBA9C]
about: [HHWW8R6F2G, Q14JS2MA1C, SXVNJY4XFY]
sources:
  - url: https://en.wikipedia.org/wiki/Mayer%E2%80%93Vietoris_sequence
---

## Statement

Let
$$\begin{array}{ccc} R & \xrightarrow{\ f_1\ } & R_1 \\ {\scriptstyle f_2}\downarrow & & \downarrow{\scriptstyle g_1} \\ R_2 & \xrightarrow{\ g_2\ } & R' \end{array}$$
be a [[Milnor square|HHWW8R6F2G]] in which $g_2$ is surjective.
Then there is a homomorphism $\partial \colon K_1(R') \to K_0(R)$ such that the sequence
$$K_1(R) \xrightarrow{\alpha} K_1(R_1) \oplus K_1(R_2) \xrightarrow{\beta} K_1(R') \xrightarrow{\partial} K_0(R) \xrightarrow{\alpha} K_0(R_1) \oplus K_0(R_2) \xrightarrow{\beta} K_0(R')$$
is [[exact|JB7ZBFBA9C]], where $\alpha(x) = (f_{1*} x, f_{2*} x)$ and $\beta(y, z) = g_{1*} y - g_{2*} z$, written additively, on the groups [[K0|Q14JS2MA1C]] and [[K1|SXVNJY4XFY]].

## Remarks

The idea of the proof is Milnor's patching construction.
Given finitely generated projective modules $P_1$ over $R_1$ and $P_2$ over $R_2$ and an isomorphism $h \colon R' \otimes P_1 \to R' \otimes P_2$, the set of pairs $(p_1, p_2)$ with $h(1 \otimes p_1) = 1 \otimes p_2$ is a finitely generated projective $R$-module.
The boundary $\partial$ sends the class of a matrix $h \in GL_n(R')$ to $[M(h)] - [R^n]$, where $M(h)$ is the module patched from $R_1^n$ and $R_2^n$ along $h$.
Surjectivity of $g_2$ is used to lift elementary matrices from $R'$ to $R_2$, which makes $\partial$ well defined on $K_1$.
Example: for $R = k[x, y]/(xy)$ with $R_1 = k[x]$, $R_2 = k[y]$ and $R' = k$, all four rings have $K_0 \cong \Z$ and the sequence gives $K_0(R) \cong \Z$, since $K_1(k[x]) \oplus K_1(k[y]) \to K_1(k) = k^\times$ is onto.

## Explanations

### L1 human

When a ring is glued from two simpler rings along a third, its $K$-groups can be computed from those of the pieces.
This is the same idea as the Mayer–Vietoris sequence for a space covered by two pieces.
The connecting map turns an invertible matrix on the overlap into a projective module, by using the matrix to glue two free modules.

### L2 human

The sequence is the main tool for computing $K_0$ of non-normal rings and of group rings such as $\Z[C_p]$, which sit in Milnor squares with simpler rings.
It continues to the left with negative K-groups, which is one way to motivate them.
It does not continue to the right in general, since excision fails for $K_1$.
For the square built from an ideal $I$ common to $R \subseteq S$, it is closely related to excision for $K_0$.
