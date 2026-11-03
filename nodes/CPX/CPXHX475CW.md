---
tag: CPXHX475CW
kind: statement
role: theorem
name: Foster's reactance theorem
msc: [94C05, 30C10]
uses: [0XDK9CGYKJ, 0V49JEZW06]
about: [0XDK9CGYKJ]
sources:
  - url: https://en.wikipedia.org/wiki/Foster%27s_reactance_theorem
same_as:
  wikidata: Q5473574
  wikipedia: Foster's reactance theorem
---

## Statement

Let $N$ be a one-port network made of finitely many inductors and capacitors with positive values, and no resistors or sources.
Let $Z(s)$ be its driving-point impedance as a function of the complex frequency $s$ of the [[Laplace transform|0V49JEZW06]].
Assume that $Z$ is a [[rational function|0XDK9CGYKJ]] that is not identically zero.
Then $Z$ has the form
$$Z(s) = k_\infty s + \frac{k_0}{s} + \sum_{j=1}^{m} \frac{2 k_j s}{s^2 + \omega_j^2},$$
with $m \ge 0$, real numbers $k_\infty \ge 0$ and $k_0 \ge 0$, real numbers $k_j > 0$, and distinct real numbers $\omega_j > 0$.
Consequently:

1. $Z$ is odd, $Z(-s) = -Z(s)$, and has real coefficients.
2. All poles and zeros of $Z$, including those at $0$ and $\infty$, are simple and lie on the imaginary axis.
   The residues at the poles are positive.
3. The reactance $X(\omega) = Z(i\omega)/i$ is real, and $X'(\omega) > 0$ at every $\omega \in \R$ that is not a pole.
   So the poles and zeros of $X$ on $(0, \infty)$ alternate.

## Remarks

The proof uses that a lossless network absorbs no average power, so $\operatorname{Re} Z(i\omega) = 0$, while passivity gives $\operatorname{Re} Z(s) \ge 0$ for $\operatorname{Re} s > 0$.
A rational function with both properties has only simple imaginary poles with positive residues, which gives the partial fraction form.
Differentiating $X(\omega) = k_\infty \omega - k_0/\omega + \sum_j 2 k_j \omega / (\omega_j^2 - \omega^2)$ term by term gives a sum of non-negative terms, not all zero.
Foster also proved the converse: every function of this form is the impedance of such a network.
Take an inductor $k_\infty$, a capacitor $1/k_0$ and, for each $j$, a capacitor $1/(2k_j)$ in parallel with an inductor $2k_j/\omega_j^2$.
Connect them all in series, and leave out the terms with zero coefficient.
Example: an inductor $L$ in parallel with a capacitor $C$ has $Z(s) = (s/C)/(s^2 + 1/(LC))$, with a pole at $\omega = 1/\sqrt{LC}$ and zeros at $0$ and $\infty$.
With a resistor the conclusion fails: $Z(s) = R + Ls$ is not odd and $X(\omega) = \omega L$ misses the real part.

## Explanations

### L1 human

A circuit of coils and capacitors only does not waste energy.
Foster's theorem says that its reactance always increases with frequency, jumping from $+\infty$ to $-\infty$ at each resonance.
So the frequencies where the circuit blocks current and where it passes current freely must take turns.

### L2 human

The theorem characterizes the impedances of lossless one-ports, and the partial fraction form is Foster's canonical realization.
It is a first result of [[network synthesis|6AX5E50CZY]]: the realizable lossless impedances are exactly the functions of this form.
Cauer's continued fraction expansions give other realizations of the same functions as ladder networks.
