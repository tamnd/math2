---
tag: PBEBXNHCPN
kind: definition
name: Haar system
msc: [42C10, 42C40]
defines: N0B51FAA9S
uses: [0AJXYH4DDQ, SASP14MA1Z, 0S9GGTR0EX]
sources:
  - url: https://en.wikipedia.org/wiki/Haar_wavelet
---

## Definition

Let $\psi \colon \R \to \R$ be the [[step function|0AJXYH4DDQ]] with $\psi = 1$ on $[0, \tfrac12)$, $\psi = -1$ on $[\tfrac12, 1)$ and $\psi = 0$ elsewhere.
For integers $n \ge 0$ and $0 \le k < 2^n$, let
$$h_{n,k}(t) = 2^{n/2} \, \psi(2^n t - k), \qquad t \in [0, 1].$$
The *Haar system* on $[0, 1]$ is the family consisting of the constant function $1$ and all the functions $h_{n,k}$.

## Remarks

The function $h_{n,k}$ is supported on the dyadic interval $[k 2^{-n}, (k+1) 2^{-n}]$, where it equals $2^{n/2}$ on the left half and $-2^{n/2}$ on the right half.
The Haar system is an [[orthonormal basis|0S9GGTR0EX]] of $L^2([0, 1])$ (see [[Lp space|SASP14MA1Z]]).
On the whole line, the functions $2^{j/2}\psi(2^j t - k)$ with $j, k \in \Z$ form an orthonormal basis of $L^2(\R)$.

Example: $h_{1,0}$ and $h_{1,1}$ are orthogonal, since their supports $[0, \tfrac12]$ and $[\tfrac12, 1]$ meet in one point.
Also $h_{0,0}$ and $h_{1,0}$ are orthogonal: on $[0, \tfrac12]$ the function $h_{0,0}$ is constant $1$, and $h_{1,0}$ has integral $0$ there.
And $\norm{h_{1,0}}^2 = 2 \cdot \tfrac12 = 1$.

Non-example: the family of all $h_{n,k}$ without the constant function $1$ is orthonormal but not a basis of $L^2([0, 1])$.
Indeed, the constant $1$ is orthogonal to every $h_{n,k}$, since each $h_{n,k}$ has integral $0$.
