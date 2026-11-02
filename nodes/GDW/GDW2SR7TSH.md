---
tag: GDW2SR7TSH
kind: definition
name: Fast wavelet transform
msc: [65T60, 42C40]
defines: PDVYQAW887
uses: [1GHQMBR7DE, YH4BERB952, P3H4MMC4ZH]
sources:
  - url: https://en.wikipedia.org/wiki/Fast_wavelet_transform
---

## Definition

Let $\varphi$ be the [[scaling function|YH4BERB952]] of an orthonormal [[multiresolution analysis|1GHQMBR7DE]] of $L^2(\R)$ with real finite filter $(h_n)_{n \in \Z}$, so that
$$\varphi(x) = \sqrt{2} \sum_{n} h_n \, \varphi(2x - n).$$
Put $g_n = (-1)^n h_{1-n}$ and let $\psi(x) = \sqrt{2}\sum_n g_n \varphi(2x - n)$ be the associated wavelet.
For $j, k \in \Z$ write $\varphi_{j,k}(x) = 2^{j/2}\varphi(2^j x - k)$ and $\psi_{j,k}(x) = 2^{j/2}\psi(2^j x - k)$.
For $f \in L^2(\R)$ put $a_{j,k} = \ip{f}{\varphi_{j,k}}$ and $d_{j,k} = \ip{f}{\psi_{j,k}}$.

The *fast wavelet transform* from level $J$ down to level $J_0 < J$ is the algorithm that takes the sequence $(a_{J,k})_k$ and, for $j = J, J-1, \dots, J_0 + 1$, computes
$$a_{j-1,k} = \sum_{m} h_{m-2k} \, a_{j,m}, \qquad d_{j-1,k} = \sum_{m} g_{m-2k} \, a_{j,m}.$$
Its output is $(a_{J_0,k})_k$ together with $(d_{j,k})_k$ for $J_0 \le j < J$.
The inverse fast wavelet transform computes, for $j = J_0 + 1, \dots, J$,
$$a_{j,m} = \sum_{k} h_{m-2k} \, a_{j-1,k} + \sum_{k} g_{m-2k} \, d_{j-1,k}.$$

## Remarks

The formulas follow from $\varphi_{j-1,k} = \sum_m h_{m-2k}\varphi_{j,m}$ and $\psi_{j-1,k} = \sum_m g_{m-2k}\varphi_{j,m}$, which are the refinement equations rescaled.
Each step is a convolution with a filter followed by downsampling by $2$.

Example: for the Haar wavelet, $h_0 = h_1 = 1/\sqrt{2}$, so $g_0 = 1/\sqrt{2}$ and $g_1 = -1/\sqrt{2}$.
One step maps $a_{j,\cdot}$ to $a_{j-1,k} = (a_{j,2k} + a_{j,2k+1})/\sqrt{2}$ and $d_{j-1,k} = (a_{j,2k} - a_{j,2k+1})/\sqrt{2}$, and the inverse step recovers $a_{j,2k}$ and $a_{j,2k+1}$ from these two numbers.

Non-example: if the downsampling is left out and all outputs of the filters are kept, the result is the undecimated (stationary) wavelet transform.
It is redundant: it doubles the number of coefficients at each level, while the fast wavelet transform keeps the total number of coefficients equal to the input length.

With an input of length $N$ and filters of length $L$, the algorithm uses at most about $2LN$ multiplications.

## Explanations

### L1 human

The fast wavelet transform computes all wavelet coefficients by repeatedly filtering and halving.
It never computes an integral: everything comes from the filter coefficients of the scaling function.
