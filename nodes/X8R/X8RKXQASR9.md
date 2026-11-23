---
tag: X8RKXQASR9
kind: object
name: Hardy hierarchy
aliases: [hardy-functions]
msc: ["03D20", "03F30"]
topics: [T6FK1E7GJ1]
audience: grad
uses: [R6ZC4BJGXV, KT50SMH3EC, 6GD30FGYDZ, 0ZHQMQ2C1N]
sources:
  - url: https://en.wikipedia.org/wiki/Hardy_hierarchy
    locator: Definition
  - url: https://en.wikipedia.org/wiki/Hardy_hierarchy
    locator: Relation to fast-growing hierarchy
  - url: https://en.wikipedia.org/wiki/Hardy_hierarchy
    locator: lead section
---

## Description

A Hardy function counts down an ordinal and counts up a number at the same time, and its value is the final count.
This is the form in which the lengths of Goodstein sequences and hydra battles come out.

Here is one run.
Start with the ordinal $\omega$ and the counter $3$.
The ordinal $\omega$ is a limit, so the counter chooses the smaller ordinal $\omega[3] = 3$, and the pair becomes $(3, 3)$.
Each successor step lowers the ordinal by $1$ and raises the counter by $1$:
$$(3, 3) \to (2, 4) \to (1, 5) \to (0, 6).$$
So $H_\omega(3) = 6$.

**The definition.**
The Hardy functions are functions $H_\alpha : \mathbb{N} \to \mathbb{N}$, one for each ordinal $\alpha \le \varepsilon_0$.
They use the standard fundamental sequences $\lambda[x]$ of the [[fast-growing hierarchy|R6ZC4BJGXV]], with $\varepsilon_0[0] = 0$.
$$H_0(x) = x, \qquad H_{\alpha + 1}(x) = H_\alpha(x + 1), \qquad H_\lambda(x) = H_{\lambda[x]}(x) \text{ for a limit } \lambda.$$
So a successor $\alpha + 1$ becomes $\alpha$ while $x$ grows by $1$, and a limit $\lambda$ becomes $\lambda[x]$ while $x$ stays the same.
The process stops at the ordinal $0$, and the output is the final value of $x$.

## Remarks

### First values

For a finite $n$, the run makes $n$ successor steps, so $H_n(x) = x + n$.
At $\omega$ it first replaces $\omega$ by $x$:
$$H_\omega(x) = H_x(x) = 2x.$$
At $\omega \cdot 2$ it replaces the ordinal by $\omega + x$, and the composition law below gives
$$H_{\omega \cdot 2}(x) = H_{\omega + x}(x) = H_\omega(H_x(x)) = H_\omega(2x) = 4x.$$
At $\omega^2$ it replaces the ordinal by $\omega \cdot x$, so $H_\omega$ is applied $x$ times:
$$H_{\omega^2}(x) = H_{\omega \cdot x}(x) = 2^x \cdot x.$$
So $H_{\omega^2}(0), \dots, H_{\omega^2}(4)$ are $0, 2, 8, 24, 64$, and $H_{\omega^\omega}(2) = H_{\omega^2}(2) = 8$.
At the top, $H_{\varepsilon_0}(0) = H_0(0) = 0$, $H_{\varepsilon_0}(1) = H_1(1) = 2$ and $H_{\varepsilon_0}(2) = H_\omega(2) = 4$.

### The composition law

**Lemma 1.** Let $\gamma, \delta < \varepsilon_0$, and suppose that the last exponent in the [[Cantor normal form|6GD30FGYDZ]] of $\gamma$ is at least the first exponent of $\delta$.
Then $H_{\gamma + \delta}(x) = H_\gamma(H_\delta(x))$ for all $x$.
The condition holds when $\gamma = 0$ or $\delta = 0$.

We prove it by [[transfinite induction|0ZHQMQ2C1N]] on $\delta$.

1. If $\delta = 0$, then $H_{\gamma}(x) = H_\gamma(H_0(x))$ by the definition of $H_0$.
2. Let $\delta = \delta' + 1$.
   The normal form of $\delta'$ drops a final term $\omega^0$, so $\delta'$ satisfies the condition.
