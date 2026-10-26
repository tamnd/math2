---
tag: ~3b1dee4f
kind: definition
name: Separable equation
msc: [34A05]
defines: ~27348380
uses: [~4841430a, 0Q1D85B8G6]
sources:
  - url: https://en.wikipedia.org/wiki/Separation_of_variables
    locator: Ordinary differential equations (ODE)
---

## Definition

Let $I$ and $J$ be open [[intervals|0Q1D85B8G6]] of $\mathbb{R}$, and let $g : I \to \mathbb{R}$ and $h : J \to \mathbb{R}$ be continuous functions.
A separable equation is a first-order [[ordinary differential equation|~4841430a]] of the form
$$y' = g(x)\, h(y),$$
for an unknown function $y$ of $x$ with values in $J$.

## Remarks

Method: if $h(y) \ne 0$, write the equation as $y'/h(y) = g(x)$ and integrate. With antiderivatives $H$ of $1/h$ and $G$ of $g$, the solutions satisfy $H(y(x)) = G(x) + C$ for a constant $C$.
For each zero $c$ of $h$, the constant function $y = c$ is a solution. The method above does not find these solutions.
Example: $y' = x y$ has the solutions $y = C e^{x^2/2}$ with a real constant $C$.
[[Exponential growth|~9ec534b9]] and the [[logistic equation|~2a91bc3d]] are separable.

## Explanations

### L1 human

In a separable equation, the right side is a product: one factor depends only on $x$ and the other only on $y$.
Put everything with $y$ on one side and everything with $x$ on the other side, then integrate both sides.
