---
tag: 0DZS7ZG0QY
kind: definition
name: Length of a vector
aliases: [magnitude-of-a-vector, euclidean-norm]
msc: [51N20]
defines: 0XKBKGTCPC
uses: [0QN3D80AWP]
sources:
  - url: https://en.wikipedia.org/wiki/Euclidean_vector
    locator: Length
---

## Definition

Let $n$ be a positive integer and let $v = (v_1, \dots, v_n)$ be a [[vector|0QN3D80AWP]] in $\mathbb{R}^n$.
The length of $v$ is the real number
$$\|v\| = \sqrt{v_1^2 + v_2^2 + \dots + v_n^2} = \sqrt{v \cdot v},$$
where $v \cdot v = v_1^2 + \dots + v_n^2$ is the dot product of $v$ with itself.
A unit vector is a vector of length 1.

## Remarks

For each vector $v$, $\|v\| \geq 0$, and $\|v\| = 0$ if and only if $v$ is the zero vector.
For each real number $c$, $\|c v\| = |c| \, \|v\|$. Thus for $v \neq 0$ the vector $v / \|v\|$ is a unit vector.
Other names for the length are the magnitude and the Euclidean norm. The notation $|v|$ is also common.

## Explanations

### L1 human

The length of a vector is how far the vector moves you. In the plane, the vector $(3, 4)$ is the hypotenuse of a right triangle with legs 3 and 4. So its length is $\sqrt{3^2 + 4^2} = 5$.
