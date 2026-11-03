---
tag: MNN7A5J3K8
kind: definition
name: Special Jordan algebra
msc: [17C50, 17C10]
defines: T4AWF1BRZB
uses: [04C5ZBG1WT, 3CTW1P4HBP, 6C2MCVB8C7, 88EQA06JD9]
sources:
  - url: https://en.wikipedia.org/wiki/Jordan_algebra
    locator: Special Jordan algebras
---

## Definition

Let $F$ be a [[field|04C5ZBG1WT]] of characteristic different from $2$.
For an [[associative algebra|3CTW1P4HBP]] $A$ over $F$, let $A^+$ be the [[Jordan algebra|6C2MCVB8C7]] with the same vector space and the product $x \circ y = \frac{1}{2}(xy + yx)$.
A Jordan algebra $J$ over $F$ is *special* if there is an associative $F$-algebra $A$ with an injective homomorphism of Jordan algebras $\varphi \colon J \to A^+$.
This means that $\varphi$ is linear and injective, and $\varphi(xy) = \varphi(x) \circ \varphi(y)$ for all $x, y \in J$.
A Jordan algebra that is not special is *exceptional*.

## Remarks

The [[Jordan identity|88EQA06JD9]] shows that $A^+$ is a Jordan algebra, and so is every subspace of $A$ closed under $\circ$.
Thus $J$ is special exactly when it is isomorphic to such a subspace.

Example: the real symmetric $n \times n$ matrices $\mathrm{Sym}_n(\R)$ with $X \circ Y = \frac{1}{2}(XY + YX)$.
Here $A = M_n(\R)$ and $\varphi$ is the inclusion; the subspace is closed under $\circ$ because $(XY + YX)^T = YX + XY$ for symmetric $X$ and $Y$.

Non-example: the Albert algebra of $3 \times 3$ Hermitian matrices over the octonions is a Jordan algebra but is not special, as Albert proved.
The definition fails there because no associative algebra $A$ and injective $\varphi$ exist.

Every subalgebra of a special Jordan algebra is special, but a homomorphic image of a special Jordan algebra need not be special.
