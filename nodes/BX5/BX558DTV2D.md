---
tag: BX558DTV2D
kind: statement
role: theorem
name: Gross–Zagier theorem
msc: [11G05, 11G40, 11G50]
uses: [427N6S6QQW, 2230ZKE4W9, 7SV4WA92SM, F1FF505PWH, CS1NVJBZMH, WWCJ7CR2R3]
about: [2230ZKE4W9, 427N6S6QQW]
sources:
  - url: https://en.wikipedia.org/wiki/Heegner_point
---

## Statement

Let $E$ be an [[elliptic curve|427N6S6QQW]] over $\Q$ of conductor $N$, with modular parametrisation $\varphi \colon X_0(N) \to E$ given by the [[modularity theorem|CS1NVJBZMH]].
Let $K$ be an imaginary [[quadratic field|7SV4WA92SM]] of discriminant $D$ such that every prime dividing $N$ splits in $K$.
Let $x$ be a [[Heegner point|2230ZKE4W9]] for $K$; it is defined over the [[Hilbert class field|WWCJ7CR2R3]] $H$ of $K$.
Let $y_K \in E(K)$ be the trace of $\varphi(x)$ from $H$ to $K$.
Let $L(E/K, s) = L(E, s) \, L(E^D, s)$, where $E^D$ is the quadratic twist of $E$ by $K$, and let $\hat{h}$ be the Néron–Tate canonical [[height|F1FF505PWH]] on $E(K)$.
Then $L(E/K, 1) = 0$, and there is a real constant $c > 0$, depending on $E$ and $K$ and given explicitly by periods and other invariants, such that
$$L'(E/K, 1) = c \cdot \hat{h}(y_K).$$

## Remarks

In particular, $y_K$ has infinite order if and only if $L'(E/K, 1) \ne 0$, since $\hat{h}$ vanishes exactly on torsion points.
The Heegner hypothesis forces the sign of the functional equation of $L(E/K, s)$ to be $-1$, which gives $L(E/K, 1) = 0$.
The proof computes both sides.
The derivative is computed by the Rankin–Selberg method, and the height by local intersection theory of Heegner points on $X_0(N)$.
Gross and Zagier then compare the two as Fourier coefficients of modular forms.
Gross and Zagier proved it in 1986, with some additional conditions on $D$ that later work removed.
Kolyvagin's Euler system argument adds the following consequence.
If $L(E, s)$ has a zero of order at most $1$ at $s = 1$, then the rank of $E(\Q)$ equals that order and the [[Tate–Shafarevich group|BK9WBMF56G]] of $E$ is finite.

## Explanations

### L1 human

The theorem gives an exact formula linking two very different numbers.
One is the slope of the $L$-function of $E$ at the central point, an analytic quantity.
The other is the height of a specific point built from complex multiplication, which measures how complicated the point's coordinates are.
So a nonzero slope guarantees an explicit point of infinite order.

### L2 human

This is the strongest known evidence for the [[Birch and Swinnerton-Dyer conjecture|ZWEFBG40H9]], covering analytic rank $0$ and $1$.
Gross and Zagier also used it, with Goldfeld's earlier work, to give an effective lower bound for class numbers of imaginary quadratic fields.
Generalisations to Shimura curves and higher-dimensional settings are an active area.
