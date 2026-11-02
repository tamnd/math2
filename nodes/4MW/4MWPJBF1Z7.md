---
tag: 4MWPJBF1Z7
kind: definition
name: Wavelet
msc: [42C40, 65T60]
defines: 4PZ35C0GV3
uses: [SASP14MA1Z, 0S9GGTR0EX]
sources:
  - url: https://en.wikipedia.org/wiki/Wavelet
---

## Definition

Let $\psi \in L^2(\R)$ (see [[Lp space|SASP14MA1Z]]).
For $j, k \in \Z$ put
$$\psi_{j,k}(x) = 2^{j/2} \, \psi(2^j x - k).$$
The function $\psi$ is an *orthonormal wavelet* if the family $(\psi_{j,k})_{j, k \in \Z}$ is an [[orthonormal basis|0S9GGTR0EX]] of $L^2(\R)$.

## Remarks

The factor $2^{j/2}$ makes $\norm{\psi_{j,k}}_2 = \norm{\psi}_2$.
Then every $f \in L^2(\R)$ has the expansion $f = \sum_{j,k} \ip{f}{\psi_{j,k}} \psi_{j,k}$, convergent in $L^2(\R)$.
If $\psi$ is also integrable, then $\int_\R \psi(x) \, dx = 0$.
Weaker notions are also called wavelets: $\psi$ such that $(\psi_{j,k})$ is a Riesz basis or a frame, and the admissible functions of the continuous wavelet transform.

Example: the [[Haar wavelet|JW5PA9XA7F]] $\psi = 1_{[0, 1/2)} - 1_{[1/2, 1)}$ is an orthonormal wavelet.
For instance, $\psi_{0,0}$ and $\psi_{1,0}$ are orthogonal, because $\psi_{1,0}$ lives on $[0, \tfrac12)$, where $\psi_{0,0} = 1$, and has integral $0$.

Non-example: the Gaussian $\psi(x) = e^{-\pi x^2}$ is not an orthonormal wavelet.
Its translates $\psi_{0,0}$ and $\psi_{0,1}$ are both positive, so $\ip{\psi_{0,0}}{\psi_{0,1}} > 0$ and they are not orthogonal.
