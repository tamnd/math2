---
tag: G4SZMHM8AA
kind: definition
name: Tangent space
msc: [58A05, 53A05]
defines: QMM8X5Y930
uses: [F45VQ47GPV, 0V33BNKZ9S, 000AYPA9AJ, 3J89REV9WQ]
sources:
  - url: https://en.wikipedia.org/wiki/Tangent_space
---

## Definition

Let $M$ be a [[smooth manifold|F45VQ47GPV]] of dimension $n$, and let $p \in M$.
Let $C^\infty(M)$ be the real algebra of [[smooth functions|0V33BNKZ9S]] $M \to \R$.
A *tangent vector* to $M$ at $p$ is a map $v \colon C^\infty(M) \to \R$ such that:

1. $v$ is $\R$-linear.
2. $v(fg) = f(p)\, v(g) + g(p)\, v(f)$ for all $f, g \in C^\infty(M)$.

Such a map is called a derivation at $p$.
It is a [[derivation|3J89REV9WQ]] of $C^\infty(M)$ with values in $\R$, where $f$ acts on $\R$ by multiplication with $f(p)$.
The *tangent space* of $M$ at $p$ is the set $T_pM$ of all tangent vectors at $p$.
With pointwise addition and scalar multiplication, it is a real [[vector space|000AYPA9AJ]].

## Remarks

If $(U, (x^1, \ldots, x^n))$ is a chart around $p$, the maps $\left.\frac{\partial}{\partial x^i}\right|_p$, which send $f$ to the partial derivative of $f$ in the chart at $p$, form a basis of $T_pM$.
Hence $\dim T_pM = n$.

Example: for $M = \R^n$ and $a \in \R^n$, each vector $w \in \R^n$ gives the directional derivative $v_w(f) = \sum_i w_i \frac{\partial f}{\partial x_i}(a)$.
It is linear, and the product rule gives $v_w(fg) = f(a)\, v_w(g) + g(a)\, v_w(f)$, so $v_w$ is a tangent vector at $a$.
The map $w \mapsto v_w$ is an isomorphism $\R^n \to T_a\R^n$.

Non-example: on $\R$ at $a = 0$, the map $v(f) = f(0)$ is linear but not a tangent vector.
For $f = g = 1$ it gives $v(fg) = 1$, while $f(0)\, v(g) + g(0)\, v(f) = 2$.

Equivalent forms: $T_pM$ can also be defined with smooth curves $\gamma$ such that $\gamma(0) = p$.
Two such curves are equivalent when they have the same velocity in a chart, and $T_pM$ is the set of classes.
Another form uses derivations of germs of smooth functions at $p$, or the dual of $\mathfrak{m}_p / \mathfrak{m}_p^2$, where $\mathfrak{m}_p$ is the ideal of germs vanishing at $p$.
For a smooth manifold all these give canonically isomorphic spaces.
For a submanifold $M$ of $\R^N$, $T_pM$ is identified with the linear subspace of velocities $\gamma'(0)$ of smooth curves $\gamma$ in $M$ with $\gamma(0) = p$.
