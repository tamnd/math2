---
tag: 2MY5GMPJP5
kind: example
name: Buchholz's psi zero is not a normal function
msc: ["03F15", "03E10"]
topics: [XTTKZTYDSD]
audience: research
not_instance_of:
  - target: ERTAM0SFVB
    note: psi zero is not strictly increasing, since it takes the value epsilon zero at epsilon zero and at Omega
uses: [E7WEFRMQTB, TZHC9KJBWF, ERTAM0SFVB]
sources:
  - url: https://en.wikipedia.org/wiki/Buchholz_psi_functions
    locator: Explanation
---

## Example

A [[normal function|ERTAM0SFVB]] is a function $f$ on ordinals that is strictly increasing and continuous, which means $f(\lambda) = \sup_{\xi < \lambda} f(\xi)$ for every limit ordinal $\lambda$.
We show that [[Buchholz's function|E7WEFRMQTB]] $\psi_0$ is not a normal function, because it is not strictly increasing.

1. By the [[small values|TZHC9KJBWF]], $\psi_0(\varepsilon_0) = \omega^{\varepsilon_0} = \varepsilon_0$.
2. By the same computation, $\psi_0(\Omega) = \varepsilon_0$.
3. We have $\varepsilon_0 < \Omega$, because $\varepsilon_0$ is countable and $\Omega$ is the first uncountable ordinal.
4. So $\psi_0(\varepsilon_0) = \psi_0(\Omega)$ although $\varepsilon_0 < \Omega$.
5. The failure already shows at the next argument: $\psi_0(\varepsilon_0 + 1) = \varepsilon_0 = \psi_0(\varepsilon_0)$, while a strictly increasing $f$ has $f(\alpha + 1) > f(\alpha)$.

## Remarks

The function $\psi_0$ is weakly increasing, and it is continuous at many limits, for example
$$\psi_0(\omega) = \omega^\omega = \sup_n \omega^n = \sup_n \psi_0(n).$$
Restricted to the arguments $\alpha \le \varepsilon_0$ it is the normal function $\alpha \mapsto \omega^\alpha$.
So the failure starts exactly where the arguments can no longer be named inside the closure set.
On the arguments $\alpha$ with $\alpha \in C_0(\alpha)$, which are the ones used in notations, $\psi_0$ is strictly increasing again.

The same failure occurs for every [[collapsing function|8S6CT4TMB7]] with countable values.
A strictly increasing function on the ordinals up to $\Omega$ would need $\Omega + 1$ distinct values, and there is no room for them below $\Omega$.

## Explanations

### L1 human

A normal function always goes up when its input goes up, and it has no jumps at limits.
Buchholz's function $\psi_0$ goes up at first, giving $1$, $\omega$, $\omega^2$, and so on.
But between $\varepsilon_0$ and the huge ordinal $\Omega$ it stays at the same value $\varepsilon_0$.
So it does not always go up, and it is not a normal function.

### L2 human

Where does strict monotonicity fail first?
For $\alpha < \varepsilon_0$ we have $\psi_0(\alpha) = \omega^\alpha$, which is strictly increasing, and $\psi_0(\varepsilon_0) = \varepsilon_0$ is above all of these values.
At $\alpha = \varepsilon_0 + 1$ we get $\varepsilon_0$ again, so the first failure is the pair $\varepsilon_0 < \varepsilon_0 + 1$.

The fact matters when you compare terms.
You may conclude $\psi_0(\alpha) < \psi_0(\beta)$ from $\alpha < \beta$ only when both arguments are in normal form.
Watch out for arguments such as $\varepsilon_0 + 1$, which is not in $C_0(\varepsilon_0 + 1)$, so the rule does not apply to it.
