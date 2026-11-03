---
tag: D39SGDWGAD
kind: statement
role: theorem
name: Heisenberg uncertainty principle
msc: ["81S07", "42A38"]
uses: [7XAKGQQWTP, 5WG6YTAA6J, JNK7GJ3AKE, E9WK6KJ4SM, EQBC3P901V, V41B4WX21N, HKP9E7N7AB]
about: [7XAKGQQWTP, 5WG6YTAA6J]
sources:
  - url: https://en.wikipedia.org/wiki/Uncertainty_principle
---

## Statement

Let $\hbar > 0$, and let $X$ and $P$ be the [[position operator|7XAKGQQWTP]] and the [[momentum operator|5WG6YTAA6J]] on $L^2(\R)$.
Let $\psi \in D(X) \cap D(P)$ be a [[wave function|E9WK6KJ4SM]], so $\norm{\psi} = 1$.
For $A \in \set{X, P}$, let $\langle A \rangle = \ip{\psi}{A\psi}$ be the [[expectation value|JNK7GJ3AKE]] and $\sigma_A = \norm{(A - \langle A \rangle)\psi}$ the standard deviation.
Then
$$\sigma_X \sigma_P \ge \frac{\hbar}{2}.$$
Equality holds if and only if $\psi(x) = C e^{ibx/\hbar} e^{-c(x - a)^2}$ for some $a, b \in \R$, $c > 0$ and $C \in \C$.

## Remarks

The statement is the [[Heisenberg inequality for the Fourier transform|EQBC3P901V]] in physical units.
With the transform $\hat\psi(\xi) = \int \psi(x) e^{-2\pi i x\xi}\, dx$, momentum acts as multiplication by $2\pi\hbar\xi$, so $\sigma_P^2 = (2\pi\hbar)^2 \int (\xi - b')^2 \abs{\hat\psi(\xi)}^2 \, d\xi$ with $b' = \langle P \rangle/(2\pi\hbar)$.
The Fourier inequality gives $\sigma_X^2 \sigma_P^2 \ge (2\pi\hbar)^2/(16\pi^2) = \hbar^2/4$.
For $\psi$ in the Schwartz space, it also follows from the [[canonical commutation relation|HKP9E7N7AB]] and the [[Robertson inequality|V41B4WX21N]]: $\sigma_X\sigma_P \ge \frac12 \abs{\ip{\psi}{i\hbar\psi}} = \frac{\hbar}{2}$.

Example: for $\psi(x) = \pi^{-1/4} e^{-x^2/2}$, $\abs{\psi}^2$ is normal with variance $\frac12$, so $\sigma_X = 1/\sqrt{2}$.
Also $P\psi = i\hbar x\psi$, so $\sigma_P^2 = \hbar^2 \int x^2 \abs{\psi}^2 = \hbar^2/2$.
Hence $\sigma_X\sigma_P = \hbar/2$, the case of equality.

The inequality in this form was proved by E. H. Kennard in 1927, after Heisenberg's heuristic argument of the same year.

## Explanations

### L1 human

A quantum particle cannot have both a sharp position and a sharp momentum.
The more narrowly its position is spread, the more widely its momentum is spread, and the product of the two spreads is at least $\hbar/2$.
This is not a defect of measuring instruments: it is a property of the wave function itself.

### L2 human

The principle is a Fourier-analytic fact: momentum is position seen through the Fourier transform, and a function and its transform cannot both be concentrated.
Gaussian wave packets, the coherent states, are the minimisers.
The Robertson inequality extends it to any two observables, with the commutator in place of $i\hbar$.
Other measures of spread give other versions, such as the entropic uncertainty principle, which is stronger.