3. Then $H_{\gamma + \delta' + 1}(x) = H_{\gamma + \delta'}(x + 1) = H_\gamma(H_{\delta'}(x+1)) = H_\gamma(H_\delta(x))$.
4. Let $\delta$ be a limit.
   The condition makes the normal form of $\gamma + \delta$ the normal form of $\gamma$ followed by that of $\delta$.
5. The rules for $\lambda[x]$ change only the last term, so $(\gamma + \delta)[x] = \gamma + \delta[x]$.
6. The first exponent of $\delta[x]$ is at most the first exponent of $\delta$, so $\delta[x]$ satisfies the condition, and $\delta[x] < \delta$.
7. So $H_{\gamma + \delta}(x) = H_{\gamma + \delta[x]}(x) = H_\gamma(H_{\delta[x]}(x)) = H_\gamma(H_\delta(x))$.

Check: $H_{\omega^2 + 3}(5) = H_{\omega^2}(H_3(5)) = H_{\omega^2}(8) = 2^8 \cdot 8 = 2048$.
Applied $x - 1$ times, the lemma gives $H_{\omega^\beta \cdot x} = (H_{\omega^\beta})^x$, the $x$-fold iterate.

### Relation to the fast-growing hierarchy

**Lemma 2.** For every $\alpha < \varepsilon_0$, $H_{\omega^\alpha} = f_\alpha$.

We prove it by transfinite induction on $\alpha$.

1. For $\alpha = 0$: $H_{\omega^0}(x) = H_1(x) = H_0(x + 1) = x + 1 = f_0(x)$.
2. For $\alpha = \beta + 1$: the first rule of the fundamental sequences gives $\omega^{\beta+1}[x] = \omega^\beta \cdot x$.
3. So $H_{\omega^{\beta+1}}(x) = H_{\omega^\beta \cdot x}(x) = (H_{\omega^\beta})^x(x)$, by Lemma 1.
4. By the induction hypothesis this is $f_\beta^x(x) = f_{\beta+1}(x)$.
   For $x = 0$ both sides are $0$.
5. For a limit $\alpha$: the second rule gives $\omega^\alpha[x] = \omega^{\alpha[x]}$, and $\alpha[x] < \alpha$.
6. So $H_{\omega^\alpha}(x) = H_{\omega^{\alpha[x]}}(x) = f_{\alpha[x]}(x) = f_\alpha(x)$.

The small cases agree: $H_\omega = f_1$ is $x \mapsto 2x$, $H_{\omega^2} = f_2$ is $x \mapsto x \cdot 2^x$, and $H_{\omega^3}(2) = f_3(2) = 2048$.

### What happens at epsilon nought

The lemma fails at $\alpha = \varepsilon_0$, although $\omega^{\varepsilon_0} = \varepsilon_0$.
For $x \ge 1$ we have $\varepsilon_0[x] = \omega^{\varepsilon_0[x-1]}$, so Lemma 2 gives
$$H_{\varepsilon_0}(x) = H_{\omega^{\varepsilon_0[x-1]}}(x) = f_{\varepsilon_0[x-1]}(x),$$
while $f_{\varepsilon_0}(x) = f_{\varepsilon_0[x]}(x)$.
For example $H_{\varepsilon_0}(2) = f_1(2) = 4$, but $f_{\varepsilon_0}(2) = f_\omega(2) = 8$.
The two still have the same growth.
Each $f_\beta$ is increasing, so $H_{\varepsilon_0}(x) = f_{\varepsilon_0[x-1]}(x) \ge f_{\varepsilon_0[x-1]}(x - 1) = f_{\varepsilon_0}(x - 1)$.
Gallier proved the matching upper bound $H_{\varepsilon_0}(x) \le f_{\varepsilon_0}(x + 1)$ for $x \ge 1$.

### Goodstein sequences and hydras

The length function $L$ of [[Goodstein's theorem|XQMNJF241J]] satisfies $L(m) = H_{o_2(m)}(3) - 2$, where $o_2(m)$ replaces each $2$ in the hereditary base-$2$ notation of $m$ by $\omega$.
For $m = 2$ this gives $L(2) = H_\omega(3) - 2 = 4$, and the sequence $2, 2, 1, 0$ has indeed $4$ terms.
The [[proof|J1NTZCSPPM]] derives the formula with $P_x$, the predecessor along fundamental sequences.
The standard battle of the [[Kirby-Paris hydra|C028FF4TWM]] lowers the ordinal of the hydra along fundamental sequences in the same way.
So the lengths of these processes are values of Hardy functions near $\varepsilon_0$, and they escape the [[provably total functions|Z742YPHPNS]] of $\mathsf{PA}$.

### The theory and the stronger theory

For a fixed $\alpha < \varepsilon_0$, [[Peano arithmetic|MPSCREYC3M]] $\mathsf{PA}$ proves that $H_\alpha$ is total, because it proves transfinite induction up to each such $\alpha$.
$\mathsf{PA}$ does not prove that $H_{\varepsilon_0}$ is total.
The reason is that $H_{\varepsilon_0}(x) \ge f_{\varepsilon_0}(x - 1)$, and $f_{\varepsilon_0}$ is not dominated by any provably total function of $\mathsf{PA}$.
$\mathsf{ZFC}$ proves that every $H_\alpha$ with $\alpha \le \varepsilon_0$ is total, by transfinite recursion.

### Watch out

The index of a Hardy function is not on the same scale as the index of a fast-growing function.
For example $H_2(5) = 7$ but $f_2(5) = 160$, and in general $H_\alpha$ is far slower than $f_\alpha$.
The correct translation is $f_\alpha = H_{\omega^\alpha}$, so $f_2 = H_{\omega^2}$.

Some authors use $\lambda[x + 1]$ in place of $\lambda[x]$ in the limit clause, and then all the values above change.
With that rule $H_\omega(3) = H_4(3) = 7$, not $6$.

### History

Stanley Wainer introduced the hierarchy in 1972.
The name comes from G. H. Hardy, whose paper of 1904 on a set of reals of cardinality $\aleph_1$ contains the idea of the definition.

### Try it

First, compute $H_{\omega + 2}(3)$.
The answer is $H_\omega(5) = 10$, by two successor steps and then $H_\omega(x) = 2x$.

Second, compute $H_{\omega^2}(3)$ and compare it with $f_2(3)$.
The answer is $3 \cdot 2^3 = 24$ for both, as Lemma 2 predicts.

## Explanations

### L1 human

A Hardy function is a countdown game with an ordinal and a counter.
Each time the ordinal goes down by one, the counter goes up by one.
When the ordinal is a limit, like $\omega$, the counter picks a smaller ordinal to replace it.
For example, start with $\omega$ and counter $3$: the ordinal becomes $3$, then three steps add $3$, and the result is $6$.
The game always stops, and the final counter is the value.

### L2 human

We compute $H_{\omega \cdot 2}(3)$ by running the countdown.
The ordinal $\omega \cdot 2$ is a limit, and $(\omega \cdot 2)[3] = \omega + 3$, so the pair becomes $(\omega + 3, 3)$.
Three successor steps give $(\omega, 6)$.
Then $\omega[6] = 6$, so the pair is $(6, 6)$, and six successor steps give $(0, 12)$.
So $H_{\omega \cdot 2}(3) = 12$, which matches the formula $4x$ at $x = 3$.
The run shows the typical use: the number of steps of a process that lowers an ordinal along fundamental sequences is read off as a Hardy value.

### L3 human

The Hardy hierarchy is the unfolded form of the fast-growing hierarchy: $H_\alpha$ runs a single descent, while $f_\alpha$ iterates functions.
Its composition law $H_{\gamma + \delta} = H_\gamma \circ H_\delta$ turns ordinal addition into composition of functions.
This makes it the natural tool for the lengths of [[Goodstein sequences|XQMNJF241J]] and of hydra battles.
At $\varepsilon_0$ it catches up with the fast-growing hierarchy, so both give the same boundary for $\mathsf{PA}$.
The [[slow-growing hierarchy|VDF6R9EVJ2]] is the third member of the family, and it counts only the successor steps.
