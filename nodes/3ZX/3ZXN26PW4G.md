---
tag: 3ZXN26PW4G
kind: statement
role: theorem
name: Wiener–Khinchin theorem
msc: [60G10, 60G12, 62M15]
uses: [DT0QXJE705, 0KBFAWYRTE, 0X3WGX95FE]
about: [DT0QXJE705, 0KBFAWYRTE]
sources:
  - url: https://en.wikipedia.org/wiki/Wiener%E2%80%93Khinchin_theorem
same_as:
  wikidata: Q2301141
  wikipedia: Wiener–Khinchin theorem
---

## Statement

Let $(X_t)_{t \in \R}$ be a complex-valued weakly [[stationary process|DT0QXJE705]]: $E[\abs{X_t}^2] < \infty$, $E[X_t] = m$ for all $t$, and the autocovariance $r(\tau) = E[(X_{t+\tau} - m)\overline{(X_t - m)}]$ does not depend on $t$.
Assume that $r$ is [[continuous|0X3WGX95FE]] at $0$.
Then there is a unique finite Borel measure $F$ on $\R$, the *spectral measure* of $X$, such that
$$r(\tau) = \int_{\R} e^{i \tau \omega} \, F(d\omega) \quad \text{for all } \tau \in \R.$$
If moreover $r$ is integrable on $\R$, then $F$ has the continuous density
$$S(\omega) = \frac{1}{2\pi} \int_{\R} r(\tau) \, e^{-i \tau \omega} \, d\tau,$$
the *power spectral density* of $X$, and $S(\omega) \ge 0$ for all $\omega$.

## Remarks

The function $r$ is positive definite: for all $\tau_1, \dots, \tau_k \in \R$ and $c_1, \dots, c_k \in \C$, $\sum_{j, l} c_j \overline{c_l} \, r(\tau_j - \tau_l) = E\bigl[\abs{\sum_j c_j (X_{\tau_j} - m)}^2\bigr] \ge 0$.
A positive definite function that is continuous at $0$ is continuous everywhere, and Bochner's theorem then gives the measure $F$.
The density formula is Fourier inversion, see the Fourier transform.

For a weakly stationary sequence $(X_n)_{n \in \Z}$, the analogue is Herglotz's theorem, with a finite measure on $[-\pi, \pi)$ and no continuity assumption.

Example: if $r(\tau) = e^{-\abs{\tau}}$, as for a suitably normalised stationary [[Ornstein–Uhlenbeck process|HZM2ASCDY4]], then $\int_{\R} e^{-\abs{\tau}} e^{-i\tau\omega} \, d\tau = \dfrac{2}{1 + \omega^2}$, so $S(\omega) = \dfrac{1}{\pi(1 + \omega^2)}$.

## Explanations

### L1 human

A stationary random signal can be analysed in two ways: by how its values at two times are correlated, or by how much of its power lies at each frequency.
The Wiener–Khinchin theorem says that these two descriptions carry the same information: the power spectrum is the Fourier transform of the autocovariance.
This is why engineers can measure the spectrum of noise from its correlations.

### L2 human

The theorem is the basis of spectral analysis of time series.
It is used to estimate the spectrum from data and to classify noise; for example, white noise has a flat spectrum.
It is also used to design filters, since a linear time-invariant filter multiplies the spectral density by the squared modulus of its transfer function.
The spectral measure also leads to the spectral representation of the process itself as a stochastic integral against a process with orthogonal increments.
