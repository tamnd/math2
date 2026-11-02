---
tag: TN2R1TDE3G
kind: definition
name: Nome
msc: ["33E05", 11F27]
defines: YSAZVCZAZC
uses: [X6XGGH5FPW, RM54CPPE12, 0J0FCWV32D]
sources:
  - url: https://en.wikipedia.org/wiki/Nome_(mathematics)
---

## Definition

Let $\tau$ be a point of the [[upper half-plane|X6XGGH5FPW]].
The *nome* of $\tau$ is $q = e^{\pi i\tau}$; it satisfies $0 < \abs{q} < 1$.

For a real modulus $0 < k < 1$, let $K = K(k)$ and $K' = K(\sqrt{1 - k^2})$ be [[complete elliptic integrals of the first kind|RM54CPPE12]], and let $\tau = iK'/K$.
The *nome of the modulus* $k$ is
$$q(k) = e^{\pi i\tau} = \exp\!\left(-\frac{\pi K'}{K}\right).$$

## Remarks

For real $k \in (0, 1)$ the nome is real with $0 < q < 1$, and it increases from $0$ to $1$ as $k$ goes from $0$ to $1$.
Example: at $k = 1/\sqrt2$ one has $k = \sqrt{1 - k^2}$, so $K = K'$ and $q = e^{-\pi} \approx 0.0432$.
As $k \to 0$, $K \to \pi/2$ and $K' = \log(4/k) + o(1)$, so $q = k^2/16 + O(k^4)$.
Non-example: $\tau = 0$ or real $\tau$ gives $\abs{q} = 1$, which is not a nome, since the theta series in $q$ do not converge there.
Notation varies: some authors, especially in the theory of [[modular forms|GWKN5VG78A]], use $q = e^{2\pi i\tau}$ instead and call it the nome as well.
With the nome $q = e^{\pi i\tau}$ defined above, the [[Jacobi theta function|2F5CYQJVAF]] is $\vartheta(z, \tau) = \sum_{n \in \Z} q^{n^2} e^{2\pi i n z}$.
