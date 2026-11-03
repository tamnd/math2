---
tag: G7CQFX22CG
kind: definition
name: Matsubara frequency
msc: [81T28, 82B10]
defines: P37VG1DT73
uses: [G12KXDHPPS, 032HKYS329, R5HWSRAK4H, FM6XWC4BST]
sources:
  - url: https://en.wikipedia.org/wiki/Matsubara_summation
---

## Definition

Let $T > 0$ be a temperature and $\beta = 1 / (k_B T)$, in units with $\hbar = 1$.
The *bosonic Matsubara frequencies* are $\omega_n = 2\pi n / \beta$ and the *fermionic Matsubara frequencies* are $\omega_n = (2n + 1)\pi / \beta$, for $n \in \Z$.
Consider functions $f$ of the imaginary time $\tau$ that satisfy $f(\tau + \beta) = f(\tau)$ (bosonic case) or $f(\tau + \beta) = -f(\tau)$ (fermionic case).
The Matsubara frequencies are the frequencies of their [[Fourier series|G12KXDHPPS]]:
$$f(\tau) = \frac{1}{\beta} \sum_{n \in \Z} \hat f(\omega_n) e^{-i \omega_n \tau}.$$

## Remarks

Check: $e^{-i \omega_n (\tau + \beta)} = e^{-i\omega_n \tau} e^{-i \omega_n \beta}$, and $e^{-i\omega_n \beta}$ equals $e^{-2\pi i n} = 1$ for bosonic and $e^{-(2n+1)\pi i} = -1$ for fermionic frequencies.
Example: for $\varepsilon > 0$, the classical sum $\sum_{n \in \Z} 1/(n^2 + a^2) = (\pi / a) \coth(\pi a)$ gives
$$\frac{1}{\beta} \sum_{n \in \Z} \frac{1}{\omega_n^2 + \varepsilon^2} = \frac{1}{2\varepsilon} \coth\frac{\beta\varepsilon}{2} = \frac{1}{2\varepsilon}\big(1 + 2 n_B(\varepsilon)\big)$$
for bosonic $\omega_n$, where $n_B(\varepsilon) = 1/(e^{\beta\varepsilon} - 1)$ is the [[Bose–Einstein|R5HWSRAK4H]] factor.
For fermionic $\omega_n$ the same sum equals $\frac{1}{2\varepsilon} \tanh\frac{\beta\varepsilon}{2} = \frac{1}{2\varepsilon}\big(1 - 2 n_F(\varepsilon)\big)$, with the [[Fermi–Dirac|FM6XWC4BST]] factor $n_F(\varepsilon) = 1/(e^{\beta\varepsilon} + 1)$.
Such sums are computed in general by the [[residue theorem|032HKYS329]], using a function such as $\beta/(e^{\beta z} - 1)$ whose poles sit at $z = i\omega_n$.
Non-example: the frequency $\pi/(2\beta)$ is neither bosonic nor fermionic, since $e^{-i\pi/2} = -i$, so $e^{-i\omega\tau}$ is neither periodic nor antiperiodic with period $\beta$.

## Explanations

### L1 human

Bosonic frequencies are even multiples of $\pi/\beta$ and fermionic ones are odd multiples.
The difference comes from the boundary condition in imaginary time, which in turn comes from the sign change when two fermions are exchanged.
