---
tag: 7JE39BAHQG
kind: definition
name: Pseudospectrum
msc: [65F15, 15A18, 47A10]
defines: F20VTSH2FM
uses: [0BQAA2BK3Q, J5YNNKSB9P, 06EKW1AKXF, 09VMDSRXWJ, BMKATJ802A]
sources:
  - url: https://en.wikipedia.org/wiki/Pseudospectrum
---

## Definition

Let $A \in \C^{n \times n}$, let $\Lambda(A)$ be its set of [[eigenvalues|0BQAA2BK3Q]], and let $\varepsilon > 0$.
Let $\norm{\cdot}$ be the Euclidean norm on $\C^n$ with its [[operator norm|06EKW1AKXF]] on matrices.
The *$\varepsilon$-pseudospectrum* of $A$ is
$$\Lambda_\varepsilon(A) = \Lambda(A) \cup \set{z \in \C \setminus \Lambda(A) : \norm{(zI - A)^{-1}} > 1/\varepsilon}.$$

## Remarks

The following sets are equal to $\Lambda_\varepsilon(A)$:

1. $\set{z \in \C : z \in \Lambda(A + E) \text{ for some } E \in \C^{n \times n} \text{ with } \norm{E} < \varepsilon}$;
2. $\set{z \in \C : \norm{(zI - A) v} < \varepsilon \text{ for some unit vector } v}$;
3. $\set{z \in \C : \sigma_{\min}(zI - A) < \varepsilon}$, where $\sigma_{\min}$ is the smallest [[singular value|09VMDSRXWJ]].

The convention $\norm{(zI - A)^{-1}} = \infty$ for $z \in \Lambda(A)$ makes the definition read $\norm{(zI - A)^{-1}} > 1/\varepsilon$ for all $z$.

Example: if $A$ is normal, then $\norm{(zI - A)^{-1}} = 1/\mathrm{dist}(z, \Lambda(A))$, so $\Lambda_\varepsilon(A)$ is the union of the open discs of radius $\varepsilon$ about the eigenvalues.
Example: for $J = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$ and $z \ne 0$, $(zI - J)^{-1} = \begin{pmatrix} 1/z & 1/z^2 \\ 0 & 1/z \end{pmatrix}$, whose norm is at least $1/\abs{z}^2$; so every $z$ with $0 < \abs{z} < \sqrt{\varepsilon}$ lies in $\Lambda_\varepsilon(J)$.
Non-example: for $A = 0 \in \C^{1 \times 1}$ and $\varepsilon = 0.1$, the point $z = 0.2$ is not in $\Lambda_\varepsilon(A)$, since $\norm{(zI - A)^{-1}} = 5 \le 10$.
The sets are open, they increase with $\varepsilon$, and their intersection over all $\varepsilon > 0$ is $\Lambda(A)$.
The same definition makes sense for a bounded operator on a Banach space, with its [[spectrum|BMKATJ802A]] in place of $\Lambda(A)$.

## Explanations

### L1 human

A point is in the $\varepsilon$-pseudospectrum when it is "almost an eigenvalue": some vector is mapped by $A - z$ to a vector shorter than $\varepsilon$.
These sets are drawn as contour plots of the resolvent norm in the complex plane.
