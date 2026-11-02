---
tag: E7QDFXK2E1
kind: definition
name: Projective tensor product
msc: [46B28, 46M05]
defines: 685ZV73JJ8
uses: [06GZ956657, 0BF2DE2SYK]
sources:
  - url: https://en.wikipedia.org/wiki/Projective_tensor_product
---

## Definition

Let $X$ and $Y$ be [[Banach spaces|06GZ956657]] over $\mathbb{K} = \R$ or $\C$, and let $X \otimes Y$ be their algebraic [[tensor product|0BF2DE2SYK]].
For $u \in X \otimes Y$, let
$$\pi(u) = \inf \Big\{ \sum_{i=1}^n \norm{x_i} \, \norm{y_i} : u = \sum_{i=1}^n x_i \otimes y_i \Big\}.$$
The infimum runs over all finite representations of $u$.
Then $\pi$ is a norm on $X \otimes Y$, the *projective norm*.
The *projective tensor product* $X \widehat{\otimes}_\pi Y$ is the completion of $X \otimes Y$ for $\pi$.

## Remarks

The norm is a cross norm: $\pi(x \otimes y) = \norm{x} \, \norm{y}$.
The bound $\le$ comes from the representation with one term.
For $\ge$, take functionals $f \in X^*$ and $g \in Y^*$ of norm $1$ with $f(x) = \norm{x}$ and $g(y) = \norm{y}$, given by the Hahn–Banach theorem.
For any representation, $\norm{x} \, \norm{y} = \abs{\sum_i f(x_i) g(y_i)} \le \sum_i \norm{x_i} \, \norm{y_i}$.

The infimum is needed: $u = 0$ can be written as $x \otimes y + x \otimes (-y)$, with cost $2 \norm{x} \, \norm{y}$.
A single representation does not give a well-defined number.

Universal property: bounded bilinear maps $B \colon X \times Y \to Z$ into a Banach space $Z$ correspond to bounded linear maps $X \widehat{\otimes}_\pi Y \to Z$ with the same norm.
In particular, the dual of $X \widehat{\otimes}_\pi Y$ is the space of bounded linear maps from $X$ to $Y^*$.
For example, $\ell^1 \widehat{\otimes}_\pi \ell^1$ is isometric to $\ell^1(\N \times \N)$.
