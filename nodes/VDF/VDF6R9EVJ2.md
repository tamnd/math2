---
tag: VDF6R9EVJ2
kind: object
name: Slow-growing hierarchy
msc: ["03D20", "03F15"]
topics: [T6FK1E7GJ1]
audience: grad
uses: [R6ZC4BJGXV, 6GD30FGYDZ, KT50SMH3EC, 0ZHQMQ2C1N]
sources:
  - url: https://en.wikipedia.org/wiki/Slow-growing_hierarchy
    locator: Definition
  - url: https://en.wikipedia.org/wiki/Slow-growing_hierarchy
    locator: Example
  - url: https://en.wikipedia.org/wiki/Slow-growing_hierarchy
    locator: Relation to fast-growing hierarchy
---

## Description

The slow-growing hierarchy reads an ordinal as a formula and evaluates it at a number: in effect it replaces every $\omega$ by $x$.
It shows how much of the growth in the other hierarchies comes from iteration, and how little comes from the ordinal notation alone.

Here is a first value.
Take $\alpha = \omega^2 + 3$ and $x = 5$.
Replace $\omega$ by $5$:
$$g_{\omega^2 + 3}(5) = 5^2 + 3 = 28.$$
For comparison, the Hardy function at the same ordinal gives $H_{\omega^2 + 3}(5) = H_{\omega^2}(8) = 2048$.

**The definition.**
The slow-growing hierarchy is a family of functions $g_\alpha : \mathbb{N} \to \mathbb{N}$, one for each ordinal $\alpha$ up to a fixed countable ordinal.
At and below $\varepsilon_0$ it uses the standard fundamental sequences $\lambda[x]$ of the [[fast-growing hierarchy|R6ZC4BJGXV]], with $\varepsilon_0[0] = 0$.
$$g_0(x) = 0, \qquad g_{\alpha + 1}(x) = g_\alpha(x) + 1, \qquad g_\lambda(x) = g_{\lambda[x]}(x) \text{ for a limit } \lambda.$$
So $g_\alpha(x)$ counts the successor steps in the descent from $\alpha$ to $0$, where each limit $\lambda$ is replaced by $\lambda[x]$.

## Remarks

### First values

Write $x \uparrow\uparrow 0 = 1$ and $x \uparrow\uparrow (k+1) = x^{x \uparrow\uparrow k}$, with $0^0 = 1$.
For a finite $n$ we get $g_n(x) = n$, and the first limit gives $g_\omega(x) = g_x(x) = x$.
In the same way $g_{\omega + m}(x) = x + m$ and $g_{\omega \cdot m}(x) = m x$.
One level higher,
$$g_{\omega^2}(x) = g_{\omega \cdot x}(x) = x \cdot x = x^2, \qquad g_{\omega^\omega}(x) = g_{\omega^x}(x) = x^x.$$
So $g_{\omega^\omega}(0), \dots, g_{\omega^\omega}(4)$ are $1, 1, 4, 27, 256$.
At the top, $g_{\varepsilon_0}(0) = g_0(0) = 0$, $g_{\varepsilon_0}(1) = g_1(1) = 1$, $g_{\varepsilon_0}(2) = g_\omega(2) = 2$ and $g_{\varepsilon_0}(3) = g_{\omega^\omega}(3) = 27$.

### The substitution rule

**Lemma.** For $\alpha < \varepsilon_0$, $g_\alpha(x)$ is the number that we get from the [[Cantor normal form|6GD30FGYDZ]] of $\alpha$ when we replace every $\omega$ by $x$.

We prove it by [[transfinite induction|0ZHQMQ2C1N]], in two parts.

1. First, $g_{\gamma + \delta} = g_\gamma + g_\delta$ when the last exponent of $\gamma$ is at least the first exponent of $\delta$.
   We use induction on $\delta$.
