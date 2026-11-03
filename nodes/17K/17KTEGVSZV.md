---
tag: 17KTEGVSZV
kind: statement
role: theorem
name: Bott–Duffin synthesis
msc: [94C05, 30C10]
uses: [6AX5E50CZY, 0XDK9CGYKJ]
about: [6AX5E50CZY]
sources:
  - url: https://en.wikipedia.org/wiki/Network_synthesis
---

## Statement

Let $Z(s)$ be a [[rational function|0XDK9CGYKJ]] with real coefficients that is positive real, that is, $\operatorname{Re} Z(s) \ge 0$ whenever $\operatorname{Re} s > 0$ and $s$ is not a pole.
Then there is a finite one-port network made only of resistors, inductors and capacitors with positive values, without transformers, whose driving-point impedance is $Z$.

## Remarks

The impedance of any passive network of these elements is positive real.
So positive-real functions are exactly the impedances of transformerless networks of resistors, inductors and capacitors.
Brune's earlier procedure of [[network synthesis|6AX5E50CZY]] realizes every positive-real function, but it needs ideal transformers or coupled coils at one step.
Raoul Bott and Richard Duffin replaced that step by a construction based on Richards' theorem, which produces new positive-real functions from a given one.
The price is size: the number of elements in the Bott–Duffin network grows very quickly with the degree of $Z$.
For example, $Z(s) = 1 + 1/s$ is positive real and is realized by a $1$ ohm resistor in series with a $1$ farad capacitor.
Without the positive-real hypothesis no passive network exists, since every passive impedance is positive real.

## Explanations

### L1 human

Engineers want to build a circuit with a given impedance from the three basic parts: resistors, coils and capacitors.
Earlier methods also needed transformers, which are bulky and imperfect.
The Bott–Duffin theorem says that transformers are never needed: whenever a passive circuit with the impedance exists, one exists without transformers.

### L2 human

The theorem completes the characterization of driving-point impedances begun by Brune.
Its realizations are far from economical, and finding the smallest transformerless realization of a given positive-real function remains a hard question.
The theorem has found new use in mechanical engineering, where the inerter makes mechanical networks of springs, dampers and inerters analogous to electrical networks.
