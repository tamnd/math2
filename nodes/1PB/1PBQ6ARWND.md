---
tag: 1PBQ6ARWND
kind: example
name: Solenoid
msc: ["22C05", "54H11"]
instance_of: [EVHCE5VR6Y]
uses: [DZB378CNCK, 04EAFVFTF7, V6TJAFZ4MD]
sources:
  - url: https://en.wikipedia.org/wiki/Solenoid_(mathematics)
same_as:
  wikidata: Q3489713
  wikipedia: Solenoid (mathematics)
---

## Example

Let $p$ be a prime and let $\mathbb{T} = \set{z \in \C : \abs{z} = 1}$ be the [[circle group|04EAFVFTF7]].
The *$p$-adic solenoid* $\Sigma_p$ is the [[inverse limit|DZB378CNCK]] of the sequence
$$\cdots \to \mathbb{T} \xrightarrow{z \mapsto z^p} \mathbb{T} \xrightarrow{z \mapsto z^p} \mathbb{T}.$$
Its elements are sequences $(z_0, z_1, z_2, \dots)$ in $\mathbb{T}$ with $z_{k+1}^p = z_k$ for all $k$.
The group law is coordinatewise multiplication, and the topology is the one induced from the product $\mathbb{T}^{\N}$.

Check that it is a [[compact group|EVHCE5VR6Y]].
Each map $z \mapsto z^p$ is a continuous homomorphism, so the sequences with $z_{k+1}^p = z_k$ form a subgroup of $\mathbb{T}^{\N}$.
This subgroup is closed, since it is cut out by the equations $z_{k+1}^p = z_k$ between continuous functions.
The product $\mathbb{T}^{\N}$ is compact by Tychonoff's theorem, so $\Sigma_p$ is a compact Hausdorff abelian group.

## Remarks

The solenoid is connected, being an inverse limit of compact connected spaces.
It is not locally connected and not path-connected, so it is a compact connected group that is not a Lie group.
The projection $(z_k) \mapsto z_0$ onto $\mathbb{T}$ is onto, and its kernel is isomorphic to the group $\Z_p$ of [[p-adic integers|V6TJAFZ4MD]].
Its Pontryagin dual is the discrete group $\Z[1/p]$ of rationals whose denominators are powers of $p$.

## Explanations

### L1 human

Wrap a loop of string around a circle $p$ times, then wrap the result $p$ times again, and continue forever.
The limiting object is the solenoid.
Near any point it looks like a line segment times a Cantor set, so it is connected but full of gaps.
It is a standard example of a compact connected group that is not a Lie group.
