---
tag: VFPP3RZGK3
kind: definition
name: Bockstein homomorphism
msc: [55S05, 55N10]
defines: H7PCM776GR
uses: [CBDM280TDF, 071DDFVG4J, 6N7BC70CX0, XT7VWNTKGB]
sources:
  - url: https://en.wikipedia.org/wiki/Bockstein_homomorphism
---

## Definition

Let $X$ be a topological space and let
$$0 \to A \xrightarrow{i} B \xrightarrow{j} C \to 0$$
be a short [[exact sequence|CBDM280TDF]] of [[abelian groups|071DDFVG4J]].
Let $C^*(X; G) = \Hom(C_*(X), G)$ be the singular cochain complex with coefficients in $G$.
Since each group $C_n(X)$ of singular chains is free abelian, the induced sequence of cochain complexes
$$0 \to C^*(X; A) \to C^*(X; B) \to C^*(X; C) \to 0$$
is exact.
The *Bockstein homomorphism* is its connecting homomorphism
$$\beta \colon H^n(X; C) \to H^{n+1}(X; A)$$
in [[singular cohomology|6N7BC70CX0]].
Explicitly, let $c$ be a cocycle representing a class in $H^n(X; C)$, and choose a cochain $b$ with values in $B$ with $j \circ b = c$.
Then $\delta b = i \circ a$ for a unique cocycle $a$, and $\beta[c] = [a]$.

## Remarks

The same construction on chains gives a homology Bockstein $H_n(X; C) \to H_{n-1}(X; A)$ in [[homology with coefficients|XT7VWNTKGB]].
The most used case is $0 \to \Z/p \to \Z/p^2 \to \Z/p \to 0$, which gives a natural map $\beta \colon H^n(X; \F_p) \to H^{n+1}(X; \F_p)$ with $\beta \circ \beta = 0$.

Example: let $X = \R P^2$ and $p = 2$, so $H^1(X; \Z/2) \cong H^2(X; \Z/2) \cong \Z/2$, while $H^1(X; \Z/4) \cong \Z/2$ and $H^2(X; \Z/4) \cong \Z/2$.
The map $H^1(X; \Z/4) \to H^1(X; \Z/2)$ is zero, since the class of order two in $H^1(X; \Z/4)$ reduces to zero mod $2$.
So by exactness the generator of $H^1(X; \Z/2)$ has nonzero Bockstein, which is the generator of $H^2(X; \Z/2)$.

Non-example of a nonzero Bockstein: for the split sequence $0 \to \Z/2 \to \Z/2 \oplus \Z/2 \to \Z/2 \to 0$, every class lifts, and the Bockstein is the zero map.
In general $\beta = 0$ whenever the coefficient sequence splits.

For $p = 2$ the Bockstein on mod $2$ cohomology equals the Steenrod square $Sq^1$.
For the sequence $0 \to \Z \xrightarrow{p} \Z \to \Z/p \to 0$ one gets the integral Bockstein $H^n(X; \Z/p) \to H^{n+1}(X; \Z)$, whose image consists of $p$-torsion classes.
