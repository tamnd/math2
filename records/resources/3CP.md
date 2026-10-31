---
records:
    - id: 3CP4RF182F
      kind: monograph
      title: A Course in Number Theory and Cryptography
      creators:
        - name: Neal Koblitz
          role: author
      date: "1987"
      expressions:
        - key: e1
          kind: edition
          date: "1987"
          ids:
            doi:
                - 10.1007/978-1-4419-8592-7
                - 10.1007/978-1-4684-0310-7
          manifestations:
            - key: m1
              kind: print
              publisher: Springer New York
              date: "1994"
              ids:
                isbn:
                    - "9781461264422"
                    - "9781441985927"
            - key: m2
              kind: print
              publisher: Springer US
              date: "1987"
              ids:
                isbn:
                    - "9781468403121"
                    - "9781468403107"
      relations:
        - kind: part_of
          to: 7ME1ABA6H5
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.7 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4419-8592-7
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4684-0310-7
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
    - id: 3CP9D7DVJX
      kind: monograph
      title: Conference on the Numerical Solution of Differential Equations
      creators:
        - name: J. Li. Morris
          role: editor
      date: "1969"
      expressions:
        - key: e1
          kind: edition
          date: "1969"
          ids:
            doi: 10.1007/bfb0060012
          manifestations:
            - key: m1
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "1969"
              ids:
                isbn:
                    - "9783540046288"
                    - "9783540361589"
      relations:
        - kind: part_of
          to: MYK049V6DA
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.7 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/bfb0060012
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
---
