---
tag: 8S6CT4TMB7
kind: concept
name: Ordinal collapsing function
aliases: [collapsing-function, ordinal-collapsing]
msc: ["03F15", "03E10"]
topics: [XTTKZTYDSD]
audience: research
uses: [0YSCSX5YZC, KAEDCQ8RM6, PQSHBKCE7V, Z92S2GVCX9, JQFAE9S2F4, 7MBX59Y7N9, 01TQB88H4C]
sources:
  - url: https://en.wikipedia.org/wiki/Ordinal_collapsing_function
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Ordinal_collapsing_function
    locator: Predicative start
  - url: https://en.wikipedia.org/wiki/Ordinal_collapsing_function
    locator: First impredicative values
  - url: https://en.wikipedia.org/wiki/Ordinal_collapsing_function
    locator: Beyond the Feferman-Schütte ordinal
  - url: https://en.wikipedia.org/wiki/Ordinal_analysis
    locator: Table of ordinal analyses
---

## Summary

Start with the names $0$, $1$ and $\omega$, and allow sums, products and powers.
You can name $\omega^\omega + 3$ and $\omega^{\omega^{\omega}}$, but never $\varepsilon_0$, the least ordinal with $\omega^{\varepsilon_0} = \varepsilon_0$.
An ordinal collapsing function records this kind of fact: its value is the first ordinal that a given stock of names misses.
The trick is to add a huge name $\Omega$ to the stock, so that terms built from $\Omega$ become names for countable ordinals.

We fix one system, the one of the Wikipedia article on collapsing functions, often called Madore's $\psi$.
Let $\Omega$ be the [[first uncountable ordinal|Z92S2GVCX9]].
For each [[ordinal|0YSCSX5YZC]] $\alpha$, let $C(\alpha)$ be the least set that contains $0$, $1$, $\omega$ and $\Omega$, is closed under $+$, $\cdot$ and $\beta^\gamma$, and contains $\psi(\xi)$ for each $\xi \in C(\alpha)$ with $\xi < \alpha$.
Then
$$\psi(\alpha) = \min \{ \rho : \rho \notin C(\alpha) \}.$$
The definition is a transfinite recursion on $\alpha$, because $C(\alpha)$ uses only the values $\psi(\xi)$ with $\xi < \alpha$.

## Motivation

The [[Veblen function|JQFAE9S2F4]] names ordinals from below: each new function lists the fixed points of the earlier ones.
This reaches the [[Feferman-Schütte ordinal|CNN7BK5YAW]] $\Gamma_0$, and its extensions with more arguments reach the [[large Veblen ordinal|ZHDM657G3D]].
The ordinals of impredicative theories, such as $\mathrm{ID}_1$ and Kripke-Platek set theory, lie beyond everything that such schemes name.

A collapsing function names ordinals from above.
We compute with terms such as $\Omega + 1$, $\Omega^\Omega$ or $\varepsilon_{\Omega + 1}$, which are uncountable, and $\psi$ turns each term into a countable ordinal.
The countable value remembers the term, because it is defined from the set of names that the term makes available.
So the order of the uncountable arguments controls the order of the countable values, and comparison of notations becomes a computation on terms.
Collapsing functions give the [[ordinal notation systems|7MBX59Y7N9]] of [[ordinal analysis|C5E5TG8PGP]] from the [[Bachmann-Howard ordinal|QH3ENXFRSV]] upward.

## Notation

The same letter $\psi$ names different functions in different books, so every page that uses one must say which it means.
In the system fixed above, $\psi(\Omega) = \zeta_0$.
In Buchholz's [[functions $\psi_\nu$|E7WEFRMQTB]], which start from $0$ and use only addition, $\psi_0(\Omega) = \varepsilon_0$.
Rathjen's surveys use a function $\psi_\Omega$ with a similar closure definition but a different base, and [[another $\psi$|M7D1HEJQVH]] for Mahlo cardinals.
Bachmann's functions $\varphi_\alpha$ with uncountable indices and Feferman's functions $\theta_\alpha$ are older collapsing systems.
In the literature $C(\alpha)$ is often built in stages $C_0(\alpha) \subseteq C_1(\alpha) \subseteq \dots$, one closure step at a time.

