---
tag: WXRVDVK1VA
kind: example
name: Comparing Veblen terms
msc: ["03E10", "03F15"]
topics: [XTTKZTYDSD]
audience: grad
instance_of: [JQFAE9S2F4]
uses: [6QFEVWKE25, ERTAM0SFVB, DXKWBFWCE0, 7MBX59Y7N9]
sources:
  - url: https://en.wikipedia.org/wiki/Veblen_function
    locator: Veblen hierarchy
---

## Example

Is $\varepsilon_{\varepsilon_0 + 1}$ smaller than $\zeta_0$?
The question compares $\varphi_1(\varepsilon_0 + 1)$ with $\varphi_2(0)$, and a short rule decides it.
We prove the comparison rule for the [[Veblen function|6QFEVWKE25]] and then apply it.

### The rule and its proof

Rule: $\varphi_\alpha(\beta) < \varphi_\gamma(\delta)$ holds exactly in these three cases:
(a) $\alpha = \gamma$ and $\beta < \delta$;
(b) $\alpha < \gamma$ and $\beta < \varphi_\gamma(\delta)$;
(c) $\alpha > \gamma$ and $\varphi_\alpha(\beta) < \delta$.
The same cases with $=$ in place of the last $<$ give the rule for equality.

1. Each $\varphi_\alpha$ is strictly increasing, so $\varphi_\alpha(x) < \varphi_\alpha(y)$ holds exactly when $x < y$.
2. Case $\alpha = \gamma$: step 1 gives (a).
3. Case $\alpha < \gamma$: by the definition, $\varphi_\gamma(\delta)$ is a fixed point of $\varphi_\alpha$.
   So the inequality reads $\varphi_\alpha(\beta) < \varphi_\alpha(\varphi_\gamma(\delta))$, and step 1 turns it into $\beta < \varphi_\gamma(\delta)$.
4. Case $\alpha > \gamma$: now $\varphi_\alpha(\beta)$ is a fixed point of $\varphi_\gamma$.
   So the inequality reads $\varphi_\gamma(\varphi_\alpha(\beta)) < \varphi_\gamma(\delta)$, and step 1 turns it into $\varphi_\alpha(\beta) < \delta$.

### Four comparisons

We now compare four pairs.

5. $\varphi_1(\varepsilon_0 + 1)$ and $\varphi_2(0)$: case (b), since $1 < 2$.
   We have $\varepsilon_0 + 1 < \zeta_0 = \varphi_2(0)$, so $\varepsilon_{\varepsilon_0 + 1} < \zeta_0$.
6. $\varphi_2(0)$ and $\varphi_1(\varphi_2(0) + 1)$: case (c), since $2 > 1$.
   We have $\varphi_2(0) < \varphi_2(0) + 1$, so $\zeta_0 < \varepsilon_{\zeta_0 + 1}$.
7. $\varphi_0(\varphi_1(0))$ and $\varphi_1(0)$: case (b) with equality.
   The argument $\varphi_1(0)$ equals $\varphi_1(0)$, so $\omega^{\varepsilon_0} = \varepsilon_0$.
8. $\varphi_\omega(0)$ and $\varphi_3(\varphi_\omega(0))$: case (c) with equality, since $\varphi_\omega(0) = \varphi_\omega(0)$.
   So $\varphi_3(\varphi_\omega(0)) = \varphi_\omega(0)$, a fixed point of $\varphi_3$.

## Remarks

The rule reduces a comparison of two Veblen terms to comparisons of smaller terms, so it runs as a recursive algorithm on finite terms.
Together with the [[comparison of Cantor normal forms|DXKWBFWCE0]] for sums, it gives a decidable order on terms built from $0$, $+$ and $\varphi$.
This is the [[notation system|7MBX59Y7N9]] for the ordinals below $\Gamma_0$.

To make the terms unique, one requires $\beta < \varphi_\alpha(\beta)$ in each term $\varphi_\alpha(\beta)$.
Step 7 shows why: $\varphi_0(\varepsilon_0)$ and $\varphi_1(0)$ name the same ordinal, and the condition excludes the first.

## Explanations

### L1 human

To compare two Veblen values, first compare the lower indices.
If they are equal, compare the arguments.
If one index is smaller, its function cannot move the value of the other one, and that turns the question into a smaller comparison.
For example, $\varepsilon_{\varepsilon_0 + 1}$ is still below $\zeta_0$, because $\varepsilon_0 + 1$ is below $\zeta_0$.

### L2 human

We decide whether $\varphi_1(\varphi_2(0)) < \varphi_2(1)$.
The indices satisfy $1 < 2$, so case (b) applies, and we compare $\varphi_2(0)$ with $\varphi_2(1)$.
These have the same index, so case (a) applies, and we compare $0$ with $1$.
Since $0 < 1$, we get $\varphi_2(0) < \varphi_2(1)$, and so $\varepsilon_{\zeta_0} < \zeta_1$.
Check: $\varepsilon_{\zeta_0} = \zeta_0$, since $\zeta_0$ is a fixed point of $\alpha \mapsto \varepsilon_\alpha$, and $\zeta_0 < \zeta_1$.

The typical use is to decide the order of a notation system by recursion on terms.
Watch out: comparing only the indices gives wrong answers.
The term $\varphi_1(\varphi_2(1))$ has the smaller index $1$, but it equals $\varphi_2(1)$, which has index $2$.
