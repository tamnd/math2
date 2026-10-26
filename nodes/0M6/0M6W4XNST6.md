---
tag: 0M6W4XNST6
kind: statement
role: theorem
name: Universal property of the product topology
msc: [54B10]
uses: [04S9HX3GAP, 0SY9ECQ19Q, 07HF9YCWPP, 0CHR35YNJQ]
sources:
  - url: https://en.wikipedia.org/wiki/Product_topology
    locator: Properties
---

## Statement

Let $(X_i)_{i \in I}$ be a family of [[topological spaces|0CNQXVBHCX]], let $X = \prod_{i \in I} X_i$ have the [[product topology|04S9HX3GAP]], and let $\pi_i \colon X \to X_i$ be the projections.
Let $Z$ be a topological space and let $f \colon Z \to X$ be a function.
Then $f$ is [[continuous|0SY9ECQ19Q]] if and only if the [[composition|07HF9YCWPP]] $\pi_i \circ f \colon Z \to X_i$ is continuous for each $i \in I$.

## Remarks

Proof of the converse: preimages of the subbasic sets $\pi_i^{-1}(U)$ under $f$ are $(\pi_i \circ f)^{-1}(U)$, which are open. Preimages respect unions and intersections, so all preimages of open sets are open.
Thus a map into a product is continuous if and only if all its coordinate functions are continuous. For example, $t \mapsto (\cos t, \sin t)$ is continuous from $\mathbb{R}$ to $\mathbb{R}^2$.
The statement fails for the [[box topology|0CTM1EHG9P]].

## Explanations

### L1 human

To check that a map into a product is continuous, check each coordinate separately.
This property characterises the product topology among all topologies on the product.
