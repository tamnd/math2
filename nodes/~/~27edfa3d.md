---
tag: ~27edfa3d
kind: definition
name: Limit of a function of several variables
msc: [26B05]
defines: ~3f10e8f7
uses: [~a5928a9d, ~e7a5e1c1, 0FFXKTKKQC]
sources:
  - url: https://en.wikipedia.org/wiki/Limit_of_a_function
    locator: Functions of more than one variable
---

## Definition

Let $D \subseteq \mathbb{R}^n$ and let $f \colon D \to \mathbb{R}^m$.
Let $a \in \mathbb{R}^n$ be a limit point of $D$: each open ball about $a$ contains a point of $D$ other than $a$.
Let $L \in \mathbb{R}^m$.
We say that $f(x)$ tends to $L$ as $x$ tends to $a$, and we write $\lim_{x \to a} f(x) = L$, when this holds.
For each $\varepsilon > 0$ there is a $\delta > 0$ such that $\|f(x) - L\| < \varepsilon$ for each $x \in D$ with $0 < \|x - a\| < \delta$.
Here $\|\cdot\|$ is the Euclidean norm of [[Euclidean space|~a5928a9d]].

## Remarks

A limit is unique when it exists, because $a$ is a limit point of $D$.
The value $f(a)$, and even whether $a$ is in $D$, has no effect on the limit.
A function into $\mathbb{R}^m$ tends to $L$ if and only if each component $f_i$ tends to $L_i$.
To show that a limit does not exist, it is enough to find two [[paths with different limits|~b3639c77]].

## Explanations

### L1 human

The definition says that you can make $f(x)$ as close to $L$ as you want. For this, take $x$ close enough to $a$ but not equal to $a$.
In the plane, "close to $a$" means inside a small disc about $a$, so $x$ can come from every direction at once.
