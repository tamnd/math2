---
records:
    - id: CMPTH9FC4F
      kind: monograph
      title: 'Numerical Analysis: Proceedings of the Fourth IIMAS Workshop held at Guanajuato, Mexico, July 23–27, 1984'
      creators:
        - name: Jean-Pierre Hennart
          role: editor
      date: "1982"
      expressions:
        - key: e1
          kind: edition
          date: "1982"
          ids:
            doi:
                - 10.1007/bfb0072666
                - 10.1007/bfb0092954
          manifestations:
            - key: m1
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "1986"
              ids:
                isbn:
                    - "9783540172000"
                    - "9783540473794"
            - key: m2
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "1982"
              ids:
                isbn:
                    - "9783540111931"
                    - "9783540389866"
      relations:
        - kind: part_of
          to: MYK049V6DA
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.4 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/bfb0072666
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/bfb0092954
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
