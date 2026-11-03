---
tag: 1GED8WK4RX
kind: example
name: Harmonic analysis on SU(2)
msc: ["43A77", "22E70", "43A80"]
illustrates: [2V97NSWT49, 6VC9QE39XH]
uses: [E5P8AG6CK7, 9V6PRD1Z90, 6VC9QE39XH, 9BP07A967R, 56TSJ9Q92R, RMWMYBY8TC]
sources:
  - url: https://en.wikipedia.org/wiki/Representation_theory_of_SU(2)
---

## Example

Let $G = \mathrm{SU}(2)$ ([[SU(2)|E5P8AG6CK7]]) with Haar measure $dg$ of total mass $1$.
By the [[representation theory of SU(2)|9V6PRD1Z90]], the irreducible representations are the spaces $V_n$ for $n = 0, 1, 2, \dots$.
Here $V_n$ is the space of homogeneous polynomials of degree $n$ in two variables, and $\dim V_n = n + 1$.

The [[Peter–Weyl theorem|6VC9QE39XH]] gives the orthogonal decomposition
$$L^2(\mathrm{SU}(2)) = \widehat{\bigoplus_{n \ge 0}} \mathcal{M}_n,$$
where $\mathcal{M}_n$ is the span of the matrix coefficients of $V_n$, of dimension $(n + 1)^2$.
The [[Fourier series|9BP07A967R]] of $f \in L^2(G)$ is $\sum_{n \ge 0} (n + 1) \tr(\hat f(n) \pi_n(g))$, and the [[Plancherel formula|56TSJ9Q92R]] reads $\int_G \abs{f}^2 \, dg = \sum_{n \ge 0} (n + 1) \norm{\hat f(n)}_{\mathrm{HS}}^2$.

Class functions give a concrete check.
Every $g \in G$ is conjugate to $t_\theta = \mathrm{diag}(e^{i \theta}, e^{-i \theta})$ for a unique $\theta \in [0, \pi]$.
For a continuous class function $f$, the Weyl integration formula for $\mathrm{SU}(2)$ is
$$\int_G f(g) \, dg = \frac{2}{\pi} \int_0^\pi f(t_\theta) \sin^2 \theta \, d\theta.$$
The [[characters|RMWMYBY8TC]] are $\chi_n(t_\theta) = \sin((n+1)\theta) / \sin \theta$, so
$$\int_G \chi_n \overline{\chi_m} \, dg = \frac{2}{\pi} \int_0^\pi \sin((n+1)\theta) \sin((m+1)\theta) \, d\theta = \delta_{nm}.$$
Thus the characters form an orthonormal basis of the class functions in $L^2(G)$, and the Fourier series of a class function $f$ is $\sum_n \ip{f}{\chi_n} \chi_n$.
Under $f(t_\theta) \sin \theta \leftrightarrow f$, this is exactly the classical sine series on $[0, \pi]$.

## Explanations

### L1 human

The group $\mathrm{SU}(2)$ is the three-dimensional sphere of unit quaternions, and it has exactly one irreducible representation in each dimension $1, 2, 3, \dots$.
Every square integrable function on it splits into pieces, one for each of these representations, and the piece for dimension $n + 1$ lives in a space of dimension $(n + 1)^2$.
For functions that depend only on the rotation angle, the pieces are the characters, and the expansion turns into an ordinary sine series.
