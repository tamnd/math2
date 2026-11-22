---
tag: NEHYK109XT
kind: proof
name: Proof that the quadratic form detects zero and self-adjoint operators
msc: ["15A04", "47B15"]
topics: [3YM9EK6VMB]
audience: ug1
proves: WAYMK9GR5S
uses: [0VGSYBWHV2, 0ST8QF9T3T, 0MB8HQW495, 05FKHRT0B4]
methods: [0NTF6DMVAP, 0WCP0PVET6]
sources:
  - url: https://en.wikipedia.org/wiki/Polarization_identity
    locator: lead section
  - book: isbn:9783031410253
    locator: Chapter 7
---

## Proof

We recover the number $\ip{Tu}{w}$ from values of the form $\ip{Tx}{x}$, as in the [[polarization identity|05FKHRT0B4]], and then we choose $w = Tu$.
The [[inner product|0VGSYBWHV2]] is linear in the first slot and conjugate linear in the second slot.

1. Let $u, w \in V$. We expand two values of the quadratic form by linearity in both slots:
$$\ip{T(u \pm w)}{u \pm w} = \ip{Tu}{u} \pm \ip{Tu}{w} \pm \ip{Tw}{u} + \ip{Tw}{w}.$$
2. We subtract the value at $u - w$ from the value at $u + w$, and the terms $\ip{Tu}{u}$ and $\ip{Tw}{w}$ cancel:
$$\ip{T(u + w)}{u + w} - \ip{T(u - w)}{u - w} = 2\ip{Tu}{w} + 2\ip{Tw}{u}.$$
3. Part 1. Let $\mathbb{K} = \mathbb{C}$, and replace $w$ by $iw$ in step 2. Since $\ip{Tu}{iw} = \overline{i} \ip{Tu}{w} = -i \ip{Tu}{w}$ and $\ip{T(iw)}{u} = i \ip{Tw}{u}$, we get
$$\ip{T(u + iw)}{u + iw} - \ip{T(u - iw)}{u - iw} = -2i \ip{Tu}{w} + 2i \ip{Tw}{u}.$$
4. We multiply step 3 by $i$ and add the result to step 2. The products $i \cdot (-2i) = 2$ and $i \cdot 2i = -2$ make the terms with $\ip{Tw}{u}$ cancel:
$$4 \ip{Tu}{w} = \ip{T(u + w)}{u + w} - \ip{T(u - w)}{u - w} + i \ip{T(u + iw)}{u + iw} - i \ip{T(u - iw)}{u - iw}.$$
5. Assume that $\ip{Tx}{x} = 0$ for all $x \in V$. Then each term on the right of step 4 is $0$, so $\ip{Tu}{w} = 0$ for all $u, w \in V$.
6. We take $w = Tu$. Then $\ip{Tu}{Tu} = 0$, so $Tu = 0$ by positivity of the inner product. As $u$ is arbitrary, $T = 0$, which proves part 1.
7. Part 2, first direction. Let $T$ be [[self-adjoint|0MB8HQW495]]. Conjugate symmetry and $T^* = T$ give $\overline{\ip{Tv}{v}} = \ip{v}{Tv} = \ip{Tv}{v}$, so $\ip{Tv}{v}$ is real.
8. Part 2, second direction. Let $\ip{Tv}{v}$ be real for all $v$. The [[definition of the adjoint|0ST8QF9T3T]] and conjugate symmetry give
$$\ip{T^* v}{v} = \overline{\ip{v}{T^* v}} = \overline{\ip{Tv}{v}} = \ip{Tv}{v},$$
where the last equality holds because the number is real.
9. Step 8 gives $\ip{(T - T^*) v}{v} = 0$ for all $v \in V$. Part 1 applied to $T - T^*$ gives $T - T^* = 0$, so $T$ is self-adjoint.
10. Part 3. Let $T$ be self-adjoint over $\mathbb{R}$ or $\mathbb{C}$, with $\ip{Tx}{x} = 0$ for all $x$. Then the left side of step 2 is $0$.
11. Self-adjointness and conjugate symmetry give $\ip{Tw}{u} = \ip{w}{Tu} = \overline{\ip{Tu}{w}}$. So step 2 becomes
$$0 = 2\ip{Tu}{w} + 2\overline{\ip{Tu}{w}} = 4 \operatorname{Re} \ip{Tu}{w}.$$
12. We take $w = Tu$. The number $\ip{Tu}{Tu} = \norm{Tu}^2$ is real, so step 11 gives $\norm{Tu}^2 = 0$. Hence $Tu = 0$ for every $u$, and $T = 0$.

## Idea

Over $\mathbb{C}$, the four values of the quadratic form at $u + w$, $u - w$, $u + iw$ and $u - iw$ determine the number $\ip{Tu}{w}$.
So a quadratic form that vanishes everywhere forces every $\ip{Tu}{w}$ to vanish, and the choice $w = Tu$ gives $Tu = 0$.
Over $\mathbb{R}$, only $u + w$ and $u - w$ are available, and they determine only the sum $\ip{Tu}{w} + \ip{Tw}{u}$.
Self-adjointness turns that sum into $2 \operatorname{Re} \ip{Tu}{w}$, which is all that the last step needs.

## Variants

Part 1 also has a proof with a basis.
Choose an orthonormal basis $e_1, \dots, e_n$ and write $a_{jk} = \ip{T e_k}{e_j}$ for the matrix entries.
The value at $e_j$ forces $a_{jj} = 0$, the value at $e_j + e_k$ then forces $a_{jk} + a_{kj} = 0$, and the value at $e_j + i e_k$ forces $a_{jk} - a_{kj} = 0$.

Part 3 also follows from [[the real spectral theorem|06J4PXRG22]].
In an orthonormal eigenbasis, $\ip{T e_j}{e_j} = \lambda_j$, so every eigenvalue is $0$ and $T = 0$.
This route uses much more than the identity of step 2.
