---
records:
    - id: DHFF3KSC2C
      kind: monograph
      title: Probability and Statistical Inference
      creators:
        - name: J. G. Kalbfleisch
          role: author
      date: "1979"
      expressions:
        - key: e1
          kind: edition
          date: "1979"
          ids:
            doi:
                - 10.1007/978-1-4684-0089-2
                - 10.1007/978-1-4684-0091-5
          manifestations:
            - key: m1
              kind: print
              publisher: Springer US
              date: "1979"
              ids:
                isbn:
                    - "9780387904573"
                    - "9781468400892"
            - key: m2
              kind: print
              publisher: Springer US
              date: "1979"
              ids:
                isbn:
                    - "9780387904580"
                    - "9781468400915"
      relations:
        - kind: part_of
          to: W0CC03QJC7
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.2 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4684-0089-2
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4684-0091-5
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
