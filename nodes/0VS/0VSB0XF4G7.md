---
tag: 0VSB0XF4G7
kind: definition
name: Indicator function
msc: ["03E20"]
defines: 0RCQZ36MME
uses: [0XHDTE5YMZ, 0FE8Q5S42Y]
sources:
  - url: https://en.wikipedia.org/wiki/Indicator_function
    locator: lead section
---

## Definition

Let $X$ be a set and let $A$ be a [[subset|0FE8Q5S42Y]] of $X$.
The indicator function of $A$ is the [[function|0XHDTE5YMZ]] $\mathbf{1}_A \colon X \to \{0, 1\}$ with
$$\mathbf{1}_A(x) = \begin{cases} 1 & \text{if } x \in A, \\ 0 & \text{if } x \notin A. \end{cases}$$

## Remarks

Other names are characteristic function and the notation $\chi_A$.
For subsets $A$ and $B$ of $X$, $\mathbf{1}_{A \cap B} = \mathbf{1}_A \mathbf{1}_B$ and $\mathbf{1}_{A^c} = 1 - \mathbf{1}_A$.
The map $A \mapsto \mathbf{1}_A$ is a [[bijection|0SNQEF7Z53]] from the [[power set|0BC7KX51Z8]] of $X$ to the set of functions from $X$ to $\{0, 1\}$.

## Explanations

### L1 human

The indicator function answers "is $x$ in $A$?" with $1$ for yes and $0$ for no.
For $A$ the even integers, $\mathbf{1}_A(4) = 1$ and $\mathbf{1}_A(5) = 0$.
