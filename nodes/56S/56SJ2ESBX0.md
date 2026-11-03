---
tag: 56SJ2ESBX0
kind: definition
name: Fourier transform on a nonabelian group
msc: ["43A30", "22D10"]
defines: N8E0GVVWG1
uses: [AHV05ZBCYW, VY0HXD3GC4, 74BPYJNZTM, 95Q8WZMN0W, HM2HHE3J51]
sources:
  - url: https://en.wikipedia.org/wiki/Noncommutative_harmonic_analysis
---

## Definition

Let $G$ be a [[locally compact group|AHV05ZBCYW]] with a left [[Haar measure|VY0HXD3GC4]] $dg$.
Let $\widehat{G}$ be its [[unitary dual|95Q8WZMN0W]].
For each class in $\widehat{G}$ fix an irreducible [[unitary representation|74BPYJNZTM]] $\pi$ of $G$ on a [[Hilbert space|HM2HHE3J51]] $\mathcal{H}_\pi$.
The *Fourier transform* of $f \in L^1(G)$ is the family of bounded operators
$$\hat f(\pi) = \int_G f(g) \, \pi(g)^* \, dg \quad \text{on } \mathcal{H}_\pi, \qquad \pi \in \widehat{G},$$
where the integral is taken in the weak sense: $\ip{\hat f(\pi) u}{v} = \int_G f(g) \ip{\pi(g)^* u}{v} \, dg$ for $u, v \in \mathcal{H}_\pi$.

## Remarks

The operator norm satisfies $\norm{\hat f(\pi)} \le \norm{f}_1$, since each $\pi(g)^*$ is unitary.
Many authors use $\pi(f) = \int_G f(g) \pi(g) \, dg$ instead; the two differ by the substitution $\pi(g)^* = \pi(g^{-1})$.
Changing $\pi$ to an equivalent representation $U \pi U^{-1}$ changes $\hat f(\pi)$ to $U \hat f(\pi) U^{-1}$, so norms and traces of $\hat f(\pi)$ depend only on the class of $\pi$.

Example: let $G = \R$ with Lebesgue measure.
The irreducible unitary representations are the characters $\pi_\xi(x) = e^{2\pi i \xi x}$ on $\C$, so $\hat f(\pi_\xi) = \int_\R f(x) e^{-2\pi i \xi x} \, dx$, the usual Fourier transform.

Example: let $G$ be a finite group with counting measure.
Then $\hat f(\pi) = \sum_{g \in G} f(g) \pi(g)^*$ is a $d_\pi \times d_\pi$ matrix, where $d_\pi = \dim \mathcal{H}_\pi$.

If $f_1 * f_2$ is the convolution $\int_G f_1(h) f_2(h^{-1} g) \, dh$, then $\widehat{f_1 * f_2}(\pi) = \hat f_2(\pi) \hat f_1(\pi)$, with the order reversed because of the adjoint.
A non-example: the family of the numbers $\int_G f(g) \chi_\pi(g) \, dg$, with $\chi_\pi$ the character, is not the Fourier transform.
It records only the traces of the operators and loses information when some $d_\pi > 1$.
