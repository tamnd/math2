---
tag: 0K8SGQSV7G
kind: statement
role: theorem
name: Compactness and sequential compactness agree in metric spaces
msc: ["54E45"]
uses: [00R0X1WGPX, 0CARW59WD2, 040CFNJEAP]
sources:
  - url: https://en.wikipedia.org/wiki/Compact_space
    locator: Metric spaces
  - url: https://en.wikipedia.org/wiki/Sequentially_compact_space
    locator: Examples and properties
---

## Statement

Let $(X, d)$ be a [[metric space|063W5JMY85]] and let $K \subseteq X$.
Then $K$ is [[compact|00R0X1WGPX]] if and only if $K$ is [[sequentially compact|0CARW59WD2]].

## Remarks

One proof of the hard direction uses the [[Lebesgue number lemma|040CFNJEAP]] and the fact that a sequentially compact metric space is [[totally bounded|0WE5BBHGM6]].
Both conditions are also equivalent to: $K$ is complete and totally bounded. This is the statement [[compact iff complete and totally bounded|054Q5PW5GX]].
Without a metric, the two notions differ. For example, the product $\{0, 1\}^{[0, 1]}$ is compact but not sequentially compact.

## Explanations

### L1 human

In a metric space, you can test compactness with sequences. A set is compact exactly when each sequence in it has a subsequence with a limit in the set.
This test is often easier than the test with open covers.