2. For $\delta = 0$ both sides equal $g_\gamma$, and for $\delta = \delta' + 1$ the claim follows from $g_{\gamma + \delta' + 1} = g_{\gamma + \delta'} + 1$.
3. For a limit $\delta$ we have $(\gamma + \delta)[x] = \gamma + \delta[x]$, as in the composition law of the [[Hardy hierarchy|X8RKXQASR9]], and the induction hypothesis for $\delta[x]$ gives the claim.
4. Second, $g_{\omega^\alpha}(x) = x^{g_\alpha(x)}$, by induction on $\alpha$.
   For $\alpha = 0$: $g_1(x) = 1 = x^0$.
5. For $\alpha = \beta + 1$: $g_{\omega^{\beta+1}}(x) = g_{\omega^\beta \cdot x}(x) = x \cdot g_{\omega^\beta}(x) = x \cdot x^{g_\beta(x)} = x^{g_\alpha(x)}$, by step 1.
6. For a limit $\alpha$: $g_{\omega^\alpha}(x) = g_{\omega^{\alpha[x]}}(x) = x^{g_{\alpha[x]}(x)} = x^{g_\alpha(x)}$.
7. Steps 1 and 4 together turn the normal form $\omega^{\alpha_1} + \cdots + \omega^{\alpha_k}$ into $x^{g_{\alpha_1}(x)} + \cdots + x^{g_{\alpha_k}(x)}$, which is the substitution.

For $x \ge 1$, $\varepsilon_0[x]$ is a tower of $x - 1$ copies of $\omega$, so the rule gives $g_{\varepsilon_0}(x) = x \uparrow\uparrow (x - 1)$.
Check at $x = 3$: the tower $\omega^\omega$ has two copies, and $3 \uparrow\uparrow 2 = 3^3 = 27$.

### Relation to the fast-growing hierarchy

The slow-growing hierarchy lags far behind the fast-growing one.
The function $g_{\varepsilon_0}$ is a finite tower of $x$, which grows at about the rate of $f_3$, while $f_{\varepsilon_0}$ escapes every provably total function of $\mathsf{PA}$.
Girard proved in 1981 that the slow-growing hierarchy still catches up with the fast-growing one, far beyond $\varepsilon_0$ and with suitable fundamental sequences.
In particular $g_\alpha$ reaches the growth of $f_{\varepsilon_0}$ only when $\alpha$ is the Bachmann-Howard ordinal.

### Dependence on the fundamental sequences

The slow-growing hierarchy is very sensitive to the choice of the fundamental sequences, as Weiermann showed for ordinals far above $\varepsilon_0$.
A small case already shows the effect.
With $\varepsilon_0[0] = 1$ in place of $\varepsilon_0[0] = 0$, the tower $\varepsilon_0[x]$ has $x$ copies of $\omega$.
Then the substitution rule gives $g_{\varepsilon_0}(x) = x \uparrow\uparrow x$, so $g_{\varepsilon_0}(3)$ becomes $3^{27}$ in place of $27$.

### The theory and the stronger theory

For $\alpha \le \varepsilon_0$ the functions $g_\alpha$ are [[primitive recursive|5NVA2JRHPV]], by the substitution rule.
So the slow-growing functions up to $\varepsilon_0$ lie far inside the [[provably total functions|Z742YPHPNS]] of [[Peano arithmetic|MPSCREYC3M]], and even of $\mathrm{I}\Sigma_1$.
To reach the growth of $f_{\varepsilon_0}$, which $\mathsf{PA}$ does not prove total, the index must go up to the Bachmann-Howard ordinal.
$\mathsf{ZFC}$ proves that every $g_\alpha$ is total, by transfinite recursion on $\alpha$.

### Watch out

The same ordinal gives very different numbers in the three hierarchies.
At $\alpha = \omega^2$ and $x = 3$ the slow-growing value is $g_{\omega^2}(3) = 9$, the Hardy value is $H_{\omega^2}(3) = 24$, and the fast-growing value $f_{\omega^2}(3) = f_{\omega \cdot 3}(3)$ is far too large to write.
So a statement such as "the length is about $\omega^2$" means nothing until you say which hierarchy turns the ordinal into a number.

### Try it

First, compute $g_{\omega^3 + \omega}(2)$.
The answer is $2^3 + 2 = 10$, by the substitution rule.

Second, compute $g_{\omega \cdot 2}(3)$ from the definition.
The ordinal becomes $\omega + 3$, three successor steps add $3$ to $g_\omega(3) = 3$, and the answer is $6$.

## Explanations

### L1 human

The slow-growing hierarchy turns an ordinal into a formula in $x$ by a lazy rule: replace every $\omega$ by $x$.
For example $\omega^2 + 3$ becomes $x^2 + 3$, so at $x = 5$ it gives $28$.
Even the huge ordinal $\varepsilon_0$, an endless tower of $\omega$, only gives a finite tower of $x$.
So these functions grow slowly compared with the fast-growing hierarchy.

### L2 human

We compute $g_{\omega^\omega}(3)$ from the definition, without the substitution rule.
The ordinal $\omega^\omega$ is a limit with a limit exponent, so $\omega^\omega[3] = \omega^{\omega[3]} = \omega^3$.
Next $\omega^3[3] = \omega^2 \cdot 3$, and the additive rule gives $g_{\omega^2 \cdot 3}(3) = 3 \cdot g_{\omega^2}(3)$.
Then $\omega^2[3] = \omega \cdot 3$, so $g_{\omega^2}(3) = 3 \cdot g_\omega(3) = 3 \cdot 3 = 9$.
So
$$g_{\omega^\omega}(3) = 3 \cdot 9 = 27 = 3^3,$$
as the substitution rule predicts.
The computation shows the typical use of the hierarchy as a contrast: the same ordinal and the same sequences give very different growth than in the Hardy and fast-growing hierarchies.

### L3 human

The slow-growing hierarchy evaluates an ordinal notation at $x$, so it measures the size of the notation system rather than the length of a descent.
Girard's theorem that it eventually matches the fast-growing hierarchy links [[ordinal analysis|C5E5TG8PGP]] with the study of dilators.
For independence results it is a warning: growth rates depend on the notation.
The [[proof-theoretic ordinal|C72RBH0CDR]] of a theory is linked to provable totality through the fast-growing hierarchy, not through this one.