## Remarks

### A first computation

Why is $\psi(0) = \varepsilon_0$?
No value of $\psi$ is allowed in $C(0)$, since no $\xi$ is below $0$.
So the countable members of $C(0)$ are the ordinals built from $0$, $1$, $\omega$ by sums, products and powers, and those are exactly the ordinals below $\varepsilon_0$, by [[Cantor normal form|6GD30FGYDZ]].
A term that contains $\Omega$ and is not $0$ or $1$ is at least $\Omega$, so it adds no countable ordinal.
The least ordinal missed is $\varepsilon_0$.
The [[small values|DM0R5VVBGJ]] continue this: $\psi(1) = \varepsilon_1$, and in general $\psi(\gamma) = \varepsilon_\gamma$ for $\gamma \le \zeta_0$, where $\zeta_0$ is the least fixed point of $\gamma \mapsto \varepsilon_\gamma$.

### Where the function gets stuck, and how $\Omega$ helps

For $\zeta_0 \le \alpha \le \Omega$ the value stays at $\zeta_0$.
The reason is that every countable argument we can name in $C(\alpha)$ is below $\zeta_0$, so the allowed values $\psi(\xi) = \varepsilon_\xi$ are below $\zeta_0$ too.
At $\alpha = \Omega + 1$ the argument $\Omega$ is allowed, and $\psi(\Omega) = \zeta_0$ becomes a name.
Then the [[first impredicative value|3HWF8NBKJE]] is
$$\psi(\Omega + 1) = \varepsilon_{\zeta_0 + 1}.$$
This is the collapse: the uncountable term $\Omega$ serves as a name for the countable ordinal $\zeta_0$.

### Landmarks of the system

Further along, the Wikipedia article gives these values, and each one is a landmark of proof theory:
$$\psi(\Omega^\Omega) = \Gamma_0, \qquad \psi(\Omega^{\Omega^\omega}) = \text{small Veblen ordinal}, \qquad \psi(\Omega^{\Omega^\Omega}) = \text{large Veblen ordinal}.$$
The [[Bachmann-Howard ordinal|QH3ENXFRSV]] is $\psi(\varepsilon_{\Omega + 1})$, the limit of $\psi(\Omega)$, $\psi(\Omega^\Omega)$, $\psi(\Omega^{\Omega^\Omega})$ and so on.
For $\alpha \ge \varepsilon_{\Omega + 1}$ the value stays there, because no term of $C(\alpha)$ reaches $\varepsilon_{\Omega + 1}$.

### The first properties

Each $C(\alpha)$ is countable, since it is built in countably many steps from countably many names, so $\psi(\alpha) < \Omega$.
The function is weakly increasing, because $\alpha \le \beta$ gives $C(\alpha) \subseteq C(\beta)$.
Each value $\rho = \psi(\alpha)$ is an [[epsilon number|PQSHBKCE7V]].
Indeed every ordinal below $\rho$ is in $C(\alpha)$, so if $\rho < \omega^\rho$, the Cantor normal form of $\rho$ would build $\rho$ from smaller members of $C(\alpha)$.
On arguments with $\alpha \in C(\alpha)$ the function is strictly increasing, and these arguments give a primitive recursive notation system below the Bachmann-Howard ordinal.

### What it is not

Drop $\Omega$ from the names, and the function [[stops at $\zeta_0$ for good|GT4KH0TTYV]]: large arguments cannot be named, so they change nothing.
The Veblen function is not a collapsing function either, because no uncountable ordinal occurs in its definition.
Finally, the condition $\xi < \alpha$ cannot be dropped.
If $C(0)$ contained $\psi(\xi)$ for every $\xi \in C(0)$, then $0 \in C(0)$ would put $\psi(0)$ into $C(0)$, against the definition of $\psi(0)$.

