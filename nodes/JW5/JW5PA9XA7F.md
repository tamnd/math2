---
tag: JW5PA9XA7F
kind: example
name: Haar wavelet
msc: [42C40, 42C10]
instance_of: [4PZ35C0GV3]
uses: [N0B51FAA9S, 1GHQMBR7DE, YH4BERB952, 7QERXM0C52]
sources:
  - url: https://en.wikipedia.org/wiki/Haar_wavelet
same_as:
  wikidata: Q766198
  wikipedia: Haar wavelet
---

## Example

The *Haar wavelet* is the function $\psi \colon \R \to \R$ with
$$\psi(x) = \begin{cases} 1 & 0 \le x < \tfrac12, \\ -1 & \tfrac12 \le x < 1, \\ 0 & \text{otherwise.} \end{cases}$$
It is an orthonormal [[wavelet|4PZ35C0GV3]]: the functions $\psi_{j,k}(x) = 2^{j/2} \psi(2^j x - k)$, $j, k \in \Z$, form an orthonormal basis of $L^2(\R)$.

Check of orthonormality.
$\psi_{j,k}$ is supported on the dyadic interval $I_{j,k} = [k 2^{-j}, (k+1) 2^{-j})$ and $\norm{\psi_{j,k}}_2^2 = 2^j \cdot 2^{-j} = 1$.
Two dyadic intervals are either disjoint or nested.
If they are disjoint, the product $\psi_{j,k} \psi_{j',k'}$ is $0$.
If $I_{j',k'}$ lies strictly inside $I_{j,k}$, then it lies inside one half of $I_{j,k}$, where $\psi_{j,k}$ is constant, and $\psi_{j',k'}$ has integral $0$.

Completeness comes from the Haar [[multiresolution analysis|1GHQMBR7DE]], whose space $V_j$ consists of the functions in $L^2(\R)$ that are constant on the intervals $I_{j,k}$.
The [[scaling function|YH4BERB952]] is $\varphi = 1_{[0, 1)}$, with $\varphi(x) = \varphi(2x) + \varphi(2x - 1)$ and $\psi(x) = \varphi(2x) - \varphi(2x - 1)$.
On $[0, 1]$, the constant $1$ together with the $\psi_{j,k}$ with $j \ge 0$ and $0 \le k < 2^j$ is the [[Haar system|N0B51FAA9S]].

The Haar wavelet has exactly one [[vanishing moment|7QERXM0C52]]: $\int \psi = 0$, while $\int_\R x \psi(x) \, dx = \tfrac18 - \tfrac38 = -\tfrac14$.
It is discontinuous, so for smooth functions its expansions converge slowly compared with smoother wavelets.

## Explanations

### L1 human

The Haar wavelet is a single up-step followed by a down-step.
Its squeezed and shifted copies work at every scale and place.
Each one measures how the average of a function on the left half of a small interval differs from its average on the right half.
Alfréd Haar used these functions in 1910, long before the word wavelet existed.
It is the first member of the family of Daubechies wavelets.
