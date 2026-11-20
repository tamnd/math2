---
tag: 4W5HFEXSKT
kind: example
name: An ultrapower of the real field contains infinitesimals
msc: ["03C20", "03H05", "26E35"]
topics: [HZG1YP26AB]
audience: grad
instance_of: [5ZVJK0V0GF]
uses: [5ZVJK0V0GF, E4TD8X2ZRX, 08J2M1JYAG, 0P3VCBDEE2, 0XH79S06J3, 421QMTFG9T]
sources:
  - url: https://en.wikipedia.org/wiki/Hyperreal_number
    locator: Ultrapower construction
  - url: https://en.wikipedia.org/wiki/Ultraproduct
    locator: Examples
---

## Example

Let $\mathcal{R} = (\R, +, \cdot, 0, 1, <)$ be the ordered field of [[real numbers|08J2M1JYAG]], and let $\mathcal{U}$ be a nonprincipal ultrafilter on $\N$.
Let ${}^*\R = \mathcal{R}^{\N} / \mathcal{U}$, with diagonal embedding $d$.
We check that ${}^*\R$ is an [[ordered field|0P3VCBDEE2]] with a positive element below every positive real.

1. The axioms of ordered fields are first-order and hold in $\R$. By the theorem that the [[diagonal embedding is elementary|E4TD8X2ZRX]], they hold in ${}^*\R$.
2. Let $\varepsilon = [(1, 1/2, 1/3, \dots)]$, the class of $i \mapsto 1/(i + 1)$. Its truth set for $x > 0$ is $\N$, so $\varepsilon > 0$.
3. Let $r > 0$ be real. The set $\set{i : 1/(i + 1) < r}$ contains every $i > 1/r$, so it is cofinite and lies in $\mathcal{U}$.
4. So $\varepsilon < d(r)$ for every real $r > 0$.

So $\varepsilon$ is a positive infinitesimal, and ${}^*\R$ is a non-Archimedean field: $n \varepsilon < d(1)$ for every $n \in \N$.

## Remarks

The field ${}^*\R$ is a field of [[hyperreal numbers|421QMTFG9T]].
It shows that the [[Archimedean property|0XH79S06J3]] is not first-order: it holds in $\R$ and fails in the elementary extension ${}^*\R$.
The element $1/\varepsilon = [i \mapsto i + 1]$ is infinite, larger than every $d(r)$.
Completeness also fails: the set $d(\R)$ is bounded above by $1/\varepsilon$ and has no least upper bound in ${}^*\R$.
If $\mathcal{U}$ is replaced by the Fréchet filter, the reduced power is not even a field.
Each element bounded by some $d(r)$ is infinitely close to a unique real, its standard part; this uses the completeness of $\R$, not Łoś's theorem.

## Explanations

### L1 human

We build new numbers as infinite lists of real numbers.
The list $1, 1/2, 1/3, \dots$ is positive, but it is smaller than $0.001$ at all but finitely many positions.
So it becomes a positive number smaller than every positive real number, an "infinitely small" number.
Every algebraic rule of the real numbers, such as $x \cdot y = y \cdot x$, still holds.

### L2 human

We check that $\varepsilon^2 < \varepsilon$ and that $\varepsilon^2$ is again infinitesimal.

1. $\varepsilon^2 = [i \mapsto 1/(i + 1)^2]$, by the coordinatewise definition of multiplication.
2. For $i \ge 1$, $1/(i + 1)^2 < 1/(i + 1)$. This holds on a cofinite set, so $\varepsilon^2 < \varepsilon$.
3. For real $r > 0$, $\varepsilon^2 < \varepsilon < d(r)$, so $\varepsilon^2$ is infinitesimal.
4. $\varepsilon^2 / \varepsilon = \varepsilon$ is infinitesimal too, so $\varepsilon^2$ is infinitely smaller than $\varepsilon$.

The typical use is to model "infinitely small" quantities of analysis and to prove facts about $\R$ by the transfer principle.
The trap is to apply transfer to statements about all subsets of $\R$, such as completeness, which are not first-order.
