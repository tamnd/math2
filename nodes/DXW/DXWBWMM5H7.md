---
tag: DXWBWMM5H7
kind: definition
name: Pixley term
msc: [08B05, 08B10]
defines: 5C91SFVTY7
uses: [AJNZJD8442, PKD440G2XW, Y203PPTS61, 9879ZMW5AA, GW78A05TNA]
sources:
  - url: https://en.wikipedia.org/wiki/Congruence-permutable_algebra
---

## Definition

Let $\mathcal{V}$ be a [[variety|AJNZJD8442]] of algebras.
A *Pixley term* for $\mathcal{V}$ is a ternary term $p(x, y, z)$ such that $\mathcal{V}$ satisfies the [[identities|PKD440G2XW]]
$$p(x, y, y) = x, \qquad p(x, x, y) = y, \qquad p(x, y, x) = x.$$

## Remarks

The first two identities say that $p$ is a [[Mal'cev term|Y203PPTS61]].
The term $m(x, y, z) = p(x, p(x, y, z), z)$ is then a [[majority term|9879ZMW5AA]]: $m(x, x, z) = p(x, z, z) = x$, $m(x, y, x) = p(x, x, x) = x$ and $m(x, z, z) = p(x, x, z) = z$.
Pixley's theorem says that $\mathcal{V}$ has a Pixley term if and only if $\mathcal{V}$ is an [[arithmetical variety|GW78A05TNA]].
Example: for Boolean algebras, $p(x, y, z) = (x \wedge \neg y) \vee (x \wedge z) \vee (\neg y \wedge z)$ is a Pixley term.
Indeed $p(x, y, y) = (x \wedge \neg y) \vee (x \wedge y) \vee 0 = x$, $p(x, x, y) = 0 \vee (x \wedge y) \vee (\neg x \wedge y) = y$, and $p(x, y, x) = (x \wedge \neg y) \vee x \vee (\neg y \wedge x) = x$.
Non-example: for groups, the Mal'cev term $x y^{-1} z$ is not a Pixley term.
In the group $\Z$, the third identity would read $x - y + x = x$, which fails for $x \ne y$.

## Explanations

### L1 human

A Pixley term is a three-input formula that returns $x$ on the inputs $x, y, y$ and $x, y, x$, and returns $y$ on the inputs $x, x, y$.
