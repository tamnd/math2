---
tag: QWXD1Z9V8F
kind: statement
role: proposition
name: Solvability of x^n - a
msc: [12F10]
uses: [0JZY3R908H, 0P3KZK0FTV, 0J817RTVG6, 1ZB13N78XW, VFE5B71E7Y, VD6VC3ZMMY]
about: [0JZY3R908H, 0P3KZK0FTV]
sources:
  - url: https://en.wikipedia.org/wiki/Solution_in_radicals
---

## Statement

Let $K$ be a field, let $n \ge 1$ be an integer that is not divisible by the [[characteristic|1ZB13N78XW]] of $K$, and let $a \in K$.
Then the [[Galois group|0JZY3R908H]] of $x^n - a$ over $K$ is a [[solvable group|0P3KZK0FTV]].

## Remarks

If $a = 0$, the polynomial $x^n$ splits over $K$ and the group is trivial.
If $a \ne 0$, let $L$ be a splitting field and $\beta \in L$ a root; the roots are $\beta \zeta^k$, where $\zeta$ is a [[primitive $n$-th root of unity|0J817RTVG6]], so $\zeta \in L$.
Put $E = K(\zeta)$; $E/K$ is a [[cyclotomic extension|VD6VC3ZMMY]], and $\Gal(E/K)$ embeds in $(\Z/n\Z)^\times$, so it is abelian.
The map $\sigma \mapsto \sigma(\beta)/\beta$ embeds $\Gal(L/E)$ in the cyclic group of $n$-th roots of unity, so $L/E$ is a [[cyclic extension|VFE5B71E7Y]].
Then $\Gal(L/E)$ is a normal subgroup of $\Gal(L/K)$ with abelian quotient $\Gal(E/K)$, so $\Gal(L/K)$ is solvable.
Example: for $x^3 - 2$ over $\Q$, the subgroup is cyclic of order $3$ and the quotient has order $2$, giving $S_3$.

## Explanations

### L1 human

The equation $x^n = a$ is the simplest equation that needs an $n$-th root.
Its roots are one $n$-th root of $a$ times the $n$-th roots of unity.
The proposition says that its Galois group is solvable, as it should be, since its roots are written with radicals.

### L2 human

This is the base case of the easy direction of [[Galois' theorem on solvability|VHCWCFA3MX]].
The two-step tower $K \subseteq K(\zeta) \subseteq L$ is the model for every radical extension: first roots of unity, then pure roots.
The same argument shows that $\Gal(L/K)$ embeds in the group of maps $x \mapsto ux + v$ on $\Z/n\Z$ with $u$ a unit.
