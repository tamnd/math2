---
tag: VSZR2CY2RS
kind: definition
name: Sine and cosine addition equations
msc: [39B22, 39B72]
defines: C73TGW752D
uses: [SRAN4EKWS0, 0EPAT51DXQ]
sources:
  - url: https://en.wikipedia.org/wiki/List_of_trigonometric_identities
---

## Definition

The *sine and cosine addition equations* are the system of [[functional equations|SRAN4EKWS0]]
$$S(x + y) = S(x) C(y) + C(x) S(y), \qquad C(x + y) = C(x) C(y) - S(x) S(y) \quad \text{for all } x, y \in \R,$$
for two unknown [[functions|0EPAT51DXQ]] $S, C \colon \R \to \R$.
The first equation is the *sine addition equation* and the second is the *cosine addition equation*.
A solution is a pair $(S, C)$ that satisfies both identities for all real $x$ and $y$.

## Remarks

Example: $S = \sin$ and $C = \cos$ form a solution, by the angle addition formulas of [[sine and cosine|08WFZP6P89]].
Non-example: $S(x) = x$, $C(x) = 1$ is not a solution, since the cosine equation gives $1 = 1 - xy$, which fails for $x = y = 1$.
Set $E = C + iS \colon \R \to \C$.
The two equations together say exactly that $E(x + y) = E(x) E(y)$.
So the continuous solutions are $S = C = 0$ and $S(x) = e^{bx} \sin(ax)$, $C(x) = e^{bx} \cos(ax)$ with $a, b \in \R$.
Each of the two equations is also studied alone, with one or both functions unknown.
