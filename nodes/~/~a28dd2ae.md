---
tag: ~a28dd2ae
kind: example
name: The Nixon diamond
aliases: [nixon-diamond]
msc: ["68T27", "03B60"]
topics: [NJB94B39QK]
audience: ug2
instance_of: [~1470d90b]
uses: [~1470d90b, ~db35e89c]
sources:
  - url: https://plato.stanford.edu/entries/logic-nonmonotonic/
    locator: Non-monotonic Logic (SEP entry), sections 3.4 and 3.6.3
  - url: https://en.wikipedia.org/wiki/Default_logic
    locator: section Semantics of default logic
---

## Example

Nixon was a Quaker and a Republican; Quakers are usually pacifists, and Republicans usually are not.
We show that the [[default theory|~1470d90b]] for this has exactly two [[extensions|~db35e89c]].
Use the atoms $q$ (Quaker), $r$ (Republican) and $p$ (pacifist).
Let $T = (W, D)$ with $W = \set{q, r}$ and $D = \set{d_1, d_2}$, where $d_1 = (q : p)/p$ and $d_2 = (r : \neg p)/\neg p$.

The candidates $E_1 = \mathrm{Cn}(\set{q, r, p})$ and $E_2 = \mathrm{Cn}(\set{q, r, \neg p})$.

1. $E_1$ is consistent and contains $p$, so $\neg p \notin E_1$ and $\neg\neg p \in E_1$.
2. So $d_1$ is not blocked by $E_1$, and $d_2$ is blocked.
3. The smallest deductively closed set that contains $W$ and is closed under $d_1$ is $\mathrm{Cn}(\set{q, r, p})$. So $\Gamma_T(E_1) = E_1$.
4. In the same way, $d_2$ is not blocked by $E_2$, $d_1$ is blocked, and $\Gamma_T(E_2) = E_2$.

No other extension: let $E$ be an extension; it is deductively closed, so $\neg\neg p \in E$ if and only if $p \in E$.

5. If neither default is blocked, then $\Gamma_T(E)$ contains $p$ and $\neg p$. So $E$ is inconsistent and contains $\neg p$, which blocks $d_1$. Contradiction.
6. If both defaults are blocked, then $\Gamma_T(E) = \mathrm{Cn}(\set{q, r})$, which contains neither $p$ nor $\neg p$. So it blocks neither default. Contradiction.
7. If only $d_2$ is blocked, then $E = \Gamma_T(E) = E_1$. If only $d_1$ is blocked, then $E = E_2$.

Consequences.

8. $p \notin E_2$ and $\neg p \notin E_1$, so neither $p$ nor $\neg p$ is a skeptical consequence of $T$.
9. Both $p$ and $\neg p$ are credulous consequences, so the set of credulous consequences is inconsistent.

## Remarks

The skeptical reader stays agnostic about Nixon's pacifism, and the credulous reader can choose either side.
Priorities between defaults, as in the work of Horty, can select one of the two extensions.
The same knowledge, written as conditional assertions, is a standard test case for preferential and rational consequence.

## Explanations

### L1 human

One rule of thumb says that Nixon is a pacifist, and another says that he is not.
Both rules apply, but we cannot use both at once.
So there are two reasonable pictures of the world, one for each rule.

### L2 human

Each extension applies one default and is blocked from applying the other.
The case analysis on the blocked defaults shows that there is no third possibility.
A trap is to take the union of the two extensions as the conclusions; it contains both $p$ and $\neg p$.
