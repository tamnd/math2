---
tag: PMMXG4Q8JR
kind: statement
role: theorem
name: Littlewood subordination theorem
msc: [30C80, 30H10]
uses: [0NAHXR1FRH, 0MB48XDBY3, 9ZV3T5C6B7, W19567AVYG]
about: [PNNNFJVF6W, Z1MHMGFNFW]
sources:
  - url: https://en.wikipedia.org/wiki/Littlewood_subordination_theorem
same_as:
  wikidata: Q6653168
  wikipedia: Littlewood subordination theorem
---

## Statement

Let $\mathbb{D} = \set{z \in \C : \abs{z} < 1}$.
Let $\omega \colon \mathbb{D} \to \mathbb{D}$ be a [[holomorphic function|0NAHXR1FRH]] with $\omega(0) = 0$, and let $F$ be a holomorphic function on $\mathbb{D}$.
Then for every $p$ with $0 < p < \infty$ and every $r$ with $0 < r < 1$,
$$\int_0^{2\pi} \abs{F(\omega(r e^{i\theta}))}^p \, d\theta \le \int_0^{2\pi} \abs{F(r e^{i\theta})}^p \, d\theta.$$

## Remarks

The function $\abs{F}^p$ is [[subharmonic|Z1MHMGFNFW]].
Let $u$ be the harmonic function on the disc $\abs{z} < r$ with boundary values $\abs{F}^p$ on $\abs{z} = r$, given by the [[Poisson kernel|TCYSWCTYYM]]; then $\abs{F}^p \le u$ on $\abs{z} \le r$.
By the [[Schwarz lemma|0MB48XDBY3]], $\abs{\omega(z)} \le \abs{z}$, so $\omega$ maps the closed disc of radius $r$ into itself and $\abs{F \circ \omega}^p \le u \circ \omega$ there.
Since $u \circ \omega$ is harmonic, its mean over $\abs{z} = r$ is $u(\omega(0)) = u(0)$, which is the mean of $\abs{F}^p$ over $\abs{z} = r$.
The hypothesis $\omega(0) = 0$ is needed.
For the constant map $\omega \equiv c$ with $0 < c < 1$ and $F(z) = z$, the left side is $2\pi c^p$ and the right side is $2\pi r^p$.
So the inequality fails for $r < c$.

## Explanations

### L1 human

Composing a function on the disc with a self-map of the disc that fixes the centre can only make the function smaller on average along circles.
The self-map pulls each circle inside a smaller region, and averages of nice functions over circles grow with the radius.
So the theorem compares the size of $F \circ \omega$ with the size of $F$ itself.

### L2 human

Taking the supremum over $r$ shows that the composition operator $F \mapsto F \circ \omega$ is a contraction on each [[Hardy space|PNNNFJVF6W]] $H^p$ when $\omega(0) = 0$.
For a general holomorphic self-map $\omega$ one composes with a disc automorphism moving $\omega(0)$ to $0$, which shows that every composition operator on $H^p$ is bounded.
The proof only uses that $\abs{F}^p$ is subharmonic, so the same inequality holds for any subharmonic function in place of $\abs{F}^p$.
This is the starting point of the theory of composition operators on spaces of analytic functions.
