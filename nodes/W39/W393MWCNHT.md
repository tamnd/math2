---
tag: W393MWCNHT
kind: proof
name: Proof of the orthogonality of eigenspaces
msc: ["47B15", "15A18"]
topics: [3YM9EK6VMB]
audience: ug1
proves: 0JHGAV9H25
uses: [0VGSYBWHV2, 0MB8HQW495, 0ENZN5G4CV, 0ST8QF9T3T, 0B5H4208Z9, 0AYEPBQMAW, 0TS7VZJBWD, ~98fd04c3]
methods: [0NTF6DMVAP]
sources:
  - url: https://linear.axler.net/LADR4e.pdf
    locator: Theorem 7.22
  - url: https://en.wikipedia.org/wiki/Normal_operator
    locator: Properties in finite-dimensional case
---

## Proof

We compute $\ip{Tv}{w}$ in two ways, and we move $T$ to the second slot as $T^*$.

1. Let $V$ be a finite-dimensional inner product space over $\mathbb{K} = \mathbb{R}$ or $\mathbb{C}$, with [[inner product|0VGSYBWHV2]] $\ip{\cdot}{\cdot}$.
2. Let $T$ be [[normal|0ENZN5G4CV]]. A [[self-adjoint|0MB8HQW495]] operator is normal, because $T^* T = T T = T T^*$. So the self-adjoint case is included.
3. Let $v$ and $w$ be [[eigenvectors|0B5H4208Z9]] with $Tv = \lambda v$ and $Tw = \mu w$, where $\lambda \neq \mu$.
4. By part 3 of [[the norm criterion for normal operators|~98fd04c3]], $Tw = \mu w$ gives $T^* w = \overline{\mu} w$.
5. Linearity in the first slot gives $\ip{Tv}{w} = \ip{\lambda v}{w} = \lambda \ip{v}{w}$.
6. By the [[definition of the adjoint|0ST8QF9T3T]] and step 4, $\ip{Tv}{w} = \ip{v}{T^* w} = \ip{v}{\overline{\mu} w}$.
7. Conjugate linearity in the second slot gives $\ip{v}{\overline{\mu} w} = \overline{\overline{\mu}}\, \ip{v}{w} = \mu \ip{v}{w}$.
8. Steps 5 to 7 give $\lambda \ip{v}{w} = \mu \ip{v}{w}$, so $(\lambda - \mu) \ip{v}{w} = 0$.
9. Since $\lambda - \mu \neq 0$, we get $\ip{v}{w} = 0$. So $v$ and $w$ are [[orthogonal|0TS7VZJBWD]].
10. Now let $E_\lambda$ and $E_\mu$ be the [[eigenspaces|0AYEPBQMAW]] for $\lambda \neq \mu$, and let $v \in E_\lambda$ and $w \in E_\mu$.
11. If $v = 0$ or $w = 0$, then $\ip{v}{w} = 0$, because the inner product is linear in the first slot and conjugate linear in the second slot.
12. Otherwise $v$ and $w$ are eigenvectors for $\lambda$ and $\mu$, and step 9 gives $\ip{v}{w} = 0$. So $E_\lambda$ and $E_\mu$ are orthogonal to each other.

## Idea

For a normal operator, an eigenvector $w$ of $T$ for $\mu$ is also an eigenvector of $T^*$ for $\overline{\mu}$.
Moving $T$ across the inner product then gives the factor $\lambda$ on one side and $\mu$ on the other.
Two different numbers times the same inner product agree only when the inner product is zero.

## Variants

For a self-adjoint $T$ there is a shorter proof without the norm criterion.
Self-adjointness gives $\ip{Tv}{w} = \ip{v}{Tw} = \overline{\mu} \ip{v}{w}$, and $\overline{\mu} = \mu$ because [[the eigenvalues are real|0C4NT4GT3X]].
So $\lambda \ip{v}{w} = \mu \ip{v}{w}$, as in step 8.
