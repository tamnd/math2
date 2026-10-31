---
records:
    - id: 7SCD0JVJ89
      kind: monograph
      title: Lyapunov Exponents
      creators:
        - name: Ludwig Arnold
          role: editor
        - name: Volker Wihstutz
          role: editor
      date: "1986"
      expressions:
        - key: e1
          kind: edition
          date: "1986"
          ids:
            doi:
                - 10.1007/bfb0076829
                - 10.1007/bfb0086653
          manifestations:
            - key: m1
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "1986"
              ids:
                isbn:
                    - "9783540164586"
                    - "9783540397953"
            - key: m2
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "1991"
              ids:
                isbn:
                    - "9783540546627"
                    - "9783540464310"
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
          native_id: 10.1007/bfb0076829
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/bfb0086653
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
