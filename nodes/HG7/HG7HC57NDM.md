---
tag: HG7HC57NDM
kind: definition
name: Nakayama algebra
msc: [16G20, 16G60]
defines: APRFMTZ10K
uses: [3CTW1P4HBP, BFFA03GE3V, E2P29GCD9T, Z1045A0V29, 0XV2A49X6Q]
sources:
  - url: https://en.wikipedia.org/wiki/Nakayama_algebra
---

## Definition

Let $K$ be a field and let $A$ be a finite-dimensional [[associative algebra|3CTW1P4HBP]] over $K$.
A module is *uniserial* if it has a unique [[composition series|0XV2A49X6Q]], equivalently if its submodules are totally ordered by inclusion.
The algebra $A$ is a *Nakayama algebra* if every [[indecomposable|E2P29GCD9T]] [[projective|BFFA03GE3V]] left $A$-module and every indecomposable projective right $A$-module is [[uniserial|Z1045A0V29]].

## Remarks

Example: $A = K[x]/(x^n)$ with $n \ge 1$.
The only indecomposable projective module on either side is $A$ itself, and its submodules are the ideals $(x^i)$ for $0 \le i \le n$, which form a chain.
Example: the algebra of upper triangular $n \times n$ matrices over $K$ is a Nakayama algebra; its indecomposable projective left modules are its columns.
Non-example: $A = K[x, y]/(x, y)^2$, with basis $1, x, y$.
The module $A$ is indecomposable and projective, but $Kx$ and $Ky$ are submodules neither of which contains the other, so $A$ is not uniserial.
Over a Nakayama algebra every indecomposable module is uniserial and is a quotient of an indecomposable projective module.
In the language of rings, a Nakayama algebra is a finite-dimensional algebra that is a [[serial ring|TW3ESQB3GQ]] on both sides.
