---
tag: 6WSWN8Q4Y6
kind: definition
name: Lieb–Yngvason axiomatization of entropy
msc: [80A05, 80A10]
defines: RXKY51MXB6
uses: [TD4C13V3J6, W1RS8DA2H6, SPY89W0RJ7]
sources:
  - url: https://en.wikipedia.org/wiki/Entropy
---

## Definition

Consider a collection of state spaces $\Gamma$ of thermodynamic systems, closed under two operations.
For states $X \in \Gamma_1$ and $Y \in \Gamma_2$, the compound state $(X, Y)$ lies in $\Gamma_1 \times \Gamma_2$.
For $t > 0$ and $X \in \Gamma$, the scaled state $tX$ lies in a scaled copy $\Gamma^{(t)}$ of $\Gamma$.
A relation $X \prec Y$ between [[states|TD4C13V3J6]], read "$Y$ is adiabatically accessible from $X$", is given.
Write $X \sim Y$ when $X \prec Y$ and $Y \prec X$.
The Lieb–Yngvason axioms on $\prec$ are:

1. Reflexivity: $X \sim X$.
2. Transitivity: if $X \prec Y$ and $Y \prec Z$, then $X \prec Z$.
3. Consistency: if $X \prec X'$ and $Y \prec Y'$, then $(X, Y) \prec (X', Y')$.
4. Scaling invariance: if $X \prec Y$, then $tX \prec tY$ for every $t > 0$.
5. Splitting and recombination: $X \sim (tX, (1 - t)X)$ for every $0 < t < 1$.
6. Stability: if $(X, \varepsilon Z_0) \prec (Y, \varepsilon Z_1)$ for some states $Z_0, Z_1$ and a sequence of $\varepsilon > 0$ tending to $0$, then $X \prec Y$.

An *entropy function* for $\prec$ is a function $S$ on all states with real values such that:

1. Monotonicity: for $X$ and $Y$ in the same state space, $X \prec Y$ if and only if $S(X) \le S(Y)$.
2. Additivity: $S((X, Y)) = S(X) + S(Y)$.
3. Extensivity: $S(tX) = t \, S(X)$ for every $t > 0$.

## Remarks

The comparison hypothesis says that any two states $X, Y$ of the same space satisfy $X \prec Y$ or $Y \prec X$.
Lieb and Yngvason proved that the six axioms and the comparison hypothesis imply the existence of an entropy function, unique up to an affine change of scale.
Example: for a single system with a known entropy $S$, define $X \prec Y$ to mean $S(X) \le S(Y)$; then $S$ satisfies monotonicity by construction.
Non-example: in that situation $-S$ is not an entropy function, since $X \prec Y$ with $S(X) < S(Y)$ gives $-S(X) > -S(Y)$, so monotonicity fails.
The relation $\prec$ models [[adiabatic processes|W1RS8DA2H6]] in a broad sense: the only change in the surroundings is the motion of a weight.

## Explanations

### L1 human

The axioms describe which states can be turned into which without leaving any trace other than raising or lowering a weight.
An entropy function is a single number per state that decides this question: one can go from $X$ to $Y$ exactly when the entropy does not go down.
The axioms are chosen so that such a number exists, adds up over parts, and doubles when the system is doubled.
