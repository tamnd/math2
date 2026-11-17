---
tag: R9YGZQ0ZG3
kind: example
name: Small values of the Veblen function and their fundamental sequences
msc: ["03E10", "03F15"]
topics: [XTTKZTYDSD]
audience: grad
instance_of: [JQFAE9S2F4]
uses: [6QFEVWKE25, VB6YXF761M, KT50SMH3EC, PQSHBKCE7V, ERTAM0SFVB]
sources:
  - url: https://en.wikipedia.org/wiki/Veblen_function
    locator: Fundamental sequences for the Veblen hierarchy
  - url: https://en.wikipedia.org/wiki/Veblen_function
    locator: The Γ function
---

## Example

We compute some values of the [[Veblen function|6QFEVWKE25]] together with [[fundamental sequences|VB6YXF761M]] $\alpha[n]$, strictly increasing sequences with supremum $\alpha$.
We use the convention of the cited section:

- $\varphi_0(\gamma + 1)[n] = \omega^\gamma \cdot n$;
- $\varphi_{\beta+1}(0)[0] = 0$ and $\varphi_{\beta+1}(0)[n+1] = \varphi_\beta(\varphi_{\beta+1}(0)[n])$;
- $\varphi_{\beta+1}(\gamma+1)[0] = \varphi_{\beta+1}(\gamma) + 1$ and $\varphi_{\beta+1}(\gamma+1)[n+1] = \varphi_\beta(\varphi_{\beta+1}(\gamma+1)[n])$;
- $\varphi_\beta(\gamma)[n] = \varphi_\beta(\gamma[n])$ for a limit $\gamma < \varphi_\beta(\gamma)$, and $\varphi_\beta(0)[n] = \varphi_{\beta[n]}(0)$ for a limit $\beta < \varphi_\beta(0)$.

1. $\varphi_0(2) = \omega^2$, with $\omega^2[n] = \omega \cdot n$: the sequence $0, \omega, \omega \cdot 2, \ldots$ has supremum $\omega \cdot \omega = \omega^2$.
2. $\varphi_1(0) = \varepsilon_0$, with the sequence $0, \varphi_0(0) = 1, \omega^1 = \omega, \omega^\omega, \ldots$. This is the tower of [[epsilon nought|KT50SMH3EC]] after an initial $0$.
3. $\varphi_1(1) = \varepsilon_1$, with the sequence $\varepsilon_0 + 1, \omega^{\varepsilon_0 + 1}, \omega^{\omega^{\varepsilon_0 + 1}}, \ldots$.
4. $\varphi_1(\omega) = \varepsilon_\omega$, with $\varepsilon_\omega[n] = \varepsilon_n$. The supremum is $\varepsilon_\omega$, since $\varphi_1$ is continuous.
5. $\varphi_2(0) = \zeta_0$, with the sequence $0, \varphi_1(0) = \varepsilon_0, \varphi_1(\varepsilon_0) = \varepsilon_{\varepsilon_0}, \varepsilon_{\varepsilon_{\varepsilon_0}}, \ldots$.
6. $\varphi_\omega(0)$, with $\varphi_\omega(0)[n] = \varphi_n(0)$: the sequence $1, \varepsilon_0, \zeta_0, \eta_0, \ldots$.
7. $\Gamma_0$, the [[Feferman-Schütte ordinal|CNN7BK5YAW]], with $\Gamma_0[0] = 0$ and $\Gamma_0[n+1] = \varphi_{\Gamma_0[n]}(0)$: the sequence $0, 1, \varepsilon_0, \varphi_{\varepsilon_0}(0), \ldots$.

Check of step 6.
For each $m$ and each $n > m$, $\varphi_n(0)$ is a fixed point of $\varphi_m$, by clause 2 or 3 of the definition.
So $\varphi_m(\sup_n \varphi_n(0)) = \sup_{n > m} \varphi_m(\varphi_n(0)) = \sup_n \varphi_n(0)$, by continuity of $\varphi_m$.
So the supremum is a common fixed point of all $\varphi_m$, and every common fixed point is at least each $\varphi_n(0)$.
Hence $\sup_n \varphi_n(0) = \varphi_\omega(0)$.

## Remarks

The convention matters.
Other books use $\varepsilon_0[0] = \omega$, or $\omega^{\gamma+1}[n] = \omega^\gamma \cdot (n + 1)$, and then $\alpha[n]$ changes for small $n$.
The limits do not change, but functions defined from the sequences, such as the fast-growing hierarchy, do change their values.
Ordinals $\alpha$ with $\alpha = \varphi_\alpha(0)$, such as $\Gamma_0$, get no sequence from these rules; the rule in step 7 is an extra choice.

## Explanations

### L1 human

A fundamental sequence is a list of smaller ordinals that climbs up to a given limit ordinal.
For $\omega^2$ the list is $0, \omega, \omega \cdot 2, \omega \cdot 3, \ldots$.
For $\varepsilon_0$ it is $0, 1, \omega, \omega^\omega, \ldots$, the tower of powers.
For the larger values of the Veblen function, each list is built by applying the previous function again and again.

### L2 human

We compute $\zeta_0[3]$ in the convention above.

1. $\zeta_0 = \varphi_2(0)$, so $\zeta_0[0] = 0$ and $\zeta_0[n+1] = \varphi_1(\zeta_0[n])$.
2. $\zeta_0[1] = \varphi_1(0) = \varepsilon_0$.
3. $\zeta_0[2] = \varphi_1(\varepsilon_0) = \varepsilon_{\varepsilon_0}$.
4. $\zeta_0[3] = \varphi_1(\varepsilon_{\varepsilon_0}) = \varepsilon_{\varepsilon_{\varepsilon_0}}$.

The typical use is to define the fast-growing hierarchy $f_\alpha$ beyond $\varepsilon_0$, by $f_\lambda(n) = f_{\lambda[n]}(n)$.
The trap: $\zeta_0[1] = \varepsilon_0$ is a limit ordinal, so a fundamental sequence can jump far at one step.
