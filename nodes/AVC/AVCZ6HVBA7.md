---
tag: AVCZ6HVBA7
kind: statement
role: theorem
name: Lüroth's theorem
msc: [12F20]
uses: [0QA8CHH8MG, 4V81611P9N, 0WCZH4AFMT, G5PVJMM37Z, 0GS74FGFEK]
about: [G5PVJMM37Z, 12JQCGTQ8W]
sources:
  - url: https://en.wikipedia.org/wiki/L%C3%BCroth%27s_theorem
same_as:
  wikidata: Q3527115
  wikipedia: Lüroth's theorem
---

## Statement

Let $K$ be a [[field|0QA8CHH8MG]] and let $K(t)$ be the [[field of rational functions|4V81611P9N]] in one variable $t$ over $K$.
Let $E$ be a field with $K \subsetneq E \subseteq K(t)$.
Then $E = K(u)$ for some [[rational function|0WCZH4AFMT]] $u \in K(t) \setminus K$.

## Remarks

Pick $u \in E \setminus K$ and write $u = f(t)/g(t)$ with $f, g$ coprime polynomials.
Then $t$ is a root of $f(x) - u\, g(x)$ over $K(u)$, and one shows that $[K(t) : K(u)] = \max(\deg f, \deg g)$.
The proof then takes the minimal polynomial of $t$ over $E$, chooses $u$ among its coefficients not in $K$, and compares degrees to get $E = K(u)$.
Example: $E = K(t^2 + t^{-2})$ lies between $K$ and $K(t)$, and the theorem says it is already of the form $K(u)$; here $u = t^2 + t^{-2}$ works, and $[K(t) : E] = 4$.
The analogue in two variables concerns fields $E \subseteq K(x, y)$ with $K(x, y)$ finite over $E$.
It holds over algebraically closed fields of characteristic $0$ by Castelnuovo's theorem, and it fails in general in three or more variables.

## Explanations

### L1 human

Every field between $K$ and the rational functions in one variable is again a field of rational functions in one variable.
So one cannot find an exotic field squeezed in there.
Geometrically, a curve that is the image of the line under a rational map is itself rational.

### L2 human

The theorem says that a subfield of a [[purely transcendental extension|G5PVJMM37Z]] of transcendence degree $1$ is purely transcendental.
In geometry, it gives that a unirational curve is rational.
The degree formula $[K(t) : K(u)] = \max(\deg f, \deg g)$ also computes the degree of a rational map from the line to itself, which is the [[degree|0GS74FGFEK]] of the field extension $K(t)/K(u)$.
