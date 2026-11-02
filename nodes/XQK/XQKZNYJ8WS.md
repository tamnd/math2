---
tag: XQKZNYJ8WS
kind: definition
name: Hochschild homology
msc: ["16E40"]
defines: S5H153HFWC
uses: [3CTW1P4HBP, EM7FHAFD3N, F0HQXQ0HCD, WQ82C0M3QB, DDQRERAQCV, M8Q24XB0AF]
sources:
  - url: https://en.wikipedia.org/wiki/Hochschild_homology
---

## Definition

Let $k$ be a commutative ring and let $A$ be an [[associative algebra|3CTW1P4HBP]] over $k$ with identity.
Let $M$ be an $A$-[[bimodule|EM7FHAFD3N]] on which $k$ acts the same way on both sides.
All [[tensor products|F0HQXQ0HCD]] are over $k$.
The *Hochschild complex* is the [[chain complex|WQ82C0M3QB]] with $C_n(A, M) = M \otimes A^{\otimes n}$ for $n \ge 0$ and boundary $b \colon C_n \to C_{n-1}$ given by
$$b(m \otimes a_1 \otimes \cdots \otimes a_n) = m a_1 \otimes a_2 \otimes \cdots \otimes a_n + \sum_{i=1}^{n-1} (-1)^i m \otimes a_1 \otimes \cdots \otimes a_i a_{i+1} \otimes \cdots \otimes a_n + (-1)^n a_n m \otimes a_1 \otimes \cdots \otimes a_{n-1}.$$
The *Hochschild homology* of $A$ with coefficients in $M$ is $HH_n(A, M) = H_n(C_\bullet(A, M), b)$.
One writes $HH_n(A) = HH_n(A, A)$.

## Remarks

One checks that $b \circ b = 0$, so the homology is defined.
In degree $0$, $b(m \otimes a) = ma - am$, so $HH_0(A, M)$ is the quotient of $M$ by the $k$-submodule spanned by all $ma - am$, and $HH_0(A) = A/[A, A]$.
Example: for $A = M_n(k)$ with $k$ a field, $[A, A]$ is the space of trace-zero matrices, so the [[trace|0XC1RDBY7A]] gives $HH_0(A) \cong k$.
If $A$ is projective as a $k$-module, then $HH_n(A, M) \cong \operatorname{Tor}_n^{A^e}(A, M)$, where $A^e = A \otimes A^{\mathrm{op}}$ uses the [[opposite ring|M8Q24XB0AF]]; see the [[Tor functor|DDQRERAQCV]].
Without such a flatness hypothesis the complex still makes sense, but this description by Tor can fail.
Hochschild cohomology $HH^n(A, M)$ is defined dually from $\Hom_k(A^{\otimes n}, M)$, and it equals $\operatorname{Ext}^n_{A^e}(A, M)$ when $A$ is projective over $k$.
