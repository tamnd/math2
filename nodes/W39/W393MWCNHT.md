---
tag: W393MWCNHT
kind: proof
name: Proof of the orthogonality of eigenspaces
msc: ["47B15", "15A18"]
topics: [3YM9EK6VMB]
audience: ug1
proves: 0JHGAV9H25
uses: [0VGSYBWHV2, 0MB8HQW495, 0ENZN5G4CV, 0ST8QF9T3T, 0B5H4208Z9, 0AYEPBQMAW, 0TS7VZJBWD, EMW3QTE3H9]
methods: [0NTF6DMVAP]
sources:
  - url: https://linear.axler.net/LADR4e.pdf
    locator: Theorem 7.22
  - url: https://en.wikipedia.org/wiki/Normal_operator
    locator: Properties in finite-dimensional case
---

## Proof

We compute $\ip{Tv}{w}$ in two ways: once with $T$ acting on $v$, and once with $T$ moved to the second slot as $T^*$.
Let $V$ be a finite-dimensional inner product space over $\mathbb{K} = \mathbb{R}$ or $\mathbb{C}$, whose [[inner product|0VGSYBWHV2]] is linear in the first slot and conjugate linear in the second.

1. Let $T$ be [[normal|0ENZN5G4CV]]. A [[self-adjoint|0MB8HQW495]] operator is normal, because $T^* T = T T = T T^*$, so the self-adjoint case is included.
2. Let $v$ and $w$ be [[eigenvectors|0B5H4208Z9]] with $Tv = \lambda v$ and $Tw = \mu w$, where $\lambda \neq \mu$.
3. By part 3 of [[the norm criterion for normal operators|EMW3QTE3H9]], $Tw = \mu w$ gives $T^* w = \overline{\mu} w$.
4. Linearity in the first slot gives the first computation:
$$\ip{Tv}{w} = \ip{\lambda v}{w} = \lambda \ip{v}{w}.$$
5. The [[definition of the adjoint|0ST8QF9T3T]], step 3 and conjugate linearity in the second slot give the second computation:
$$\ip{Tv}{w} = \ip{v}{T^* w} = \ip{v}{\overline{\mu} w} = \mu \ip{v}{w}.$$
6. Steps 4 and 5 give $\lambda \ip{v}{w} = \mu \ip{v}{w}$, that is, $(\lambda - \mu) \ip{v}{w} = 0$.
7. Since $\lambda - \mu \neq 0$, we get $\ip{v}{w} = 0$, so $v$ and $w$ are [[orthogonal|0TS7VZJBWD]].
8. Let $v \in E_\lambda$ and $w \in E_\mu$ be arbitrary elements of the [[eigenspaces|0AYEPBQMAW]]. If $v = 0$ or $w = 0$, then $\ip{v}{w} = 0$. Otherwise they are eigenvectors, and step 7 applies. So $E_\lambda$ and $E_\mu$ are orthogonal to each other.

## Idea

For a normal operator, an eigenvector $w$ of $T$ for $\mu$ is also an eigenvector of $T^*$ for $\overline{\mu}$.
So moving $T$ across the inner product puts the factor $\lambda$ on one side and the factor $\mu$ on the other.
Two different numbers times the same inner product can agree only when that inner product is zero.

## Variants

For a self-adjoint $T$ there is a shorter proof that does not need the norm criterion.
Self-adjointness gives $\ip{Tv}{w} = \ip{v}{Tw} = \ip{v}{\mu w} = \overline{\mu} \ip{v}{w}$.
Since [[the eigenvalues are real|0C4NT4GT3X]], $\overline{\mu} = \mu$, and the proof ends as in step 6.
