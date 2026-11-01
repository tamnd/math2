---
tag: YFF8B5A0QG
kind: statement
role: theorem
name: Hilbert's Theorem 90
msc: [12G05, 12F10]
uses: [VFE5B71E7Y, 0DS2F7GK05, 0XVR72M51M, 8HHY1K3XDC, N43G50YHG2]
about: [KRNFEZWPY0, 9MPCZ3EAJM]
sources:
  - url: https://en.wikipedia.org/wiki/Hilbert%27s_Theorem_90
same_as:
  wikidata: Q1420905
  wikipedia: Hilbert's Theorem 90
---

## Statement

1. Let $L/K$ be a finite [[cyclic extension|VFE5B71E7Y]] and let $\sigma$ be a generator of its [[Galois group|0XVR72M51M]].
   An element $\alpha \in L$ has [[norm|8HHY1K3XDC]] $N_{L/K}(\alpha) = 1$ if and only if $\alpha = \beta / \sigma(\beta)$ for some $\beta \in L^\times$.
2. Let $L/K$ be a finite [[Galois extension|0DS2F7GK05]] with Galois group $G$.
   Let $f \colon G \to L^\times$ be a map with $f(\sigma\tau) = f(\sigma)\, \sigma(f(\tau))$ for all $\sigma, \tau \in G$.
   Then there is $\beta \in L^\times$ with $f(\sigma) = \beta / \sigma(\beta)$ for all $\sigma \in G$.
   In the language of group cohomology, $H^1(G, L^\times) = 1$.

## Remarks

For part 2, [[Dedekind's lemma|N43G50YHG2]] gives $\gamma \in L$ such that $\beta = \sum_{\tau \in G} f(\tau)\, \tau(\gamma)$ is nonzero.
Then $\sigma(\beta) = \sum_\tau \sigma(f(\tau))\, \sigma\tau(\gamma) = f(\sigma)^{-1} \sum_\tau f(\sigma\tau)\, \sigma\tau(\gamma) = f(\sigma)^{-1} \beta$.
For part 1, if $N(\alpha) = 1$ then $f(\sigma^i) = \alpha\, \sigma(\alpha) \cdots \sigma^{i-1}(\alpha)$ is well defined on the cyclic group and satisfies the condition of part 2; conversely $N(\beta / \sigma(\beta)) = N(\beta)/N(\sigma(\beta)) = 1$.

Example: take $L = \Q(i)$ and $K = \Q$, with $\sigma$ complex conjugation.
The elements of norm $1$ are the $a + bi$ with $a^2 + b^2 = 1$, and the theorem writes each as $(m + ni)/(m - ni) = (m^2 - n^2 + 2mni)/(m^2 + n^2)$ with integers $m, n$ not both zero.
This recovers the parametrization of rational points on the unit circle and of Pythagorean triples.

Part 1 needs a generator $\sigma$ of the Galois group, so it applies only to cyclic extensions; for a general finite Galois extension one uses part 2.

## Explanations

### L1 human

The norm of an element multiplies it with all its conjugates.
Hilbert's Theorem 90 says that, in a cyclic extension, the elements of norm $1$ are exactly the quotients of an element by its conjugate.
For the Gaussian numbers this explains why every rational point on the circle $a^2 + b^2 = 1$ has the form $\left(\frac{m^2 - n^2}{m^2 + n^2}, \frac{2mn}{m^2 + n^2}\right)$.

### L2 human

The cohomological form $H^1(\Gal(L/K), L^\times) = 1$ is the starting point of [[Galois cohomology|9MPCZ3EAJM]].
It is the main step in Kummer theory.
When $K$ contains a primitive $n$-th root of unity, it shows that every cyclic extension of degree $n$ is obtained by adjoining an $n$-th root.
There is also an additive version: in a cyclic extension, the elements of [[trace|WPE5Z53QYJ]] $0$ are exactly the $\beta - \sigma(\beta)$, which gives Artin–Schreier theory in characteristic $p$.
