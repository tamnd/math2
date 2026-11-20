---
tag: A3CP855PNV
kind: example
name: An isomorphism from R^2 to its dual given by a basis is not canonical
msc: ["00A35", "15A04"]
topics: [Z2WNQ1DNTX, 9K7FFF26QR]
audience: ug2
not_instance_of:
  - target: F8WNADZFMM
    note: the isomorphism depends on the choice of basis, and two bases give two different isomorphisms
uses: [F8WNADZFMM, 07JBSZE0V4, 0ZD2CF6ZS0, 0KCQ9Y3QKA]
sources:
  - url: https://en.wikipedia.org/wiki/Natural_transformation
    locator: "Example: dual of a finite-dimensional vector space"
  - url: https://en.wikipedia.org/wiki/Dual_space
    locator: Finite-dimensional case
---

## Example

Let $V = \mathbb{R}^2$ with its [[dual space|07JBSZE0V4]] $V^*$.
For a [[basis|0KCQ9Y3QKA]] $B = (b_1, b_2)$ of $V$, let $b_1^*, b_2^*$ be the [[dual basis|0ZD2CF6ZS0]], and let $\Phi_B \colon V \to V^*$ be the linear map with $\Phi_B(b_1) = b_1^*$ and $\Phi_B(b_2) = b_2^*$.
Each $\Phi_B$ is an isomorphism, because it sends a basis to a basis.
We show that $\Phi_B$ changes when $B$ changes, so this isomorphism is not [[canonical|F8WNADZFMM]].

1. Take the standard basis $E$: $e_1 = (1, 0)$ and $e_2 = (0, 1)$. The dual basis is $e_1^*(u, v) = u$ and $e_2^*(u, v) = v$. So $\Phi_E(x, y)$ is the functional $(u, v) \mapsto xu + yv$.
2. Take the basis $B$: $b_1 = (1, 0)$ and $b_2 = (1, 1)$. The dual basis is $b_1^*(u, v) = u - v$ and $b_2^*(u, v) = v$.
3. We check the dual basis: $b_1^*(b_1) = 1 - 0 = 1$, $b_1^*(b_2) = 1 - 1 = 0$, $b_2^*(b_1) = 0$ and $b_2^*(b_2) = 1$.
4. We write a vector in the basis $B$: $(x, y) = (x - y) b_1 + y b_2$. Check: $(x - y)(1, 0) + y(1, 1) = (x, y)$.
5. So $\Phi_B(x, y) = (x - y) b_1^* + y b_2^*$, the functional $(u, v) \mapsto (x - y)(u - v) + yv = (x - y)u + (2y - x)v$.
6. For $(x, y) = (1, 0)$, step 1 gives $\Phi_E(1, 0) \colon (u, v) \mapsto u$, and step 5 gives $\Phi_B(1, 0) \colon (u, v) \mapsto u - v$.
7. At the point $(u, v) = (0, 1)$ these functionals take the values $0$ and $-1$. So $\Phi_E(1, 0) \neq \Phi_B(1, 0)$, and $\Phi_E \neq \Phi_B$.
8. The vector $b_1 = e_1 = (1, 0)$ is the same in both bases, but the two rules send it to different functionals. So the condition "no arbitrary choice" of a canonical map fails.

## Remarks

The example shows that "isomorphic" is weaker than "canonically isomorphic": $V$ and $V^*$ are isomorphic, but no isomorphism between them is preferred.
The map $\Phi_E$ looks choice-free, because it is $x \mapsto (y \mapsto x \cdot y)$ with the dot product.
The dot product is itself a choice: a different inner product gives a different isomorphism.
The dependence is visible already in dimension $1$: on $V = \mathbb{R}$, the basis $\{1\}$ gives $1 \mapsto (u \mapsto u)$, and the basis $\{2\}$ gives $1 \mapsto (u \mapsto u/4)$.
Compare the [[evaluation map to the double dual|J3X26BSQEY]], where every basis gives the same map.

## Explanations

### L1 human

To turn a vector into a rule that eats vectors, we can use coordinates: the vector $(x, y)$ becomes the rule "multiply the first coordinate by $x$, the second by $y$, and add".
But coordinates depend on the choice of axes.
With slanted axes, the same arrow gets different coordinates, and the rule changes.
So this way to turn vectors into rules is not canonical: it depends on a choice that the problem does not make.

### L2 human

We find the vector $w$ with $\Phi_B(w) = \Phi_E(1, 0)$, to see how far apart the two maps are.

1. By step 1, $\Phi_E(1, 0)$ is $(u, v) \mapsto u$.
2. By step 5, $\Phi_B(x, y)$ is $(u, v) \mapsto (x - y)u + (2y - x)v$.
3. We need $x - y = 1$ and $2y - x = 0$. The second equation gives $x = 2y$, and then the first gives $y = 1$ and $x = 2$.
4. So $\Phi_B(2, 1) = \Phi_E(1, 0)$, and the map $\Phi_B^{-1} \circ \Phi_E$ sends $(1, 0)$ to $(2, 1)$, not to itself.

The typical use of this example is a warning: a proof that identifies $V$ with $V^*$ must fix a basis or an inner product and keep it fixed.
A trap: in $\mathbb{R}^n$ with the dot product the identification is so common that it seems canonical, but on an abstract vector space no such choice is given.
