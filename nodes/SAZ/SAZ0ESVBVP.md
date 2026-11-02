---
tag: SAZ0ESVBVP
kind: statement
role: theorem
name: Lebesgue differentiation theorem
msc: [28A15, 42B25]
uses: [2Z2QVWZ262, X7GTF3D98F, RARTMA0ZEC, 0YE5868HZB, 19WRHM5NAT, VX1A56P5KQ, FCA0J1X07K]
about: [19WRHM5NAT]
sources:
  - url: https://en.wikipedia.org/wiki/Lebesgue_differentiation_theorem
same_as:
  wikidata: Q2275191
  wikipedia: Lebesgue differentiation theorem
---

## Statement

Let $n \ge 1$, let $\lambda$ be [[Lebesgue measure|2Z2QVWZ262]] on $\R^n$, and let $f \colon \R^n \to \R$ be locally [[integrable|X7GTF3D98F]], that is, integrable on every bounded measurable set.
For $x \in \R^n$ and $r > 0$, let $B(x, r)$ be the [[open ball|0YE5868HZB]] of centre $x$ and radius $r$.
Then for [[almost every|RARTMA0ZEC]] $x \in \R^n$,
$$\lim_{r \to 0^+} \frac{1}{\lambda(B(x, r))} \int_{B(x, r)} \abs{f(y) - f(x)} \, d\lambda(y) = 0.$$
In particular, $\lim_{r \to 0^+} \frac{1}{\lambda(B(x, r))} \int_{B(x, r)} f \, d\lambda = f(x)$ for almost every $x$.

## Remarks

The conclusion says that almost every point is a [[Lebesgue point|19WRHM5NAT]] of $f$.
The proof first notes that the claim is clear for continuous $f$ with compact support, which are dense in $L^1$.
The error for general $f$ is controlled by the [[Hardy–Littlewood maximal function|VX1A56P5KQ]], which satisfies the weak type bound $\lambda(\set{Mf > t}) \le 3^n \norm{f}_1 / t$.
This bound comes from the [[Vitali covering lemma|FCA0J1X07K]].

Example: for $n = 1$ and $f$ integrable on $\R$, the theorem says $F(x) = \int_0^x f$ satisfies $F'(x) = f(x)$ for almost every $x$.

The balls can be replaced by other families that shrink nicely, such as cubes containing $x$.
They cannot be replaced by arbitrary rectangles containing $x$: in dimension $n \ge 2$, for rectangles of unbounded eccentricity the conclusion can fail for some integrable $f$.

## Explanations

### L1 human

Average an integrable function over smaller and smaller balls around a point.
For almost every point, these averages tend to the value of the function at that point.
So an integrable function, however rough, is determined by its local averages.

### L2 human

The theorem is the measure-theoretic form of the fundamental theorem of calculus.
It gives Lebesgue's density theorem when $f$ is an indicator function.
It extends to Radon measures on $\R^n$ through the Besicovitch covering theorem, and to doubling metric measure spaces.
