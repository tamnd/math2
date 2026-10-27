---
tag: 0ZTEH055YF
kind: definition
name: Operator norm
msc: [47A30]
defines: 06EKW1AKXF
uses: [0S3SMRH0Z5, 0F3K4C7XYW, 0BTMQ04556]
sources:
  - url: https://en.wikipedia.org/wiki/Operator_norm
    locator: Introduction and definition
  - url: https://en.wikipedia.org/wiki/Operator_norm
    locator: Equivalent definitions
inventory: [XQ2YBSPVWW]
---

## Definition

Let $V$ and $W$ be normed spaces and let $T \colon V \to W$ be a [[continuous linear map|0S3SMRH0Z5]].
The operator norm of $T$ is
$$\|T\| = \sup \{ \|Tx\|_W : x \in V, \ \|x\|_V \le 1 \}.$$

## Remarks

The [[supremum|0BTMQ04556]] is finite because $T$ is [[bounded|0F3K4C7XYW]]. If $V \neq \{0\}$, then $\|T\| = \sup_{x \neq 0} \|Tx\|_W / \|x\|_V$.
It is the smallest $C \ge 0$ with $\|Tx\|_W \le C \|x\|_V$ for all $x \in V$.
The operator norm is a norm on the space $L(V, W)$ of continuous linear maps. It satisfies $\|ST\| \le \|S\| \, \|T\|$. If $W$ is a [[Banach space|0BDTTM24DP]], so is $L(V, W)$.
For a diagonal matrix on $\mathbb{R}^n$ with the Euclidean norm, the operator norm is the largest absolute value of a diagonal entry.

## Explanations

### L1 human

The operator norm tells you how much $T$ can stretch a vector at most.
For example, the map $x \mapsto 3x$ on $\mathbb{R}$ has operator norm $3$.
