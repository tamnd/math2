---
tag: QH3ENXFRSV
kind: object
name: Bachmann-Howard ordinal
msc: ["03F15", "03E10"]
topics: [XTTKZTYDSD]
audience: research
uses: [8S6CT4TMB7, DM0R5VVBGJ, 3HWF8NBKJE, PQSHBKCE7V, Z92S2GVCX9, C72RBH0CDR, 5VNT564Y2W, CRP7Z3M9XD, E7WEFRMQTB, ZHDM657G3D, CNN7BK5YAW, 01TQB88H4C]
sources:
  - url: https://en.wikipedia.org/wiki/Bachmann%E2%80%93Howard_ordinal
    locator: Definition
  - url: https://en.wikipedia.org/wiki/Ordinal_analysis
    locator: Table of ordinal analyses
---

## Description

Take the ordinals $\psi(\Omega) = \zeta_0$, $\psi(\Omega^\Omega) = \Gamma_0$, $\psi(\Omega^{\Omega^\Omega})$, and so on, in Madore's [[collapsing function|8S6CT4TMB7]] $\psi$.
Their supremum is the Bachmann-Howard ordinal $\psi(\varepsilon_{\Omega + 1})$.
Here $\Omega$ is the [[first uncountable ordinal|Z92S2GVCX9]], and $\varepsilon_{\Omega + 1}$ is the least [[epsilon number|PQSHBKCE7V]] above $\Omega$.
The closure sets $C(\alpha)$ of $\psi$ are generated from $0, 1, \omega, \Omega$ by $+$, $\cdot$, exponentiation and the values $\psi(\xi)$ with $\xi < \alpha$, and $\psi(\alpha)$ is the least countable ordinal not in $C(\alpha)$.
The Bachmann-Howard ordinal is [[countable|01TQB88H4C]], and it is the [[proof-theoretic ordinal|C72RBH0CDR]] of Kripke-Platek set theory $\mathrm{KP}$ and of the theory $\mathrm{ID}_1$ of one inductive definition.

## Remarks

### Where the collapse stops

1. The set $E$ of ordinals below $\varepsilon_{\Omega + 1}$ contains $0, 1, \omega, \Omega$ and is closed under $+$, $\cdot$ and exponentiation, since $\varepsilon_{\Omega + 1}$ is an epsilon number.
2. Every value $\psi(\xi)$ is countable, so it lies in $E$.
3. By induction on the stages of the generation, $C(\alpha) \subseteq E$ for every $\alpha$.
4. Let $\alpha \ge \varepsilon_{\Omega + 1}$.
   Every $\xi \in C(\alpha)$ satisfies $\xi < \varepsilon_{\Omega + 1}$, so the extra values $\psi(\xi)$ allowed by $\alpha$ are never used, and $C(\alpha) = C(\varepsilon_{\Omega + 1})$.
5. Hence $\psi(\alpha) = \psi(\varepsilon_{\Omega + 1})$ for all $\alpha \ge \varepsilon_{\Omega + 1}$, and this system names nothing beyond the Bachmann-Howard ordinal.

### Approximations from below

The ordinals $\Omega$, $\Omega^\Omega$, $\Omega^{\Omega^\Omega}$, and so on, have supremum $\varepsilon_{\Omega + 1}$.
Applying $\psi$ gives $\zeta_0$, then $\Gamma_0$, then the [[large Veblen ordinal|ZHDM657G3D]], and their supremum is the Bachmann-Howard ordinal.
So it lies far above the [[Feferman-Schütte ordinal|CNN7BK5YAW]] and every Veblen ordinal.
The values $\psi(\Omega)$ and $\psi(\Omega + 1)$ are computed in [[small values|DM0R5VVBGJ]] and [[the first impredicative value|3HWF8NBKJE]].

### Other notations

In Buchholz's [[functions $\psi_\nu$|E7WEFRMQTB]], with $\Omega_0 = 1$ and $\Omega_\nu = \aleph_\nu$ for $\nu > 0$, the same ordinal is $\psi_0(\varepsilon_{\Omega_1 + 1})$.
In that system $\psi_0(\varepsilon_{\Omega_1 + 1}) = \psi_0(\Omega_2)$, so $\psi_0(\Omega_2)$ is another name for it.
Each formula holds only in its own system.

### Role in proof theory

For the [[theories of iterated inductive definitions|5VNT564Y2W]], $\lvert \mathrm{ID}_1 \rvert$ is the Bachmann-Howard ordinal.
The lower bound uses [[the accessible part as an inductive definition|CRP7Z3M9XD]], and the upper bound can be proved with [[Buchholz's Ω-rule|5C4YBXQV15]].
Kripke-Platek set theory with infinity has the same ordinal, and so does the constructive set theory $\mathrm{CZF}$.
These theories are impredicative, and their analysis needs a collapsing function, since the Veblen functions stop at the large Veblen ordinal.

### History

Heinz Bachmann introduced the notation system in 1950, with Veblen-style functions indexed by uncountable ordinals.
William Howard studied the ordinal in 1972.
The name honors both.

### Common errors

One error treats $\psi(\varepsilon_{\Omega+1})$ as an uncountable ordinal.
The argument $\varepsilon_{\Omega+1}$ is uncountable, but the value is countable.

Another error takes the uncountability of $\Omega$ as essential.
The notation system works with formal terms and a decidable order on them, and $\Omega$ only serves to define that order and prove it well-founded.

## Explanations

### L1 human

The Bachmann-Howard ordinal is a very large countable ordinal.
To name it, logicians use a trick: they first name a huge uncountable ordinal, and then a "collapsing" function turns that name into a countable ordinal.
It measures the strength of theories that can talk about the smallest set closed under a rule, such as the set of well-founded trees.

### L2 human

We see why the argument $\varepsilon_{\Omega + 1}$ is the end of the line.

1. Start from $\Omega$ and apply exponentiation: $\Omega$, $\Omega^\Omega$, $\Omega^{\Omega^\Omega}$, and so on.
2. Each term is below $\varepsilon_{\Omega + 1}$, and their supremum is $\varepsilon_{\Omega + 1}$.
3. The closure sets $C(\alpha)$ can only form terms from such towers, from sums and products, and from values of $\psi$, which are countable.
4. So no term in any $C(\alpha)$ reaches $\varepsilon_{\Omega + 1}$, and making $\alpha$ larger adds nothing.

The typical use is as the upper end of the notation system for $\mathrm{ID}_1$ and $\mathrm{KP}$.
The trap: the formula $\psi(\varepsilon_{\Omega+1})$ names the ordinal only in Madore's system; in other systems the same letters mean other ordinals.
