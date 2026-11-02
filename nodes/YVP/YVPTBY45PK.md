---
tag: YVPTBY45PK
kind: object
name: Surreal number
msc: [06F25, 12J15, "03E10"]
instance_of: [0P3VCBDEE2]
uses: [0YSCSX5YZC, 0G3RRM41X9, 421QMTFG9T, 0XH79S06J3, DDY3Q3PJ6W]
sources:
  - url: https://en.wikipedia.org/wiki/Surreal_number
same_as:
  wikidata: Q875333
  wikipedia: Surreal number
---

## Description

The *surreal numbers* are built in stages, called days.
A surreal number is written $x = \{ L \mid R \}$, where $L$ and $R$ are sets of surreal numbers built on earlier days.
The condition is that no element of $L$ is greater than or equal to any element of $R$.
The order is defined at the same time.
The rule is: $x \le y$ holds when no left option of $x$ is $\ge y$ and no right option of $y$ is $\le x$.
Two forms $x$ and $y$ name the same number when $x \le y$ and $y \le x$.

On day $0$, only $0 = \{ \mid \}$ exists, with both sets empty.
On day $1$, one gets $1 = \{ 0 \mid \}$ and $-1 = \{ \mid 0 \}$.
On day $2$, one gets $2 = \{ 1 \mid \}$, $\tfrac12 = \{ 0 \mid 1 \}$, and their negatives.
After infinitely many days one gets $\omega = \{ 0, 1, 2, \dots \mid \}$, which is larger than every natural number.
One also gets $\varepsilon = \{ 0 \mid 1, \tfrac12, \tfrac14, \dots \}$, which is positive but smaller than every positive real number.

Addition and multiplication are defined by recursion on the options.
With them the surreal numbers satisfy all the axioms of an [[ordered field|0P3VCBDEE2]].
The one caveat is size: they form a proper class, not a set, so strictly they are an ordered field only in this class sense.
This field contains a copy of the real numbers and a copy of every [[ordinal number|0YSCSX5YZC]].
It is not [[Archimedean|0XH79S06J3]], since $\omega$ exceeds every natural number, and $\omega \cdot \varepsilon = 1$.
It is a [[real closed field|DDY3Q3PJ6W]].

## Remarks

Each real number $r$ is the surreal number $\{ L \mid R \}$ with $L$ the rationals below $r$ with power-of-two denominators and $R$ those above $r$; this mirrors a [[Dedekind cut|0G3RRM41X9]].
Like the [[hyperreal numbers|421QMTFG9T]], the surreals contain infinite and infinitesimal elements.
The surreals were introduced by John Conway, and the name comes from Donald Knuth's book *Surreal Numbers* (1974).

## Explanations

### L1 human

Surreal numbers start from nothing and grow by one rule: a new number sits between a set of numbers on its left and a set on its right.
From the empty pair one gets $0$, then $1$ and $-1$, then $2$, $\tfrac12$ and so on.
Every real number appears, and so do infinite numbers like $\omega$ and tiny numbers like $1/\omega$.
You can still add, subtract, multiply and divide them, and compare any two of them.
So they are one huge number line that holds both the reals and the ordinals.