### Watch out

Two slips are common.
First, $\psi$ is not strictly increasing: $\psi(\zeta_0 + 1) = \psi(\Omega) = \zeta_0$, although $\zeta_0 + 1 < \Omega$.
Only arguments with $\alpha \in C(\alpha)$ give distinct notations.
Second, terms from different systems do not compare: $\psi(\Omega) = \zeta_0$ here, while Buchholz's $\psi_0(\Omega) = \varepsilon_0$.
Before you compare two $\psi$-terms, check that they come from the same definition.

### History

Heinz Bachmann defined the first collapsing functions in 1950.
His method needs a fundamental sequence for each limit ordinal, including sequences of length $\Omega$, and later authors found it heavy.
Feferman's functions $\theta_\alpha$ simplified the method.
Buchholz introduced his functions $\psi_\nu$ in 1986, with a short definition by closure sets like the one above.
Rathjen later extended collapsing to Mahlo and weakly compact cardinals.

### Try it

Compute $\psi(2)$.
Now $\psi(0) = \varepsilon_0$ and $\psi(1) = \varepsilon_1$ are names, every ordinal below $\varepsilon_2$ can be built from them, and $\varepsilon_2$ cannot, so $\psi(2) = \varepsilon_2$.

Compute $\psi(\Omega + 2)$.
Now $\psi(\Omega + 1) = \varepsilon_{\zeta_0 + 1}$ is a new name, and the same argument as before gives $\psi(\Omega + 2) = \varepsilon_{\zeta_0 + 2}$.

## Explanations

### L1 human

Counting with ordinals, we soon run out of names, even with powers of $\omega$.
A collapsing function borrows a huge number $\Omega$, far beyond everything we want to name.
We compute with expressions like $\Omega + 1$ or $\Omega \cdot 2$, and the function turns each expression into a countable ordinal.
For example, $\psi(0)$ is the first ordinal that cannot be written with $0$, $1$, $\omega$, sums, products and powers, and that ordinal is $\varepsilon_0$.
Larger expressions turn into larger countable ordinals, so the huge number works like a ladder that we climb and then take away.

### L2 human

We compute $\psi(1)$.
The set $C(1)$ may use $\psi(0) = \varepsilon_0$, because $0 \in C(1)$ and $0 < 1$.
With sums, products and powers we get $\varepsilon_0 + 1$, $\varepsilon_0 \cdot 2$, $\omega^{\varepsilon_0 + 1}$, $\omega^{\omega^{\varepsilon_0 + 1}}$, and in fact every ordinal below $\varepsilon_1$.
No term reaches $\varepsilon_1$, because $\varepsilon_1$ is closed under the three operations and the only allowed value of $\psi$ is $\varepsilon_0$.
So $\psi(1) = \varepsilon_1$.

The typical use is to compare two notations: for arguments in normal form, $\psi(\alpha) < \psi(\beta)$ holds exactly when $\alpha < \beta$.
So the comparison of two countable ordinals reduces to the comparison of two terms in $\Omega$, which is a finite computation.

### L3 human

A collapsing function uses a large ordinal as a source of names for small ordinals.
In proof theory the role of $\Omega$ is played by the first nonrecursive ordinal $\omega_1^{\mathrm{CK}}$ when one interprets the notations in Kripke-Platek set theory.
The collapse matches the collapsing lemma for infinitary derivations with the [[Ω-rule|5C4YBXQV15]]: a derivation of height $\alpha$ becomes one without impredicative cuts, of height $\psi(\beta)$ for a $\beta$ computed from $\alpha$.
Stronger theories need more uncountable cardinals $\Omega_1, \Omega_2, \dots$ ([[Buchholz's psi functions|E7WEFRMQTB]]), an inaccessible, a Mahlo cardinal ([[Rathjen's psi function|M7D1HEJQVH]]) or a weakly compact cardinal.
Each kind of large cardinal matches a reflection property of the theory that is analyzed.
