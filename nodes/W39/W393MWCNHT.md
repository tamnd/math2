---
tag: W393MWCNHT
kind: proof
name: Proof that the eigenspaces of a self-adjoint operator are orthogonal
msc: [47B15, 15A18]
proves: 0JHGAV9H25
uses: [0VGSYBWHV2, 0MB8HQW495, 0B5H4208Z9, 0AYEPBQMAW, 0C4NT4GT3X, 0TS7VZJBWD]
sources:
  - url: https://linear.axler.net/LADR4e.pdf
    locator: Theorem 7.22
---

## Proof

We compute $\ip{T(v)}{w}$ in two ways.

1. Let $V$ be a finite-dimensional inner product space over $\mathbb{K} = \R$ or $\C$, with [[inner product|0VGSYBWHV2]] $\ip{\cdot}{\cdot}$. Let $T \colon V \to V$ be [[self-adjoint|0MB8HQW495]].
2. Let $v$ and $w$ be [[eigenvectors|0B5H4208Z9]] with $T(v) = \lambda v$ and $T(w) = \mu w$, where $\lambda \ne \mu$.
3. Linearity in the first argument gives $\ip{T(v)}{w} = \lambda \ip{v}{w}$.
4. Conjugate symmetry and linearity in the first argument give $\ip{v}{T(w)} = \ip{v}{\mu w} = \overline{\mu} \ip{v}{w}$.
5. The eigenvalue $\mu$ is [[real|0C4NT4GT3X]], so $\overline{\mu} = \mu$.
6. By self-adjointness, $\ip{T(v)}{w} = \ip{v}{T(w)}$. Steps 3 to 5 give $\lambda \ip{v}{w} = \mu \ip{v}{w}$.
7. So $(\lambda - \mu) \ip{v}{w} = 0$. Since $\lambda - \mu \ne 0$, we get $\ip{v}{w} = 0$. So $v$ and $w$ are [[orthogonal|0TS7VZJBWD]].
8. Now let $E_\lambda$ and $E_\mu$ be the [[eigenspaces|0AYEPBQMAW]] for $\lambda \ne \mu$. Let $v \in E_\lambda$ and $w \in E_\mu$.
9. If $v = 0$, then $\ip{v}{w} = \ip{0 \cdot v}{w} = 0 \cdot \ip{v}{w} = 0$. If $w = 0$, then $\ip{v}{w} = \overline{\ip{w}{v}} = 0$ in the same way.
10. Otherwise $v$ and $w$ are eigenvectors for $\lambda$ and $\mu$, and step 7 gives $\ip{v}{w} = 0$. So $E_\lambda$ and $E_\mu$ are orthogonal to each other.

## Idea

Moving $T$ across the inner product gives the factor $\lambda$ on one side and $\overline{\mu} = \mu$ on the other. Two different numbers times the same inner product can agree only when the inner product is zero.
