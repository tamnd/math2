---
tag: BV0NXXGQZB
kind: definition
name: Biorthogonal wavelet
msc: [42C40, 42C15, 65T60]
defines: Q7PENKTFHA
uses: [4PZ35C0GV3, ZYDYD7FB1Z, SASP14MA1Z]
sources:
  - url: https://en.wikipedia.org/wiki/Biorthogonal_wavelet
---

## Definition

Let $\psi$ and $\tilde\psi$ be functions in the [[Lp space|SASP14MA1Z]] $L^2(\R)$.
For $j, k \in \Z$ put $\psi_{j,k}(x) = 2^{j/2}\psi(2^j x - k)$ and $\tilde\psi_{j,k}(x) = 2^{j/2}\tilde\psi(2^j x - k)$.
The pair $(\psi, \tilde\psi)$ is a *biorthogonal wavelet* pair if:

1. the family $\set{\psi_{j,k} : j, k \in \Z}$ is a [[Riesz basis|ZYDYD7FB1Z]] of $L^2(\R)$;
2. the family $\set{\tilde\psi_{j,k} : j, k \in \Z}$ is a Riesz basis of $L^2(\R)$;
3. $\ip{\psi_{j,k}}{\tilde\psi_{j',k'}} = 1$ if $(j,k) = (j',k')$ and $0$ otherwise.

The function $\tilde\psi$ is called the dual wavelet of $\psi$.

## Remarks

Under these conditions every $f \in L^2(\R)$ has the expansions
$$f = \sum_{j,k \in \Z} \ip{f}{\tilde\psi_{j,k}} \, \psi_{j,k} = \sum_{j,k \in \Z} \ip{f}{\psi_{j,k}} \, \tilde\psi_{j,k},$$
with convergence in $L^2(\R)$.

Example: if $\psi$ is an orthonormal [[wavelet|4PZ35C0GV3]], such as the Haar wavelet, then $(\psi, \psi)$ is a biorthogonal pair.
Each family is an orthonormal basis, hence a Riesz basis, and clause 3 is orthonormality.

Non-example: take $\psi$ the Haar wavelet and $\tilde\psi = 2\psi$.
Both families are Riesz bases, but $\ip{\psi_{0,0}}{\tilde\psi_{0,0}} = 2$, so clause 3 fails.

In practice biorthogonal pairs come from two multiresolution analyses with dual scaling functions $\varphi$ and $\tilde\varphi$, and the transform is computed with two pairs of finite filters.
The Cohen–Daubechies–Feauveau family contains the 5/3 and 9/7 biorthogonal wavelets used in JPEG 2000.

## Explanations

### L1 human

Two families of wavelets are used: one to measure a signal and one to rebuild it.
They must be dual, which means each measuring function gives $1$ on its own partner and $0$ on every other rebuilding function.
